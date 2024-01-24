# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_4_0.models.s3_bucket import S3Bucket  # noqa: F401,E501
from isilon_sdk.v9_4_0.models.s3_bucket_acl_item import S3BucketAclItem  # noqa: F401,E501


class S3BucketCreateParams(object):
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
        'acl': 'list[S3BucketAclItem]',
        'description': 'str',
        'object_acl_policy': 'str',
        'create_path': 'bool',
        'name': 'str',
        'owner': 'str',
        'path': 'str'
    }

    attribute_map = {
        'acl': 'acl',
        'description': 'description',
        'object_acl_policy': 'object_acl_policy',
        'create_path': 'create_path',
        'name': 'name',
        'owner': 'owner',
        'path': 'path'
    }

    def __init__(self, acl=None, description=None, object_acl_policy=None, create_path=None, name=None, owner=None, path=None):  # noqa: E501
        """S3BucketCreateParams - a model defined in Swagger"""  # noqa: E501

        self._acl = None
        self._description = None
        self._object_acl_policy = None
        self._create_path = None
        self._name = None
        self._owner = None
        self._path = None
        self.discriminator = None

        if acl is not None:
            self.acl = acl
        if description is not None:
            self.description = description
        if object_acl_policy is not None:
            self.object_acl_policy = object_acl_policy
        if create_path is not None:
            self.create_path = create_path
        self.name = name
        if owner is not None:
            self.owner = owner
        self.path = path

    @property
    def acl(self):
        """Gets the acl of this S3BucketCreateParams.  # noqa: E501

        Specifies an ordered list of S3 permissions.  # noqa: E501

        :return: The acl of this S3BucketCreateParams.  # noqa: E501
        :rtype: list[S3BucketAclItem]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this S3BucketCreateParams.

        Specifies an ordered list of S3 permissions.  # noqa: E501

        :param acl: The acl of this S3BucketCreateParams.  # noqa: E501
        :type: list[S3BucketAclItem]
        """

        self._acl = acl

    @property
    def description(self):
        """Gets the description of this S3BucketCreateParams.  # noqa: E501

        Description for this S3 bucket.  # noqa: E501

        :return: The description of this S3BucketCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this S3BucketCreateParams.

        Description for this S3 bucket.  # noqa: E501

        :param description: The description of this S3BucketCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 8192:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def object_acl_policy(self):
        """Gets the object_acl_policy of this S3BucketCreateParams.  # noqa: E501

        Set behavior of modifying object acls  # noqa: E501

        :return: The object_acl_policy of this S3BucketCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._object_acl_policy

    @object_acl_policy.setter
    def object_acl_policy(self, object_acl_policy):
        """Sets the object_acl_policy of this S3BucketCreateParams.

        Set behavior of modifying object acls  # noqa: E501

        :param object_acl_policy: The object_acl_policy of this S3BucketCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["replace", "deny"]  # noqa: E501
        if object_acl_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `object_acl_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(object_acl_policy, allowed_values)
            )

        self._object_acl_policy = object_acl_policy

    @property
    def create_path(self):
        """Gets the create_path of this S3BucketCreateParams.  # noqa: E501

        Create path if it does not exist.  # noqa: E501

        :return: The create_path of this S3BucketCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._create_path

    @create_path.setter
    def create_path(self, create_path):
        """Sets the create_path of this S3BucketCreateParams.

        Create path if it does not exist.  # noqa: E501

        :param create_path: The create_path of this S3BucketCreateParams.  # noqa: E501
        :type: bool
        """

        self._create_path = create_path

    @property
    def name(self):
        """Gets the name of this S3BucketCreateParams.  # noqa: E501

        Bucket name.  # noqa: E501

        :return: The name of this S3BucketCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this S3BucketCreateParams.

        Bucket name.  # noqa: E501

        :param name: The name of this S3BucketCreateParams.  # noqa: E501
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
    def owner(self):
        """Gets the owner of this S3BucketCreateParams.  # noqa: E501

        Specifies the name of the owner.  # noqa: E501

        :return: The owner of this S3BucketCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this S3BucketCreateParams.

        Specifies the name of the owner.  # noqa: E501

        :param owner: The owner of this S3BucketCreateParams.  # noqa: E501
        :type: str
        """
        if owner is not None and len(owner) > 255:
            raise ValueError("Invalid value for `owner`, length must be less than or equal to `255`")  # noqa: E501
        if owner is not None and len(owner) < 0:
            raise ValueError("Invalid value for `owner`, length must be greater than or equal to `0`")  # noqa: E501

        self._owner = owner

    @property
    def path(self):
        """Gets the path of this S3BucketCreateParams.  # noqa: E501

        Path of bucket within /ifs.  # noqa: E501

        :return: The path of this S3BucketCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this S3BucketCreateParams.

        Path of bucket within /ifs.  # noqa: E501

        :param path: The path of this S3BucketCreateParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 1:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, S3BucketCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other