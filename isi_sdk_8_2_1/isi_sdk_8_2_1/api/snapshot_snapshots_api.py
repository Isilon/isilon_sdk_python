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


class SnapshotSnapshotsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_snapshot_lock(self, snapshot_lock, sid, **kwargs):  # noqa: E501
        """create_snapshot_lock  # noqa: E501

        Create a new lock on this snapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_snapshot_lock(snapshot_lock, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotLockCreateParams snapshot_lock: (required)
        :param str sid: (required)
        :return: CreateSnapshotLockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_snapshot_lock_with_http_info(snapshot_lock, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.create_snapshot_lock_with_http_info(snapshot_lock, sid, **kwargs)  # noqa: E501
            return data

    def create_snapshot_lock_with_http_info(self, snapshot_lock, sid, **kwargs):  # noqa: E501
        """create_snapshot_lock  # noqa: E501

        Create a new lock on this snapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_snapshot_lock_with_http_info(snapshot_lock, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotLockCreateParams snapshot_lock: (required)
        :param str sid: (required)
        :return: CreateSnapshotLockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_lock' is set
        if ('snapshot_lock' not in params or
                params['snapshot_lock'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock` when calling `create_snapshot_lock`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `create_snapshot_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'snapshot_lock' in params:
            body_params = params['snapshot_lock']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/snapshot/snapshots/{Sid}/locks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateSnapshotLockResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_snapshot_lock(self, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """delete_snapshot_lock  # noqa: E501

        Delete the snapshot lock.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_snapshot_lock(snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_lock_id: Delete the snapshot lock. (required)
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_snapshot_lock_with_http_info(snapshot_lock_id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_snapshot_lock_with_http_info(snapshot_lock_id, sid, **kwargs)  # noqa: E501
            return data

    def delete_snapshot_lock_with_http_info(self, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """delete_snapshot_lock  # noqa: E501

        Delete the snapshot lock.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_snapshot_lock_with_http_info(snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_lock_id: Delete the snapshot lock. (required)
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock_id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params or
                params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `delete_snapshot_lock`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `delete_snapshot_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']  # noqa: E501
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

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
            '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}', 'DELETE',
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

    def delete_snapshot_locks(self, sid, **kwargs):  # noqa: E501
        """delete_snapshot_locks  # noqa: E501

        Delete all locks. Will try to drain count of recursively held locks so that the snapshot can be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_snapshot_locks(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_snapshot_locks_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_snapshot_locks_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def delete_snapshot_locks_with_http_info(self, sid, **kwargs):  # noqa: E501
        """delete_snapshot_locks  # noqa: E501

        Delete all locks. Will try to drain count of recursively held locks so that the snapshot can be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_snapshot_locks_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_snapshot_locks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `delete_snapshot_locks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

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
            '/platform/1/snapshot/snapshots/{Sid}/locks', 'DELETE',
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

    def get_snapshot_lock(self, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """get_snapshot_lock  # noqa: E501

        Retrieve lock information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snapshot_lock(snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_lock_id: Retrieve lock information. (required)
        :param str sid: (required)
        :return: SnapshotLocks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_snapshot_lock_with_http_info(snapshot_lock_id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_snapshot_lock_with_http_info(snapshot_lock_id, sid, **kwargs)  # noqa: E501
            return data

    def get_snapshot_lock_with_http_info(self, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """get_snapshot_lock  # noqa: E501

        Retrieve lock information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snapshot_lock_with_http_info(snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_lock_id: Retrieve lock information. (required)
        :param str sid: (required)
        :return: SnapshotLocks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock_id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params or
                params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `get_snapshot_lock`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_snapshot_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']  # noqa: E501
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

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
            '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotLocks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_snapshot_locks(self, sid, **kwargs):  # noqa: E501
        """list_snapshot_locks  # noqa: E501

        List all locks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_snapshot_locks(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: (required)
        :param str sort: The field that will be used for sorting.  Choices are id, expires, and comment.  Default is id.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: SnapshotLocksExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_snapshot_locks_with_http_info(sid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_snapshot_locks_with_http_info(sid, **kwargs)  # noqa: E501
            return data

    def list_snapshot_locks_with_http_info(self, sid, **kwargs):  # noqa: E501
        """list_snapshot_locks  # noqa: E501

        List all locks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_snapshot_locks_with_http_info(sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sid: (required)
        :param str sort: The field that will be used for sorting.  Choices are id, expires, and comment.  Default is id.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: SnapshotLocksExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'sort', 'limit', 'dir', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_snapshot_locks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `list_snapshot_locks`")  # noqa: E501

        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_snapshot_locks`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_snapshot_locks`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `list_snapshot_locks`, length must be greater than or equal to `0`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_snapshot_locks`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_snapshot_locks`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

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
            '/platform/1/snapshot/snapshots/{Sid}/locks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotLocksExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_snapshot_lock(self, snapshot_lock, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """update_snapshot_lock  # noqa: E501

        Modify lock. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_snapshot_lock(snapshot_lock, snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotLock snapshot_lock: (required)
        :param str snapshot_lock_id: Modify lock. All input fields are optional, but one or more must be supplied. (required)
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_snapshot_lock_with_http_info(snapshot_lock, snapshot_lock_id, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_snapshot_lock_with_http_info(snapshot_lock, snapshot_lock_id, sid, **kwargs)  # noqa: E501
            return data

    def update_snapshot_lock_with_http_info(self, snapshot_lock, snapshot_lock_id, sid, **kwargs):  # noqa: E501
        """update_snapshot_lock  # noqa: E501

        Modify lock. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_snapshot_lock_with_http_info(snapshot_lock, snapshot_lock_id, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotLock snapshot_lock: (required)
        :param str snapshot_lock_id: Modify lock. All input fields are optional, but one or more must be supplied. (required)
        :param str sid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock', 'snapshot_lock_id', 'sid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_lock' is set
        if ('snapshot_lock' not in params or
                params['snapshot_lock'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock` when calling `update_snapshot_lock`")  # noqa: E501
        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params or
                params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `update_snapshot_lock`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `update_snapshot_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']  # noqa: E501
        if 'sid' in params:
            path_params['Sid'] = params['sid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'snapshot_lock' in params:
            body_params = params['snapshot_lock']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}', 'PUT',
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
