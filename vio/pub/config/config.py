# Copyright 2017 VMware Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

# [MSB]
MSB_SERVICE_IP = '172.17.0.2'
MSB_SERVICE_PORT = '80'

# [IMAGE LOCAL PATH]
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMAGE_ROOT_PATH = os.path.join(ROOT_PATH, "/VmNfvo/VnfProduct")

# [REDIS]
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_PASSWD = ''

# [mysql]
DB_IP = '172.17.0.4'
DB_PORT = 3306
DB_NAME = 'inventory'
DB_USER = 'inventory'
DB_PASSWD = 'inventory'

# [register]
REG_TO_MSB_WHEN_START = True
REG_TO_MSB_REG_URL = "/openoapi/microservices/v1/services"
REG_TO_MSB_REG_PARAM = {
    "serviceName": "multivim-vio",
    "version": "v1",
    "url": "/openoapi/multivim-vio/v1",
    "protocol": "REST",
    "visualRange": "1",
    "nodes": [{
        "ip": "172.17.0.4",
        "port": "9004",
        "ttl": 0
    }]
}