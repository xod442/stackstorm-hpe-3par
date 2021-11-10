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


class getDb(MongoBaseAction):
    def run(self):

        mydb = self.dbclient["app_db"]
        known = mydb["tasks3par"]

        task_list = []

        myquery = { "u_snow_process" : 'no' }
        records = known.find(myquery)

        task = {}

        for r in records:
            # TODO add records processing
            new_task['u_id']=r['id']
            new_task['u_name']=r['name']
            new_task['u_finishTime']=r['finishTime']
            new_task['u_startTime']=r['startTime']
            new_task['u_status']=r['status']
            new_task['u_type']=r['type']
            new_task['u_user']=r['user']
            tak_list.append(new_task)

        return (task_list)
