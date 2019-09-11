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


class CreateHardwareTapeNameResponseNodeRescanReportItem(object):
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
        'devicename': 'str',
        'path': 'str',
        'product': 'str',
        'serial': 'str',
        'status_report': 'str',
        'wwnn': 'str'
    }

    attribute_map = {
        'devicename': 'devicename',
        'path': 'path',
        'product': 'product',
        'serial': 'serial',
        'status_report': 'status_report',
        'wwnn': 'wwnn'
    }

    def __init__(self, devicename=None, path=None, product=None, serial=None, status_report=None, wwnn=None):  # noqa: E501
        """CreateHardwareTapeNameResponseNodeRescanReportItem - a model defined in Swagger"""  # noqa: E501

        self._devicename = None
        self._path = None
        self._product = None
        self._serial = None
        self._status_report = None
        self._wwnn = None
        self.discriminator = None

        if devicename is not None:
            self.devicename = devicename
        if path is not None:
            self.path = path
        if product is not None:
            self.product = product
        if serial is not None:
            self.serial = serial
        if status_report is not None:
            self.status_report = status_report
        if wwnn is not None:
            self.wwnn = wwnn

    @property
    def devicename(self):
        """Gets the devicename of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device name  # noqa: E501

        :return: The devicename of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._devicename

    @devicename.setter
    def devicename(self, devicename):
        """Sets the devicename of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device name  # noqa: E501

        :param devicename: The devicename of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._devicename = devicename

    @property
    def path(self):
        """Gets the path of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device driver path  # noqa: E501

        :return: The path of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device driver path  # noqa: E501

        :param path: The path of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def product(self):
        """Gets the product of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device product name  # noqa: E501

        :return: The product of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device product name  # noqa: E501

        :param product: The product of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def serial(self):
        """Gets the serial of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device serial:L number  # noqa: E501

        :return: The serial of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device serial:L number  # noqa: E501

        :param serial: The serial of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def status_report(self):
        """Gets the status_report of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device change status  # noqa: E501

        :return: The status_report of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._status_report

    @status_report.setter
    def status_report(self, status_report):
        """Sets the status_report of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device change status  # noqa: E501

        :param status_report: The status_report of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._status_report = status_report

    @property
    def wwnn(self):
        """Gets the wwnn of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501

        device node world wide name  # noqa: E501

        :return: The wwnn of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this CreateHardwareTapeNameResponseNodeRescanReportItem.

        device node world wide name  # noqa: E501

        :param wwnn: The wwnn of this CreateHardwareTapeNameResponseNodeRescanReportItem.  # noqa: E501
        :type: str
        """

        self._wwnn = wwnn

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
        if not isinstance(other, CreateHardwareTapeNameResponseNodeRescanReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
