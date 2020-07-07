# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_0.api_client import ApiClient


class DedupeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_dedupe_dedupe_summary(self, **kwargs):  # noqa: E501
        """get_dedupe_dedupe_summary  # noqa: E501

        Return summary information about dedupe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_dedupe_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DedupeDedupeSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dedupe_dedupe_summary_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dedupe_dedupe_summary_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dedupe_dedupe_summary_with_http_info(self, **kwargs):  # noqa: E501
        """get_dedupe_dedupe_summary  # noqa: E501

        Return summary information about dedupe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_dedupe_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DedupeDedupeSummary
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
                    " to method get_dedupe_dedupe_summary" % key
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
            '/platform/1/dedupe/dedupe-summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DedupeDedupeSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dedupe_report(self, dedupe_report_id, **kwargs):  # noqa: E501
        """get_dedupe_report  # noqa: E501

        Retrieve a report for a single dedupe job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_report(dedupe_report_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dedupe_report_id: Retrieve a report for a single dedupe job. (required)
        :param str scope: If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned.
        :return: DedupeReports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dedupe_report_with_http_info(dedupe_report_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dedupe_report_with_http_info(dedupe_report_id, **kwargs)  # noqa: E501
            return data

    def get_dedupe_report_with_http_info(self, dedupe_report_id, **kwargs):  # noqa: E501
        """get_dedupe_report  # noqa: E501

        Retrieve a report for a single dedupe job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_report_with_http_info(dedupe_report_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dedupe_report_id: Retrieve a report for a single dedupe job. (required)
        :param str scope: If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned.
        :return: DedupeReports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dedupe_report_id', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dedupe_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dedupe_report_id' is set
        if ('dedupe_report_id' not in params or
                params['dedupe_report_id'] is None):
            raise ValueError("Missing the required parameter `dedupe_report_id` when calling `get_dedupe_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dedupe_report_id' in params:
            path_params['DedupeReportId'] = params['dedupe_report_id']  # noqa: E501

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
            '/platform/1/dedupe/reports/{DedupeReportId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DedupeReports',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dedupe_reports(self, **kwargs):  # noqa: E501
        """get_dedupe_reports  # noqa: E501

        List dedupe reports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_reports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The field that will be used for sorting.
        :param int begin: Restrict the query to reports at or after the given time, in seconds since the Epoch.
        :param int end: Restrict the query to reports at or before the given time, in seconds since the Epoch.
        :param int job_id: Restrict the query to the given job ID.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str job_type: Restrict the query to the given job type.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: DedupeReportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dedupe_reports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dedupe_reports_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dedupe_reports_with_http_info(self, **kwargs):  # noqa: E501
        """get_dedupe_reports  # noqa: E501

        List dedupe reports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_reports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The field that will be used for sorting.
        :param int begin: Restrict the query to reports at or after the given time, in seconds since the Epoch.
        :param int end: Restrict the query to reports at or before the given time, in seconds since the Epoch.
        :param int job_id: Restrict the query to the given job ID.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str job_type: Restrict the query to the given job type.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: DedupeReportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'begin', 'end', 'job_id', 'resume', 'job_type', 'limit', 'dir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dedupe_reports" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_dedupe_reports`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'begin' in params:
            query_params.append(('begin', params['begin']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'job_id' in params:
            query_params.append(('job_id', params['job_id']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'job_type' in params:
            query_params.append(('job_type', params['job_type']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501

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
            '/platform/1/dedupe/reports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DedupeReportsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dedupe_settings(self, **kwargs):  # noqa: E501
        """get_dedupe_settings  # noqa: E501

        Retrieve the dedupe settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DedupeSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dedupe_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dedupe_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dedupe_settings_with_http_info(self, **kwargs):  # noqa: E501
        """get_dedupe_settings  # noqa: E501

        Retrieve the dedupe settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dedupe_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DedupeSettings
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
                    " to method get_dedupe_settings" % key
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
            '/platform/1/dedupe/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DedupeSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dedupe_settings(self, dedupe_settings, **kwargs):  # noqa: E501
        """update_dedupe_settings  # noqa: E501

        Modify the dedupe settings. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dedupe_settings(dedupe_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DedupeSettingsExtended dedupe_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dedupe_settings_with_http_info(dedupe_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dedupe_settings_with_http_info(dedupe_settings, **kwargs)  # noqa: E501
            return data

    def update_dedupe_settings_with_http_info(self, dedupe_settings, **kwargs):  # noqa: E501
        """update_dedupe_settings  # noqa: E501

        Modify the dedupe settings. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dedupe_settings_with_http_info(dedupe_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DedupeSettingsExtended dedupe_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dedupe_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dedupe_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dedupe_settings' is set
        if ('dedupe_settings' not in params or
                params['dedupe_settings'] is None):
            raise ValueError("Missing the required parameter `dedupe_settings` when calling `update_dedupe_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dedupe_settings' in params:
            body_params = params['dedupe_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/dedupe/settings', 'PUT',
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
