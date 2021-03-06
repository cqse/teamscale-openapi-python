# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def calculate_project_mappings(self, project, request_body, **kwargs):  # noqa: E501
        """Calculate project mappings  # noqa: E501

        Returns path prefix mappings to which the given paths could be mapped to. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_project_mappings(project, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param list[str] request_body: (required)
        :param str branch: Optional branch name, will use the default branch if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ProjectMapping]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.calculate_project_mappings_with_http_info(project, request_body, **kwargs)  # noqa: E501

    def calculate_project_mappings_with_http_info(self, project, request_body, **kwargs):  # noqa: E501
        """Calculate project mappings  # noqa: E501

        Returns path prefix mappings to which the given paths could be mapped to. This service is public API since Teamscale 5.7. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_project_mappings_with_http_info(project, request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param list[str] request_body: (required)
        :param str branch: Optional branch name, will use the default branch if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ProjectMapping], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project',
            'request_body',
            'branch'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate_project_mappings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project' is set
        if self.api_client.client_side_validation and ('project' not in local_var_params or  # noqa: E501
                                                        local_var_params['project'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project` when calling `calculate_project_mappings`")  # noqa: E501
        # verify the required parameter 'request_body' is set
        if self.api_client.client_side_validation and ('request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_body` when calling `calculate_project_mappings`")  # noqa: E501

        if self.api_client.client_side_validation and 'project' in local_var_params and not re.search(r'^(?!aliases$)[-_.a-zA-Z0-9]+$', local_var_params['project']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project` when calling `calculate_project_mappings`, must conform to the pattern `/^(?!aliases$)[-_.a-zA-Z0-9]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']  # noqa: E501

        query_params = []
        if 'branch' in local_var_params and local_var_params['branch'] is not None:  # noqa: E501
            query_params.append(('branch', local_var_params['branch']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{project}/auto-prefix-mappings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectMapping]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_commits_for_revision(self, project, revision, **kwargs):  # noqa: E501
        """Get teamscale commits  # noqa: E501

        Returns the teamscale commit representations for a given revision. As a revision can occur in multiple repositories, more than one commit may be returned. This service is public API since Teamscale 5.9.6. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_commits_for_revision(project, revision, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str revision: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CommitDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_commits_for_revision_with_http_info(project, revision, **kwargs)  # noqa: E501

    def get_commits_for_revision_with_http_info(self, project, revision, **kwargs):  # noqa: E501
        """Get teamscale commits  # noqa: E501

        Returns the teamscale commit representations for a given revision. As a revision can occur in multiple repositories, more than one commit may be returned. This service is public API since Teamscale 5.9.6. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_commits_for_revision_with_http_info(project, revision, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str revision: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CommitDescriptor], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project',
            'revision'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_commits_for_revision" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project' is set
        if self.api_client.client_side_validation and ('project' not in local_var_params or  # noqa: E501
                                                        local_var_params['project'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project` when calling `get_commits_for_revision`")  # noqa: E501
        # verify the required parameter 'revision' is set
        if self.api_client.client_side_validation and ('revision' not in local_var_params or  # noqa: E501
                                                        local_var_params['revision'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `revision` when calling `get_commits_for_revision`")  # noqa: E501

        if self.api_client.client_side_validation and 'project' in local_var_params and not re.search(r'^(?!aliases$)[-_.a-zA-Z0-9]+$', local_var_params['project']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project` when calling `get_commits_for_revision`, must conform to the pattern `/^(?!aliases$)[-_.a-zA-Z0-9]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']  # noqa: E501
        if 'revision' in local_var_params:
            path_params['revision'] = local_var_params['revision']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{project}/revision/{revision}/commits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CommitDescriptor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard_gadget(self, **kwargs):  # noqa: E501
        """Get the dashboard gadget  # noqa: E501

        Returns the XML descriptor for the dashboard gadget. This service is public API since Teamscale 5.8. The API requires no login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_gadget(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dashboard_gadget_with_http_info(**kwargs)  # noqa: E501

    def get_dashboard_gadget_with_http_info(self, **kwargs):  # noqa: E501
        """Get the dashboard gadget  # noqa: E501

        Returns the XML descriptor for the dashboard gadget. This service is public API since Teamscale 5.8. The API requires no login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_gadget_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard_gadget" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gadgets/jira/dashboard.xml', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard_thumbnail(self, **kwargs):  # noqa: E501
        """Get the thumbnail of the Jira dashboard gadget  # noqa: E501

        Returns the thumbnail of the Jira dashboard gadget This service is public API since Teamscale 5.8. The API requires no login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_thumbnail(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dashboard_thumbnail_with_http_info(**kwargs)  # noqa: E501

    def get_dashboard_thumbnail_with_http_info(self, **kwargs):  # noqa: E501
        """Get the thumbnail of the Jira dashboard gadget  # noqa: E501

        Returns the thumbnail of the Jira dashboard gadget This service is public API since Teamscale 5.8. The API requires no login  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_thumbnail_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[str], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard_thumbnail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/png'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gadgets/jira/dashboard-thumbnail.png', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
