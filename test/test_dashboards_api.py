# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.dashboards_api import DashboardsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.dashboards_api.DashboardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_import_file(self):
        """Test case for import_file

        Post a dashboard or a dashboard template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
