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


class NodeStatusBatterystatusNode(object):
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
        'error': 'str',
        'id': 'int',
        'last_test_time1': 'str',
        'last_test_time2': 'str',
        'lnn': 'int',
        'next_test_time1': 'str',
        'next_test_time2': 'str',
        'present': 'bool',
        'result1': 'str',
        'result2': 'str',
        'status': 'int',
        'status1': 'str',
        'status2': 'str',
        'supported': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'last_test_time1': 'last_test_time1',
        'last_test_time2': 'last_test_time2',
        'lnn': 'lnn',
        'next_test_time1': 'next_test_time1',
        'next_test_time2': 'next_test_time2',
        'present': 'present',
        'result1': 'result1',
        'result2': 'result2',
        'status': 'status',
        'status1': 'status1',
        'status2': 'status2',
        'supported': 'supported'
    }

    def __init__(self, error=None, id=None, last_test_time1=None, last_test_time2=None, lnn=None, next_test_time1=None, next_test_time2=None, present=None, result1=None, result2=None, status=None, status1=None, status2=None, supported=None):  # noqa: E501
        """NodeStatusBatterystatusNode - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._id = None
        self._last_test_time1 = None
        self._last_test_time2 = None
        self._lnn = None
        self._next_test_time1 = None
        self._next_test_time2 = None
        self._present = None
        self._result1 = None
        self._result2 = None
        self._status = None
        self._status1 = None
        self._status2 = None
        self._supported = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if last_test_time1 is not None:
            self.last_test_time1 = last_test_time1
        if last_test_time2 is not None:
            self.last_test_time2 = last_test_time2
        if lnn is not None:
            self.lnn = lnn
        if next_test_time1 is not None:
            self.next_test_time1 = next_test_time1
        if next_test_time2 is not None:
            self.next_test_time2 = next_test_time2
        if present is not None:
            self.present = present
        if result1 is not None:
            self.result1 = result1
        if result2 is not None:
            self.result2 = result2
        if status is not None:
            self.status = status
        if status1 is not None:
            self.status1 = status1
        if status2 is not None:
            self.status2 = status2
        if supported is not None:
            self.supported = supported

    @property
    def error(self):
        """Gets the error of this NodeStatusBatterystatusNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeStatusBatterystatusNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 8192:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if error is not None and len(error) < 0:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeStatusBatterystatusNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusBatterystatusNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def last_test_time1(self):
        """Gets the last_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501

        The last battery test time for battery 1.  # noqa: E501

        :return: The last_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._last_test_time1

    @last_test_time1.setter
    def last_test_time1(self, last_test_time1):
        """Sets the last_test_time1 of this NodeStatusBatterystatusNode.

        The last battery test time for battery 1.  # noqa: E501

        :param last_test_time1: The last_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if last_test_time1 is not None and len(last_test_time1) > 255:
            raise ValueError("Invalid value for `last_test_time1`, length must be less than or equal to `255`")  # noqa: E501
        if last_test_time1 is not None and len(last_test_time1) < 0:
            raise ValueError("Invalid value for `last_test_time1`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_test_time1 = last_test_time1

    @property
    def last_test_time2(self):
        """Gets the last_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501

        The last battery test time for battery 2.  # noqa: E501

        :return: The last_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._last_test_time2

    @last_test_time2.setter
    def last_test_time2(self, last_test_time2):
        """Sets the last_test_time2 of this NodeStatusBatterystatusNode.

        The last battery test time for battery 2.  # noqa: E501

        :param last_test_time2: The last_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if last_test_time2 is not None and len(last_test_time2) > 255:
            raise ValueError("Invalid value for `last_test_time2`, length must be less than or equal to `255`")  # noqa: E501
        if last_test_time2 is not None and len(last_test_time2) < 0:
            raise ValueError("Invalid value for `last_test_time2`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_test_time2 = last_test_time2

    @property
    def lnn(self):
        """Gets the lnn of this NodeStatusBatterystatusNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStatusBatterystatusNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def next_test_time1(self):
        """Gets the next_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501

        The next checkup for battery 1.  # noqa: E501

        :return: The next_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._next_test_time1

    @next_test_time1.setter
    def next_test_time1(self, next_test_time1):
        """Sets the next_test_time1 of this NodeStatusBatterystatusNode.

        The next checkup for battery 1.  # noqa: E501

        :param next_test_time1: The next_test_time1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if next_test_time1 is not None and len(next_test_time1) > 255:
            raise ValueError("Invalid value for `next_test_time1`, length must be less than or equal to `255`")  # noqa: E501
        if next_test_time1 is not None and len(next_test_time1) < 0:
            raise ValueError("Invalid value for `next_test_time1`, length must be greater than or equal to `0`")  # noqa: E501

        self._next_test_time1 = next_test_time1

    @property
    def next_test_time2(self):
        """Gets the next_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501

        The next checkup for battery 2.  # noqa: E501

        :return: The next_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._next_test_time2

    @next_test_time2.setter
    def next_test_time2(self, next_test_time2):
        """Sets the next_test_time2 of this NodeStatusBatterystatusNode.

        The next checkup for battery 2.  # noqa: E501

        :param next_test_time2: The next_test_time2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if next_test_time2 is not None and len(next_test_time2) > 255:
            raise ValueError("Invalid value for `next_test_time2`, length must be less than or equal to `255`")  # noqa: E501
        if next_test_time2 is not None and len(next_test_time2) < 0:
            raise ValueError("Invalid value for `next_test_time2`, length must be greater than or equal to `0`")  # noqa: E501

        self._next_test_time2 = next_test_time2

    @property
    def present(self):
        """Gets the present of this NodeStatusBatterystatusNode.  # noqa: E501

        Node has battery status.  # noqa: E501

        :return: The present of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this NodeStatusBatterystatusNode.

        Node has battery status.  # noqa: E501

        :param present: The present of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def result1(self):
        """Gets the result1 of this NodeStatusBatterystatusNode.  # noqa: E501

        The result of the last battery test for battery 1.  # noqa: E501

        :return: The result1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._result1

    @result1.setter
    def result1(self, result1):
        """Sets the result1 of this NodeStatusBatterystatusNode.

        The result of the last battery test for battery 1.  # noqa: E501

        :param result1: The result1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if result1 is not None and len(result1) > 255:
            raise ValueError("Invalid value for `result1`, length must be less than or equal to `255`")  # noqa: E501
        if result1 is not None and len(result1) < 0:
            raise ValueError("Invalid value for `result1`, length must be greater than or equal to `0`")  # noqa: E501

        self._result1 = result1

    @property
    def result2(self):
        """Gets the result2 of this NodeStatusBatterystatusNode.  # noqa: E501

        The result of the last battery test for battery 2.  # noqa: E501

        :return: The result2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._result2

    @result2.setter
    def result2(self, result2):
        """Sets the result2 of this NodeStatusBatterystatusNode.

        The result of the last battery test for battery 2.  # noqa: E501

        :param result2: The result2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if result2 is not None and len(result2) > 255:
            raise ValueError("Invalid value for `result2`, length must be less than or equal to `255`")  # noqa: E501
        if result2 is not None and len(result2) < 0:
            raise ValueError("Invalid value for `result2`, length must be greater than or equal to `0`")  # noqa: E501

        self._result2 = result2

    @property
    def status(self):
        """Gets the status of this NodeStatusBatterystatusNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStatusBatterystatusNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def status1(self):
        """Gets the status1 of this NodeStatusBatterystatusNode.  # noqa: E501

        The status of battery 1.  # noqa: E501

        :return: The status1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._status1

    @status1.setter
    def status1(self, status1):
        """Sets the status1 of this NodeStatusBatterystatusNode.

        The status of battery 1.  # noqa: E501

        :param status1: The status1 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if status1 is not None and len(status1) > 255:
            raise ValueError("Invalid value for `status1`, length must be less than or equal to `255`")  # noqa: E501
        if status1 is not None and len(status1) < 0:
            raise ValueError("Invalid value for `status1`, length must be greater than or equal to `0`")  # noqa: E501

        self._status1 = status1

    @property
    def status2(self):
        """Gets the status2 of this NodeStatusBatterystatusNode.  # noqa: E501

        The status of battery 2.  # noqa: E501

        :return: The status2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: str
        """
        return self._status2

    @status2.setter
    def status2(self, status2):
        """Sets the status2 of this NodeStatusBatterystatusNode.

        The status of battery 2.  # noqa: E501

        :param status2: The status2 of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: str
        """
        if status2 is not None and len(status2) > 255:
            raise ValueError("Invalid value for `status2`, length must be less than or equal to `255`")  # noqa: E501
        if status2 is not None and len(status2) < 0:
            raise ValueError("Invalid value for `status2`, length must be greater than or equal to `0`")  # noqa: E501

        self._status2 = status2

    @property
    def supported(self):
        """Gets the supported of this NodeStatusBatterystatusNode.  # noqa: E501

        Node supports battery status.  # noqa: E501

        :return: The supported of this NodeStatusBatterystatusNode.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this NodeStatusBatterystatusNode.

        Node supports battery status.  # noqa: E501

        :param supported: The supported of this NodeStatusBatterystatusNode.  # noqa: E501
        :type: bool
        """

        self._supported = supported

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
        if not isinstance(other, NodeStatusBatterystatusNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
