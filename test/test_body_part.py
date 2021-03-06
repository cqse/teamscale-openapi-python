# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.body_part import BodyPart  # noqa: E501
from openapi_client.rest import ApiException

class TestBodyPart(unittest.TestCase):
    """BodyPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.body_part.BodyPart()  # noqa: E501
        if include_optional :
            return BodyPart(
                content_disposition = openapi_client.models.content_disposition.ContentDisposition(
                    type = openapi_client.models.type.type(), 
                    parameters = {
                        'key' : '0'
                        }, 
                    file_name = '0', 
                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    read_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    size = 56, ), 
                entity = None, 
                headers = {
                    'key' : [
                        '0'
                        ]
                    }, 
                media_type = openapi_client.models.body_part_media_type.BodyPart_mediaType(
                    type = '0', 
                    subtype = '0', 
                    parameters = {
                        'key' : '0'
                        }, ), 
                message_body_workers = None, 
                parent = openapi_client.models.multi_part.MultiPart(
                    content_disposition = openapi_client.models.content_disposition.ContentDisposition(
                        type = openapi_client.models.type.type(), 
                        parameters = {
                            'key' : '0'
                            }, 
                        file_name = '0', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        read_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        size = 56, ), 
                    entity = openapi_client.models.entity.entity(), 
                    headers = {
                        'key' : [
                            '0'
                            ]
                        }, 
                    media_type = openapi_client.models.body_part_media_type.BodyPart_mediaType(
                        type = '0', 
                        subtype = '0', ), 
                    message_body_workers = openapi_client.models.message_body_workers.MessageBodyWorkers(), 
                    parent = openapi_client.models.multi_part.MultiPart(
                        entity = openapi_client.models.entity.entity(), 
                        providers = openapi_client.models.providers.providers(), 
                        body_parts = [
                            openapi_client.models.body_part.BodyPart(
                                entity = openapi_client.models.entity.entity(), 
                                providers = openapi_client.models.providers.providers(), )
                            ], ), 
                    providers = openapi_client.models.providers.providers(), 
                    body_parts = [
                        openapi_client.models.body_part.BodyPart(
                            entity = openapi_client.models.entity.entity(), 
                            providers = openapi_client.models.providers.providers(), )
                        ], ), 
                providers = openapi_client.models.providers.providers()
            )
        else :
            return BodyPart(
        )

    def testBodyPart(self):
        """Test BodyPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
