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


class JobJobTreedeleteParams(object):
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
        'delete_quotas': 'bool'
    }

    attribute_map = {
        'delete_quotas': 'delete_quotas'
    }

    def __init__(self, delete_quotas=False):  # noqa: E501
        """JobJobTreedeleteParams - a model defined in Swagger"""  # noqa: E501

        self._delete_quotas = None
        self.discriminator = None

        if delete_quotas is not None:
            self.delete_quotas = delete_quotas

    @property
    def delete_quotas(self):
        """Gets the delete_quotas of this JobJobTreedeleteParams.  # noqa: E501

        Delete quotas encountered during TreeDelete. When set to false, the job will fail if a quota is encountered.  # noqa: E501

        :return: The delete_quotas of this JobJobTreedeleteParams.  # noqa: E501
        :rtype: bool
        """
        return self._delete_quotas

    @delete_quotas.setter
    def delete_quotas(self, delete_quotas):
        """Sets the delete_quotas of this JobJobTreedeleteParams.

        Delete quotas encountered during TreeDelete. When set to false, the job will fail if a quota is encountered.  # noqa: E501

        :param delete_quotas: The delete_quotas of this JobJobTreedeleteParams.  # noqa: E501
        :type: bool
        """

        self._delete_quotas = delete_quotas

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
        if not isinstance(other, JobJobTreedeleteParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
