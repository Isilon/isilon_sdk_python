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


class FilepoolApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_filepool_policy(self, filepool_policy, **kwargs):  # noqa: E501
        """create_filepool_policy  # noqa: E501

        Create a new policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_filepool_policy(filepool_policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolPolicyCreateParams filepool_policy: (required)
        :return: CreateFilepoolPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_filepool_policy_with_http_info(filepool_policy, **kwargs)  # noqa: E501
        else:
            (data) = self.create_filepool_policy_with_http_info(filepool_policy, **kwargs)  # noqa: E501
            return data

    def create_filepool_policy_with_http_info(self, filepool_policy, **kwargs):  # noqa: E501
        """create_filepool_policy  # noqa: E501

        Create a new policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_filepool_policy_with_http_info(filepool_policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolPolicyCreateParams filepool_policy: (required)
        :return: CreateFilepoolPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_policy']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_filepool_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_policy' is set
        if ('filepool_policy' not in params or
                params['filepool_policy'] is None):
            raise ValueError("Missing the required parameter `filepool_policy` when calling `create_filepool_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filepool_policy' in params:
            body_params = params['filepool_policy']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/filepool/policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateFilepoolPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_filepool_policy(self, filepool_policy_id, **kwargs):  # noqa: E501
        """delete_filepool_policy  # noqa: E501

        Delete file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_filepool_policy(filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_policy_id: Delete file pool policy. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_filepool_policy_with_http_info(filepool_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_filepool_policy_with_http_info(filepool_policy_id, **kwargs)  # noqa: E501
            return data

    def delete_filepool_policy_with_http_info(self, filepool_policy_id, **kwargs):  # noqa: E501
        """delete_filepool_policy  # noqa: E501

        Delete file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_filepool_policy_with_http_info(filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_policy_id: Delete file pool policy. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_policy_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_filepool_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_policy_id' is set
        if ('filepool_policy_id' not in params or
                params['filepool_policy_id'] is None):
            raise ValueError("Missing the required parameter `filepool_policy_id` when calling `delete_filepool_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filepool_policy_id' in params:
            path_params['FilepoolPolicyId'] = params['filepool_policy_id']  # noqa: E501

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
            '/platform/4/filepool/policies/{FilepoolPolicyId}', 'DELETE',
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

    def get_filepool_default_policy(self, **kwargs):  # noqa: E501
        """get_filepool_default_policy  # noqa: E501

        List default file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_default_policy(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolDefaultPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_filepool_default_policy_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_filepool_default_policy_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_filepool_default_policy_with_http_info(self, **kwargs):  # noqa: E501
        """get_filepool_default_policy  # noqa: E501

        List default file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_default_policy_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolDefaultPolicy
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
                    " to method get_filepool_default_policy" % key
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
            '/platform/4/filepool/default-policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilepoolDefaultPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_filepool_policy(self, filepool_policy_id, **kwargs):  # noqa: E501
        """get_filepool_policy  # noqa: E501

        Retrieve file pool policy information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_policy(filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_policy_id: Retrieve file pool policy information. (required)
        :return: FilepoolPolicies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_filepool_policy_with_http_info(filepool_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_filepool_policy_with_http_info(filepool_policy_id, **kwargs)  # noqa: E501
            return data

    def get_filepool_policy_with_http_info(self, filepool_policy_id, **kwargs):  # noqa: E501
        """get_filepool_policy  # noqa: E501

        Retrieve file pool policy information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_policy_with_http_info(filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_policy_id: Retrieve file pool policy information. (required)
        :return: FilepoolPolicies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_policy_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_filepool_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_policy_id' is set
        if ('filepool_policy_id' not in params or
                params['filepool_policy_id'] is None):
            raise ValueError("Missing the required parameter `filepool_policy_id` when calling `get_filepool_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filepool_policy_id' in params:
            path_params['FilepoolPolicyId'] = params['filepool_policy_id']  # noqa: E501

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
            '/platform/4/filepool/policies/{FilepoolPolicyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilepoolPolicies',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_filepool_template(self, filepool_template_id, **kwargs):  # noqa: E501
        """get_filepool_template  # noqa: E501

        List all templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_template(filepool_template_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_template_id: List all templates. (required)
        :return: FilepoolTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_filepool_template_with_http_info(filepool_template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_filepool_template_with_http_info(filepool_template_id, **kwargs)  # noqa: E501
            return data

    def get_filepool_template_with_http_info(self, filepool_template_id, **kwargs):  # noqa: E501
        """get_filepool_template  # noqa: E501

        List all templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_template_with_http_info(filepool_template_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str filepool_template_id: List all templates. (required)
        :return: FilepoolTemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_template_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_filepool_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_template_id' is set
        if ('filepool_template_id' not in params or
                params['filepool_template_id'] is None):
            raise ValueError("Missing the required parameter `filepool_template_id` when calling `get_filepool_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filepool_template_id' in params:
            path_params['FilepoolTemplateId'] = params['filepool_template_id']  # noqa: E501

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
            '/platform/4/filepool/templates/{FilepoolTemplateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilepoolTemplates',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_filepool_templates(self, **kwargs):  # noqa: E501
        """get_filepool_templates  # noqa: E501

        List all templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_templates(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolTemplatesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_filepool_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_filepool_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_filepool_templates_with_http_info(self, **kwargs):  # noqa: E501
        """get_filepool_templates  # noqa: E501

        List all templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_filepool_templates_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolTemplatesExtended
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
                    " to method get_filepool_templates" % key
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
            '/platform/4/filepool/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilepoolTemplatesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_filepool_policies(self, **kwargs):  # noqa: E501
        """list_filepool_policies  # noqa: E501

        List all policies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_filepool_policies(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolPoliciesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_filepool_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_filepool_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_filepool_policies_with_http_info(self, **kwargs):  # noqa: E501
        """list_filepool_policies  # noqa: E501

        List all policies.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_filepool_policies_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FilepoolPoliciesExtended
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
                    " to method list_filepool_policies" % key
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
            '/platform/4/filepool/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilepoolPoliciesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_filepool_default_policy(self, filepool_default_policy, **kwargs):  # noqa: E501
        """update_filepool_default_policy  # noqa: E501

        Set default file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_filepool_default_policy(filepool_default_policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolDefaultPolicyExtended filepool_default_policy: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_filepool_default_policy_with_http_info(filepool_default_policy, **kwargs)  # noqa: E501
        else:
            (data) = self.update_filepool_default_policy_with_http_info(filepool_default_policy, **kwargs)  # noqa: E501
            return data

    def update_filepool_default_policy_with_http_info(self, filepool_default_policy, **kwargs):  # noqa: E501
        """update_filepool_default_policy  # noqa: E501

        Set default file pool policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_filepool_default_policy_with_http_info(filepool_default_policy, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolDefaultPolicyExtended filepool_default_policy: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_default_policy']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_filepool_default_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_default_policy' is set
        if ('filepool_default_policy' not in params or
                params['filepool_default_policy'] is None):
            raise ValueError("Missing the required parameter `filepool_default_policy` when calling `update_filepool_default_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filepool_default_policy' in params:
            body_params = params['filepool_default_policy']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/filepool/default-policy', 'PUT',
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

    def update_filepool_policy(self, filepool_policy, filepool_policy_id, **kwargs):  # noqa: E501
        """update_filepool_policy  # noqa: E501

        Modify file pool policy. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_filepool_policy(filepool_policy, filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolPolicy filepool_policy: (required)
        :param str filepool_policy_id: Modify file pool policy. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_filepool_policy_with_http_info(filepool_policy, filepool_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_filepool_policy_with_http_info(filepool_policy, filepool_policy_id, **kwargs)  # noqa: E501
            return data

    def update_filepool_policy_with_http_info(self, filepool_policy, filepool_policy_id, **kwargs):  # noqa: E501
        """update_filepool_policy  # noqa: E501

        Modify file pool policy. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_filepool_policy_with_http_info(filepool_policy, filepool_policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param FilepoolPolicy filepool_policy: (required)
        :param str filepool_policy_id: Modify file pool policy. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filepool_policy', 'filepool_policy_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_filepool_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filepool_policy' is set
        if ('filepool_policy' not in params or
                params['filepool_policy'] is None):
            raise ValueError("Missing the required parameter `filepool_policy` when calling `update_filepool_policy`")  # noqa: E501
        # verify the required parameter 'filepool_policy_id' is set
        if ('filepool_policy_id' not in params or
                params['filepool_policy_id'] is None):
            raise ValueError("Missing the required parameter `filepool_policy_id` when calling `update_filepool_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filepool_policy_id' in params:
            path_params['FilepoolPolicyId'] = params['filepool_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filepool_policy' in params:
            body_params = params['filepool_policy']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/filepool/policies/{FilepoolPolicyId}', 'PUT',
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
