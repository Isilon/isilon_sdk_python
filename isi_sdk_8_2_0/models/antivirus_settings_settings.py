# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AntivirusSettingsSettings(object):
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
        'fail_open': 'bool',
        'glob_filters': 'list[str]',
        'glob_filters_enabled': 'bool',
        'glob_filters_include': 'bool',
        'path_prefixes': 'list[str]',
        'quarantine': 'bool',
        'repair': 'bool',
        'report_expiry': 'int',
        'scan_cloudpool_files': 'bool',
        'scan_on_close': 'bool',
        'scan_on_open': 'bool',
        'scan_size_maximum': 'int',
        'service': 'bool',
        'truncate': 'bool'
    }

    attribute_map = {
        'fail_open': 'fail_open',
        'glob_filters': 'glob_filters',
        'glob_filters_enabled': 'glob_filters_enabled',
        'glob_filters_include': 'glob_filters_include',
        'path_prefixes': 'path_prefixes',
        'quarantine': 'quarantine',
        'repair': 'repair',
        'report_expiry': 'report_expiry',
        'scan_cloudpool_files': 'scan_cloudpool_files',
        'scan_on_close': 'scan_on_close',
        'scan_on_open': 'scan_on_open',
        'scan_size_maximum': 'scan_size_maximum',
        'service': 'service',
        'truncate': 'truncate'
    }

    def __init__(self, fail_open=None, glob_filters=None, glob_filters_enabled=None, glob_filters_include=None, path_prefixes=None, quarantine=None, repair=None, report_expiry=None, scan_cloudpool_files=None, scan_on_close=None, scan_on_open=None, scan_size_maximum=None, service=None, truncate=None):  # noqa: E501
        """AntivirusSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._fail_open = None
        self._glob_filters = None
        self._glob_filters_enabled = None
        self._glob_filters_include = None
        self._path_prefixes = None
        self._quarantine = None
        self._repair = None
        self._report_expiry = None
        self._scan_cloudpool_files = None
        self._scan_on_close = None
        self._scan_on_open = None
        self._scan_size_maximum = None
        self._service = None
        self._truncate = None
        self.discriminator = None

        self.fail_open = fail_open
        self.glob_filters = glob_filters
        self.glob_filters_enabled = glob_filters_enabled
        self.glob_filters_include = glob_filters_include
        self.path_prefixes = path_prefixes
        self.quarantine = quarantine
        self.repair = repair
        self.report_expiry = report_expiry
        self.scan_cloudpool_files = scan_cloudpool_files
        self.scan_on_close = scan_on_close
        self.scan_on_open = scan_on_open
        self.scan_size_maximum = scan_size_maximum
        self.service = service
        self.truncate = truncate

    @property
    def fail_open(self):
        """Gets the fail_open of this AntivirusSettingsSettings.  # noqa: E501

        Allow access when scanning fails.  # noqa: E501

        :return: The fail_open of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._fail_open

    @fail_open.setter
    def fail_open(self, fail_open):
        """Sets the fail_open of this AntivirusSettingsSettings.

        Allow access when scanning fails.  # noqa: E501

        :param fail_open: The fail_open of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if fail_open is None:
            raise ValueError("Invalid value for `fail_open`, must not be `None`")  # noqa: E501

        self._fail_open = fail_open

    @property
    def glob_filters(self):
        """Gets the glob_filters of this AntivirusSettingsSettings.  # noqa: E501

        Glob patterns for leaf filenames.  # noqa: E501

        :return: The glob_filters of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._glob_filters

    @glob_filters.setter
    def glob_filters(self, glob_filters):
        """Sets the glob_filters of this AntivirusSettingsSettings.

        Glob patterns for leaf filenames.  # noqa: E501

        :param glob_filters: The glob_filters of this AntivirusSettingsSettings.  # noqa: E501
        :type: list[str]
        """
        if glob_filters is None:
            raise ValueError("Invalid value for `glob_filters`, must not be `None`")  # noqa: E501

        self._glob_filters = glob_filters

    @property
    def glob_filters_enabled(self):
        """Gets the glob_filters_enabled of this AntivirusSettingsSettings.  # noqa: E501

        Enable glob filters.  # noqa: E501

        :return: The glob_filters_enabled of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._glob_filters_enabled

    @glob_filters_enabled.setter
    def glob_filters_enabled(self, glob_filters_enabled):
        """Sets the glob_filters_enabled of this AntivirusSettingsSettings.

        Enable glob filters.  # noqa: E501

        :param glob_filters_enabled: The glob_filters_enabled of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if glob_filters_enabled is None:
            raise ValueError("Invalid value for `glob_filters_enabled`, must not be `None`")  # noqa: E501

        self._glob_filters_enabled = glob_filters_enabled

    @property
    def glob_filters_include(self):
        """Gets the glob_filters_include of this AntivirusSettingsSettings.  # noqa: E501

        If true, only scan files matching a glob filter. If false, only scan files that don't match a glob filter.  # noqa: E501

        :return: The glob_filters_include of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._glob_filters_include

    @glob_filters_include.setter
    def glob_filters_include(self, glob_filters_include):
        """Sets the glob_filters_include of this AntivirusSettingsSettings.

        If true, only scan files matching a glob filter. If false, only scan files that don't match a glob filter.  # noqa: E501

        :param glob_filters_include: The glob_filters_include of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if glob_filters_include is None:
            raise ValueError("Invalid value for `glob_filters_include`, must not be `None`")  # noqa: E501

        self._glob_filters_include = glob_filters_include

    @property
    def path_prefixes(self):
        """Gets the path_prefixes of this AntivirusSettingsSettings.  # noqa: E501

        Paths to include in realtime scans.  # noqa: E501

        :return: The path_prefixes of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._path_prefixes

    @path_prefixes.setter
    def path_prefixes(self, path_prefixes):
        """Sets the path_prefixes of this AntivirusSettingsSettings.

        Paths to include in realtime scans.  # noqa: E501

        :param path_prefixes: The path_prefixes of this AntivirusSettingsSettings.  # noqa: E501
        :type: list[str]
        """
        if path_prefixes is None:
            raise ValueError("Invalid value for `path_prefixes`, must not be `None`")  # noqa: E501

        self._path_prefixes = path_prefixes

    @property
    def quarantine(self):
        """Gets the quarantine of this AntivirusSettingsSettings.  # noqa: E501

        Try to quarantine files when threats are found.  # noqa: E501

        :return: The quarantine of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._quarantine

    @quarantine.setter
    def quarantine(self, quarantine):
        """Sets the quarantine of this AntivirusSettingsSettings.

        Try to quarantine files when threats are found.  # noqa: E501

        :param quarantine: The quarantine of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if quarantine is None:
            raise ValueError("Invalid value for `quarantine`, must not be `None`")  # noqa: E501

        self._quarantine = quarantine

    @property
    def repair(self):
        """Gets the repair of this AntivirusSettingsSettings.  # noqa: E501

        Try to repair files when threats are found.  # noqa: E501

        :return: The repair of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._repair

    @repair.setter
    def repair(self, repair):
        """Sets the repair of this AntivirusSettingsSettings.

        Try to repair files when threats are found.  # noqa: E501

        :param repair: The repair of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if repair is None:
            raise ValueError("Invalid value for `repair`, must not be `None`")  # noqa: E501

        self._repair = repair

    @property
    def report_expiry(self):
        """Gets the report_expiry of this AntivirusSettingsSettings.  # noqa: E501

        Amount of time in seconds until old reporting data is purged.  # noqa: E501

        :return: The report_expiry of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_expiry

    @report_expiry.setter
    def report_expiry(self, report_expiry):
        """Sets the report_expiry of this AntivirusSettingsSettings.

        Amount of time in seconds until old reporting data is purged.  # noqa: E501

        :param report_expiry: The report_expiry of this AntivirusSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_expiry is None:
            raise ValueError("Invalid value for `report_expiry`, must not be `None`")  # noqa: E501
        if report_expiry is not None and report_expiry > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `report_expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if report_expiry is not None and report_expiry < 1:  # noqa: E501
            raise ValueError("Invalid value for `report_expiry`, must be a value greater than or equal to `1`")  # noqa: E501

        self._report_expiry = report_expiry

    @property
    def scan_cloudpool_files(self):
        """Gets the scan_cloudpool_files of this AntivirusSettingsSettings.  # noqa: E501

        Scan files stored in CloudPools.  # noqa: E501

        :return: The scan_cloudpool_files of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._scan_cloudpool_files

    @scan_cloudpool_files.setter
    def scan_cloudpool_files(self, scan_cloudpool_files):
        """Sets the scan_cloudpool_files of this AntivirusSettingsSettings.

        Scan files stored in CloudPools.  # noqa: E501

        :param scan_cloudpool_files: The scan_cloudpool_files of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if scan_cloudpool_files is None:
            raise ValueError("Invalid value for `scan_cloudpool_files`, must not be `None`")  # noqa: E501

        self._scan_cloudpool_files = scan_cloudpool_files

    @property
    def scan_on_close(self):
        """Gets the scan_on_close of this AntivirusSettingsSettings.  # noqa: E501

        Scan files when apps close them.  # noqa: E501

        :return: The scan_on_close of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._scan_on_close

    @scan_on_close.setter
    def scan_on_close(self, scan_on_close):
        """Sets the scan_on_close of this AntivirusSettingsSettings.

        Scan files when apps close them.  # noqa: E501

        :param scan_on_close: The scan_on_close of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if scan_on_close is None:
            raise ValueError("Invalid value for `scan_on_close`, must not be `None`")  # noqa: E501

        self._scan_on_close = scan_on_close

    @property
    def scan_on_open(self):
        """Gets the scan_on_open of this AntivirusSettingsSettings.  # noqa: E501

        Scan files on access.  # noqa: E501

        :return: The scan_on_open of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._scan_on_open

    @scan_on_open.setter
    def scan_on_open(self, scan_on_open):
        """Sets the scan_on_open of this AntivirusSettingsSettings.

        Scan files on access.  # noqa: E501

        :param scan_on_open: The scan_on_open of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if scan_on_open is None:
            raise ValueError("Invalid value for `scan_on_open`, must not be `None`")  # noqa: E501

        self._scan_on_open = scan_on_open

    @property
    def scan_size_maximum(self):
        """Gets the scan_size_maximum of this AntivirusSettingsSettings.  # noqa: E501

        Skip scanning files larger than this.  # noqa: E501

        :return: The scan_size_maximum of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._scan_size_maximum

    @scan_size_maximum.setter
    def scan_size_maximum(self, scan_size_maximum):
        """Sets the scan_size_maximum of this AntivirusSettingsSettings.

        Skip scanning files larger than this.  # noqa: E501

        :param scan_size_maximum: The scan_size_maximum of this AntivirusSettingsSettings.  # noqa: E501
        :type: int
        """
        if scan_size_maximum is None:
            raise ValueError("Invalid value for `scan_size_maximum`, must not be `None`")  # noqa: E501
        if scan_size_maximum is not None and scan_size_maximum > 2147483648:  # noqa: E501
            raise ValueError("Invalid value for `scan_size_maximum`, must be a value less than or equal to `2147483648`")  # noqa: E501
        if scan_size_maximum is not None and scan_size_maximum < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_size_maximum`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_size_maximum = scan_size_maximum

    @property
    def service(self):
        """Gets the service of this AntivirusSettingsSettings.  # noqa: E501

        Whether the antivirus service is enabled.  # noqa: E501

        :return: The service of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this AntivirusSettingsSettings.

        Whether the antivirus service is enabled.  # noqa: E501

        :param service: The service of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def truncate(self):
        """Gets the truncate of this AntivirusSettingsSettings.  # noqa: E501

        Try to truncate files when threats are found.  # noqa: E501

        :return: The truncate of this AntivirusSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._truncate

    @truncate.setter
    def truncate(self, truncate):
        """Sets the truncate of this AntivirusSettingsSettings.

        Try to truncate files when threats are found.  # noqa: E501

        :param truncate: The truncate of this AntivirusSettingsSettings.  # noqa: E501
        :type: bool
        """
        if truncate is None:
            raise ValueError("Invalid value for `truncate`, must not be `None`")  # noqa: E501

        self._truncate = truncate

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
        if not isinstance(other, AntivirusSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
