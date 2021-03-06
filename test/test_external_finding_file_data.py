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
from openapi_client.models.external_finding_file_data import ExternalFindingFileData  # noqa: E501
from openapi_client.rest import ApiException

class TestExternalFindingFileData(unittest.TestCase):
    """ExternalFindingFileData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExternalFindingFileData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.external_finding_file_data.ExternalFindingFileData()  # noqa: E501
        if include_optional :
            return ExternalFindingFileData(
                findings = [
                    openapi_client.models.external_finding_data.ExternalFindingData(
                        finding_type_id = '0', 
                        message = '0', 
                        assessment = 'RED', 
                        start_offset = 56, 
                        end_offset = 56, 
                        start_line = 56, 
                        end_line = 56, 
                        identifier = '0', 
                        finding_properties = {
                            'key' : None
                            }, )
                    ], 
                path = '0', 
                content = '0'
            )
        else :
            return ExternalFindingFileData(
        )

    def testExternalFindingFileData(self):
        """Test ExternalFindingFileData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
