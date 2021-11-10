# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction


class loadDb(MongoBaseAction):
    def run(self, volumes):

        mydb = self.dbclient["app_db"]
        known = mydb["volz3par"]

        new_volume={}

        for vol in volumes:
            myquery = { "u_uuid" : vol['uuid'] }
            records = known.find(myquery).count()
            if records == 0:
                new_volume['u_nimble_process']='no'
                new_volume['u_snow_process']='no'
                new_volume['u_id']=vol['id']
                new_volume['u_name']=vol['name']
                new_volume['u_provisioningType']=vol['provisioningType']
                new_volume['u_copyType']=vol['copyType']
                new_volume['u_baseId']=vol['baseId']
                new_volume['u_readOnly']=vol['readOnly']
                new_volume['u_state']=vol['state']
                new_volume['u_failedStates']=vol['failedStates']
                new_volume['u_degradedStates']=vol['degradedStates']
                new_volume['u_additionalStates']=vol['additionalStates']
                new_volume['u_adminSpace']=vol['adminSpace']
                new_volume['u_snapshotSpace']=vol['snapshotSpace']
                new_volume['u_sizeMiB']=vol['sizeMiB']
                new_volume['u_wwn']=vol['wwn']
                new_volume['u_creationTimeSec']=vol['creationTimeSec']
                new_volume['u_creationTime8601']=vol['creationTime8601']
                new_volume['u_ssSpcAllocWarningPct']=vol['ssSpcAllocWarningPct']
                new_volume['u_ssSpcAllocLimitPct']=vol['ssSpcAllocLimitPct']
                new_volume['u_usrSpcAllocWarningPct']=vol['usrSpcAllocWarningPct']
                new_volume['u_usrSpcAllocLimitPct']=vol['usrSpcAllocLimitPct']
                new_volume['u_policies']=vol['policies']
                new_volume['u_uuid']=vol['uuid']
                new_volume['u_capacityEfficiency']=vol['capacityEfficiency']
                new_volume['u_links']=vol['links']
                write_record = known.insert_one(new_volume)
                new_volume={}

            else:
                records='Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
