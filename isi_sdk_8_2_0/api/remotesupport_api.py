# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_2_0.api_client import ApiClient


class RemotesupportApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_remotesupport_connectemc(self, **kwargs):  # noqa: E501
        """get_remotesupport_connectemc  # noqa: E501

        List all settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_remotesupport_connectemc(async=True)
        >>> result = thread.get()

        :param async bool
        :return: RemotesupportConnectemc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_remotesupport_connectemc_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_remotesupport_connectemc_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_remotesupport_connectemc_with_http_info(self, **kwargs):  # noqa: E501
        """get_remotesupport_connectemc  # noqa: E501

        List all settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_remotesupport_connectemc_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: RemotesupportConnectemc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_remotesupport_connectemc" % key
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
            '/platform/1/remotesupport/connectemc', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemotesupportConnectemc',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_remotesupport_connectemc(self, remotesupport_connectemc, **kwargs):  # noqa: E501
        """update_remotesupport_connectemc  # noqa: E501

        Modify one or more settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_remotesupport_connectemc(remotesupport_connectemc, async=True)
        >>> result = thread.get()

        :param async bool
        :param RemotesupportConnectemcConnectemc remotesupport_connectemc: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_remotesupport_connectemc_with_http_info(remotesupport_connectemc, **kwargs)  # noqa: E501
        else:
            (data) = self.update_remotesupport_connectemc_with_http_info(remotesupport_connectemc, **kwargs)  # noqa: E501
            return data

    def update_remotesupport_connectemc_with_http_info(self, remotesupport_connectemc, **kwargs):  # noqa: E501
        """update_remotesupport_connectemc  # noqa: E501

        Modify one or more settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_remotesupport_connectemc_with_http_info(remotesupport_connectemc, async=True)
        >>> result = thread.get()

        :param async bool
        :param RemotesupportConnectemcConnectemc remotesupport_connectemc: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['remotesupport_connectemc']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_remotesupport_connectemc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'remotesupport_connectemc' is set
        if ('remotesupport_connectemc' not in params or
                params['remotesupport_connectemc'] is None):
            raise ValueError("Missing the required parameter `remotesupport_connectemc` when calling `update_remotesupport_connectemc`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'remotesupport_connectemc' in params:
            body_params = params['remotesupport_connectemc']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/remotesupport/connectemc', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
