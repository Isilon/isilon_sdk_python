# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class HdfsSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HdfsSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ambari_namenode': 'str',
            'ambari_server': 'str',
            'authentication_mode': 'str',
            'default_block_size': 'int',
            'default_checksum_type': 'str',
            'odp_version': 'str',
            'root_directory': 'str',
            'service': 'bool',
            'webhdfs_enabled': 'bool'
        }

        self.attribute_map = {
            'ambari_namenode': 'ambari_namenode',
            'ambari_server': 'ambari_server',
            'authentication_mode': 'authentication_mode',
            'default_block_size': 'default_block_size',
            'default_checksum_type': 'default_checksum_type',
            'odp_version': 'odp_version',
            'root_directory': 'root_directory',
            'service': 'service',
            'webhdfs_enabled': 'webhdfs_enabled'
        }

        self._ambari_namenode = None
        self._ambari_server = None
        self._authentication_mode = None
        self._default_block_size = None
        self._default_checksum_type = None
        self._odp_version = None
        self._root_directory = None
        self._service = None
        self._webhdfs_enabled = None

    @property
    def ambari_namenode(self):
        """
        Gets the ambari_namenode of this HdfsSettingsSettings.
        NameNode of Ambari server

        :return: The ambari_namenode of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._ambari_namenode

    @ambari_namenode.setter
    def ambari_namenode(self, ambari_namenode):
        """
        Sets the ambari_namenode of this HdfsSettingsSettings.
        NameNode of Ambari server

        :param ambari_namenode: The ambari_namenode of this HdfsSettingsSettings.
        :type: str
        """
        
        self._ambari_namenode = ambari_namenode

    @property
    def ambari_server(self):
        """
        Gets the ambari_server of this HdfsSettingsSettings.
        Ambari server

        :return: The ambari_server of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._ambari_server

    @ambari_server.setter
    def ambari_server(self, ambari_server):
        """
        Sets the ambari_server of this HdfsSettingsSettings.
        Ambari server

        :param ambari_server: The ambari_server of this HdfsSettingsSettings.
        :type: str
        """
        
        self._ambari_server = ambari_server

    @property
    def authentication_mode(self):
        """
        Gets the authentication_mode of this HdfsSettingsSettings.
        Type of authentication for HDFS protocol.

        :return: The authentication_mode of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._authentication_mode

    @authentication_mode.setter
    def authentication_mode(self, authentication_mode):
        """
        Sets the authentication_mode of this HdfsSettingsSettings.
        Type of authentication for HDFS protocol.

        :param authentication_mode: The authentication_mode of this HdfsSettingsSettings.
        :type: str
        """
        allowed_values = ["all", "simple_only", "kerberos_only"]
        if authentication_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._authentication_mode = authentication_mode

    @property
    def default_block_size(self):
        """
        Gets the default_block_size of this HdfsSettingsSettings.
        Block size (size=2**value) reported by HDFS server.

        :return: The default_block_size of this HdfsSettingsSettings.
        :rtype: int
        """
        return self._default_block_size

    @default_block_size.setter
    def default_block_size(self, default_block_size):
        """
        Sets the default_block_size of this HdfsSettingsSettings.
        Block size (size=2**value) reported by HDFS server.

        :param default_block_size: The default_block_size of this HdfsSettingsSettings.
        :type: int
        """
        
        self._default_block_size = default_block_size

    @property
    def default_checksum_type(self):
        """
        Gets the default_checksum_type of this HdfsSettingsSettings.
        Checksum type reported by HDFS server.

        :return: The default_checksum_type of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._default_checksum_type

    @default_checksum_type.setter
    def default_checksum_type(self, default_checksum_type):
        """
        Sets the default_checksum_type of this HdfsSettingsSettings.
        Checksum type reported by HDFS server.

        :param default_checksum_type: The default_checksum_type of this HdfsSettingsSettings.
        :type: str
        """
        allowed_values = ["none", "crc32", "crc32c"]
        if default_checksum_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_checksum_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._default_checksum_type = default_checksum_type

    @property
    def odp_version(self):
        """
        Gets the odp_version of this HdfsSettingsSettings.
        ODP stack repository version number

        :return: The odp_version of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._odp_version

    @odp_version.setter
    def odp_version(self, odp_version):
        """
        Sets the odp_version of this HdfsSettingsSettings.
        ODP stack repository version number

        :param odp_version: The odp_version of this HdfsSettingsSettings.
        :type: str
        """
        
        self._odp_version = odp_version

    @property
    def root_directory(self):
        """
        Gets the root_directory of this HdfsSettingsSettings.
        HDFS root directory

        :return: The root_directory of this HdfsSettingsSettings.
        :rtype: str
        """
        return self._root_directory

    @root_directory.setter
    def root_directory(self, root_directory):
        """
        Sets the root_directory of this HdfsSettingsSettings.
        HDFS root directory

        :param root_directory: The root_directory of this HdfsSettingsSettings.
        :type: str
        """
        
        self._root_directory = root_directory

    @property
    def service(self):
        """
        Gets the service of this HdfsSettingsSettings.
        Enable or disable the HDFS service.

        :return: The service of this HdfsSettingsSettings.
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this HdfsSettingsSettings.
        Enable or disable the HDFS service.

        :param service: The service of this HdfsSettingsSettings.
        :type: bool
        """
        
        self._service = service

    @property
    def webhdfs_enabled(self):
        """
        Gets the webhdfs_enabled of this HdfsSettingsSettings.
        Enable or disable WebHDFS

        :return: The webhdfs_enabled of this HdfsSettingsSettings.
        :rtype: bool
        """
        return self._webhdfs_enabled

    @webhdfs_enabled.setter
    def webhdfs_enabled(self, webhdfs_enabled):
        """
        Sets the webhdfs_enabled of this HdfsSettingsSettings.
        Enable or disable WebHDFS

        :param webhdfs_enabled: The webhdfs_enabled of this HdfsSettingsSettings.
        :type: bool
        """
        
        self._webhdfs_enabled = webhdfs_enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

