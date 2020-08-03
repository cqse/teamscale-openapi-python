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
from openapi_client.models.diff_input_description import DiffInputDescription  # noqa: E501
from openapi_client.rest import ApiException

class TestDiffInputDescription(unittest.TestCase):
    """DiffInputDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DiffInputDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.diff_input_description.DiffInputDescription()  # noqa: E501
        if include_optional :
            return DiffInputDescription(
                left = openapi_client.models.diff_input_location.DiffInputLocation(
                    uniform_path = '0', 
                    commit = openapi_client.models.commit_descriptor.CommitDescriptor(
                        branch_name = '0', 
                        timestamp = 56, ), 
                    line_number = 56, ), 
                right = openapi_client.models.diff_input_location.DiffInputLocation(
                    uniform_path = '0', 
                    commit = openapi_client.models.commit_descriptor.CommitDescriptor(
                        branch_name = '0', 
                        timestamp = 56, ), 
                    line_number = 56, )
            )
        else :
            return DiffInputDescription(
        )

    def testDiffInputDescription(self):
        """Test DiffInputDescription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()