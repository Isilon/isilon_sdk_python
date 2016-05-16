# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ProvidersAdsItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProvidersAdsItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account': 'str',
            'allocate_gids': 'bool',
            'allocate_uids': 'bool',
            'assume_default_domain': 'bool',
            'authentication': 'bool',
            'check_online_interval': 'int',
            'controller_time': 'int',
            'create_home_directory': 'bool',
            'dns_domain': 'str',
            'domain_offline_alerts': 'bool',
            'findable_groups': 'list[str]',
            'findable_users': 'list[str]',
            'groupnet': 'str',
            'home_directory_template': 'str',
            'ignore_all_trusts': 'bool',
            'ignored_trusted_domains': 'list[str]',
            'include_trusted_domains': 'list[str]',
            'instance': 'str',
            'kerberos_hdfs_spn': 'bool',
            'kerberos_nfs_spn': 'bool',
            'ldap_sign_and_seal': 'bool',
            'login_shell': 'str',
            'lookup_domains': 'list[str]',
            'lookup_groups': 'bool',
            'lookup_normalize_groups': 'bool',
            'lookup_normalize_users': 'bool',
            'lookup_users': 'bool',
            'machine_name': 'str',
            'machine_password_changes': 'bool',
            'machine_password_lifespan': 'int',
            'name': 'str',
            'node_dc_affinity': 'str',
            'node_dc_affinity_timeout': 'int',
            'nss_enumeration': 'bool',
            'organizational_unit': 'str',
            'password': 'str',
            'restrict_findable': 'bool',
            'sfu_support': 'str',
            'store_sfu_mappings': 'bool',
            'unfindable_groups': 'list[str]',
            'unfindable_users': 'list[str]',
            'user': 'str'
        }

        self.attribute_map = {
            'account': 'account',
            'allocate_gids': 'allocate_gids',
            'allocate_uids': 'allocate_uids',
            'assume_default_domain': 'assume_default_domain',
            'authentication': 'authentication',
            'check_online_interval': 'check_online_interval',
            'controller_time': 'controller_time',
            'create_home_directory': 'create_home_directory',
            'dns_domain': 'dns_domain',
            'domain_offline_alerts': 'domain_offline_alerts',
            'findable_groups': 'findable_groups',
            'findable_users': 'findable_users',
            'groupnet': 'groupnet',
            'home_directory_template': 'home_directory_template',
            'ignore_all_trusts': 'ignore_all_trusts',
            'ignored_trusted_domains': 'ignored_trusted_domains',
            'include_trusted_domains': 'include_trusted_domains',
            'instance': 'instance',
            'kerberos_hdfs_spn': 'kerberos_hdfs_spn',
            'kerberos_nfs_spn': 'kerberos_nfs_spn',
            'ldap_sign_and_seal': 'ldap_sign_and_seal',
            'login_shell': 'login_shell',
            'lookup_domains': 'lookup_domains',
            'lookup_groups': 'lookup_groups',
            'lookup_normalize_groups': 'lookup_normalize_groups',
            'lookup_normalize_users': 'lookup_normalize_users',
            'lookup_users': 'lookup_users',
            'machine_name': 'machine_name',
            'machine_password_changes': 'machine_password_changes',
            'machine_password_lifespan': 'machine_password_lifespan',
            'name': 'name',
            'node_dc_affinity': 'node_dc_affinity',
            'node_dc_affinity_timeout': 'node_dc_affinity_timeout',
            'nss_enumeration': 'nss_enumeration',
            'organizational_unit': 'organizational_unit',
            'password': 'password',
            'restrict_findable': 'restrict_findable',
            'sfu_support': 'sfu_support',
            'store_sfu_mappings': 'store_sfu_mappings',
            'unfindable_groups': 'unfindable_groups',
            'unfindable_users': 'unfindable_users',
            'user': 'user'
        }

        self._account = None
        self._allocate_gids = None
        self._allocate_uids = None
        self._assume_default_domain = None
        self._authentication = None
        self._check_online_interval = None
        self._controller_time = None
        self._create_home_directory = None
        self._dns_domain = None
        self._domain_offline_alerts = None
        self._findable_groups = None
        self._findable_users = None
        self._groupnet = None
        self._home_directory_template = None
        self._ignore_all_trusts = None
        self._ignored_trusted_domains = None
        self._include_trusted_domains = None
        self._instance = None
        self._kerberos_hdfs_spn = None
        self._kerberos_nfs_spn = None
        self._ldap_sign_and_seal = None
        self._login_shell = None
        self._lookup_domains = None
        self._lookup_groups = None
        self._lookup_normalize_groups = None
        self._lookup_normalize_users = None
        self._lookup_users = None
        self._machine_name = None
        self._machine_password_changes = None
        self._machine_password_lifespan = None
        self._name = None
        self._node_dc_affinity = None
        self._node_dc_affinity_timeout = None
        self._nss_enumeration = None
        self._organizational_unit = None
        self._password = None
        self._restrict_findable = None
        self._sfu_support = None
        self._store_sfu_mappings = None
        self._unfindable_groups = None
        self._unfindable_users = None
        self._user = None

    @property
    def account(self):
        """
        Gets the account of this ProvidersAdsItem.
        Specifies the machine account name when creating a SAM account with Active Directory. The default cluster name is called 'default'.

        :return: The account of this ProvidersAdsItem.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this ProvidersAdsItem.
        Specifies the machine account name when creating a SAM account with Active Directory. The default cluster name is called 'default'.

        :param account: The account of this ProvidersAdsItem.
        :type: str
        """
        
        self._account = account

    @property
    def allocate_gids(self):
        """
        Gets the allocate_gids of this ProvidersAdsItem.
        Allocates an ID for an unmapped Active Directory (ADS) group. ADS groups without GIDs can be proactively assigned a GID by the ID mapper. If the ID mapper option is disabled, GIDs are not proactively assigned, and when a primary group for a user does not include a GID, the system may allocate one. 

        :return: The allocate_gids of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._allocate_gids

    @allocate_gids.setter
    def allocate_gids(self, allocate_gids):
        """
        Sets the allocate_gids of this ProvidersAdsItem.
        Allocates an ID for an unmapped Active Directory (ADS) group. ADS groups without GIDs can be proactively assigned a GID by the ID mapper. If the ID mapper option is disabled, GIDs are not proactively assigned, and when a primary group for a user does not include a GID, the system may allocate one. 

        :param allocate_gids: The allocate_gids of this ProvidersAdsItem.
        :type: bool
        """
        
        self._allocate_gids = allocate_gids

    @property
    def allocate_uids(self):
        """
        Gets the allocate_uids of this ProvidersAdsItem.
        Allocates a user ID for an unmapped Active Directory (ADS) user. ADS users without UIDs can be proactively assigned a UID by the ID mapper. IF the ID mapper option is disabled, UIDs are not proactively assigned, and when an identify for a user does not include a UID, the system may allocate one.

        :return: The allocate_uids of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._allocate_uids

    @allocate_uids.setter
    def allocate_uids(self, allocate_uids):
        """
        Sets the allocate_uids of this ProvidersAdsItem.
        Allocates a user ID for an unmapped Active Directory (ADS) user. ADS users without UIDs can be proactively assigned a UID by the ID mapper. IF the ID mapper option is disabled, UIDs are not proactively assigned, and when an identify for a user does not include a UID, the system may allocate one.

        :param allocate_uids: The allocate_uids of this ProvidersAdsItem.
        :type: bool
        """
        
        self._allocate_uids = allocate_uids

    @property
    def assume_default_domain(self):
        """
        Gets the assume_default_domain of this ProvidersAdsItem.
        Enables lookup of unqualified user names in the primary domain.

        :return: The assume_default_domain of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._assume_default_domain

    @assume_default_domain.setter
    def assume_default_domain(self, assume_default_domain):
        """
        Sets the assume_default_domain of this ProvidersAdsItem.
        Enables lookup of unqualified user names in the primary domain.

        :param assume_default_domain: The assume_default_domain of this ProvidersAdsItem.
        :type: bool
        """
        
        self._assume_default_domain = assume_default_domain

    @property
    def authentication(self):
        """
        Gets the authentication of this ProvidersAdsItem.
        Enables authentication and identity management through the authentication provider.

        :return: The authentication of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ProvidersAdsItem.
        Enables authentication and identity management through the authentication provider.

        :param authentication: The authentication of this ProvidersAdsItem.
        :type: bool
        """
        
        self._authentication = authentication

    @property
    def check_online_interval(self):
        """
        Gets the check_online_interval of this ProvidersAdsItem.
        Specifies the time in seconds between provider online checks.

        :return: The check_online_interval of this ProvidersAdsItem.
        :rtype: int
        """
        return self._check_online_interval

    @check_online_interval.setter
    def check_online_interval(self, check_online_interval):
        """
        Sets the check_online_interval of this ProvidersAdsItem.
        Specifies the time in seconds between provider online checks.

        :param check_online_interval: The check_online_interval of this ProvidersAdsItem.
        :type: int
        """
        
        self._check_online_interval = check_online_interval

    @property
    def controller_time(self):
        """
        Gets the controller_time of this ProvidersAdsItem.
        Specifies the current time for the domain controllers.

        :return: The controller_time of this ProvidersAdsItem.
        :rtype: int
        """
        return self._controller_time

    @controller_time.setter
    def controller_time(self, controller_time):
        """
        Sets the controller_time of this ProvidersAdsItem.
        Specifies the current time for the domain controllers.

        :param controller_time: The controller_time of this ProvidersAdsItem.
        :type: int
        """
        
        self._controller_time = controller_time

    @property
    def create_home_directory(self):
        """
        Gets the create_home_directory of this ProvidersAdsItem.
        Automatically creates a home directory on the first login.

        :return: The create_home_directory of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """
        Sets the create_home_directory of this ProvidersAdsItem.
        Automatically creates a home directory on the first login.

        :param create_home_directory: The create_home_directory of this ProvidersAdsItem.
        :type: bool
        """
        
        self._create_home_directory = create_home_directory

    @property
    def dns_domain(self):
        """
        Gets the dns_domain of this ProvidersAdsItem.
        Specifies the DNS search domain. Set this parameter if the DNS search domain has a unique name or address.

        :return: The dns_domain of this ProvidersAdsItem.
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """
        Sets the dns_domain of this ProvidersAdsItem.
        Specifies the DNS search domain. Set this parameter if the DNS search domain has a unique name or address.

        :param dns_domain: The dns_domain of this ProvidersAdsItem.
        :type: str
        """
        
        self._dns_domain = dns_domain

    @property
    def domain_offline_alerts(self):
        """
        Gets the domain_offline_alerts of this ProvidersAdsItem.
        Sends an alert if the domain goes offline.

        :return: The domain_offline_alerts of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._domain_offline_alerts

    @domain_offline_alerts.setter
    def domain_offline_alerts(self, domain_offline_alerts):
        """
        Sets the domain_offline_alerts of this ProvidersAdsItem.
        Sends an alert if the domain goes offline.

        :param domain_offline_alerts: The domain_offline_alerts of this ProvidersAdsItem.
        :type: bool
        """
        
        self._domain_offline_alerts = domain_offline_alerts

    @property
    def findable_groups(self):
        """
        Gets the findable_groups of this ProvidersAdsItem.
        Sets list of groups that can be resolved.

        :return: The findable_groups of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._findable_groups

    @findable_groups.setter
    def findable_groups(self, findable_groups):
        """
        Sets the findable_groups of this ProvidersAdsItem.
        Sets list of groups that can be resolved.

        :param findable_groups: The findable_groups of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._findable_groups = findable_groups

    @property
    def findable_users(self):
        """
        Gets the findable_users of this ProvidersAdsItem.
        Sets list of users that can be resolved.

        :return: The findable_users of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._findable_users

    @findable_users.setter
    def findable_users(self, findable_users):
        """
        Sets the findable_users of this ProvidersAdsItem.
        Sets list of users that can be resolved.

        :param findable_users: The findable_users of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._findable_users = findable_users

    @property
    def groupnet(self):
        """
        Gets the groupnet of this ProvidersAdsItem.
        Groupnet identifier.

        :return: The groupnet of this ProvidersAdsItem.
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """
        Sets the groupnet of this ProvidersAdsItem.
        Groupnet identifier.

        :param groupnet: The groupnet of this ProvidersAdsItem.
        :type: str
        """
        
        self._groupnet = groupnet

    @property
    def home_directory_template(self):
        """
        Gets the home_directory_template of this ProvidersAdsItem.
        Specifies the path to the home directory template.

        :return: The home_directory_template of this ProvidersAdsItem.
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """
        Sets the home_directory_template of this ProvidersAdsItem.
        Specifies the path to the home directory template.

        :param home_directory_template: The home_directory_template of this ProvidersAdsItem.
        :type: str
        """
        
        self._home_directory_template = home_directory_template

    @property
    def ignore_all_trusts(self):
        """
        Gets the ignore_all_trusts of this ProvidersAdsItem.
        If set to true, ignores all trusted domains.

        :return: The ignore_all_trusts of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._ignore_all_trusts

    @ignore_all_trusts.setter
    def ignore_all_trusts(self, ignore_all_trusts):
        """
        Sets the ignore_all_trusts of this ProvidersAdsItem.
        If set to true, ignores all trusted domains.

        :param ignore_all_trusts: The ignore_all_trusts of this ProvidersAdsItem.
        :type: bool
        """
        
        self._ignore_all_trusts = ignore_all_trusts

    @property
    def ignored_trusted_domains(self):
        """
        Gets the ignored_trusted_domains of this ProvidersAdsItem.
        Includes trusted domains when 'ignore_all_trusts' is set to false.

        :return: The ignored_trusted_domains of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._ignored_trusted_domains

    @ignored_trusted_domains.setter
    def ignored_trusted_domains(self, ignored_trusted_domains):
        """
        Sets the ignored_trusted_domains of this ProvidersAdsItem.
        Includes trusted domains when 'ignore_all_trusts' is set to false.

        :param ignored_trusted_domains: The ignored_trusted_domains of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._ignored_trusted_domains = ignored_trusted_domains

    @property
    def include_trusted_domains(self):
        """
        Gets the include_trusted_domains of this ProvidersAdsItem.
        Includes trusted domains when 'ignore_all_trusts' is set to true.

        :return: The include_trusted_domains of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._include_trusted_domains

    @include_trusted_domains.setter
    def include_trusted_domains(self, include_trusted_domains):
        """
        Sets the include_trusted_domains of this ProvidersAdsItem.
        Includes trusted domains when 'ignore_all_trusts' is set to true.

        :param include_trusted_domains: The include_trusted_domains of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._include_trusted_domains = include_trusted_domains

    @property
    def instance(self):
        """
        Gets the instance of this ProvidersAdsItem.
        Specifies Active Directory provider instnace.

        :return: The instance of this ProvidersAdsItem.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """
        Sets the instance of this ProvidersAdsItem.
        Specifies Active Directory provider instnace.

        :param instance: The instance of this ProvidersAdsItem.
        :type: str
        """
        
        self._instance = instance

    @property
    def kerberos_hdfs_spn(self):
        """
        Gets the kerberos_hdfs_spn of this ProvidersAdsItem.
        Determines if connecting through HDFS with Kerberos.

        :return: The kerberos_hdfs_spn of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._kerberos_hdfs_spn

    @kerberos_hdfs_spn.setter
    def kerberos_hdfs_spn(self, kerberos_hdfs_spn):
        """
        Sets the kerberos_hdfs_spn of this ProvidersAdsItem.
        Determines if connecting through HDFS with Kerberos.

        :param kerberos_hdfs_spn: The kerberos_hdfs_spn of this ProvidersAdsItem.
        :type: bool
        """
        
        self._kerberos_hdfs_spn = kerberos_hdfs_spn

    @property
    def kerberos_nfs_spn(self):
        """
        Gets the kerberos_nfs_spn of this ProvidersAdsItem.
        Determines if connecting through NFS with Kerberos.

        :return: The kerberos_nfs_spn of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._kerberos_nfs_spn

    @kerberos_nfs_spn.setter
    def kerberos_nfs_spn(self, kerberos_nfs_spn):
        """
        Sets the kerberos_nfs_spn of this ProvidersAdsItem.
        Determines if connecting through NFS with Kerberos.

        :param kerberos_nfs_spn: The kerberos_nfs_spn of this ProvidersAdsItem.
        :type: bool
        """
        
        self._kerberos_nfs_spn = kerberos_nfs_spn

    @property
    def ldap_sign_and_seal(self):
        """
        Gets the ldap_sign_and_seal of this ProvidersAdsItem.
        Enables encryption and signing on LDAP requests.

        :return: The ldap_sign_and_seal of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._ldap_sign_and_seal

    @ldap_sign_and_seal.setter
    def ldap_sign_and_seal(self, ldap_sign_and_seal):
        """
        Sets the ldap_sign_and_seal of this ProvidersAdsItem.
        Enables encryption and signing on LDAP requests.

        :param ldap_sign_and_seal: The ldap_sign_and_seal of this ProvidersAdsItem.
        :type: bool
        """
        
        self._ldap_sign_and_seal = ldap_sign_and_seal

    @property
    def login_shell(self):
        """
        Gets the login_shell of this ProvidersAdsItem.
        Specifies the login shell path.

        :return: The login_shell of this ProvidersAdsItem.
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """
        Sets the login_shell of this ProvidersAdsItem.
        Specifies the login shell path.

        :param login_shell: The login_shell of this ProvidersAdsItem.
        :type: str
        """
        
        self._login_shell = login_shell

    @property
    def lookup_domains(self):
        """
        Gets the lookup_domains of this ProvidersAdsItem.
        Limits user and group lookups to the specified domains.

        :return: The lookup_domains of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._lookup_domains

    @lookup_domains.setter
    def lookup_domains(self, lookup_domains):
        """
        Sets the lookup_domains of this ProvidersAdsItem.
        Limits user and group lookups to the specified domains.

        :param lookup_domains: The lookup_domains of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._lookup_domains = lookup_domains

    @property
    def lookup_groups(self):
        """
        Gets the lookup_groups of this ProvidersAdsItem.
        Looks up AD groups in other providers before allocating a group ID.

        :return: The lookup_groups of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._lookup_groups

    @lookup_groups.setter
    def lookup_groups(self, lookup_groups):
        """
        Sets the lookup_groups of this ProvidersAdsItem.
        Looks up AD groups in other providers before allocating a group ID.

        :param lookup_groups: The lookup_groups of this ProvidersAdsItem.
        :type: bool
        """
        
        self._lookup_groups = lookup_groups

    @property
    def lookup_normalize_groups(self):
        """
        Gets the lookup_normalize_groups of this ProvidersAdsItem.
        Normalizes AD group names to lowercase before look up.

        :return: The lookup_normalize_groups of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._lookup_normalize_groups

    @lookup_normalize_groups.setter
    def lookup_normalize_groups(self, lookup_normalize_groups):
        """
        Sets the lookup_normalize_groups of this ProvidersAdsItem.
        Normalizes AD group names to lowercase before look up.

        :param lookup_normalize_groups: The lookup_normalize_groups of this ProvidersAdsItem.
        :type: bool
        """
        
        self._lookup_normalize_groups = lookup_normalize_groups

    @property
    def lookup_normalize_users(self):
        """
        Gets the lookup_normalize_users of this ProvidersAdsItem.
        Normalize AD user names to lowercase before look up.

        :return: The lookup_normalize_users of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._lookup_normalize_users

    @lookup_normalize_users.setter
    def lookup_normalize_users(self, lookup_normalize_users):
        """
        Sets the lookup_normalize_users of this ProvidersAdsItem.
        Normalize AD user names to lowercase before look up.

        :param lookup_normalize_users: The lookup_normalize_users of this ProvidersAdsItem.
        :type: bool
        """
        
        self._lookup_normalize_users = lookup_normalize_users

    @property
    def lookup_users(self):
        """
        Gets the lookup_users of this ProvidersAdsItem.
        Looks up AD users in other providers before allocating a user ID.

        :return: The lookup_users of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._lookup_users

    @lookup_users.setter
    def lookup_users(self, lookup_users):
        """
        Sets the lookup_users of this ProvidersAdsItem.
        Looks up AD users in other providers before allocating a user ID.

        :param lookup_users: The lookup_users of this ProvidersAdsItem.
        :type: bool
        """
        
        self._lookup_users = lookup_users

    @property
    def machine_name(self):
        """
        Gets the machine_name of this ProvidersAdsItem.
        Specifies name to join AD as.

        :return: The machine_name of this ProvidersAdsItem.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """
        Sets the machine_name of this ProvidersAdsItem.
        Specifies name to join AD as.

        :param machine_name: The machine_name of this ProvidersAdsItem.
        :type: str
        """
        
        self._machine_name = machine_name

    @property
    def machine_password_changes(self):
        """
        Gets the machine_password_changes of this ProvidersAdsItem.
        Enables periodic changes of the machine password for security.

        :return: The machine_password_changes of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._machine_password_changes

    @machine_password_changes.setter
    def machine_password_changes(self, machine_password_changes):
        """
        Sets the machine_password_changes of this ProvidersAdsItem.
        Enables periodic changes of the machine password for security.

        :param machine_password_changes: The machine_password_changes of this ProvidersAdsItem.
        :type: bool
        """
        
        self._machine_password_changes = machine_password_changes

    @property
    def machine_password_lifespan(self):
        """
        Gets the machine_password_lifespan of this ProvidersAdsItem.
        Sets maximum age of a password in seconds.

        :return: The machine_password_lifespan of this ProvidersAdsItem.
        :rtype: int
        """
        return self._machine_password_lifespan

    @machine_password_lifespan.setter
    def machine_password_lifespan(self, machine_password_lifespan):
        """
        Sets the machine_password_lifespan of this ProvidersAdsItem.
        Sets maximum age of a password in seconds.

        :param machine_password_lifespan: The machine_password_lifespan of this ProvidersAdsItem.
        :type: int
        """
        
        if not machine_password_lifespan:
            raise ValueError("Invalid value for `machine_password_lifespan`, must not be `None`")
        if machine_password_lifespan > 3.1536E7: 
            raise ValueError("Invalid value for `machine_password_lifespan`, must be a value less than or equal to `3.1536E7`")
        if machine_password_lifespan < 3600.0: 
            raise ValueError("Invalid value for `machine_password_lifespan`, must be a value greater than or equal to `3600.0`")

        self._machine_password_lifespan = machine_password_lifespan

    @property
    def name(self):
        """
        Gets the name of this ProvidersAdsItem.
        Specifies the Active Directory provider name.

        :return: The name of this ProvidersAdsItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProvidersAdsItem.
        Specifies the Active Directory provider name.

        :param name: The name of this ProvidersAdsItem.
        :type: str
        """
        
        self._name = name

    @property
    def node_dc_affinity(self):
        """
        Gets the node_dc_affinity of this ProvidersAdsItem.
        Specifies the domain controller for which the node has affinity.

        :return: The node_dc_affinity of this ProvidersAdsItem.
        :rtype: str
        """
        return self._node_dc_affinity

    @node_dc_affinity.setter
    def node_dc_affinity(self, node_dc_affinity):
        """
        Sets the node_dc_affinity of this ProvidersAdsItem.
        Specifies the domain controller for which the node has affinity.

        :param node_dc_affinity: The node_dc_affinity of this ProvidersAdsItem.
        :type: str
        """
        
        self._node_dc_affinity = node_dc_affinity

    @property
    def node_dc_affinity_timeout(self):
        """
        Gets the node_dc_affinity_timeout of this ProvidersAdsItem.
        Specifies the timeout for the domain controller for which the local node has affinity.

        :return: The node_dc_affinity_timeout of this ProvidersAdsItem.
        :rtype: int
        """
        return self._node_dc_affinity_timeout

    @node_dc_affinity_timeout.setter
    def node_dc_affinity_timeout(self, node_dc_affinity_timeout):
        """
        Sets the node_dc_affinity_timeout of this ProvidersAdsItem.
        Specifies the timeout for the domain controller for which the local node has affinity.

        :param node_dc_affinity_timeout: The node_dc_affinity_timeout of this ProvidersAdsItem.
        :type: int
        """
        
        self._node_dc_affinity_timeout = node_dc_affinity_timeout

    @property
    def nss_enumeration(self):
        """
        Gets the nss_enumeration of this ProvidersAdsItem.
        Enables the Active Directory provider to respond to 'getpwent' and 'getgrent' requests.

        :return: The nss_enumeration of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._nss_enumeration

    @nss_enumeration.setter
    def nss_enumeration(self, nss_enumeration):
        """
        Sets the nss_enumeration of this ProvidersAdsItem.
        Enables the Active Directory provider to respond to 'getpwent' and 'getgrent' requests.

        :param nss_enumeration: The nss_enumeration of this ProvidersAdsItem.
        :type: bool
        """
        
        self._nss_enumeration = nss_enumeration

    @property
    def organizational_unit(self):
        """
        Gets the organizational_unit of this ProvidersAdsItem.
        Specifies the organizational unit.

        :return: The organizational_unit of this ProvidersAdsItem.
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """
        Sets the organizational_unit of this ProvidersAdsItem.
        Specifies the organizational unit.

        :param organizational_unit: The organizational_unit of this ProvidersAdsItem.
        :type: str
        """
        
        self._organizational_unit = organizational_unit

    @property
    def password(self):
        """
        Gets the password of this ProvidersAdsItem.
        Specifies the password used during domain join.

        :return: The password of this ProvidersAdsItem.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ProvidersAdsItem.
        Specifies the password used during domain join.

        :param password: The password of this ProvidersAdsItem.
        :type: str
        """
        
        self._password = password

    @property
    def restrict_findable(self):
        """
        Gets the restrict_findable of this ProvidersAdsItem.
        Check the provider for filtered lists of findable and unfindable users and groups.

        :return: The restrict_findable of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._restrict_findable

    @restrict_findable.setter
    def restrict_findable(self, restrict_findable):
        """
        Sets the restrict_findable of this ProvidersAdsItem.
        Check the provider for filtered lists of findable and unfindable users and groups.

        :param restrict_findable: The restrict_findable of this ProvidersAdsItem.
        :type: bool
        """
        
        self._restrict_findable = restrict_findable

    @property
    def sfu_support(self):
        """
        Gets the sfu_support of this ProvidersAdsItem.
        Specifies whether to support RFC 2307 attributes on ADS domain controllers.

        :return: The sfu_support of this ProvidersAdsItem.
        :rtype: str
        """
        return self._sfu_support

    @sfu_support.setter
    def sfu_support(self, sfu_support):
        """
        Sets the sfu_support of this ProvidersAdsItem.
        Specifies whether to support RFC 2307 attributes on ADS domain controllers.

        :param sfu_support: The sfu_support of this ProvidersAdsItem.
        :type: str
        """
        allowed_values = ["none", "rfc2307"]
        if sfu_support not in allowed_values:
            raise ValueError(
                "Invalid value for `sfu_support`, must be one of {0}"
                .format(allowed_values)
            )

        self._sfu_support = sfu_support

    @property
    def store_sfu_mappings(self):
        """
        Gets the store_sfu_mappings of this ProvidersAdsItem.
        Stores SFU mappings permanently in the ID mapper.

        :return: The store_sfu_mappings of this ProvidersAdsItem.
        :rtype: bool
        """
        return self._store_sfu_mappings

    @store_sfu_mappings.setter
    def store_sfu_mappings(self, store_sfu_mappings):
        """
        Sets the store_sfu_mappings of this ProvidersAdsItem.
        Stores SFU mappings permanently in the ID mapper.

        :param store_sfu_mappings: The store_sfu_mappings of this ProvidersAdsItem.
        :type: bool
        """
        
        self._store_sfu_mappings = store_sfu_mappings

    @property
    def unfindable_groups(self):
        """
        Gets the unfindable_groups of this ProvidersAdsItem.
        Specifies groups that cannot be resolved by the provider.

        :return: The unfindable_groups of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._unfindable_groups

    @unfindable_groups.setter
    def unfindable_groups(self, unfindable_groups):
        """
        Sets the unfindable_groups of this ProvidersAdsItem.
        Specifies groups that cannot be resolved by the provider.

        :param unfindable_groups: The unfindable_groups of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._unfindable_groups = unfindable_groups

    @property
    def unfindable_users(self):
        """
        Gets the unfindable_users of this ProvidersAdsItem.
        Specifies users that cannot be resolved by the provider.

        :return: The unfindable_users of this ProvidersAdsItem.
        :rtype: list[str]
        """
        return self._unfindable_users

    @unfindable_users.setter
    def unfindable_users(self, unfindable_users):
        """
        Sets the unfindable_users of this ProvidersAdsItem.
        Specifies users that cannot be resolved by the provider.

        :param unfindable_users: The unfindable_users of this ProvidersAdsItem.
        :type: list[str]
        """
        
        self._unfindable_users = unfindable_users

    @property
    def user(self):
        """
        Gets the user of this ProvidersAdsItem.
        Specifies the user name that has permission to join a machine to the given domain.

        :return: The user of this ProvidersAdsItem.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ProvidersAdsItem.
        Specifies the user name that has permission to join a machine to the given domain.

        :param user: The user of this ProvidersAdsItem.
        :type: str
        """
        
        self._user = user

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

