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

from isi_sdk_9_0_0.models.event_alert_conditions_alert_condition import EventAlertConditionsAlertCondition  # noqa: F401,E501


class EventAlertConditionCreateParams(object):
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
        'categories': 'list[str]',
        'channels': 'list[str]',
        'condition': 'str',
        'eventgroup_ids': 'list[str]',
        'id': 'str',
        'interval': 'int',
        'limit': 'int',
        'name': 'str',
        'severities': 'list[str]',
        'transient': 'int'
    }

    attribute_map = {
        'categories': 'categories',
        'channels': 'channels',
        'condition': 'condition',
        'eventgroup_ids': 'eventgroup_ids',
        'id': 'id',
        'interval': 'interval',
        'limit': 'limit',
        'name': 'name',
        'severities': 'severities',
        'transient': 'transient'
    }

    def __init__(self, categories=None, channels=None, condition=None, eventgroup_ids=None, id=None, interval=None, limit=None, name=None, severities=None, transient=None):  # noqa: E501
        """EventAlertConditionCreateParams - a model defined in Swagger"""  # noqa: E501

        self._categories = None
        self._channels = None
        self._condition = None
        self._eventgroup_ids = None
        self._id = None
        self._interval = None
        self._limit = None
        self._name = None
        self._severities = None
        self._transient = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        self.channels = channels
        self.condition = condition
        if eventgroup_ids is not None:
            self.eventgroup_ids = eventgroup_ids
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if limit is not None:
            self.limit = limit
        self.name = name
        if severities is not None:
            self.severities = severities
        if transient is not None:
            self.transient = transient

    @property
    def categories(self):
        """Gets the categories of this EventAlertConditionCreateParams.  # noqa: E501

        Event Group categories to be alerted: all, 100000000 (SYS_DISK_EVENTS), 200000000 (NODE_STATUS_EVENTS), 300000000 (REBOOT_EVENTS), 400000000 (SW_EVENTS), 500000000 (QUOTA_EVENTS), 600000000 (SNAP_EVENTS), 700000000 (WINNET_EVENTS), 800000000 (FILESYS_EVENTS), 900000000 (HW_EVENTS), 1100000000 (CPOOL_EVENTS).  # noqa: E501

        :return: The categories of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this EventAlertConditionCreateParams.

        Event Group categories to be alerted: all, 100000000 (SYS_DISK_EVENTS), 200000000 (NODE_STATUS_EVENTS), 300000000 (REBOOT_EVENTS), 400000000 (SW_EVENTS), 500000000 (QUOTA_EVENTS), 600000000 (SNAP_EVENTS), 700000000 (WINNET_EVENTS), 800000000 (FILESYS_EVENTS), 900000000 (HW_EVENTS), 1100000000 (CPOOL_EVENTS).  # noqa: E501

        :param categories: The categories of this EventAlertConditionCreateParams.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all", "SYS_DISK_EVENTS", "100000000", "NODE_STATUS_EVENTS", "200000000", "REBOOT_EVENTS", "300000000", "SW_EVENTS", "400000000", "QUOTA_EVENTS", "500000000", "SNAP_EVENTS", "600000000", "WINNET_EVENTS", "700000000", "FILESYS_EVENTS", "800000000", "HW_EVENTS", "900000000", "CPOOL_EVENTS", "1100000000"]  # noqa: E501
        if not set(categories).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `categories` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(categories) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._categories = categories

    @property
    def channels(self):
        """Gets the channels of this EventAlertConditionCreateParams.  # noqa: E501

        Channels for alert.  # noqa: E501

        :return: The channels of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this EventAlertConditionCreateParams.

        Channels for alert.  # noqa: E501

        :param channels: The channels of this EventAlertConditionCreateParams.  # noqa: E501
        :type: list[str]
        """
        if channels is None:
            raise ValueError("Invalid value for `channels`, must not be `None`")  # noqa: E501

        self._channels = channels

    @property
    def condition(self):
        """Gets the condition of this EventAlertConditionCreateParams.  # noqa: E501

        Trigger condition for alert.  # noqa: E501

        :return: The condition of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this EventAlertConditionCreateParams.

        Trigger condition for alert.  # noqa: E501

        :param condition: The condition of this EventAlertConditionCreateParams.  # noqa: E501
        :type: str
        """
        if condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501
        allowed_values = ["NEW", "NEW EVENTS", "ONGOING", "SEVERITY INCREASE", "SEVERITY DECREASE", "RESOLVED"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def eventgroup_ids(self):
        """Gets the eventgroup_ids of this EventAlertConditionCreateParams.  # noqa: E501

        Event Group IDs to be alerted.  # noqa: E501

        :return: The eventgroup_ids of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._eventgroup_ids

    @eventgroup_ids.setter
    def eventgroup_ids(self, eventgroup_ids):
        """Sets the eventgroup_ids of this EventAlertConditionCreateParams.

        Event Group IDs to be alerted.  # noqa: E501

        :param eventgroup_ids: The eventgroup_ids of this EventAlertConditionCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._eventgroup_ids = eventgroup_ids

    @property
    def id(self):
        """Gets the id of this EventAlertConditionCreateParams.  # noqa: E501

        Unique identifier.  # noqa: E501

        :return: The id of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventAlertConditionCreateParams.

        Unique identifier.  # noqa: E501

        :param id: The id of this EventAlertConditionCreateParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this EventAlertConditionCreateParams.  # noqa: E501

        Required with ONGOING condition only, period in seconds between alerts of ongoing conditions.  # noqa: E501

        :return: The interval of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this EventAlertConditionCreateParams.

        Required with ONGOING condition only, period in seconds between alerts of ongoing conditions.  # noqa: E501

        :param interval: The interval of this EventAlertConditionCreateParams.  # noqa: E501
        :type: int
        """
        if interval is not None and interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._interval = interval

    @property
    def limit(self):
        """Gets the limit of this EventAlertConditionCreateParams.  # noqa: E501

        Required with NEW EVENTS condition only, limits the number of alerts sent as events are added.  # noqa: E501

        :return: The limit of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this EventAlertConditionCreateParams.

        Required with NEW EVENTS condition only, limits the number of alerts sent as events are added.  # noqa: E501

        :param limit: The limit of this EventAlertConditionCreateParams.  # noqa: E501
        :type: int
        """
        if limit is not None and limit < 0:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this EventAlertConditionCreateParams.  # noqa: E501

        Unique identifier.  # noqa: E501

        :return: The name of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventAlertConditionCreateParams.

        Unique identifier.  # noqa: E501

        :param name: The name of this EventAlertConditionCreateParams.  # noqa: E501
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
    def severities(self):
        """Gets the severities of this EventAlertConditionCreateParams.  # noqa: E501

        Severities to be alerted.  # noqa: E501

        :return: The severities of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._severities

    @severities.setter
    def severities(self, severities):
        """Sets the severities of this EventAlertConditionCreateParams.

        Severities to be alerted.  # noqa: E501

        :param severities: The severities of this EventAlertConditionCreateParams.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["emergency", "critical", "warning", "information"]  # noqa: E501
        if not set(severities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `severities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(severities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._severities = severities

    @property
    def transient(self):
        """Gets the transient of this EventAlertConditionCreateParams.  # noqa: E501

        Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition.  # noqa: E501

        :return: The transient of this EventAlertConditionCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """Sets the transient of this EventAlertConditionCreateParams.

        Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition.  # noqa: E501

        :param transient: The transient of this EventAlertConditionCreateParams.  # noqa: E501
        :type: int
        """
        if transient is not None and transient < 0:  # noqa: E501
            raise ValueError("Invalid value for `transient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transient = transient

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
        if not isinstance(other, EventAlertConditionCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
