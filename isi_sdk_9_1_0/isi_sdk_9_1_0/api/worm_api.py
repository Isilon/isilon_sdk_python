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


class WormApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_worm_domain(self, worm_domain, **kwargs):  # noqa: E501
        """create_worm_domain  # noqa: E501

        Create a WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_worm_domain(worm_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormDomainCreateParams worm_domain: (required)
        :return: WormDomainExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_worm_domain_with_http_info(worm_domain, **kwargs)  # noqa: E501
        else:
            (data) = self.create_worm_domain_with_http_info(worm_domain, **kwargs)  # noqa: E501
            return data

    def create_worm_domain_with_http_info(self, worm_domain, **kwargs):  # noqa: E501
        """create_worm_domain  # noqa: E501

        Create a WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_worm_domain_with_http_info(worm_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormDomainCreateParams worm_domain: (required)
        :return: WormDomainExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['worm_domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_worm_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'worm_domain' is set
        if ('worm_domain' not in params or
                params['worm_domain'] is None):
            raise ValueError("Missing the required parameter `worm_domain` when calling `create_worm_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'worm_domain' in params:
            body_params = params['worm_domain']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/worm/domains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WormDomainExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_worm_domain(self, worm_domain_id, **kwargs):  # noqa: E501
        """get_worm_domain  # noqa: E501

        View a single WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_worm_domain(worm_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str worm_domain_id: View a single WORM domain. (required)
        :return: WormDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_worm_domain_with_http_info(worm_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_worm_domain_with_http_info(worm_domain_id, **kwargs)  # noqa: E501
            return data

    def get_worm_domain_with_http_info(self, worm_domain_id, **kwargs):  # noqa: E501
        """get_worm_domain  # noqa: E501

        View a single WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_worm_domain_with_http_info(worm_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str worm_domain_id: View a single WORM domain. (required)
        :return: WormDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['worm_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worm_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'worm_domain_id' is set
        if ('worm_domain_id' not in params or
                params['worm_domain_id'] is None):
            raise ValueError("Missing the required parameter `worm_domain_id` when calling `get_worm_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'worm_domain_id' in params:
            path_params['WormDomainId'] = params['worm_domain_id']  # noqa: E501

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
            '/platform/7/worm/domains/{WormDomainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WormDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_worm_settings(self, **kwargs):  # noqa: E501
        """get_worm_settings  # noqa: E501

        Get the global WORM settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_worm_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WormSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_worm_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_worm_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_worm_settings_with_http_info(self, **kwargs):  # noqa: E501
        """get_worm_settings  # noqa: E501

        Get the global WORM settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_worm_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WormSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_worm_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/platform/1/worm/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WormSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_worm_domains(self, **kwargs):  # noqa: E501
        """list_worm_domains  # noqa: E501

        List all WORM domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_worm_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The field that will be used for sorting.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: WormDomainsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_worm_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_worm_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_worm_domains_with_http_info(self, **kwargs):  # noqa: E501
        """list_worm_domains  # noqa: E501

        List all WORM domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_worm_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The field that will be used for sorting.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: WormDomainsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'limit', 'dir', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_worm_domains" % key
                )
            params[key] = val
        del params['kwargs']

        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `list_worm_domains`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `list_worm_domains`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_worm_domains`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_worm_domains`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `list_worm_domains`, length must be greater than or equal to `0`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_worm_domains`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_worm_domains`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

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
            '/platform/7/worm/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WormDomainsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_worm_domain(self, worm_domain, worm_domain_id, **kwargs):  # noqa: E501
        """update_worm_domain  # noqa: E501

        Modify a single WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_worm_domain(worm_domain, worm_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormDomain worm_domain: (required)
        :param str worm_domain_id: Modify a single WORM domain. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_worm_domain_with_http_info(worm_domain, worm_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_worm_domain_with_http_info(worm_domain, worm_domain_id, **kwargs)  # noqa: E501
            return data

    def update_worm_domain_with_http_info(self, worm_domain, worm_domain_id, **kwargs):  # noqa: E501
        """update_worm_domain  # noqa: E501

        Modify a single WORM domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_worm_domain_with_http_info(worm_domain, worm_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormDomain worm_domain: (required)
        :param str worm_domain_id: Modify a single WORM domain. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['worm_domain', 'worm_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_worm_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'worm_domain' is set
        if ('worm_domain' not in params or
                params['worm_domain'] is None):
            raise ValueError("Missing the required parameter `worm_domain` when calling `update_worm_domain`")  # noqa: E501
        # verify the required parameter 'worm_domain_id' is set
        if ('worm_domain_id' not in params or
                params['worm_domain_id'] is None):
            raise ValueError("Missing the required parameter `worm_domain_id` when calling `update_worm_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'worm_domain_id' in params:
            path_params['WormDomainId'] = params['worm_domain_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'worm_domain' in params:
            body_params = params['worm_domain']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/worm/domains/{WormDomainId}', 'PUT',
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

    def update_worm_settings(self, worm_settings, **kwargs):  # noqa: E501
        """update_worm_settings  # noqa: E501

        Modify the global WORM settings.  All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_worm_settings(worm_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormSettingsExtended worm_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_worm_settings_with_http_info(worm_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_worm_settings_with_http_info(worm_settings, **kwargs)  # noqa: E501
            return data

    def update_worm_settings_with_http_info(self, worm_settings, **kwargs):  # noqa: E501
        """update_worm_settings  # noqa: E501

        Modify the global WORM settings.  All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_worm_settings_with_http_info(worm_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WormSettingsExtended worm_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['worm_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_worm_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'worm_settings' is set
        if ('worm_settings' not in params or
                params['worm_settings'] is None):
            raise ValueError("Missing the required parameter `worm_settings` when calling `update_worm_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'worm_settings' in params:
            body_params = params['worm_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/worm/settings', 'PUT',
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
