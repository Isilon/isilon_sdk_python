# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResultTopFilesFile(object):
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
        'atime': 'int',
        'btime': 'int',
        'ctime': 'int',
        'log_size': 'int',
        'path': 'str',
        'phys_size': 'int'
    }

    attribute_map = {
        'atime': 'atime',
        'btime': 'btime',
        'ctime': 'ctime',
        'log_size': 'log_size',
        'path': 'path',
        'phys_size': 'phys_size'
    }

    def __init__(self, atime=None, btime=None, ctime=None, log_size=None, path=None, phys_size=None):  # noqa: E501
        """ResultTopFilesFile - a model defined in Swagger"""  # noqa: E501

        self._atime = None
        self._btime = None
        self._ctime = None
        self._log_size = None
        self._path = None
        self._phys_size = None
        self.discriminator = None

        self.atime = atime
        self.btime = btime
        self.ctime = ctime
        self.log_size = log_size
        self.path = path
        self.phys_size = phys_size

    @property
    def atime(self):
        """Gets the atime of this ResultTopFilesFile.  # noqa: E501

        File access time.  # noqa: E501

        :return: The atime of this ResultTopFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this ResultTopFilesFile.

        File access time.  # noqa: E501

        :param atime: The atime of this ResultTopFilesFile.  # noqa: E501
        :type: int
        """
        if atime is None:
            raise ValueError("Invalid value for `atime`, must not be `None`")  # noqa: E501

        self._atime = atime

    @property
    def btime(self):
        """Gets the btime of this ResultTopFilesFile.  # noqa: E501

        File creation begin time.  # noqa: E501

        :return: The btime of this ResultTopFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._btime

    @btime.setter
    def btime(self, btime):
        """Sets the btime of this ResultTopFilesFile.

        File creation begin time.  # noqa: E501

        :param btime: The btime of this ResultTopFilesFile.  # noqa: E501
        :type: int
        """
        if btime is None:
            raise ValueError("Invalid value for `btime`, must not be `None`")  # noqa: E501

        self._btime = btime

    @property
    def ctime(self):
        """Gets the ctime of this ResultTopFilesFile.  # noqa: E501

        Unix inode change time.  # noqa: E501

        :return: The ctime of this ResultTopFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ResultTopFilesFile.

        Unix inode change time.  # noqa: E501

        :param ctime: The ctime of this ResultTopFilesFile.  # noqa: E501
        :type: int
        """
        if ctime is None:
            raise ValueError("Invalid value for `ctime`, must not be `None`")  # noqa: E501

        self._ctime = ctime

    @property
    def log_size(self):
        """Gets the log_size of this ResultTopFilesFile.  # noqa: E501

        Logical file size in bytes.  # noqa: E501

        :return: The log_size of this ResultTopFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._log_size

    @log_size.setter
    def log_size(self, log_size):
        """Sets the log_size of this ResultTopFilesFile.

        Logical file size in bytes.  # noqa: E501

        :param log_size: The log_size of this ResultTopFilesFile.  # noqa: E501
        :type: int
        """
        if log_size is None:
            raise ValueError("Invalid value for `log_size`, must not be `None`")  # noqa: E501

        self._log_size = log_size

    @property
    def path(self):
        """Gets the path of this ResultTopFilesFile.  # noqa: E501

        Relative file path under /ifs/.  # noqa: E501

        :return: The path of this ResultTopFilesFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ResultTopFilesFile.

        Relative file path under /ifs/.  # noqa: E501

        :param path: The path of this ResultTopFilesFile.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def phys_size(self):
        """Gets the phys_size of this ResultTopFilesFile.  # noqa: E501

        Physical file size in bytes.  # noqa: E501

        :return: The phys_size of this ResultTopFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._phys_size

    @phys_size.setter
    def phys_size(self, phys_size):
        """Sets the phys_size of this ResultTopFilesFile.

        Physical file size in bytes.  # noqa: E501

        :param phys_size: The phys_size of this ResultTopFilesFile.  # noqa: E501
        :type: int
        """
        if phys_size is None:
            raise ValueError("Invalid value for `phys_size`, must not be `None`")  # noqa: E501

        self._phys_size = phys_size

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
        if not isinstance(other, ResultTopFilesFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
