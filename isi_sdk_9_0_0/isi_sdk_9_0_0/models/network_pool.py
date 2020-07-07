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

from isi_sdk_9_0_0.models.subnets_subnet_pool_iface import SubnetsSubnetPoolIface  # noqa: F401,E501
from isi_sdk_9_0_0.models.subnets_subnet_pool_range import SubnetsSubnetPoolRange  # noqa: F401,E501
from isi_sdk_9_0_0.models.subnets_subnet_pool_static_route import SubnetsSubnetPoolStaticRoute  # noqa: F401,E501


class NetworkPool(object):
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
        'access_zone': 'str',
        'addr_family': 'str',
        'aggregation_mode': 'str',
        'alloc_method': 'str',
        'description': 'str',
        'groupnet': 'str',
        'id': 'str',
        'ifaces': 'list[SubnetsSubnetPoolIface]',
        'name': 'str',
        'ranges': 'list[SubnetsSubnetPoolRange]',
        'rebalance_policy': 'str',
        'rules': 'list[str]',
        'sc_auto_unsuspend_delay': 'int',
        'sc_connect_policy': 'str',
        'sc_dns_zone': 'str',
        'sc_dns_zone_aliases': 'list[str]',
        'sc_failover_policy': 'str',
        'sc_subnet': 'str',
        'sc_suspended_nodes': 'list[int]',
        'sc_ttl': 'int',
        'static_routes': 'list[SubnetsSubnetPoolStaticRoute]',
        'subnet': 'str'
    }

    attribute_map = {
        'access_zone': 'access_zone',
        'addr_family': 'addr_family',
        'aggregation_mode': 'aggregation_mode',
        'alloc_method': 'alloc_method',
        'description': 'description',
        'groupnet': 'groupnet',
        'id': 'id',
        'ifaces': 'ifaces',
        'name': 'name',
        'ranges': 'ranges',
        'rebalance_policy': 'rebalance_policy',
        'rules': 'rules',
        'sc_auto_unsuspend_delay': 'sc_auto_unsuspend_delay',
        'sc_connect_policy': 'sc_connect_policy',
        'sc_dns_zone': 'sc_dns_zone',
        'sc_dns_zone_aliases': 'sc_dns_zone_aliases',
        'sc_failover_policy': 'sc_failover_policy',
        'sc_subnet': 'sc_subnet',
        'sc_suspended_nodes': 'sc_suspended_nodes',
        'sc_ttl': 'sc_ttl',
        'static_routes': 'static_routes',
        'subnet': 'subnet'
    }

    def __init__(self, access_zone=None, addr_family=None, aggregation_mode=None, alloc_method=None, description=None, groupnet=None, id=None, ifaces=None, name=None, ranges=None, rebalance_policy=None, rules=None, sc_auto_unsuspend_delay=None, sc_connect_policy=None, sc_dns_zone=None, sc_dns_zone_aliases=None, sc_failover_policy=None, sc_subnet=None, sc_suspended_nodes=None, sc_ttl=None, static_routes=None, subnet=None):  # noqa: E501
        """NetworkPool - a model defined in Swagger"""  # noqa: E501

        self._access_zone = None
        self._addr_family = None
        self._aggregation_mode = None
        self._alloc_method = None
        self._description = None
        self._groupnet = None
        self._id = None
        self._ifaces = None
        self._name = None
        self._ranges = None
        self._rebalance_policy = None
        self._rules = None
        self._sc_auto_unsuspend_delay = None
        self._sc_connect_policy = None
        self._sc_dns_zone = None
        self._sc_dns_zone_aliases = None
        self._sc_failover_policy = None
        self._sc_subnet = None
        self._sc_suspended_nodes = None
        self._sc_ttl = None
        self._static_routes = None
        self._subnet = None
        self.discriminator = None

        if access_zone is not None:
            self.access_zone = access_zone
        if addr_family is not None:
            self.addr_family = addr_family
        if aggregation_mode is not None:
            self.aggregation_mode = aggregation_mode
        if alloc_method is not None:
            self.alloc_method = alloc_method
        if description is not None:
            self.description = description
        if groupnet is not None:
            self.groupnet = groupnet
        if id is not None:
            self.id = id
        if ifaces is not None:
            self.ifaces = ifaces
        if name is not None:
            self.name = name
        if ranges is not None:
            self.ranges = ranges
        if rebalance_policy is not None:
            self.rebalance_policy = rebalance_policy
        if rules is not None:
            self.rules = rules
        if sc_auto_unsuspend_delay is not None:
            self.sc_auto_unsuspend_delay = sc_auto_unsuspend_delay
        if sc_connect_policy is not None:
            self.sc_connect_policy = sc_connect_policy
        if sc_dns_zone is not None:
            self.sc_dns_zone = sc_dns_zone
        if sc_dns_zone_aliases is not None:
            self.sc_dns_zone_aliases = sc_dns_zone_aliases
        if sc_failover_policy is not None:
            self.sc_failover_policy = sc_failover_policy
        if sc_subnet is not None:
            self.sc_subnet = sc_subnet
        if sc_suspended_nodes is not None:
            self.sc_suspended_nodes = sc_suspended_nodes
        if sc_ttl is not None:
            self.sc_ttl = sc_ttl
        if static_routes is not None:
            self.static_routes = static_routes
        if subnet is not None:
            self.subnet = subnet

    @property
    def access_zone(self):
        """Gets the access_zone of this NetworkPool.  # noqa: E501

        Name of a valid access zone to map IP address pool to the zone.  # noqa: E501

        :return: The access_zone of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._access_zone

    @access_zone.setter
    def access_zone(self, access_zone):
        """Sets the access_zone of this NetworkPool.

        Name of a valid access zone to map IP address pool to the zone.  # noqa: E501

        :param access_zone: The access_zone of this NetworkPool.  # noqa: E501
        :type: str
        """
        if access_zone is not None and len(access_zone) > 255:
            raise ValueError("Invalid value for `access_zone`, length must be less than or equal to `255`")  # noqa: E501
        if access_zone is not None and len(access_zone) < 1:
            raise ValueError("Invalid value for `access_zone`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_zone = access_zone

    @property
    def addr_family(self):
        """Gets the addr_family of this NetworkPool.  # noqa: E501

        IP address format.  # noqa: E501

        :return: The addr_family of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._addr_family

    @addr_family.setter
    def addr_family(self, addr_family):
        """Sets the addr_family of this NetworkPool.

        IP address format.  # noqa: E501

        :param addr_family: The addr_family of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["ipv4", "ipv6"]  # noqa: E501
        if addr_family not in allowed_values:
            raise ValueError(
                "Invalid value for `addr_family` ({0}), must be one of {1}"  # noqa: E501
                .format(addr_family, allowed_values)
            )

        self._addr_family = addr_family

    @property
    def aggregation_mode(self):
        """Gets the aggregation_mode of this NetworkPool.  # noqa: E501

        OneFS supports the following NIC aggregation modes.  # noqa: E501

        :return: The aggregation_mode of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_mode

    @aggregation_mode.setter
    def aggregation_mode(self, aggregation_mode):
        """Sets the aggregation_mode of this NetworkPool.

        OneFS supports the following NIC aggregation modes.  # noqa: E501

        :param aggregation_mode: The aggregation_mode of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["roundrobin", "failover", "lacp", "fec"]  # noqa: E501
        if aggregation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_mode, allowed_values)
            )

        self._aggregation_mode = aggregation_mode

    @property
    def alloc_method(self):
        """Gets the alloc_method of this NetworkPool.  # noqa: E501

        Specifies how IP address allocation is done among pool members.  # noqa: E501

        :return: The alloc_method of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._alloc_method

    @alloc_method.setter
    def alloc_method(self, alloc_method):
        """Sets the alloc_method of this NetworkPool.

        Specifies how IP address allocation is done among pool members.  # noqa: E501

        :param alloc_method: The alloc_method of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["dynamic", "static"]  # noqa: E501
        if alloc_method not in allowed_values:
            raise ValueError(
                "Invalid value for `alloc_method` ({0}), must be one of {1}"  # noqa: E501
                .format(alloc_method, allowed_values)
            )

        self._alloc_method = alloc_method

    @property
    def description(self):
        """Gets the description of this NetworkPool.  # noqa: E501

        A description of the pool.  # noqa: E501

        :return: The description of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkPool.

        A description of the pool.  # noqa: E501

        :param description: The description of this NetworkPool.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def groupnet(self):
        """Gets the groupnet of this NetworkPool.  # noqa: E501

        Name of the groupnet this pool belongs to.  # noqa: E501

        :return: The groupnet of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this NetworkPool.

        Name of the groupnet this pool belongs to.  # noqa: E501

        :param groupnet: The groupnet of this NetworkPool.  # noqa: E501
        :type: str
        """
        if groupnet is not None and len(groupnet) > 32:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `32`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 1:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def id(self):
        """Gets the id of this NetworkPool.  # noqa: E501

        Unique Pool ID.  # noqa: E501

        :return: The id of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkPool.

        Unique Pool ID.  # noqa: E501

        :param id: The id of this NetworkPool.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 99:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `99`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def ifaces(self):
        """Gets the ifaces of this NetworkPool.  # noqa: E501

        List of interface members in this pool.  # noqa: E501

        :return: The ifaces of this NetworkPool.  # noqa: E501
        :rtype: list[SubnetsSubnetPoolIface]
        """
        return self._ifaces

    @ifaces.setter
    def ifaces(self, ifaces):
        """Sets the ifaces of this NetworkPool.

        List of interface members in this pool.  # noqa: E501

        :param ifaces: The ifaces of this NetworkPool.  # noqa: E501
        :type: list[SubnetsSubnetPoolIface]
        """

        self._ifaces = ifaces

    @property
    def name(self):
        """Gets the name of this NetworkPool.  # noqa: E501

        The name of the pool. It must be unique throughout the given subnet.It's a required field with POST method.  # noqa: E501

        :return: The name of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkPool.

        The name of the pool. It must be unique throughout the given subnet.It's a required field with POST method.  # noqa: E501

        :param name: The name of this NetworkPool.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[0-9a-zA-Z_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def ranges(self):
        """Gets the ranges of this NetworkPool.  # noqa: E501

        List of IP address ranges in this pool.  # noqa: E501

        :return: The ranges of this NetworkPool.  # noqa: E501
        :rtype: list[SubnetsSubnetPoolRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this NetworkPool.

        List of IP address ranges in this pool.  # noqa: E501

        :param ranges: The ranges of this NetworkPool.  # noqa: E501
        :type: list[SubnetsSubnetPoolRange]
        """

        self._ranges = ranges

    @property
    def rebalance_policy(self):
        """Gets the rebalance_policy of this NetworkPool.  # noqa: E501

        Rebalance policy..  # noqa: E501

        :return: The rebalance_policy of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._rebalance_policy

    @rebalance_policy.setter
    def rebalance_policy(self, rebalance_policy):
        """Sets the rebalance_policy of this NetworkPool.

        Rebalance policy..  # noqa: E501

        :param rebalance_policy: The rebalance_policy of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "manual"]  # noqa: E501
        if rebalance_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `rebalance_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(rebalance_policy, allowed_values)
            )

        self._rebalance_policy = rebalance_policy

    @property
    def rules(self):
        """Gets the rules of this NetworkPool.  # noqa: E501

        Names of the rules in this pool.  # noqa: E501

        :return: The rules of this NetworkPool.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this NetworkPool.

        Names of the rules in this pool.  # noqa: E501

        :param rules: The rules of this NetworkPool.  # noqa: E501
        :type: list[str]
        """

        self._rules = rules

    @property
    def sc_auto_unsuspend_delay(self):
        """Gets the sc_auto_unsuspend_delay of this NetworkPool.  # noqa: E501

        Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones.  # noqa: E501

        :return: The sc_auto_unsuspend_delay of this NetworkPool.  # noqa: E501
        :rtype: int
        """
        return self._sc_auto_unsuspend_delay

    @sc_auto_unsuspend_delay.setter
    def sc_auto_unsuspend_delay(self, sc_auto_unsuspend_delay):
        """Sets the sc_auto_unsuspend_delay of this NetworkPool.

        Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones.  # noqa: E501

        :param sc_auto_unsuspend_delay: The sc_auto_unsuspend_delay of this NetworkPool.  # noqa: E501
        :type: int
        """
        if sc_auto_unsuspend_delay is not None and sc_auto_unsuspend_delay > 86400:  # noqa: E501
            raise ValueError("Invalid value for `sc_auto_unsuspend_delay`, must be a value less than or equal to `86400`")  # noqa: E501
        if sc_auto_unsuspend_delay is not None and sc_auto_unsuspend_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `sc_auto_unsuspend_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sc_auto_unsuspend_delay = sc_auto_unsuspend_delay

    @property
    def sc_connect_policy(self):
        """Gets the sc_connect_policy of this NetworkPool.  # noqa: E501

        SmartConnect client connection balancing policy.  # noqa: E501

        :return: The sc_connect_policy of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._sc_connect_policy

    @sc_connect_policy.setter
    def sc_connect_policy(self, sc_connect_policy):
        """Sets the sc_connect_policy of this NetworkPool.

        SmartConnect client connection balancing policy.  # noqa: E501

        :param sc_connect_policy: The sc_connect_policy of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["round_robin", "conn_count", "throughput", "cpu_usage"]  # noqa: E501
        if sc_connect_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `sc_connect_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(sc_connect_policy, allowed_values)
            )

        self._sc_connect_policy = sc_connect_policy

    @property
    def sc_dns_zone(self):
        """Gets the sc_dns_zone of this NetworkPool.  # noqa: E501

        SmartConnect zone name for the pool.  # noqa: E501

        :return: The sc_dns_zone of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._sc_dns_zone

    @sc_dns_zone.setter
    def sc_dns_zone(self, sc_dns_zone):
        """Sets the sc_dns_zone of this NetworkPool.

        SmartConnect zone name for the pool.  # noqa: E501

        :param sc_dns_zone: The sc_dns_zone of this NetworkPool.  # noqa: E501
        :type: str
        """
        if sc_dns_zone is not None and len(sc_dns_zone) > 2048:
            raise ValueError("Invalid value for `sc_dns_zone`, length must be less than or equal to `2048`")  # noqa: E501
        if sc_dns_zone is not None and len(sc_dns_zone) < 0:
            raise ValueError("Invalid value for `sc_dns_zone`, length must be greater than or equal to `0`")  # noqa: E501
        if sc_dns_zone is not None and not re.search('^$|^[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]*)*$', sc_dns_zone):  # noqa: E501
            raise ValueError("Invalid value for `sc_dns_zone`, must be a follow pattern or equal to `/^$|^[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]*)*$/`")  # noqa: E501

        self._sc_dns_zone = sc_dns_zone

    @property
    def sc_dns_zone_aliases(self):
        """Gets the sc_dns_zone_aliases of this NetworkPool.  # noqa: E501

        List of SmartConnect zone aliases (DNS names) to the pool.  # noqa: E501

        :return: The sc_dns_zone_aliases of this NetworkPool.  # noqa: E501
        :rtype: list[str]
        """
        return self._sc_dns_zone_aliases

    @sc_dns_zone_aliases.setter
    def sc_dns_zone_aliases(self, sc_dns_zone_aliases):
        """Sets the sc_dns_zone_aliases of this NetworkPool.

        List of SmartConnect zone aliases (DNS names) to the pool.  # noqa: E501

        :param sc_dns_zone_aliases: The sc_dns_zone_aliases of this NetworkPool.  # noqa: E501
        :type: list[str]
        """

        self._sc_dns_zone_aliases = sc_dns_zone_aliases

    @property
    def sc_failover_policy(self):
        """Gets the sc_failover_policy of this NetworkPool.  # noqa: E501

        SmartConnect IP failover policy.  # noqa: E501

        :return: The sc_failover_policy of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._sc_failover_policy

    @sc_failover_policy.setter
    def sc_failover_policy(self, sc_failover_policy):
        """Sets the sc_failover_policy of this NetworkPool.

        SmartConnect IP failover policy.  # noqa: E501

        :param sc_failover_policy: The sc_failover_policy of this NetworkPool.  # noqa: E501
        :type: str
        """
        allowed_values = ["round_robin", "conn_count", "throughput", "cpu_usage"]  # noqa: E501
        if sc_failover_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `sc_failover_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(sc_failover_policy, allowed_values)
            )

        self._sc_failover_policy = sc_failover_policy

    @property
    def sc_subnet(self):
        """Gets the sc_subnet of this NetworkPool.  # noqa: E501

        Name of SmartConnect service subnet for this pool.  # noqa: E501

        :return: The sc_subnet of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._sc_subnet

    @sc_subnet.setter
    def sc_subnet(self, sc_subnet):
        """Sets the sc_subnet of this NetworkPool.

        Name of SmartConnect service subnet for this pool.  # noqa: E501

        :param sc_subnet: The sc_subnet of this NetworkPool.  # noqa: E501
        :type: str
        """
        if sc_subnet is not None and len(sc_subnet) > 32:
            raise ValueError("Invalid value for `sc_subnet`, length must be less than or equal to `32`")  # noqa: E501
        if sc_subnet is not None and len(sc_subnet) < 0:
            raise ValueError("Invalid value for `sc_subnet`, length must be greater than or equal to `0`")  # noqa: E501

        self._sc_subnet = sc_subnet

    @property
    def sc_suspended_nodes(self):
        """Gets the sc_suspended_nodes of this NetworkPool.  # noqa: E501

        List of LNNs showing currently suspended nodes in SmartConnect.  # noqa: E501

        :return: The sc_suspended_nodes of this NetworkPool.  # noqa: E501
        :rtype: list[int]
        """
        return self._sc_suspended_nodes

    @sc_suspended_nodes.setter
    def sc_suspended_nodes(self, sc_suspended_nodes):
        """Sets the sc_suspended_nodes of this NetworkPool.

        List of LNNs showing currently suspended nodes in SmartConnect.  # noqa: E501

        :param sc_suspended_nodes: The sc_suspended_nodes of this NetworkPool.  # noqa: E501
        :type: list[int]
        """

        self._sc_suspended_nodes = sc_suspended_nodes

    @property
    def sc_ttl(self):
        """Gets the sc_ttl of this NetworkPool.  # noqa: E501

        Time to live value for SmartConnect DNS query responses in seconds.  # noqa: E501

        :return: The sc_ttl of this NetworkPool.  # noqa: E501
        :rtype: int
        """
        return self._sc_ttl

    @sc_ttl.setter
    def sc_ttl(self, sc_ttl):
        """Sets the sc_ttl of this NetworkPool.

        Time to live value for SmartConnect DNS query responses in seconds.  # noqa: E501

        :param sc_ttl: The sc_ttl of this NetworkPool.  # noqa: E501
        :type: int
        """
        if sc_ttl is not None and sc_ttl > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `sc_ttl`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if sc_ttl is not None and sc_ttl < 0:  # noqa: E501
            raise ValueError("Invalid value for `sc_ttl`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sc_ttl = sc_ttl

    @property
    def static_routes(self):
        """Gets the static_routes of this NetworkPool.  # noqa: E501

        List of interface members in this pool.  # noqa: E501

        :return: The static_routes of this NetworkPool.  # noqa: E501
        :rtype: list[SubnetsSubnetPoolStaticRoute]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """Sets the static_routes of this NetworkPool.

        List of interface members in this pool.  # noqa: E501

        :param static_routes: The static_routes of this NetworkPool.  # noqa: E501
        :type: list[SubnetsSubnetPoolStaticRoute]
        """

        self._static_routes = static_routes

    @property
    def subnet(self):
        """Gets the subnet of this NetworkPool.  # noqa: E501

        The name of the subnet.  # noqa: E501

        :return: The subnet of this NetworkPool.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this NetworkPool.

        The name of the subnet.  # noqa: E501

        :param subnet: The subnet of this NetworkPool.  # noqa: E501
        :type: str
        """
        if subnet is not None and len(subnet) > 32:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `32`")  # noqa: E501
        if subnet is not None and len(subnet) < 1:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._subnet = subnet

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
        if not isinstance(other, NetworkPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
