# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_2_1.models.ndmp_contexts_bre_context_env_variable import NdmpContextsBreContextEnvVariable  # noqa: F401,E501


class NdmpContextsBreContext(object):
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
        'backup_type': 'str',
        'bkp_context_id': 'str',
        'bre_context_id': 'str',
        'create_time': 'int',
        'env_variables': 'list[NdmpContextsBreContextEnvVariable]',
        'id': 'str',
        'results': 'int',
        'snap_name': 'str',
        'status': 'int',
        'stream_id': 'int'
    }

    attribute_map = {
        'backup_type': 'backup type',
        'bkp_context_id': 'bkp_context_id',
        'bre_context_id': 'bre_context_id',
        'create_time': 'create_time',
        'env_variables': 'env_variables',
        'id': 'id',
        'results': 'results',
        'snap_name': 'snap_name',
        'status': 'status',
        'stream_id': 'stream_id'
    }

    def __init__(self, backup_type=None, bkp_context_id=None, bre_context_id=None, create_time=None, env_variables=None, id=None, results=None, snap_name=None, status=None, stream_id=None):  # noqa: E501
        """NdmpContextsBreContext - a model defined in Swagger"""  # noqa: E501

        self._backup_type = None
        self._bkp_context_id = None
        self._bre_context_id = None
        self._create_time = None
        self._env_variables = None
        self._id = None
        self._results = None
        self._snap_name = None
        self._status = None
        self._stream_id = None
        self.discriminator = None

        if backup_type is not None:
            self.backup_type = backup_type
        if bkp_context_id is not None:
            self.bkp_context_id = bkp_context_id
        if bre_context_id is not None:
            self.bre_context_id = bre_context_id
        if create_time is not None:
            self.create_time = create_time
        if env_variables is not None:
            self.env_variables = env_variables
        if id is not None:
            self.id = id
        if results is not None:
            self.results = results
        if snap_name is not None:
            self.snap_name = snap_name
        if status is not None:
            self.status = status
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def backup_type(self):
        """Gets the backup_type of this NdmpContextsBreContext.  # noqa: E501

        Backup type  # noqa: E501

        :return: The backup_type of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this NdmpContextsBreContext.

        Backup type  # noqa: E501

        :param backup_type: The backup_type of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def bkp_context_id(self):
        """Gets the bkp_context_id of this NdmpContextsBreContext.  # noqa: E501

        Backup Context ID  # noqa: E501

        :return: The bkp_context_id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._bkp_context_id

    @bkp_context_id.setter
    def bkp_context_id(self, bkp_context_id):
        """Sets the bkp_context_id of this NdmpContextsBreContext.

        Backup Context ID  # noqa: E501

        :param bkp_context_id: The bkp_context_id of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._bkp_context_id = bkp_context_id

    @property
    def bre_context_id(self):
        """Gets the bre_context_id of this NdmpContextsBreContext.  # noqa: E501

        Unique ID of NDMP BRE context  # noqa: E501

        :return: The bre_context_id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._bre_context_id

    @bre_context_id.setter
    def bre_context_id(self, bre_context_id):
        """Sets the bre_context_id of this NdmpContextsBreContext.

        Unique ID of NDMP BRE context  # noqa: E501

        :param bre_context_id: The bre_context_id of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._bre_context_id = bre_context_id

    @property
    def create_time(self):
        """Gets the create_time of this NdmpContextsBreContext.  # noqa: E501

        Context creation time  # noqa: E501

        :return: The create_time of this NdmpContextsBreContext.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this NdmpContextsBreContext.

        Context creation time  # noqa: E501

        :param create_time: The create_time of this NdmpContextsBreContext.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def env_variables(self):
        """Gets the env_variables of this NdmpContextsBreContext.  # noqa: E501

        List of environment variables for restartable backup  # noqa: E501

        :return: The env_variables of this NdmpContextsBreContext.  # noqa: E501
        :rtype: list[NdmpContextsBreContextEnvVariable]
        """
        return self._env_variables

    @env_variables.setter
    def env_variables(self, env_variables):
        """Sets the env_variables of this NdmpContextsBreContext.

        List of environment variables for restartable backup  # noqa: E501

        :param env_variables: The env_variables of this NdmpContextsBreContext.  # noqa: E501
        :type: list[NdmpContextsBreContextEnvVariable]
        """

        self._env_variables = env_variables

    @property
    def id(self):
        """Gets the id of this NdmpContextsBreContext.  # noqa: E501

        Unique display id.  # noqa: E501

        :return: The id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NdmpContextsBreContext.

        Unique display id.  # noqa: E501

        :param id: The id of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def results(self):
        """Gets the results of this NdmpContextsBreContext.  # noqa: E501

        Backup result  # noqa: E501

        :return: The results of this NdmpContextsBreContext.  # noqa: E501
        :rtype: int
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this NdmpContextsBreContext.

        Backup result  # noqa: E501

        :param results: The results of this NdmpContextsBreContext.  # noqa: E501
        :type: int
        """

        self._results = results

    @property
    def snap_name(self):
        """Gets the snap_name of this NdmpContextsBreContext.  # noqa: E501

        Snapshot name of backup  # noqa: E501

        :return: The snap_name of this NdmpContextsBreContext.  # noqa: E501
        :rtype: str
        """
        return self._snap_name

    @snap_name.setter
    def snap_name(self, snap_name):
        """Sets the snap_name of this NdmpContextsBreContext.

        Snapshot name of backup  # noqa: E501

        :param snap_name: The snap_name of this NdmpContextsBreContext.  # noqa: E501
        :type: str
        """

        self._snap_name = snap_name

    @property
    def status(self):
        """Gets the status of this NdmpContextsBreContext.  # noqa: E501

        Context status bits  # noqa: E501

        :return: The status of this NdmpContextsBreContext.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NdmpContextsBreContext.

        Context status bits  # noqa: E501

        :param status: The status of this NdmpContextsBreContext.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def stream_id(self):
        """Gets the stream_id of this NdmpContextsBreContext.  # noqa: E501

        Backup Stream ID  # noqa: E501

        :return: The stream_id of this NdmpContextsBreContext.  # noqa: E501
        :rtype: int
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this NdmpContextsBreContext.

        Backup Stream ID  # noqa: E501

        :param stream_id: The stream_id of this NdmpContextsBreContext.  # noqa: E501
        :type: int
        """

        self._stream_id = stream_id

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
        if not isinstance(other, NdmpContextsBreContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other