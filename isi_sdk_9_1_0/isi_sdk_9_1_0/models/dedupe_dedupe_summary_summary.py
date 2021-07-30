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


class DedupeDedupeSummarySummary(object):
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
        'block_size': 'float',
        'estimated_physical_blocks': 'float',
        'estimated_saved_blocks': 'float',
        'logical_blocks': 'float',
        'saved_logical_blocks': 'float',
        'total_blocks': 'float',
        'used_blocks': 'float'
    }

    attribute_map = {
        'block_size': 'block_size',
        'estimated_physical_blocks': 'estimated_physical_blocks',
        'estimated_saved_blocks': 'estimated_saved_blocks',
        'logical_blocks': 'logical_blocks',
        'saved_logical_blocks': 'saved_logical_blocks',
        'total_blocks': 'total_blocks',
        'used_blocks': 'used_blocks'
    }

    def __init__(self, block_size=None, estimated_physical_blocks=None, estimated_saved_blocks=None, logical_blocks=None, saved_logical_blocks=None, total_blocks=None, used_blocks=None):  # noqa: E501
        """DedupeDedupeSummarySummary - a model defined in Swagger"""  # noqa: E501

        self._block_size = None
        self._estimated_physical_blocks = None
        self._estimated_saved_blocks = None
        self._logical_blocks = None
        self._saved_logical_blocks = None
        self._total_blocks = None
        self._used_blocks = None
        self.discriminator = None

        self.block_size = block_size
        self.estimated_physical_blocks = estimated_physical_blocks
        self.estimated_saved_blocks = estimated_saved_blocks
        self.logical_blocks = logical_blocks
        self.saved_logical_blocks = saved_logical_blocks
        self.total_blocks = total_blocks
        self.used_blocks = used_blocks

    @property
    def block_size(self):
        """Gets the block_size of this DedupeDedupeSummarySummary.  # noqa: E501

        Size in bytes of a filesystem block.  # noqa: E501

        :return: The block_size of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this DedupeDedupeSummarySummary.

        Size in bytes of a filesystem block.  # noqa: E501

        :param block_size: The block_size of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if block_size is None:
            raise ValueError("Invalid value for `block_size`, must not be `None`")  # noqa: E501

        self._block_size = block_size

    @property
    def estimated_physical_blocks(self):
        """Gets the estimated_physical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Estimated number of physical blocks deduped.  # noqa: E501

        :return: The estimated_physical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._estimated_physical_blocks

    @estimated_physical_blocks.setter
    def estimated_physical_blocks(self, estimated_physical_blocks):
        """Sets the estimated_physical_blocks of this DedupeDedupeSummarySummary.

        Estimated number of physical blocks deduped.  # noqa: E501

        :param estimated_physical_blocks: The estimated_physical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if estimated_physical_blocks is None:
            raise ValueError("Invalid value for `estimated_physical_blocks`, must not be `None`")  # noqa: E501

        self._estimated_physical_blocks = estimated_physical_blocks

    @property
    def estimated_saved_blocks(self):
        """Gets the estimated_saved_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Estimated number of physical blocks saved by dedupe.  # noqa: E501

        :return: The estimated_saved_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._estimated_saved_blocks

    @estimated_saved_blocks.setter
    def estimated_saved_blocks(self, estimated_saved_blocks):
        """Sets the estimated_saved_blocks of this DedupeDedupeSummarySummary.

        Estimated number of physical blocks saved by dedupe.  # noqa: E501

        :param estimated_saved_blocks: The estimated_saved_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if estimated_saved_blocks is None:
            raise ValueError("Invalid value for `estimated_saved_blocks`, must not be `None`")  # noqa: E501

        self._estimated_saved_blocks = estimated_saved_blocks

    @property
    def logical_blocks(self):
        """Gets the logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Number of logical blocks deduped.  # noqa: E501

        :return: The logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._logical_blocks

    @logical_blocks.setter
    def logical_blocks(self, logical_blocks):
        """Sets the logical_blocks of this DedupeDedupeSummarySummary.

        Number of logical blocks deduped.  # noqa: E501

        :param logical_blocks: The logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if logical_blocks is None:
            raise ValueError("Invalid value for `logical_blocks`, must not be `None`")  # noqa: E501

        self._logical_blocks = logical_blocks

    @property
    def saved_logical_blocks(self):
        """Gets the saved_logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Number of logical blocks saved by dedupe.  # noqa: E501

        :return: The saved_logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._saved_logical_blocks

    @saved_logical_blocks.setter
    def saved_logical_blocks(self, saved_logical_blocks):
        """Sets the saved_logical_blocks of this DedupeDedupeSummarySummary.

        Number of logical blocks saved by dedupe.  # noqa: E501

        :param saved_logical_blocks: The saved_logical_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if saved_logical_blocks is None:
            raise ValueError("Invalid value for `saved_logical_blocks`, must not be `None`")  # noqa: E501

        self._saved_logical_blocks = saved_logical_blocks

    @property
    def total_blocks(self):
        """Gets the total_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Total physical blocks in the cluster.  # noqa: E501

        :return: The total_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._total_blocks

    @total_blocks.setter
    def total_blocks(self, total_blocks):
        """Sets the total_blocks of this DedupeDedupeSummarySummary.

        Total physical blocks in the cluster.  # noqa: E501

        :param total_blocks: The total_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if total_blocks is None:
            raise ValueError("Invalid value for `total_blocks`, must not be `None`")  # noqa: E501

        self._total_blocks = total_blocks

    @property
    def used_blocks(self):
        """Gets the used_blocks of this DedupeDedupeSummarySummary.  # noqa: E501

        Total physical blocks used in the cluster.  # noqa: E501

        :return: The used_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :rtype: float
        """
        return self._used_blocks

    @used_blocks.setter
    def used_blocks(self, used_blocks):
        """Sets the used_blocks of this DedupeDedupeSummarySummary.

        Total physical blocks used in the cluster.  # noqa: E501

        :param used_blocks: The used_blocks of this DedupeDedupeSummarySummary.  # noqa: E501
        :type: float
        """
        if used_blocks is None:
            raise ValueError("Invalid value for `used_blocks`, must not be `None`")  # noqa: E501

        self._used_blocks = used_blocks

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
        if not isinstance(other, DedupeDedupeSummarySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
