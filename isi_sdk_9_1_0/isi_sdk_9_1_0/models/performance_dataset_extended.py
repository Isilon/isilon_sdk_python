# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_9_1_0.models.performance_dataset import PerformanceDataset  # noqa: F401,E501


class PerformanceDatasetExtended(object):
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
        'name': 'str',
        'creation_time': 'int',
        'filter_count': 'int',
        'filters': 'list[str]',
        'id': 'int',
        'metrics': 'list[str]',
        'note': 'str',
        'statkey': 'str',
        'workload_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'creation_time': 'creation_time',
        'filter_count': 'filter_count',
        'filters': 'filters',
        'id': 'id',
        'metrics': 'metrics',
        'note': 'note',
        'statkey': 'statkey',
        'workload_count': 'workload_count'
    }

    def __init__(self, name=None, creation_time=None, filter_count=None, filters=None, id=None, metrics=None, note=None, statkey=None, workload_count=None):  # noqa: E501
        """PerformanceDatasetExtended - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._creation_time = None
        self._filter_count = None
        self._filters = None
        self._id = None
        self._metrics = None
        self._note = None
        self._statkey = None
        self._workload_count = None
        self.discriminator = None

        self.name = name
        self.creation_time = creation_time
        self.filter_count = filter_count
        self.filters = filters
        self.id = id
        self.metrics = metrics
        if note is not None:
            self.note = note
        self.statkey = statkey
        self.workload_count = workload_count

    @property
    def name(self):
        """Gets the name of this PerformanceDatasetExtended.  # noqa: E501

        The name of the performance dataset. If a name is not specified then a default name is assigned. The default name will be an underscore separated list of the performance metrics and filters used to configure the dataset.  # noqa: E501

        :return: The name of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PerformanceDatasetExtended.

        The name of the performance dataset. If a name is not specified then a default name is assigned. The default name will be an underscore separated list of the performance metrics and filters used to configure the dataset.  # noqa: E501

        :param name: The name of this PerformanceDatasetExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this PerformanceDatasetExtended.  # noqa: E501

        Timestamp of when the dataset was created.  # noqa: E501

        :return: The creation_time of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this PerformanceDatasetExtended.

        Timestamp of when the dataset was created.  # noqa: E501

        :param creation_time: The creation_time of this PerformanceDatasetExtended.  # noqa: E501
        :type: int
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501
        if creation_time is not None and creation_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `creation_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if creation_time is not None and creation_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `creation_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def filter_count(self):
        """Gets the filter_count of this PerformanceDatasetExtended.  # noqa: E501

        Number of filters applied to this dataset.  # noqa: E501

        :return: The filter_count of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: int
        """
        return self._filter_count

    @filter_count.setter
    def filter_count(self, filter_count):
        """Sets the filter_count of this PerformanceDatasetExtended.

        Number of filters applied to this dataset.  # noqa: E501

        :param filter_count: The filter_count of this PerformanceDatasetExtended.  # noqa: E501
        :type: int
        """
        if filter_count is None:
            raise ValueError("Invalid value for `filter_count`, must not be `None`")  # noqa: E501
        if filter_count is not None and filter_count > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `filter_count`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if filter_count is not None and filter_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `filter_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._filter_count = filter_count

    @property
    def filters(self):
        """Gets the filters of this PerformanceDatasetExtended.  # noqa: E501

        Filtered metrics for configuring this dataset.  # noqa: E501

        :return: The filters of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this PerformanceDatasetExtended.

        Filtered metrics for configuring this dataset.  # noqa: E501

        :param filters: The filters of this PerformanceDatasetExtended.  # noqa: E501
        :type: list[str]
        """
        if filters is None:
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501
        allowed_values = ["groupname", "local_address", "path", "protocol", "remote_address", "share_name", "username", "zone_name", "job_type", "system_name", "export_id"]  # noqa: E501
        if not set(filters).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `filters` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(filters) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._filters = filters

    @property
    def id(self):
        """Gets the id of this PerformanceDatasetExtended.  # noqa: E501

        Unique identifier for the configured dataset.  # noqa: E501

        :return: The id of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceDatasetExtended.

        Unique identifier for the configured dataset.  # noqa: E501

        :param id: The id of this PerformanceDatasetExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def metrics(self):
        """Gets the metrics of this PerformanceDatasetExtended.  # noqa: E501

        Performance metrics defining the dataset.  # noqa: E501

        :return: The metrics of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this PerformanceDatasetExtended.

        Performance metrics defining the dataset.  # noqa: E501

        :param metrics: The metrics of this PerformanceDatasetExtended.  # noqa: E501
        :type: list[str]
        """
        if metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501
        allowed_values = ["groupname", "local_address", "path", "protocol", "remote_address", "share_name", "username", "zone_name", "job_type", "system_name", "export_id"]  # noqa: E501
        if not set(metrics).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `metrics` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(metrics) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._metrics = metrics

    @property
    def note(self):
        """Gets the note of this PerformanceDatasetExtended.  # noqa: E501

        Additional information about this dataset  # noqa: E501

        :return: The note of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PerformanceDatasetExtended.

        Additional information about this dataset  # noqa: E501

        :param note: The note of this PerformanceDatasetExtended.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 255:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `255`")  # noqa: E501
        if note is not None and len(note) < 1:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `1`")  # noqa: E501

        self._note = note

    @property
    def statkey(self):
        """Gets the statkey of this PerformanceDatasetExtended.  # noqa: E501

        Key for use in viewing associated raw statistics under the endpoints /statistics/history and /statistics/current.  # noqa: E501

        :return: The statkey of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: str
        """
        return self._statkey

    @statkey.setter
    def statkey(self, statkey):
        """Sets the statkey of this PerformanceDatasetExtended.

        Key for use in viewing associated raw statistics under the endpoints /statistics/history and /statistics/current.  # noqa: E501

        :param statkey: The statkey of this PerformanceDatasetExtended.  # noqa: E501
        :type: str
        """
        if statkey is None:
            raise ValueError("Invalid value for `statkey`, must not be `None`")  # noqa: E501
        if statkey is not None and len(statkey) > 29:
            raise ValueError("Invalid value for `statkey`, length must be less than or equal to `29`")  # noqa: E501
        if statkey is not None and len(statkey) < 29:
            raise ValueError("Invalid value for `statkey`, length must be greater than or equal to `29`")  # noqa: E501

        self._statkey = statkey

    @property
    def workload_count(self):
        """Gets the workload_count of this PerformanceDatasetExtended.  # noqa: E501

        Number of workloads pinned to this dataset.  # noqa: E501

        :return: The workload_count of this PerformanceDatasetExtended.  # noqa: E501
        :rtype: int
        """
        return self._workload_count

    @workload_count.setter
    def workload_count(self, workload_count):
        """Sets the workload_count of this PerformanceDatasetExtended.

        Number of workloads pinned to this dataset.  # noqa: E501

        :param workload_count: The workload_count of this PerformanceDatasetExtended.  # noqa: E501
        :type: int
        """
        if workload_count is None:
            raise ValueError("Invalid value for `workload_count`, must not be `None`")  # noqa: E501
        if workload_count is not None and workload_count > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `workload_count`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if workload_count is not None and workload_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `workload_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._workload_count = workload_count

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
        if not isinstance(other, PerformanceDatasetExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
