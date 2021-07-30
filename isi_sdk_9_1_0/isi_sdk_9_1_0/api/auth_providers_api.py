# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_9_1_0.api_client import ApiClient


class AuthProvidersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ads_provider_controllers(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_controllers  # noqa: E501

        List all ADS controllers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_controllers(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str dc_site: Domain Controller site name
        :param str groupnet: Groupnet identifier
        :return: AdsProviderControllers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ads_provider_controllers_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ads_provider_controllers_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_ads_provider_controllers_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_controllers  # noqa: E501

        List all ADS controllers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_controllers_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str dc_site: Domain Controller site name
        :param str groupnet: Groupnet identifier
        :return: AdsProviderControllers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'dc_site', 'groupnet']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ads_provider_controllers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_ads_provider_controllers`")  # noqa: E501

        if ('dc_site' in params and
                len(params['dc_site']) > 255):
            raise ValueError("Invalid value for parameter `dc_site` when calling `get_ads_provider_controllers`, length must be less than or equal to `255`")  # noqa: E501
        if ('dc_site' in params and
                len(params['dc_site']) < 0):
            raise ValueError("Invalid value for parameter `dc_site` when calling `get_ads_provider_controllers`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'dc_site' in params:
            query_params.append(('dc_site', params['dc_site']))  # noqa: E501
        if 'groupnet' in params:
            query_params.append(('groupnet', params['groupnet']))  # noqa: E501

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
            '/platform/7/auth/providers/ads/{Id}/controllers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdsProviderControllers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ads_provider_domain(self, ads_provider_domain_id, id, **kwargs):  # noqa: E501
        """get_ads_provider_domain  # noqa: E501

        Retrieve the ADS domain information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_domain(ads_provider_domain_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ads_provider_domain_id: Retrieve the ADS domain information. (required)
        :param str id: (required)
        :return: AdsProviderDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ads_provider_domain_with_http_info(ads_provider_domain_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ads_provider_domain_with_http_info(ads_provider_domain_id, id, **kwargs)  # noqa: E501
            return data

    def get_ads_provider_domain_with_http_info(self, ads_provider_domain_id, id, **kwargs):  # noqa: E501
        """get_ads_provider_domain  # noqa: E501

        Retrieve the ADS domain information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_domain_with_http_info(ads_provider_domain_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ads_provider_domain_id: Retrieve the ADS domain information. (required)
        :param str id: (required)
        :return: AdsProviderDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ads_provider_domain_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ads_provider_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ads_provider_domain_id' is set
        if ('ads_provider_domain_id' not in params or
                params['ads_provider_domain_id'] is None):
            raise ValueError("Missing the required parameter `ads_provider_domain_id` when calling `get_ads_provider_domain`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_ads_provider_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ads_provider_domain_id' in params:
            path_params['AdsProviderDomainId'] = params['ads_provider_domain_id']  # noqa: E501
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []

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
            '/platform/7/auth/providers/ads/{Id}/domains/{AdsProviderDomainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdsProviderDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ads_provider_domains(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_domains  # noqa: E501

        List all ADS domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_domains(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str scope: If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned.
        :return: AdsProviderDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ads_provider_domains_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ads_provider_domains_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_ads_provider_domains_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_domains  # noqa: E501

        List all ADS domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_domains_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str scope: If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned.
        :return: AdsProviderDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ads_provider_domains" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_ads_provider_domains`")  # noqa: E501

        if ('scope' in params and
                len(params['scope']) > 255):
            raise ValueError("Invalid value for parameter `scope` when calling `get_ads_provider_domains`, length must be less than or equal to `255`")  # noqa: E501
        if ('scope' in params and
                len(params['scope']) < 0):
            raise ValueError("Invalid value for parameter `scope` when calling `get_ads_provider_domains`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

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
            '/platform/7/auth/providers/ads/{Id}/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdsProviderDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ads_provider_search(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_search  # noqa: E501

        Retrieve search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_search(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str domain: The Active Directory provider name to search for.
        :param str description: The user or group description to search for.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param bool search_users: If true, search for users.
        :param str filter: The LDAP filter to apply to the search.
        :param int limit: Return no more than this many results at once (see resume).
        :param str user: The user name for the domain if untrusted.
        :param str password: The password for the domain if untrusted.
        :param bool search_groups: If true, search for groups.
        :return: AdsProviderSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ads_provider_search_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ads_provider_search_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_ads_provider_search_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_ads_provider_search  # noqa: E501

        Retrieve search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ads_provider_search_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str domain: The Active Directory provider name to search for.
        :param str description: The user or group description to search for.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param bool search_users: If true, search for users.
        :param str filter: The LDAP filter to apply to the search.
        :param int limit: Return no more than this many results at once (see resume).
        :param str user: The user name for the domain if untrusted.
        :param str password: The password for the domain if untrusted.
        :param bool search_groups: If true, search for groups.
        :return: AdsProviderSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'domain', 'description', 'resume', 'search_users', 'filter', 'limit', 'user', 'password', 'search_groups']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ads_provider_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_ads_provider_search`")  # noqa: E501

        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_ads_provider_search`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_ads_provider_search`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_ads_provider_search`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_ads_provider_search`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'search_users' in params:
            query_params.append(('search_users', params['search_users']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501
        if 'password' in params:
            query_params.append(('password', params['password']))  # noqa: E501
        if 'search_groups' in params:
            query_params.append(('search_groups', params['search_groups']))  # noqa: E501

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
            '/platform/1/auth/providers/ads/{Id}/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdsProviderSearch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
