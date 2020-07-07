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

from isi_sdk_9_0_0.models.job_statistics_job_node import JobStatisticsJobNode  # noqa: F401,E501


class JobStatisticsJob(object):
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
        'job_id': 'int',
        'nodes': 'list[JobStatisticsJobNode]',
        'phase': 'int',
        'total_nodes': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'nodes': 'nodes',
        'phase': 'phase',
        'total_nodes': 'total_nodes'
    }

    def __init__(self, job_id=None, nodes=None, phase=None, total_nodes=None):  # noqa: E501
        """JobStatisticsJob - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._nodes = None
        self._phase = None
        self._total_nodes = None
        self.discriminator = None

        self.job_id = job_id
        self.nodes = nodes
        self.phase = phase
        self.total_nodes = total_nodes

    @property
    def job_id(self):
        """Gets the job_id of this JobStatisticsJob.  # noqa: E501

        The job ID.  # noqa: E501

        :return: The job_id of this JobStatisticsJob.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobStatisticsJob.

        The job ID.  # noqa: E501

        :param job_id: The job_id of this JobStatisticsJob.  # noqa: E501
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def nodes(self):
        """Gets the nodes of this JobStatisticsJob.  # noqa: E501


        :return: The nodes of this JobStatisticsJob.  # noqa: E501
        :rtype: list[JobStatisticsJobNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this JobStatisticsJob.


        :param nodes: The nodes of this JobStatisticsJob.  # noqa: E501
        :type: list[JobStatisticsJobNode]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def phase(self):
        """Gets the phase of this JobStatisticsJob.  # noqa: E501

        The current phase of the job.  # noqa: E501

        :return: The phase of this JobStatisticsJob.  # noqa: E501
        :rtype: int
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this JobStatisticsJob.

        The current phase of the job.  # noqa: E501

        :param phase: The phase of this JobStatisticsJob.  # noqa: E501
        :type: int
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def total_nodes(self):
        """Gets the total_nodes of this JobStatisticsJob.  # noqa: E501

        The number of nodes participating in the job.  # noqa: E501

        :return: The total_nodes of this JobStatisticsJob.  # noqa: E501
        :rtype: int
        """
        return self._total_nodes

    @total_nodes.setter
    def total_nodes(self, total_nodes):
        """Sets the total_nodes of this JobStatisticsJob.

        The number of nodes participating in the job.  # noqa: E501

        :param total_nodes: The total_nodes of this JobStatisticsJob.  # noqa: E501
        :type: int
        """
        if total_nodes is None:
            raise ValueError("Invalid value for `total_nodes`, must not be `None`")  # noqa: E501

        self._total_nodes = total_nodes

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
        if not isinstance(other, JobStatisticsJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
