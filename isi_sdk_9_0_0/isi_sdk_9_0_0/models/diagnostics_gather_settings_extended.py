# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DiagnosticsGatherSettingsExtended(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'esrs': 'bool',
        'ftp_upload': 'bool',
        'ftp_upload_host': 'str',
        'ftp_upload_mode': 'str',
        'ftp_upload_pass': 'str',
        'ftp_upload_path': 'str',
        'ftp_upload_proxy': 'str',
        'ftp_upload_proxy_port': 'int',
        'ftp_upload_user': 'str',
        'gather_mode': 'str',
        'http_upload': 'bool',
        'http_upload_host': 'str',
        'http_upload_path': 'str',
        'http_upload_proxy': 'str',
        'http_upload_proxy_port': 'int',
        'upload': 'bool'
    }

    attribute_map = {
        'esrs': 'esrs',
        'ftp_upload': 'ftp_upload',
        'ftp_upload_host': 'ftp_upload_host',
        'ftp_upload_mode': 'ftp_upload_mode',
        'ftp_upload_pass': 'ftp_upload_pass',
        'ftp_upload_path': 'ftp_upload_path',
        'ftp_upload_proxy': 'ftp_upload_proxy',
        'ftp_upload_proxy_port': 'ftp_upload_proxy_port',
        'ftp_upload_user': 'ftp_upload_user',
        'gather_mode': 'gather_mode',
        'http_upload': 'http_upload',
        'http_upload_host': 'http_upload_host',
        'http_upload_path': 'http_upload_path',
        'http_upload_proxy': 'http_upload_proxy',
        'http_upload_proxy_port': 'http_upload_proxy_port',
        'upload': 'upload'
    }

    def __init__(self, esrs=None, ftp_upload=None, ftp_upload_host=None, ftp_upload_mode=None, ftp_upload_pass=None, ftp_upload_path=None, ftp_upload_proxy=None, ftp_upload_proxy_port=None, ftp_upload_user=None, gather_mode=None, http_upload=None, http_upload_host=None, http_upload_path=None, http_upload_proxy=None, http_upload_proxy_port=None, upload=None):  # noqa: E501
        """DiagnosticsGatherSettingsExtended - a model defined in Swagger"""  # noqa: E501

        self._esrs = None
        self._ftp_upload = None
        self._ftp_upload_host = None
        self._ftp_upload_mode = None
        self._ftp_upload_pass = None
        self._ftp_upload_path = None
        self._ftp_upload_proxy = None
        self._ftp_upload_proxy_port = None
        self._ftp_upload_user = None
        self._gather_mode = None
        self._http_upload = None
        self._http_upload_host = None
        self._http_upload_path = None
        self._http_upload_proxy = None
        self._http_upload_proxy_port = None
        self._upload = None
        self.discriminator = None

        if esrs is not None:
            self.esrs = esrs
        if ftp_upload is not None:
            self.ftp_upload = ftp_upload
        if ftp_upload_host is not None:
            self.ftp_upload_host = ftp_upload_host
        if ftp_upload_mode is not None:
            self.ftp_upload_mode = ftp_upload_mode
        if ftp_upload_pass is not None:
            self.ftp_upload_pass = ftp_upload_pass
        if ftp_upload_path is not None:
            self.ftp_upload_path = ftp_upload_path
        if ftp_upload_proxy is not None:
            self.ftp_upload_proxy = ftp_upload_proxy
        if ftp_upload_proxy_port is not None:
            self.ftp_upload_proxy_port = ftp_upload_proxy_port
        if ftp_upload_user is not None:
            self.ftp_upload_user = ftp_upload_user
        if gather_mode is not None:
            self.gather_mode = gather_mode
        if http_upload is not None:
            self.http_upload = http_upload
        if http_upload_host is not None:
            self.http_upload_host = http_upload_host
        if http_upload_path is not None:
            self.http_upload_path = http_upload_path
        if http_upload_proxy is not None:
            self.http_upload_proxy = http_upload_proxy
        if http_upload_proxy_port is not None:
            self.http_upload_proxy_port = http_upload_proxy_port
        if upload is not None:
            self.upload = upload

    @property
    def esrs(self):
        """Gets the esrs of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Use ESRS for upload of gather.  # noqa: E501

        :return: The esrs of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._esrs

    @esrs.setter
    def esrs(self, esrs):
        """Sets the esrs of this DiagnosticsGatherSettingsExtended.

        Use ESRS for upload of gather.  # noqa: E501

        :param esrs: The esrs of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._esrs = esrs

    @property
    def ftp_upload(self):
        """Gets the ftp_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Use FTP to upload logs from the isi gather command  # noqa: E501

        :return: The ftp_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._ftp_upload

    @ftp_upload.setter
    def ftp_upload(self, ftp_upload):
        """Sets the ftp_upload of this DiagnosticsGatherSettingsExtended.

        Use FTP to upload logs from the isi gather command  # noqa: E501

        :param ftp_upload: The ftp_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._ftp_upload = ftp_upload

    @property
    def ftp_upload_host(self):
        """Gets the ftp_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Alternate FTP host to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_host

    @ftp_upload_host.setter
    def ftp_upload_host(self, ftp_upload_host):
        """Sets the ftp_upload_host of this DiagnosticsGatherSettingsExtended.

        Alternate FTP host to use for FTP upload.  # noqa: E501

        :param ftp_upload_host: The ftp_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """
        if ftp_upload_host is not None and not re.search('(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', ftp_upload_host):  # noqa: E501
            raise ValueError("Invalid value for `ftp_upload_host`, must be a follow pattern or equal to `/(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._ftp_upload_host = ftp_upload_host

    @property
    def ftp_upload_mode(self):
        """Gets the ftp_upload_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        FTP upload mode.  # noqa: E501

        :return: The ftp_upload_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_mode

    @ftp_upload_mode.setter
    def ftp_upload_mode(self, ftp_upload_mode):
        """Sets the ftp_upload_mode of this DiagnosticsGatherSettingsExtended.

        FTP upload mode.  # noqa: E501

        :param ftp_upload_mode: The ftp_upload_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """

        self._ftp_upload_mode = ftp_upload_mode

    @property
    def ftp_upload_pass(self):
        """Gets the ftp_upload_pass of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        FTP password to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_pass of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_pass

    @ftp_upload_pass.setter
    def ftp_upload_pass(self, ftp_upload_pass):
        """Sets the ftp_upload_pass of this DiagnosticsGatherSettingsExtended.

        FTP password to use for FTP upload.  # noqa: E501

        :param ftp_upload_pass: The ftp_upload_pass of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """

        self._ftp_upload_pass = ftp_upload_pass

    @property
    def ftp_upload_path(self):
        """Gets the ftp_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Alternate FTP path to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_path

    @ftp_upload_path.setter
    def ftp_upload_path(self, ftp_upload_path):
        """Sets the ftp_upload_path of this DiagnosticsGatherSettingsExtended.

        Alternate FTP path to use for FTP upload.  # noqa: E501

        :param ftp_upload_path: The ftp_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """

        self._ftp_upload_path = ftp_upload_path

    @property
    def ftp_upload_proxy(self):
        """Gets the ftp_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Proxy server to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_proxy

    @ftp_upload_proxy.setter
    def ftp_upload_proxy(self, ftp_upload_proxy):
        """Sets the ftp_upload_proxy of this DiagnosticsGatherSettingsExtended.

        Proxy server to use for FTP upload.  # noqa: E501

        :param ftp_upload_proxy: The ftp_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """
        if ftp_upload_proxy is not None and not re.search('(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', ftp_upload_proxy):  # noqa: E501
            raise ValueError("Invalid value for `ftp_upload_proxy`, must be a follow pattern or equal to `/(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._ftp_upload_proxy = ftp_upload_proxy

    @property
    def ftp_upload_proxy_port(self):
        """Gets the ftp_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Proxy server port to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._ftp_upload_proxy_port

    @ftp_upload_proxy_port.setter
    def ftp_upload_proxy_port(self, ftp_upload_proxy_port):
        """Sets the ftp_upload_proxy_port of this DiagnosticsGatherSettingsExtended.

        Proxy server port to use for FTP upload.  # noqa: E501

        :param ftp_upload_proxy_port: The ftp_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: int
        """
        if ftp_upload_proxy_port is not None and ftp_upload_proxy_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `ftp_upload_proxy_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if ftp_upload_proxy_port is not None and ftp_upload_proxy_port < 1:  # noqa: E501
            raise ValueError("Invalid value for `ftp_upload_proxy_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ftp_upload_proxy_port = ftp_upload_proxy_port

    @property
    def ftp_upload_user(self):
        """Gets the ftp_upload_user of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        FTP user to use for FTP upload.  # noqa: E501

        :return: The ftp_upload_user of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ftp_upload_user

    @ftp_upload_user.setter
    def ftp_upload_user(self, ftp_upload_user):
        """Sets the ftp_upload_user of this DiagnosticsGatherSettingsExtended.

        FTP user to use for FTP upload.  # noqa: E501

        :param ftp_upload_user: The ftp_upload_user of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """

        self._ftp_upload_user = ftp_upload_user

    @property
    def gather_mode(self):
        """Gets the gather_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Set gather to full or incremental.  # noqa: E501

        :return: The gather_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._gather_mode

    @gather_mode.setter
    def gather_mode(self, gather_mode):
        """Sets the gather_mode of this DiagnosticsGatherSettingsExtended.

        Set gather to full or incremental.  # noqa: E501

        :param gather_mode: The gather_mode of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["full", "incremental"]  # noqa: E501
        if gather_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `gather_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(gather_mode, allowed_values)
            )

        self._gather_mode = gather_mode

    @property
    def http_upload(self):
        """Gets the http_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Use HTTP to upload logs from the isi gather command  # noqa: E501

        :return: The http_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._http_upload

    @http_upload.setter
    def http_upload(self, http_upload):
        """Sets the http_upload of this DiagnosticsGatherSettingsExtended.

        Use HTTP to upload logs from the isi gather command  # noqa: E501

        :param http_upload: The http_upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._http_upload = http_upload

    @property
    def http_upload_host(self):
        """Gets the http_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Address of an alternate HTTP host used to upload logs  # noqa: E501

        :return: The http_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._http_upload_host

    @http_upload_host.setter
    def http_upload_host(self, http_upload_host):
        """Sets the http_upload_host of this DiagnosticsGatherSettingsExtended.

        Address of an alternate HTTP host used to upload logs  # noqa: E501

        :param http_upload_host: The http_upload_host of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """
        if http_upload_host is not None and not re.search('(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', http_upload_host):  # noqa: E501
            raise ValueError("Invalid value for `http_upload_host`, must be a follow pattern or equal to `/(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._http_upload_host = http_upload_host

    @property
    def http_upload_path(self):
        """Gets the http_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Alternate path on HTTP server to use for HTTP upload.  # noqa: E501

        :return: The http_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._http_upload_path

    @http_upload_path.setter
    def http_upload_path(self, http_upload_path):
        """Sets the http_upload_path of this DiagnosticsGatherSettingsExtended.

        Alternate path on HTTP server to use for HTTP upload.  # noqa: E501

        :param http_upload_path: The http_upload_path of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """

        self._http_upload_path = http_upload_path

    @property
    def http_upload_proxy(self):
        """Gets the http_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Proxy server to use for HTTP upload.  # noqa: E501

        :return: The http_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._http_upload_proxy

    @http_upload_proxy.setter
    def http_upload_proxy(self, http_upload_proxy):
        """Sets the http_upload_proxy of this DiagnosticsGatherSettingsExtended.

        Proxy server to use for HTTP upload.  # noqa: E501

        :param http_upload_proxy: The http_upload_proxy of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: str
        """
        if http_upload_proxy is not None and not re.search('(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', http_upload_proxy):  # noqa: E501
            raise ValueError("Invalid value for `http_upload_proxy`, must be a follow pattern or equal to `/(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._http_upload_proxy = http_upload_proxy

    @property
    def http_upload_proxy_port(self):
        """Gets the http_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Proxy server port to use for HTTP upload.  # noqa: E501

        :return: The http_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._http_upload_proxy_port

    @http_upload_proxy_port.setter
    def http_upload_proxy_port(self, http_upload_proxy_port):
        """Sets the http_upload_proxy_port of this DiagnosticsGatherSettingsExtended.

        Proxy server port to use for HTTP upload.  # noqa: E501

        :param http_upload_proxy_port: The http_upload_proxy_port of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: int
        """
        if http_upload_proxy_port is not None and http_upload_proxy_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `http_upload_proxy_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if http_upload_proxy_port is not None and http_upload_proxy_port < 1:  # noqa: E501
            raise ValueError("Invalid value for `http_upload_proxy_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._http_upload_proxy_port = http_upload_proxy_port

    @property
    def upload(self):
        """Gets the upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501

        Upload gather to Dell EMC.  # noqa: E501

        :return: The upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this DiagnosticsGatherSettingsExtended.

        Upload gather to Dell EMC.  # noqa: E501

        :param upload: The upload of this DiagnosticsGatherSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._upload = upload

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DiagnosticsGatherSettingsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
