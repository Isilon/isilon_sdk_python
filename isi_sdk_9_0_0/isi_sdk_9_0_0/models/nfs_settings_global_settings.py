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


class NfsSettingsGlobalSettings(object):
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
        'nfsv3_enabled': 'bool',
        'nfsv4_enabled': 'bool',
        'rpc_maxthreads': 'int',
        'rpc_minthreads': 'int',
        'rquota_enabled': 'bool',
        'service': 'bool'
    }

    attribute_map = {
        'nfsv3_enabled': 'nfsv3_enabled',
        'nfsv4_enabled': 'nfsv4_enabled',
        'rpc_maxthreads': 'rpc_maxthreads',
        'rpc_minthreads': 'rpc_minthreads',
        'rquota_enabled': 'rquota_enabled',
        'service': 'service'
    }

    def __init__(self, nfsv3_enabled=None, nfsv4_enabled=None, rpc_maxthreads=None, rpc_minthreads=None, rquota_enabled=None, service=None):  # noqa: E501
        """NfsSettingsGlobalSettings - a model defined in Swagger"""  # noqa: E501

        self._nfsv3_enabled = None
        self._nfsv4_enabled = None
        self._rpc_maxthreads = None
        self._rpc_minthreads = None
        self._rquota_enabled = None
        self._service = None
        self.discriminator = None

        if nfsv3_enabled is not None:
            self.nfsv3_enabled = nfsv3_enabled
        if nfsv4_enabled is not None:
            self.nfsv4_enabled = nfsv4_enabled
        if rpc_maxthreads is not None:
            self.rpc_maxthreads = rpc_maxthreads
        if rpc_minthreads is not None:
            self.rpc_minthreads = rpc_minthreads
        if rquota_enabled is not None:
            self.rquota_enabled = rquota_enabled
        if service is not None:
            self.service = service

    @property
    def nfsv3_enabled(self):
        """Gets the nfsv3_enabled of this NfsSettingsGlobalSettings.  # noqa: E501

        True if NFSv3 is enabled.  # noqa: E501

        :return: The nfsv3_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv3_enabled

    @nfsv3_enabled.setter
    def nfsv3_enabled(self, nfsv3_enabled):
        """Sets the nfsv3_enabled of this NfsSettingsGlobalSettings.

        True if NFSv3 is enabled.  # noqa: E501

        :param nfsv3_enabled: The nfsv3_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv3_enabled = nfsv3_enabled

    @property
    def nfsv4_enabled(self):
        """Gets the nfsv4_enabled of this NfsSettingsGlobalSettings.  # noqa: E501

        True if NFSv4 is enabled.  # noqa: E501

        :return: The nfsv4_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_enabled

    @nfsv4_enabled.setter
    def nfsv4_enabled(self, nfsv4_enabled):
        """Sets the nfsv4_enabled of this NfsSettingsGlobalSettings.

        True if NFSv4 is enabled.  # noqa: E501

        :param nfsv4_enabled: The nfsv4_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_enabled = nfsv4_enabled

    @property
    def rpc_maxthreads(self):
        """Gets the rpc_maxthreads of this NfsSettingsGlobalSettings.  # noqa: E501

        Specifies the maximum number of threads in the nfsd thread pool.  # noqa: E501

        :return: The rpc_maxthreads of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._rpc_maxthreads

    @rpc_maxthreads.setter
    def rpc_maxthreads(self, rpc_maxthreads):
        """Sets the rpc_maxthreads of this NfsSettingsGlobalSettings.

        Specifies the maximum number of threads in the nfsd thread pool.  # noqa: E501

        :param rpc_maxthreads: The rpc_maxthreads of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: int
        """
        if rpc_maxthreads is not None and rpc_maxthreads > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `rpc_maxthreads`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if rpc_maxthreads is not None and rpc_maxthreads < 1:  # noqa: E501
            raise ValueError("Invalid value for `rpc_maxthreads`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rpc_maxthreads = rpc_maxthreads

    @property
    def rpc_minthreads(self):
        """Gets the rpc_minthreads of this NfsSettingsGlobalSettings.  # noqa: E501

        Specifies the minimum number of threads in the nfsd thread pool.  # noqa: E501

        :return: The rpc_minthreads of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._rpc_minthreads

    @rpc_minthreads.setter
    def rpc_minthreads(self, rpc_minthreads):
        """Sets the rpc_minthreads of this NfsSettingsGlobalSettings.

        Specifies the minimum number of threads in the nfsd thread pool.  # noqa: E501

        :param rpc_minthreads: The rpc_minthreads of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: int
        """
        if rpc_minthreads is not None and rpc_minthreads > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `rpc_minthreads`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if rpc_minthreads is not None and rpc_minthreads < 1:  # noqa: E501
            raise ValueError("Invalid value for `rpc_minthreads`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rpc_minthreads = rpc_minthreads

    @property
    def rquota_enabled(self):
        """Gets the rquota_enabled of this NfsSettingsGlobalSettings.  # noqa: E501

        True if the rquota protocol is enabled.  # noqa: E501

        :return: The rquota_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._rquota_enabled

    @rquota_enabled.setter
    def rquota_enabled(self, rquota_enabled):
        """Sets the rquota_enabled of this NfsSettingsGlobalSettings.

        True if the rquota protocol is enabled.  # noqa: E501

        :param rquota_enabled: The rquota_enabled of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._rquota_enabled = rquota_enabled

    @property
    def service(self):
        """Gets the service of this NfsSettingsGlobalSettings.  # noqa: E501

        True if the NFS service is enabled. When set to false, the NFS service is disabled.  # noqa: E501

        :return: The service of this NfsSettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this NfsSettingsGlobalSettings.

        True if the NFS service is enabled. When set to false, the NFS service is disabled.  # noqa: E501

        :param service: The service of this NfsSettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._service = service

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
        if not isinstance(other, NfsSettingsGlobalSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
