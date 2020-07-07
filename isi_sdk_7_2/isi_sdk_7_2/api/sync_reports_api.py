# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_7_2.api_client import ApiClient


class SyncReportsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_report_subreport(self, report_subreport_id, rid, **kwargs):  # noqa: E501
        """get_report_subreport  # noqa: E501

        View a single SyncIQ subreport.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_subreport(report_subreport_id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_subreport_id: View a single SyncIQ subreport. (required)
        :param str rid: (required)
        :return: ReportSubreports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_subreport_with_http_info(report_subreport_id, rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_subreport_with_http_info(report_subreport_id, rid, **kwargs)  # noqa: E501
            return data

    def get_report_subreport_with_http_info(self, report_subreport_id, rid, **kwargs):  # noqa: E501
        """get_report_subreport  # noqa: E501

        View a single SyncIQ subreport.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_subreport_with_http_info(report_subreport_id, rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_subreport_id: View a single SyncIQ subreport. (required)
        :param str rid: (required)
        :return: ReportSubreports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_subreport_id', 'rid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_subreport" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_subreport_id' is set
        if ('report_subreport_id' not in params or
                params['report_subreport_id'] is None):
            raise ValueError("Missing the required parameter `report_subreport_id` when calling `get_report_subreport`")  # noqa: E501
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_report_subreport`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'report_subreport_id' in params:
            path_params['ReportSubreportId'] = params['report_subreport_id']  # noqa: E501
        if 'rid' in params:
            path_params['Rid'] = params['rid']  # noqa: E501

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
            '/platform/1/sync/reports/{Rid}/subreports/{ReportSubreportId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportSubreports',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_report_subreports(self, rid, **kwargs):  # noqa: E501
        """get_report_subreports  # noqa: E501

        Get a list of SyncIQ subreports for a report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_subreports(rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rid: (required)
        :param str sort: The field that will be used for sorting.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int newer_than: Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago.
        :param str state: Filter the returned reports to include only those whose jobs are in this state.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: ReportSubreportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_subreports_with_http_info(rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_subreports_with_http_info(rid, **kwargs)  # noqa: E501
            return data

    def get_report_subreports_with_http_info(self, rid, **kwargs):  # noqa: E501
        """get_report_subreports  # noqa: E501

        Get a list of SyncIQ subreports for a report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_subreports_with_http_info(rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rid: (required)
        :param str sort: The field that will be used for sorting.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param int newer_than: Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago.
        :param str state: Filter the returned reports to include only those whose jobs are in this state.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :return: ReportSubreportsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rid', 'sort', 'resume', 'newer_than', 'state', 'limit', 'dir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_subreports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_report_subreports`")  # noqa: E501

        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_report_subreports`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'rid' in params:
            path_params['Rid'] = params['rid']  # noqa: E501

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'newer_than' in params:
            query_params.append(('newer_than', params['newer_than']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
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
            '/platform/1/sync/reports/{Rid}/subreports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportSubreportsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
