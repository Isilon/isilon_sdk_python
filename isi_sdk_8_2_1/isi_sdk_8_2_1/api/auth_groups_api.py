# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_2_1.api_client import ApiClient


class AuthGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_group_member(self, group_member, group, **kwargs):  # noqa: E501
        """create_group_member  # noqa: E501

        Add a member to the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_member(group_member, group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthAccessAccessItemFileGroup group_member: (required)
        :param str group: (required)
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_group_member_with_http_info(group_member, group, **kwargs)  # noqa: E501
        else:
            (data) = self.create_group_member_with_http_info(group_member, group, **kwargs)  # noqa: E501
            return data

    def create_group_member_with_http_info(self, group_member, group, **kwargs):  # noqa: E501
        """create_group_member  # noqa: E501

        Add a member to the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_member_with_http_info(group_member, group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthAccessAccessItemFileGroup group_member: (required)
        :param str group: (required)
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_member', 'group', 'zone', 'provider']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_member' is set
        if ('group_member' not in params or
                params['group_member'] is None):
            raise ValueError("Missing the required parameter `group_member` when calling `create_group_member`")  # noqa: E501
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `create_group_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['Group'] = params['group']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_member' in params:
            body_params = params['group_member']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/auth/groups/{Group}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_group_member(self, group_member_id, group, **kwargs):  # noqa: E501
        """delete_group_member  # noqa: E501

        Remove the member from the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_member(group_member_id, group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_member_id: Remove the member from the group. (required)
        :param str group: (required)
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_group_member_with_http_info(group_member_id, group, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_group_member_with_http_info(group_member_id, group, **kwargs)  # noqa: E501
            return data

    def delete_group_member_with_http_info(self, group_member_id, group, **kwargs):  # noqa: E501
        """delete_group_member  # noqa: E501

        Remove the member from the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_member_with_http_info(group_member_id, group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_member_id: Remove the member from the group. (required)
        :param str group: (required)
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_member_id', 'group', 'zone', 'provider']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_member_id' is set
        if ('group_member_id' not in params or
                params['group_member_id'] is None):
            raise ValueError("Missing the required parameter `group_member_id` when calling `delete_group_member`")  # noqa: E501
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `delete_group_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_member_id' in params:
            path_params['GroupMemberId'] = params['group_member_id']  # noqa: E501
        if 'group' in params:
            path_params['Group'] = params['group']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/auth/groups/{Group}/members/{GroupMemberId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_members(self, group, **kwargs):  # noqa: E501
        """list_group_members  # noqa: E501

        List all the members of the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_members(group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: (required)
        :param bool resolve_names: Resolve names of personas.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int limit: Return no more than this many results at once (see resume).
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_group_members_with_http_info(group, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_members_with_http_info(group, **kwargs)  # noqa: E501
            return data

    def list_group_members_with_http_info(self, group, **kwargs):  # noqa: E501
        """list_group_members  # noqa: E501

        List all the members of the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_group_members_with_http_info(group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: (required)
        :param bool resolve_names: Resolve names of personas.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int limit: Return no more than this many results at once (see resume).
        :param str zone: Filter group members by zone.
        :param str provider: Filter group members by provider.
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group', 'resolve_names', 'resume', 'limit', 'zone', 'provider']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_group_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `list_group_members`")  # noqa: E501

        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_group_members`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_group_members`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_group_members`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_group_members`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['Group'] = params['group']  # noqa: E501

        query_params = []
        if 'resolve_names' in params:
            query_params.append(('resolve_names', params['resolve_names']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/auth/groups/{Group}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupMembers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
