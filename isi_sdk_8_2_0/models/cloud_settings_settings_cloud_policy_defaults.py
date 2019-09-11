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

from isi_sdk_8_2_0.models.cloud_settings_settings_cloud_policy_defaults_cache import CloudSettingsSettingsCloudPolicyDefaultsCache  # noqa: F401,E501


class CloudSettingsSettingsCloudPolicyDefaults(object):
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
        'archive_snapshot_files': 'bool',
        'cache': 'CloudSettingsSettingsCloudPolicyDefaultsCache',
        'compression': 'bool',
        'data_retention': 'int',
        'encryption': 'bool',
        'full_backup_retention': 'int',
        'incremental_backup_retention': 'int',
        'writeback_frequency': 'int'
    }

    attribute_map = {
        'archive_snapshot_files': 'archive_snapshot_files',
        'cache': 'cache',
        'compression': 'compression',
        'data_retention': 'data_retention',
        'encryption': 'encryption',
        'full_backup_retention': 'full_backup_retention',
        'incremental_backup_retention': 'incremental_backup_retention',
        'writeback_frequency': 'writeback_frequency'
    }

    def __init__(self, archive_snapshot_files=None, cache=None, compression=None, data_retention=None, encryption=None, full_backup_retention=None, incremental_backup_retention=None, writeback_frequency=None):  # noqa: E501
        """CloudSettingsSettingsCloudPolicyDefaults - a model defined in Swagger"""  # noqa: E501

        self._archive_snapshot_files = None
        self._cache = None
        self._compression = None
        self._data_retention = None
        self._encryption = None
        self._full_backup_retention = None
        self._incremental_backup_retention = None
        self._writeback_frequency = None
        self.discriminator = None

        if archive_snapshot_files is not None:
            self.archive_snapshot_files = archive_snapshot_files
        if cache is not None:
            self.cache = cache
        if compression is not None:
            self.compression = compression
        if data_retention is not None:
            self.data_retention = data_retention
        if encryption is not None:
            self.encryption = encryption
        if full_backup_retention is not None:
            self.full_backup_retention = full_backup_retention
        if incremental_backup_retention is not None:
            self.incremental_backup_retention = incremental_backup_retention
        if writeback_frequency is not None:
            self.writeback_frequency = writeback_frequency

    @property
    def archive_snapshot_files(self):
        """Gets the archive_snapshot_files of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        Specifies if files with snapshots should be archived.  # noqa: E501

        :return: The archive_snapshot_files of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: bool
        """
        return self._archive_snapshot_files

    @archive_snapshot_files.setter
    def archive_snapshot_files(self, archive_snapshot_files):
        """Sets the archive_snapshot_files of this CloudSettingsSettingsCloudPolicyDefaults.

        Specifies if files with snapshots should be archived.  # noqa: E501

        :param archive_snapshot_files: The archive_snapshot_files of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: bool
        """

        self._archive_snapshot_files = archive_snapshot_files

    @property
    def cache(self):
        """Gets the cache of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        Specifies default cloudpool cache settings for new filepool policies.  # noqa: E501

        :return: The cache of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: CloudSettingsSettingsCloudPolicyDefaultsCache
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this CloudSettingsSettingsCloudPolicyDefaults.

        Specifies default cloudpool cache settings for new filepool policies.  # noqa: E501

        :param cache: The cache of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: CloudSettingsSettingsCloudPolicyDefaultsCache
        """

        self._cache = cache

    @property
    def compression(self):
        """Gets the compression of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        Specifies if files should be compressed.  # noqa: E501

        :return: The compression of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: bool
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this CloudSettingsSettingsCloudPolicyDefaults.

        Specifies if files should be compressed.  # noqa: E501

        :param compression: The compression of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: bool
        """

        self._compression = compression

    @property
    def data_retention(self):
        """Gets the data_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        Specifies the minimum amount of time archived data will be retained in the cloud after deletion.  # noqa: E501

        :return: The data_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: int
        """
        return self._data_retention

    @data_retention.setter
    def data_retention(self, data_retention):
        """Sets the data_retention of this CloudSettingsSettingsCloudPolicyDefaults.

        Specifies the minimum amount of time archived data will be retained in the cloud after deletion.  # noqa: E501

        :param data_retention: The data_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: int
        """

        self._data_retention = data_retention

    @property
    def encryption(self):
        """Gets the encryption of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        Specifies if files should be encrypted.  # noqa: E501

        :return: The encryption of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: bool
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this CloudSettingsSettingsCloudPolicyDefaults.

        Specifies if files should be encrypted.  # noqa: E501

        :param encryption: The encryption of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: bool
        """

        self._encryption = encryption

    @property
    def full_backup_retention(self):
        """Gets the full_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        (Used with NDMP backups only.  Not applicable to SyncIQ.)  The minimum amount of time cloud files will be retained after the creation of a full NDMP backup.  # noqa: E501

        :return: The full_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: int
        """
        return self._full_backup_retention

    @full_backup_retention.setter
    def full_backup_retention(self, full_backup_retention):
        """Sets the full_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.

        (Used with NDMP backups only.  Not applicable to SyncIQ.)  The minimum amount of time cloud files will be retained after the creation of a full NDMP backup.  # noqa: E501

        :param full_backup_retention: The full_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: int
        """

        self._full_backup_retention = full_backup_retention

    @property
    def incremental_backup_retention(self):
        """Gets the incremental_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        (Used with SyncIQ and NDMP backups.)  The minimum amount of time cloud files will be retained after the creation of a SyncIQ backup or an incremental NDMP backup.  # noqa: E501

        :return: The incremental_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: int
        """
        return self._incremental_backup_retention

    @incremental_backup_retention.setter
    def incremental_backup_retention(self, incremental_backup_retention):
        """Sets the incremental_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.

        (Used with SyncIQ and NDMP backups.)  The minimum amount of time cloud files will be retained after the creation of a SyncIQ backup or an incremental NDMP backup.  # noqa: E501

        :param incremental_backup_retention: The incremental_backup_retention of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: int
        """

        self._incremental_backup_retention = incremental_backup_retention

    @property
    def writeback_frequency(self):
        """Gets the writeback_frequency of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501

        The minimum amount of time to wait before updating cloud data with local changes.  # noqa: E501

        :return: The writeback_frequency of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :rtype: int
        """
        return self._writeback_frequency

    @writeback_frequency.setter
    def writeback_frequency(self, writeback_frequency):
        """Sets the writeback_frequency of this CloudSettingsSettingsCloudPolicyDefaults.

        The minimum amount of time to wait before updating cloud data with local changes.  # noqa: E501

        :param writeback_frequency: The writeback_frequency of this CloudSettingsSettingsCloudPolicyDefaults.  # noqa: E501
        :type: int
        """

        self._writeback_frequency = writeback_frequency

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
        if not isinstance(other, CloudSettingsSettingsCloudPolicyDefaults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
