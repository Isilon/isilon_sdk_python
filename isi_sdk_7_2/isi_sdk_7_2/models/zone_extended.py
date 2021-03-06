# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_7_2.models.group_member import GroupMember  # noqa: F401,E501


class ZoneExtended(object):
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
        'all_auth_providers': 'bool',
        'alternate_system_provider': 'str',
        'audit_failure': 'list[str]',
        'audit_success': 'list[str]',
        'auth_providers': 'list[str]',
        'cache_size': 'int',
        'create_path': 'bool',
        'hdfs_ambari_namenode': 'str',
        'hdfs_ambari_server': 'str',
        'hdfs_authentication': 'str',
        'hdfs_keytab': 'str',
        'hdfs_odp_version': 'str',
        'hdfs_root_directory': 'str',
        'home_directory_umask': 'int',
        'id': 'str',
        'ifs_restricted': 'list[GroupMember]',
        'map_untrusted': 'str',
        'name': 'str',
        'netbios_name': 'str',
        'path': 'str',
        'protocol_audit_enabled': 'bool',
        'skeleton_directory': 'str',
        'syslog_audit_events': 'list[str]',
        'syslog_forwarding_enabled': 'bool',
        'system': 'bool',
        'system_provider': 'str',
        'user_mapping_rules': 'list[str]',
        'webhdfs_enabled': 'bool',
        'zone_id': 'int'
    }

    attribute_map = {
        'all_auth_providers': 'all_auth_providers',
        'alternate_system_provider': 'alternate_system_provider',
        'audit_failure': 'audit_failure',
        'audit_success': 'audit_success',
        'auth_providers': 'auth_providers',
        'cache_size': 'cache_size',
        'create_path': 'create_path',
        'hdfs_ambari_namenode': 'hdfs_ambari_namenode',
        'hdfs_ambari_server': 'hdfs_ambari_server',
        'hdfs_authentication': 'hdfs_authentication',
        'hdfs_keytab': 'hdfs_keytab',
        'hdfs_odp_version': 'hdfs_odp_version',
        'hdfs_root_directory': 'hdfs_root_directory',
        'home_directory_umask': 'home_directory_umask',
        'id': 'id',
        'ifs_restricted': 'ifs_restricted',
        'map_untrusted': 'map_untrusted',
        'name': 'name',
        'netbios_name': 'netbios_name',
        'path': 'path',
        'protocol_audit_enabled': 'protocol_audit_enabled',
        'skeleton_directory': 'skeleton_directory',
        'syslog_audit_events': 'syslog_audit_events',
        'syslog_forwarding_enabled': 'syslog_forwarding_enabled',
        'system': 'system',
        'system_provider': 'system_provider',
        'user_mapping_rules': 'user_mapping_rules',
        'webhdfs_enabled': 'webhdfs_enabled',
        'zone_id': 'zone_id'
    }

    def __init__(self, all_auth_providers=None, alternate_system_provider=None, audit_failure=None, audit_success=None, auth_providers=None, cache_size=None, create_path=None, hdfs_ambari_namenode=None, hdfs_ambari_server=None, hdfs_authentication=None, hdfs_keytab=None, hdfs_odp_version=None, hdfs_root_directory=None, home_directory_umask=None, id=None, ifs_restricted=None, map_untrusted=None, name=None, netbios_name=None, path=None, protocol_audit_enabled=None, skeleton_directory=None, syslog_audit_events=None, syslog_forwarding_enabled=None, system=None, system_provider=None, user_mapping_rules=None, webhdfs_enabled=None, zone_id=None):  # noqa: E501
        """ZoneExtended - a model defined in Swagger"""  # noqa: E501

        self._all_auth_providers = None
        self._alternate_system_provider = None
        self._audit_failure = None
        self._audit_success = None
        self._auth_providers = None
        self._cache_size = None
        self._create_path = None
        self._hdfs_ambari_namenode = None
        self._hdfs_ambari_server = None
        self._hdfs_authentication = None
        self._hdfs_keytab = None
        self._hdfs_odp_version = None
        self._hdfs_root_directory = None
        self._home_directory_umask = None
        self._id = None
        self._ifs_restricted = None
        self._map_untrusted = None
        self._name = None
        self._netbios_name = None
        self._path = None
        self._protocol_audit_enabled = None
        self._skeleton_directory = None
        self._syslog_audit_events = None
        self._syslog_forwarding_enabled = None
        self._system = None
        self._system_provider = None
        self._user_mapping_rules = None
        self._webhdfs_enabled = None
        self._zone_id = None
        self.discriminator = None

        if all_auth_providers is not None:
            self.all_auth_providers = all_auth_providers
        if alternate_system_provider is not None:
            self.alternate_system_provider = alternate_system_provider
        if audit_failure is not None:
            self.audit_failure = audit_failure
        if audit_success is not None:
            self.audit_success = audit_success
        if auth_providers is not None:
            self.auth_providers = auth_providers
        if cache_size is not None:
            self.cache_size = cache_size
        if create_path is not None:
            self.create_path = create_path
        if hdfs_ambari_namenode is not None:
            self.hdfs_ambari_namenode = hdfs_ambari_namenode
        if hdfs_ambari_server is not None:
            self.hdfs_ambari_server = hdfs_ambari_server
        if hdfs_authentication is not None:
            self.hdfs_authentication = hdfs_authentication
        if hdfs_keytab is not None:
            self.hdfs_keytab = hdfs_keytab
        if hdfs_odp_version is not None:
            self.hdfs_odp_version = hdfs_odp_version
        if hdfs_root_directory is not None:
            self.hdfs_root_directory = hdfs_root_directory
        if home_directory_umask is not None:
            self.home_directory_umask = home_directory_umask
        if id is not None:
            self.id = id
        if ifs_restricted is not None:
            self.ifs_restricted = ifs_restricted
        if map_untrusted is not None:
            self.map_untrusted = map_untrusted
        if name is not None:
            self.name = name
        if netbios_name is not None:
            self.netbios_name = netbios_name
        if path is not None:
            self.path = path
        if protocol_audit_enabled is not None:
            self.protocol_audit_enabled = protocol_audit_enabled
        if skeleton_directory is not None:
            self.skeleton_directory = skeleton_directory
        if syslog_audit_events is not None:
            self.syslog_audit_events = syslog_audit_events
        if syslog_forwarding_enabled is not None:
            self.syslog_forwarding_enabled = syslog_forwarding_enabled
        if system is not None:
            self.system = system
        if system_provider is not None:
            self.system_provider = system_provider
        if user_mapping_rules is not None:
            self.user_mapping_rules = user_mapping_rules
        if webhdfs_enabled is not None:
            self.webhdfs_enabled = webhdfs_enabled
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def all_auth_providers(self):
        """Gets the all_auth_providers of this ZoneExtended.  # noqa: E501

        Use all authentication providers available.  # noqa: E501

        :return: The all_auth_providers of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._all_auth_providers

    @all_auth_providers.setter
    def all_auth_providers(self, all_auth_providers):
        """Sets the all_auth_providers of this ZoneExtended.

        Use all authentication providers available.  # noqa: E501

        :param all_auth_providers: The all_auth_providers of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._all_auth_providers = all_auth_providers

    @property
    def alternate_system_provider(self):
        """Gets the alternate_system_provider of this ZoneExtended.  # noqa: E501

        Alternate system provider.  # noqa: E501

        :return: The alternate_system_provider of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._alternate_system_provider

    @alternate_system_provider.setter
    def alternate_system_provider(self, alternate_system_provider):
        """Sets the alternate_system_provider of this ZoneExtended.

        Alternate system provider.  # noqa: E501

        :param alternate_system_provider: The alternate_system_provider of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._alternate_system_provider = alternate_system_provider

    @property
    def audit_failure(self):
        """Gets the audit_failure of this ZoneExtended.  # noqa: E501

        List of failed operations to audit.  # noqa: E501

        :return: The audit_failure of this ZoneExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_failure

    @audit_failure.setter
    def audit_failure(self, audit_failure):
        """Sets the audit_failure of this ZoneExtended.

        List of failed operations to audit.  # noqa: E501

        :param audit_failure: The audit_failure of this ZoneExtended.  # noqa: E501
        :type: list[str]
        """

        self._audit_failure = audit_failure

    @property
    def audit_success(self):
        """Gets the audit_success of this ZoneExtended.  # noqa: E501

        List of successful operations to audit.  # noqa: E501

        :return: The audit_success of this ZoneExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_success

    @audit_success.setter
    def audit_success(self, audit_success):
        """Sets the audit_success of this ZoneExtended.

        List of successful operations to audit.  # noqa: E501

        :param audit_success: The audit_success of this ZoneExtended.  # noqa: E501
        :type: list[str]
        """

        self._audit_success = audit_success

    @property
    def auth_providers(self):
        """Gets the auth_providers of this ZoneExtended.  # noqa: E501

        List of authentication providers used on this zone.  # noqa: E501

        :return: The auth_providers of this ZoneExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._auth_providers

    @auth_providers.setter
    def auth_providers(self, auth_providers):
        """Sets the auth_providers of this ZoneExtended.

        List of authentication providers used on this zone.  # noqa: E501

        :param auth_providers: The auth_providers of this ZoneExtended.  # noqa: E501
        :type: list[str]
        """

        self._auth_providers = auth_providers

    @property
    def cache_size(self):
        """Gets the cache_size of this ZoneExtended.  # noqa: E501

        Specifies the maximum size of zone in-memory cache.  # noqa: E501

        :return: The cache_size of this ZoneExtended.  # noqa: E501
        :rtype: int
        """
        return self._cache_size

    @cache_size.setter
    def cache_size(self, cache_size):
        """Sets the cache_size of this ZoneExtended.

        Specifies the maximum size of zone in-memory cache.  # noqa: E501

        :param cache_size: The cache_size of this ZoneExtended.  # noqa: E501
        :type: int
        """

        self._cache_size = cache_size

    @property
    def create_path(self):
        """Gets the create_path of this ZoneExtended.  # noqa: E501

        Create path if it does not exist.  # noqa: E501

        :return: The create_path of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._create_path

    @create_path.setter
    def create_path(self, create_path):
        """Sets the create_path of this ZoneExtended.

        Create path if it does not exist.  # noqa: E501

        :param create_path: The create_path of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._create_path = create_path

    @property
    def hdfs_ambari_namenode(self):
        """Gets the hdfs_ambari_namenode of this ZoneExtended.  # noqa: E501

        The SmartConnect name of this cluster that will be used for the HDFS service.  # noqa: E501

        :return: The hdfs_ambari_namenode of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_ambari_namenode

    @hdfs_ambari_namenode.setter
    def hdfs_ambari_namenode(self, hdfs_ambari_namenode):
        """Sets the hdfs_ambari_namenode of this ZoneExtended.

        The SmartConnect name of this cluster that will be used for the HDFS service.  # noqa: E501

        :param hdfs_ambari_namenode: The hdfs_ambari_namenode of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._hdfs_ambari_namenode = hdfs_ambari_namenode

    @property
    def hdfs_ambari_server(self):
        """Gets the hdfs_ambari_server of this ZoneExtended.  # noqa: E501

        A valid hostname, FQDN, IPv4, or IPv6 string of the Ambari server.  # noqa: E501

        :return: The hdfs_ambari_server of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_ambari_server

    @hdfs_ambari_server.setter
    def hdfs_ambari_server(self, hdfs_ambari_server):
        """Sets the hdfs_ambari_server of this ZoneExtended.

        A valid hostname, FQDN, IPv4, or IPv6 string of the Ambari server.  # noqa: E501

        :param hdfs_ambari_server: The hdfs_ambari_server of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._hdfs_ambari_server = hdfs_ambari_server

    @property
    def hdfs_authentication(self):
        """Gets the hdfs_authentication of this ZoneExtended.  # noqa: E501

        Authentication type for HDFS protocol.  # noqa: E501

        :return: The hdfs_authentication of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_authentication

    @hdfs_authentication.setter
    def hdfs_authentication(self, hdfs_authentication):
        """Sets the hdfs_authentication of this ZoneExtended.

        Authentication type for HDFS protocol.  # noqa: E501

        :param hdfs_authentication: The hdfs_authentication of this ZoneExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "simple_only", "kerberos_only"]  # noqa: E501
        if hdfs_authentication not in allowed_values:
            raise ValueError(
                "Invalid value for `hdfs_authentication` ({0}), must be one of {1}"  # noqa: E501
                .format(hdfs_authentication, allowed_values)
            )

        self._hdfs_authentication = hdfs_authentication

    @property
    def hdfs_keytab(self):
        """Gets the hdfs_keytab of this ZoneExtended.  # noqa: E501

        Kerberos keytab to use for HDFS authentication.  # noqa: E501

        :return: The hdfs_keytab of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_keytab

    @hdfs_keytab.setter
    def hdfs_keytab(self, hdfs_keytab):
        """Sets the hdfs_keytab of this ZoneExtended.

        Kerberos keytab to use for HDFS authentication.  # noqa: E501

        :param hdfs_keytab: The hdfs_keytab of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._hdfs_keytab = hdfs_keytab

    @property
    def hdfs_odp_version(self):
        """Gets the hdfs_odp_version of this ZoneExtended.  # noqa: E501

        ODP stack repository version number.  # noqa: E501

        :return: The hdfs_odp_version of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_odp_version

    @hdfs_odp_version.setter
    def hdfs_odp_version(self, hdfs_odp_version):
        """Sets the hdfs_odp_version of this ZoneExtended.

        ODP stack repository version number.  # noqa: E501

        :param hdfs_odp_version: The hdfs_odp_version of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._hdfs_odp_version = hdfs_odp_version

    @property
    def hdfs_root_directory(self):
        """Gets the hdfs_root_directory of this ZoneExtended.  # noqa: E501

        Root directory for HDFS protocol.  # noqa: E501

        :return: The hdfs_root_directory of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_root_directory

    @hdfs_root_directory.setter
    def hdfs_root_directory(self, hdfs_root_directory):
        """Sets the hdfs_root_directory of this ZoneExtended.

        Root directory for HDFS protocol.  # noqa: E501

        :param hdfs_root_directory: The hdfs_root_directory of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._hdfs_root_directory = hdfs_root_directory

    @property
    def home_directory_umask(self):
        """Gets the home_directory_umask of this ZoneExtended.  # noqa: E501

        Permissions set on auto-created user home directories.  # noqa: E501

        :return: The home_directory_umask of this ZoneExtended.  # noqa: E501
        :rtype: int
        """
        return self._home_directory_umask

    @home_directory_umask.setter
    def home_directory_umask(self, home_directory_umask):
        """Sets the home_directory_umask of this ZoneExtended.

        Permissions set on auto-created user home directories.  # noqa: E501

        :param home_directory_umask: The home_directory_umask of this ZoneExtended.  # noqa: E501
        :type: int
        """

        self._home_directory_umask = home_directory_umask

    @property
    def id(self):
        """Gets the id of this ZoneExtended.  # noqa: E501

        ID.  # noqa: E501

        :return: The id of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ZoneExtended.

        ID.  # noqa: E501

        :param id: The id of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ifs_restricted(self):
        """Gets the ifs_restricted of this ZoneExtended.  # noqa: E501

        User restrictions for this zone.  # noqa: E501

        :return: The ifs_restricted of this ZoneExtended.  # noqa: E501
        :rtype: list[GroupMember]
        """
        return self._ifs_restricted

    @ifs_restricted.setter
    def ifs_restricted(self, ifs_restricted):
        """Sets the ifs_restricted of this ZoneExtended.

        User restrictions for this zone.  # noqa: E501

        :param ifs_restricted: The ifs_restricted of this ZoneExtended.  # noqa: E501
        :type: list[GroupMember]
        """

        self._ifs_restricted = ifs_restricted

    @property
    def map_untrusted(self):
        """Gets the map_untrusted of this ZoneExtended.  # noqa: E501

        Maps untrusted domains to this NetBIOS domain during authentication.  # noqa: E501

        :return: The map_untrusted of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._map_untrusted

    @map_untrusted.setter
    def map_untrusted(self, map_untrusted):
        """Sets the map_untrusted of this ZoneExtended.

        Maps untrusted domains to this NetBIOS domain during authentication.  # noqa: E501

        :param map_untrusted: The map_untrusted of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._map_untrusted = map_untrusted

    @property
    def name(self):
        """Gets the name of this ZoneExtended.  # noqa: E501

        Zone name.  # noqa: E501

        :return: The name of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ZoneExtended.

        Zone name.  # noqa: E501

        :param name: The name of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def netbios_name(self):
        """Gets the netbios_name of this ZoneExtended.  # noqa: E501

        NetBIOS name.  # noqa: E501

        :return: The netbios_name of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """Sets the netbios_name of this ZoneExtended.

        NetBIOS name.  # noqa: E501

        :param netbios_name: The netbios_name of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._netbios_name = netbios_name

    @property
    def path(self):
        """Gets the path of this ZoneExtended.  # noqa: E501

        zone path.  # noqa: E501

        :return: The path of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ZoneExtended.

        zone path.  # noqa: E501

        :param path: The path of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def protocol_audit_enabled(self):
        """Gets the protocol_audit_enabled of this ZoneExtended.  # noqa: E501

        Indicates whether I/O auditing is set on this zone.  # noqa: E501

        :return: The protocol_audit_enabled of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._protocol_audit_enabled

    @protocol_audit_enabled.setter
    def protocol_audit_enabled(self, protocol_audit_enabled):
        """Sets the protocol_audit_enabled of this ZoneExtended.

        Indicates whether I/O auditing is set on this zone.  # noqa: E501

        :param protocol_audit_enabled: The protocol_audit_enabled of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._protocol_audit_enabled = protocol_audit_enabled

    @property
    def skeleton_directory(self):
        """Gets the skeleton_directory of this ZoneExtended.  # noqa: E501

        Skeleton directory for user home directories.  # noqa: E501

        :return: The skeleton_directory of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._skeleton_directory

    @skeleton_directory.setter
    def skeleton_directory(self, skeleton_directory):
        """Sets the skeleton_directory of this ZoneExtended.

        Skeleton directory for user home directories.  # noqa: E501

        :param skeleton_directory: The skeleton_directory of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._skeleton_directory = skeleton_directory

    @property
    def syslog_audit_events(self):
        """Gets the syslog_audit_events of this ZoneExtended.  # noqa: E501

        List of audit operations to forward to syslog.  # noqa: E501

        :return: The syslog_audit_events of this ZoneExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._syslog_audit_events

    @syslog_audit_events.setter
    def syslog_audit_events(self, syslog_audit_events):
        """Sets the syslog_audit_events of this ZoneExtended.

        List of audit operations to forward to syslog.  # noqa: E501

        :param syslog_audit_events: The syslog_audit_events of this ZoneExtended.  # noqa: E501
        :type: list[str]
        """

        self._syslog_audit_events = syslog_audit_events

    @property
    def syslog_forwarding_enabled(self):
        """Gets the syslog_forwarding_enabled of this ZoneExtended.  # noqa: E501

        Enable syslog forwarding of zone audit events.  # noqa: E501

        :return: The syslog_forwarding_enabled of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._syslog_forwarding_enabled

    @syslog_forwarding_enabled.setter
    def syslog_forwarding_enabled(self, syslog_forwarding_enabled):
        """Sets the syslog_forwarding_enabled of this ZoneExtended.

        Enable syslog forwarding of zone audit events.  # noqa: E501

        :param syslog_forwarding_enabled: The syslog_forwarding_enabled of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._syslog_forwarding_enabled = syslog_forwarding_enabled

    @property
    def system(self):
        """Gets the system of this ZoneExtended.  # noqa: E501

        Zone is built-in.  # noqa: E501

        :return: The system of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this ZoneExtended.

        Zone is built-in.  # noqa: E501

        :param system: The system of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def system_provider(self):
        """Gets the system_provider of this ZoneExtended.  # noqa: E501

        System provider.  # noqa: E501

        :return: The system_provider of this ZoneExtended.  # noqa: E501
        :rtype: str
        """
        return self._system_provider

    @system_provider.setter
    def system_provider(self, system_provider):
        """Sets the system_provider of this ZoneExtended.

        System provider.  # noqa: E501

        :param system_provider: The system_provider of this ZoneExtended.  # noqa: E501
        :type: str
        """

        self._system_provider = system_provider

    @property
    def user_mapping_rules(self):
        """Gets the user_mapping_rules of this ZoneExtended.  # noqa: E501

        Current ID mapping rules.  # noqa: E501

        :return: The user_mapping_rules of this ZoneExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_mapping_rules

    @user_mapping_rules.setter
    def user_mapping_rules(self, user_mapping_rules):
        """Sets the user_mapping_rules of this ZoneExtended.

        Current ID mapping rules.  # noqa: E501

        :param user_mapping_rules: The user_mapping_rules of this ZoneExtended.  # noqa: E501
        :type: list[str]
        """

        self._user_mapping_rules = user_mapping_rules

    @property
    def webhdfs_enabled(self):
        """Gets the webhdfs_enabled of this ZoneExtended.  # noqa: E501

        Indicates whether WebHDFS is enabled on this zone.  # noqa: E501

        :return: The webhdfs_enabled of this ZoneExtended.  # noqa: E501
        :rtype: bool
        """
        return self._webhdfs_enabled

    @webhdfs_enabled.setter
    def webhdfs_enabled(self, webhdfs_enabled):
        """Sets the webhdfs_enabled of this ZoneExtended.

        Indicates whether WebHDFS is enabled on this zone.  # noqa: E501

        :param webhdfs_enabled: The webhdfs_enabled of this ZoneExtended.  # noqa: E501
        :type: bool
        """

        self._webhdfs_enabled = webhdfs_enabled

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneExtended.  # noqa: E501

        Zone ID.  # noqa: E501

        :return: The zone_id of this ZoneExtended.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneExtended.

        Zone ID.  # noqa: E501

        :param zone_id: The zone_id of this ZoneExtended.  # noqa: E501
        :type: int
        """

        self._zone_id = zone_id

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
        if not isinstance(other, ZoneExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
