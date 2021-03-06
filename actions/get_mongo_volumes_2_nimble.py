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


class fetchDb(MongoBaseAction):
    def run(self):

        mydb = self.dbclient["app_db"]
        known = mydb["volz3par"]

        nimble_volume_list = []

        myquery = { "u_nimble_process" : 'no' }
        records = known.find(myquery)

        limit_iops = 12000

        volume = {}

        for r in records:
            # TODO add records processing
            if r['u_name'] != 'admin' and r['u_name'] != '.srdata':
                volume['name'] = r['u_name']
                volume['size'] = r['u_sizeMiB']
                volume['limit_iops'] = limit_iops
                nimble_volume_list.append(volume)
                volume = {}

        return (nimble_volume_list)
