# Copyright 2016 ZTE Corporation.
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


import json
import logging
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from vio.pub.msapi import extsys
from vio.pub.vim.vimapi.glance import OperateImage
from vio.pub.vim.vimapi.keystone import OperateTenant


logger = logging.getLogger(__name__)


class ListTenantsView(APIView):
    def get(self, request, vimid):
        vim_info = extsys.get_vim_by_id(vimid)

        data = {}
        data['vimid'] = vim_info['vimId']
        data['vimName'] = vim_info['name']
        data['username'] = vim_info['userName']
        data['password'] = vim_info['password']
        data['url'] = vim_info['url']
        data['project_name'] = vim_info['tenant']

        tenant_instance = OperateTenant.OperateTenant()
        projects = tenant_instance.get_projects(data)

        rsp = {}
        rsp['vimid'] = vim_info['vimId']
        rsp['vimName'] = vim_info['name']
        rsp['tenants'] = []

        for project in projects:
            tenant = {}
            tenant['id'] = project['id']
            tenant['name'] = project['name']
            rsp['tenants'].append(tenant)
        return Response(data=rsp, status=status.HTTP_200_OK)


class CreateListImagesView(APIView):
    def post(self, request):
        data = {
            'imageName' : request.data['imageName'],
            'imagePath' : request.data['imagePath'],
            'imageType' : request.data['imageType'],
            'containerFormat' : request.data['containerFormat']
            }
        rsp = OperateImage.create_image(data)
        return Response(data=rsp, status=status.HTTP_200_OK)

    def get(self, request):
        data = {
            'imageName' : request.data['imageName'],
            'imagePath' : request.data['imagePath'],
            'imageType' : request.data['imageType'],
            'containerFormat' : request.data['containerFormat']
        }
        rsp = OperateImage.list_images(data)
        return Response(data=rsp, status=status.HTTP_200_OK)

class GetDeleteImageView(APIView):
    def post(self, request):
        data = {
            'imageName' : request.data['imageName'],
            'imagePath' : request.data['imagePath'],
            'imageType' : request.data['imageType'],
            'containerFormat' : request.data['containerFormat']
        }
        rsp = OperateImage.delete_image(data)
        return Response(data=rsp, status=status.HTTP_200_OK)

    def get(self, request):
        data = {
            'imageName' : request.data['imageName'],
            'imagePath' : request.data['imagePath'],
            'imageType' : request.data['imageType'],
            'containerFormat' : request.data['containerFormat']
        }
        rsp = OperateImage.get_image(data)
        return Response(data=rsp, status=status.HTTP_200_OK)

class SwaggerJsonView(APIView):
    def get(self, request):
        json_file = os.path.join(os.path.dirname(__file__), 'swagger.json')
        f = open(json_file)
        json_data = json.JSONDecoder().decode(f.read())
        f.close()
        return Response(json_data)


