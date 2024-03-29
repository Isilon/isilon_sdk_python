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


class ConfigImport(object):
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
        'done': 'str',
        'export_id': 'str',
        'failed': 'str',
        'id': 'str',
        'message': 'str',
        'path': 'str',
        'pending': 'str',
        'status': 'str'
    }

    attribute_map = {
        'done': 'done',
        'export_id': 'export_id',
        'failed': 'failed',
        'id': 'id',
        'message': 'message',
        'path': 'path',
        'pending': 'pending',
        'status': 'status'
    }

    def __init__(self, done=None, export_id=None, failed=None, id=None, message=None, path=None, pending=None, status=None):  # noqa: E501
        """ConfigImport - a model defined in Swagger"""  # noqa: E501

        self._done = None
        self._export_id = None
        self._failed = None
        self._id = None
        self._message = None
        self._path = None
        self._pending = None
        self._status = None
        self.discriminator = None

        if done is not None:
            self.done = done
        if export_id is not None:
            self.export_id = export_id
        if failed is not None:
            self.failed = failed
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if path is not None:
            self.path = path
        if pending is not None:
            self.pending = pending
        if status is not None:
            self.status = status

    @property
    def done(self):
        """Gets the done of this ConfigImport.  # noqa: E501

        All finished components.  # noqa: E501

        :return: The done of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this ConfigImport.

        All finished components.  # noqa: E501

        :param done: The done of this ConfigImport.  # noqa: E501
        :type: str
        """
        if done is not None and len(done) > 8192:
            raise ValueError("Invalid value for `done`, length must be less than or equal to `8192`")  # noqa: E501
        if done is not None and len(done) < 1:
            raise ValueError("Invalid value for `done`, length must be greater than or equal to `1`")  # noqa: E501

        self._done = done

    @property
    def export_id(self):
        """Gets the export_id of this ConfigImport.  # noqa: E501

        The export ID given to the task.  # noqa: E501

        :return: The export_id of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """Sets the export_id of this ConfigImport.

        The export ID given to the task.  # noqa: E501

        :param export_id: The export_id of this ConfigImport.  # noqa: E501
        :type: str
        """
        if export_id is not None and len(export_id) > 255:
            raise ValueError("Invalid value for `export_id`, length must be less than or equal to `255`")  # noqa: E501
        if export_id is not None and len(export_id) < 14:
            raise ValueError("Invalid value for `export_id`, length must be greater than or equal to `14`")  # noqa: E501

        self._export_id = export_id

    @property
    def failed(self):
        """Gets the failed of this ConfigImport.  # noqa: E501

        All failed components.  # noqa: E501

        :return: The failed of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this ConfigImport.

        All failed components.  # noqa: E501

        :param failed: The failed of this ConfigImport.  # noqa: E501
        :type: str
        """
        if failed is not None and len(failed) > 8192:
            raise ValueError("Invalid value for `failed`, length must be less than or equal to `8192`")  # noqa: E501
        if failed is not None and len(failed) < 1:
            raise ValueError("Invalid value for `failed`, length must be greater than or equal to `1`")  # noqa: E501

        self._failed = failed

    @property
    def id(self):
        """Gets the id of this ConfigImport.  # noqa: E501

        The import ID given to the task.  # noqa: E501

        :return: The id of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigImport.

        The import ID given to the task.  # noqa: E501

        :param id: The id of this ConfigImport.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 14:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `14`")  # noqa: E501

        self._id = id

    @property
    def message(self):
        """Gets the message of this ConfigImport.  # noqa: E501

        Message of job.  # noqa: E501

        :return: The message of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConfigImport.

        Message of job.  # noqa: E501

        :param message: The message of this ConfigImport.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) > 8192:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `8192`")  # noqa: E501
        if message is not None and len(message) < 0:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")  # noqa: E501

        self._message = message

    @property
    def path(self):
        """Gets the path of this ConfigImport.  # noqa: E501

        The path where import job's result is stored.  # noqa: E501

        :return: The path of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ConfigImport.

        The path where import job's result is stored.  # noqa: E501

        :param path: The path of this ConfigImport.  # noqa: E501
        :type: str
        """
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 0:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `0`")  # noqa: E501

        self._path = path

    @property
    def pending(self):
        """Gets the pending of this ConfigImport.  # noqa: E501

        All components to be imported.  # noqa: E501

        :return: The pending of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this ConfigImport.

        All components to be imported.  # noqa: E501

        :param pending: The pending of this ConfigImport.  # noqa: E501
        :type: str
        """
        if pending is not None and len(pending) > 8192:
            raise ValueError("Invalid value for `pending`, length must be less than or equal to `8192`")  # noqa: E501
        if pending is not None and len(pending) < 1:
            raise ValueError("Invalid value for `pending`, length must be greater than or equal to `1`")  # noqa: E501

        self._pending = pending

    @property
    def status(self):
        """Gets the status of this ConfigImport.  # noqa: E501

        The status of the job.  # noqa: E501

        :return: The status of this ConfigImport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfigImport.

        The status of the job.  # noqa: E501

        :param status: The status of this ConfigImport.  # noqa: E501
        :type: str
        """
        if status is not None and len(status) > 255:
            raise ValueError("Invalid value for `status`, length must be less than or equal to `255`")  # noqa: E501
        if status is not None and len(status) < 1:
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, ConfigImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
