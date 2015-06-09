from ceph_client.wrapper import *


class ModelsData:

    def __init__(self):
        self.rest_client = CephWrapper(
            endpoint='http://163.17.136.249:5100/api/v1/'
        )

    # Root Models
    # Additionally, we include PUT,GET for the API.
    def cluster_ids(self):
        response, body = self.rest_client.fsid(body='json')
        return body['output']

    def health(self):
        health_response = self.rest_client.health(body='json')
        health = health_response[1]['output']
        return {
            'overall_status': health['overall_status'],
            'summary': health['summary']
        }

    def status(self):
        status_response = self.rest_client.status(body='json')
        status = status_response[1]['output']
        monmap = {}

        if 'timechecks' in status['health']:
            monmap = status['health']['timechecks']['mons']

        pool_response = self.rest_client.osd_lspools(body='json')
        pools = pool_response[1]['output']
        pool_count = 0
        for pool in pools:
            pool_count += 1

        return {
            'mds_map': status['mdsmap'],
            'mon_map': monmap,
            'osd_map': status['osdmap']['osdmap'],
            'pg_map': status['pgmap'],
            'quorum_num': status['quorum'],
            'pool_num': pool_count
        }

    def df(self):
        response, body = self.rest_client.df(body='json')
        return body['output']['stats']

    def fs(self):
        response, body = self.rest_client.fs(body='json')
        return body['output']

    def performance(self):
        status_response = self.rest_client.status(body='json')
        pg_map = status_response[1]['output']['pgmap']

        write_iop_sec = 0
        read_iop_sec = 0
        operation_sec = 0
        if 'write_bytes_sec' in pg_map:
            write_iop_sec = pg_map['write_bytes_sec']

        if 'read_bytes_sec' in pg_map:
            read_iop_sec = pg_map['read_bytes_sec']

        if 'op_per_sec' in pg_map:
            operation_sec = pg_map['op_per_sec']

        return {
            'write_bytes_sec': write_iop_sec,
            'read_bytes_sec': read_iop_sec,
            'op_per_sec': operation_sec,
        }

    # OSD Models
    # Additionally, we include PUT,GET for the API.
    def osd_all_object(self, osd_body, perf):
        return {
            'id': osd_body['osd'],
            'cluster_address': osd_body['cluster_addr'],
            'public_address': osd_body['public_addr'],
            'weight': osd_body['weight'],
            'uuid': osd_body['uuid'],
            'up': osd_body['up'],
            'in': osd_body['in'],
            'apply_latency_ms': perf['perf_stats']['apply_latency_ms'],
            'commit_latency_ms': perf['perf_stats']['commit_latency_ms'],
        }

    def osd(self):
        response, body = self.rest_client.osd_dump(body='json')
        body_osd = body['output']['osds']
        osd_perf_response = self.rest_client.osd_perf(body='json')
        osd_perf = osd_perf_response[1]['output']['osd_perf_infos']

        osd_list = {}

        for count in range(0, len(body_osd)):
            osd_id = body_osd[count]['osd']
            meta_response = self.rest_client.osd_find_metadata(osd_id, body='json')
            host_name = meta_response[1]['output']['hostname']
            if host_name not in osd_list:
                osd_list[meta_response[1]['output']['hostname']] = [
                    self.osd_all_object(body_osd[count], osd_perf[count])
                ]
            else:
                osd_list[meta_response[1]['output']['hostname']].append(
                    self.osd_all_object(body_osd[count], osd_perf[count])
                )

        return osd_list

    def performance(self):
        osd_perf_response = self.rest_client.osd_perf(body='json')
        osd_perf = osd_perf_response[1]['output']['osd_perf_infos']
        return osd_perf

    def lstree(self):
        osd_tree_response = self.rest_client.osd_tree(body='json')
        return osd_tree_response[1]['output']

    def lscrush(self):
        osd_crush_response = self.rest_client.osd_tree(body='json')
        return osd_crush_response[1]['output']

    def lspool(self):
        osd_pool_response = self.rest_client.osd_lspools(body='json')
        return osd_pool_response[1]['output']

    # put method action
    def osd_in(self, osd_id):
        action_response = self.rest_client.osd_in(osd_id, body='json')
        return {
            'message': action_response[1]['status']
        }

    def osd_out(self, osd_id):
        action_response = self.rest_client.osd_out(osd_id, body='json')
        return {
            'message': action_response[1]['status']
        }

    def osd_down(self, osd_id):
        action_response = self.rest_client.osd_down(osd_id, body='json')
        return {
            'message': action_response[1]['status']
        }

    # Mon API Models
    # Additionally, we include PUT,GET for the API.

    def mon_list(self):
        status_response = self.rest_client.status(body='json')
        status = status_response[1]['output']
        monmap = {}
        mons = status['monmap']['mons']

        if 'timechecks' in status['health']:
            timechecks = status['health']['timechecks']['mons']
            for count in range(0, len(timechecks)):
                mons[count]['latency'] = timechecks[count]['latency']
                mons[count]['skew'] = timechecks[count]['skew']
                mons[count]['health'] = timechecks[count]['health']
                if 'details' in timechecks[count]:
                    mons[count]['details'] = timechecks[count]['details']
                else:
                    mons[count]['details'] = "monitor is okay"
        else:
            for count in range(0, len(mons)):
                mons[count]['latency'] = 0
                mons[count]['skew'] = 0
                mons[count]['health'] = "HEALTH_OK"
                mons[count]['details'] = "monitor is okay"

        return mons

    # Pool API Models
    # Additionally, we include PUT,GET for the API.

    def pool_list(self):
        pool_response = self.rest_client.osd_pool_ls('', body='json')
        cluster_pools = pool_response[1]['output']
        pool_df_response = self.rest_client.df('', body='json')
        pool_dfs = pool_df_response[1]['output']['pools']
        pool_dirty_count = 0
        pools = []

        for count in range(0, len(cluster_pools)):
            pool = cluster_pools[count]
            pools.append({
                'id': pool_dfs[count]['id'],
                'name': pool['pool_name'],
                'pg_placement_num': pool['pg_placement_num'],
                'pg_num': pool['pg_num'],
                'write_count': pool_dfs[count]['stats']['wr'],
                'write_bytes': pool_dfs[count]['stats']['wr_bytes'],
                'read_count': pool_dfs[count]['stats']['rd'],
                'read_bytes': pool_dfs[count]['stats']['rd_bytes'],
                'objects': pool_dfs[count]['stats']['objects'],
                'dirty': pool_dfs[count]['stats']['dirty'],
                'bytes_used': pool_dfs[count]['stats']['bytes_used'],
                'size': pool['size'],
            })
            pool_dirty_count += pool_dfs[count]['stats']['dirty']

        return {
            'pools': pools,
            'dirty_count': pool_dirty_count
        }

    # Placement of Groups API Models
    # Additionally, we include PUT,GET for the API.

    def pg_status(self):
        pg_response = self.rest_client.pg_stat(body='json')
        pgs = pg_response[1]['output']
        return pgs

    def pg_pools_dump(self):
        pg_response = self.rest_client.pg_dump_pools_json(body='json')
        pgs = pg_response[1]['output']
        return pgs

    # PUT Method
    def set_full_ratio(self, ration):
        response = self.rest_client.set_full_ratio(ration, body='json')
        return {
            'message': response[1]['status']
        }

    def set_nearfull_ratio(self, ration):
        response = self.rest_client.set_nearfull_ratio(ration, body='json')
        return {
            'message': response[1]['status']
        }

    # Metadata Server API Models
    # Additionally, we include PUT,GET for the API.

    def mds_status(self):
        mds_response = self.rest_client.mds_stat(body='json')
        return mds_response[1]['output']

    def mds_dump(self):
        mds_response = self.rest_client.mds_dump(body='json')
        return mds_response[1]['output']

    # Logging API Models
    # Additionally, we include PUT,GET for the API.

# Static Model Variable
staticModel = ModelsData()
