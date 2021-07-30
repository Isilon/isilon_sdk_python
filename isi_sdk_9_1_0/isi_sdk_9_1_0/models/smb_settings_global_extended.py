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


class SmbSettingsGlobalExtended(object):
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
        'access_based_share_enum': 'bool',
        'audit_fileshare': 'str',
        'audit_logon': 'str',
        'dot_snap_accessible_child': 'bool',
        'dot_snap_accessible_root': 'bool',
        'dot_snap_visible_child': 'bool',
        'dot_snap_visible_root': 'bool',
        'enable_security_signatures': 'bool',
        'guest_user': 'str',
        'ignore_eas': 'bool',
        'onefs_cpu_multiplier': 'int',
        'onefs_num_workers': 'int',
        'reject_unencrypted_access': 'bool',
        'require_security_signatures': 'bool',
        'server_side_copy': 'bool',
        'server_string': 'str',
        'service': 'bool',
        'srv_cpu_multiplier': 'int',
        'srv_num_workers': 'int',
        'support_multichannel': 'bool',
        'support_netbios': 'bool',
        'support_smb2': 'bool',
        'support_smb3_encryption': 'bool'
    }

    attribute_map = {
        'access_based_share_enum': 'access_based_share_enum',
        'audit_fileshare': 'audit_fileshare',
        'audit_logon': 'audit_logon',
        'dot_snap_accessible_child': 'dot_snap_accessible_child',
        'dot_snap_accessible_root': 'dot_snap_accessible_root',
        'dot_snap_visible_child': 'dot_snap_visible_child',
        'dot_snap_visible_root': 'dot_snap_visible_root',
        'enable_security_signatures': 'enable_security_signatures',
        'guest_user': 'guest_user',
        'ignore_eas': 'ignore_eas',
        'onefs_cpu_multiplier': 'onefs_cpu_multiplier',
        'onefs_num_workers': 'onefs_num_workers',
        'reject_unencrypted_access': 'reject_unencrypted_access',
        'require_security_signatures': 'require_security_signatures',
        'server_side_copy': 'server_side_copy',
        'server_string': 'server_string',
        'service': 'service',
        'srv_cpu_multiplier': 'srv_cpu_multiplier',
        'srv_num_workers': 'srv_num_workers',
        'support_multichannel': 'support_multichannel',
        'support_netbios': 'support_netbios',
        'support_smb2': 'support_smb2',
        'support_smb3_encryption': 'support_smb3_encryption'
    }

    def __init__(self, access_based_share_enum=None, audit_fileshare=None, audit_logon=None, dot_snap_accessible_child=None, dot_snap_accessible_root=None, dot_snap_visible_child=None, dot_snap_visible_root=None, enable_security_signatures=None, guest_user=None, ignore_eas=None, onefs_cpu_multiplier=None, onefs_num_workers=None, reject_unencrypted_access=None, require_security_signatures=None, server_side_copy=None, server_string=None, service=None, srv_cpu_multiplier=None, srv_num_workers=None, support_multichannel=None, support_netbios=None, support_smb2=None, support_smb3_encryption=None):  # noqa: E501
        """SmbSettingsGlobalExtended - a model defined in Swagger"""  # noqa: E501

        self._access_based_share_enum = None
        self._audit_fileshare = None
        self._audit_logon = None
        self._dot_snap_accessible_child = None
        self._dot_snap_accessible_root = None
        self._dot_snap_visible_child = None
        self._dot_snap_visible_root = None
        self._enable_security_signatures = None
        self._guest_user = None
        self._ignore_eas = None
        self._onefs_cpu_multiplier = None
        self._onefs_num_workers = None
        self._reject_unencrypted_access = None
        self._require_security_signatures = None
        self._server_side_copy = None
        self._server_string = None
        self._service = None
        self._srv_cpu_multiplier = None
        self._srv_num_workers = None
        self._support_multichannel = None
        self._support_netbios = None
        self._support_smb2 = None
        self._support_smb3_encryption = None
        self.discriminator = None

        if access_based_share_enum is not None:
            self.access_based_share_enum = access_based_share_enum
        if audit_fileshare is not None:
            self.audit_fileshare = audit_fileshare
        if audit_logon is not None:
            self.audit_logon = audit_logon
        if dot_snap_accessible_child is not None:
            self.dot_snap_accessible_child = dot_snap_accessible_child
        if dot_snap_accessible_root is not None:
            self.dot_snap_accessible_root = dot_snap_accessible_root
        if dot_snap_visible_child is not None:
            self.dot_snap_visible_child = dot_snap_visible_child
        if dot_snap_visible_root is not None:
            self.dot_snap_visible_root = dot_snap_visible_root
        if enable_security_signatures is not None:
            self.enable_security_signatures = enable_security_signatures
        if guest_user is not None:
            self.guest_user = guest_user
        if ignore_eas is not None:
            self.ignore_eas = ignore_eas
        if onefs_cpu_multiplier is not None:
            self.onefs_cpu_multiplier = onefs_cpu_multiplier
        if onefs_num_workers is not None:
            self.onefs_num_workers = onefs_num_workers
        if reject_unencrypted_access is not None:
            self.reject_unencrypted_access = reject_unencrypted_access
        if require_security_signatures is not None:
            self.require_security_signatures = require_security_signatures
        if server_side_copy is not None:
            self.server_side_copy = server_side_copy
        if server_string is not None:
            self.server_string = server_string
        if service is not None:
            self.service = service
        if srv_cpu_multiplier is not None:
            self.srv_cpu_multiplier = srv_cpu_multiplier
        if srv_num_workers is not None:
            self.srv_num_workers = srv_num_workers
        if support_multichannel is not None:
            self.support_multichannel = support_multichannel
        if support_netbios is not None:
            self.support_netbios = support_netbios
        if support_smb2 is not None:
            self.support_smb2 = support_smb2
        if support_smb3_encryption is not None:
            self.support_smb3_encryption = support_smb3_encryption

    @property
    def access_based_share_enum(self):
        """Gets the access_based_share_enum of this SmbSettingsGlobalExtended.  # noqa: E501

        Only enumerate files and folders the requesting user has access to.  # noqa: E501

        :return: The access_based_share_enum of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._access_based_share_enum

    @access_based_share_enum.setter
    def access_based_share_enum(self, access_based_share_enum):
        """Sets the access_based_share_enum of this SmbSettingsGlobalExtended.

        Only enumerate files and folders the requesting user has access to.  # noqa: E501

        :param access_based_share_enum: The access_based_share_enum of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._access_based_share_enum = access_based_share_enum

    @property
    def audit_fileshare(self):
        """Gets the audit_fileshare of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify level of file share audit events to log.  # noqa: E501

        :return: The audit_fileshare of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: str
        """
        return self._audit_fileshare

    @audit_fileshare.setter
    def audit_fileshare(self, audit_fileshare):
        """Sets the audit_fileshare of this SmbSettingsGlobalExtended.

        Specify level of file share audit events to log.  # noqa: E501

        :param audit_fileshare: The audit_fileshare of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: str
        """

        self._audit_fileshare = audit_fileshare

    @property
    def audit_logon(self):
        """Gets the audit_logon of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify the level of logon audit events to log.  # noqa: E501

        :return: The audit_logon of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: str
        """
        return self._audit_logon

    @audit_logon.setter
    def audit_logon(self, audit_logon):
        """Sets the audit_logon of this SmbSettingsGlobalExtended.

        Specify the level of logon audit events to log.  # noqa: E501

        :param audit_logon: The audit_logon of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: str
        """

        self._audit_logon = audit_logon

    @property
    def dot_snap_accessible_child(self):
        """Gets the dot_snap_accessible_child of this SmbSettingsGlobalExtended.  # noqa: E501

        Allow access to .snapshot directories in share subdirectories.  # noqa: E501

        :return: The dot_snap_accessible_child of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dot_snap_accessible_child

    @dot_snap_accessible_child.setter
    def dot_snap_accessible_child(self, dot_snap_accessible_child):
        """Sets the dot_snap_accessible_child of this SmbSettingsGlobalExtended.

        Allow access to .snapshot directories in share subdirectories.  # noqa: E501

        :param dot_snap_accessible_child: The dot_snap_accessible_child of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._dot_snap_accessible_child = dot_snap_accessible_child

    @property
    def dot_snap_accessible_root(self):
        """Gets the dot_snap_accessible_root of this SmbSettingsGlobalExtended.  # noqa: E501

        Allow access to the .snapshot directory in the root of the share.  # noqa: E501

        :return: The dot_snap_accessible_root of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dot_snap_accessible_root

    @dot_snap_accessible_root.setter
    def dot_snap_accessible_root(self, dot_snap_accessible_root):
        """Sets the dot_snap_accessible_root of this SmbSettingsGlobalExtended.

        Allow access to the .snapshot directory in the root of the share.  # noqa: E501

        :param dot_snap_accessible_root: The dot_snap_accessible_root of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._dot_snap_accessible_root = dot_snap_accessible_root

    @property
    def dot_snap_visible_child(self):
        """Gets the dot_snap_visible_child of this SmbSettingsGlobalExtended.  # noqa: E501

        Show .snapshot directories in share subdirectories.  # noqa: E501

        :return: The dot_snap_visible_child of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dot_snap_visible_child

    @dot_snap_visible_child.setter
    def dot_snap_visible_child(self, dot_snap_visible_child):
        """Sets the dot_snap_visible_child of this SmbSettingsGlobalExtended.

        Show .snapshot directories in share subdirectories.  # noqa: E501

        :param dot_snap_visible_child: The dot_snap_visible_child of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._dot_snap_visible_child = dot_snap_visible_child

    @property
    def dot_snap_visible_root(self):
        """Gets the dot_snap_visible_root of this SmbSettingsGlobalExtended.  # noqa: E501

        Show the .snapshot directory in the root of a share.  # noqa: E501

        :return: The dot_snap_visible_root of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dot_snap_visible_root

    @dot_snap_visible_root.setter
    def dot_snap_visible_root(self, dot_snap_visible_root):
        """Sets the dot_snap_visible_root of this SmbSettingsGlobalExtended.

        Show the .snapshot directory in the root of a share.  # noqa: E501

        :param dot_snap_visible_root: The dot_snap_visible_root of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._dot_snap_visible_root = dot_snap_visible_root

    @property
    def enable_security_signatures(self):
        """Gets the enable_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501

        Indicates whether the server supports signed SMB packets.  # noqa: E501

        :return: The enable_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enable_security_signatures

    @enable_security_signatures.setter
    def enable_security_signatures(self, enable_security_signatures):
        """Sets the enable_security_signatures of this SmbSettingsGlobalExtended.

        Indicates whether the server supports signed SMB packets.  # noqa: E501

        :param enable_security_signatures: The enable_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._enable_security_signatures = enable_security_signatures

    @property
    def guest_user(self):
        """Gets the guest_user of this SmbSettingsGlobalExtended.  # noqa: E501

        Specifies the fully-qualified user to use for guest access.  # noqa: E501

        :return: The guest_user of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: str
        """
        return self._guest_user

    @guest_user.setter
    def guest_user(self, guest_user):
        """Sets the guest_user of this SmbSettingsGlobalExtended.

        Specifies the fully-qualified user to use for guest access.  # noqa: E501

        :param guest_user: The guest_user of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: str
        """
        if guest_user is not None and len(guest_user) > 511:
            raise ValueError("Invalid value for `guest_user`, length must be less than or equal to `511`")  # noqa: E501
        if guest_user is not None and len(guest_user) < 1:
            raise ValueError("Invalid value for `guest_user`, length must be greater than or equal to `1`")  # noqa: E501

        self._guest_user = guest_user

    @property
    def ignore_eas(self):
        """Gets the ignore_eas of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify whether to ignore EAs on files.  # noqa: E501

        :return: The ignore_eas of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_eas

    @ignore_eas.setter
    def ignore_eas(self, ignore_eas):
        """Sets the ignore_eas of this SmbSettingsGlobalExtended.

        Specify whether to ignore EAs on files.  # noqa: E501

        :param ignore_eas: The ignore_eas of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._ignore_eas = ignore_eas

    @property
    def onefs_cpu_multiplier(self):
        """Gets the onefs_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify the number of OneFS driver worker threads per CPU.  # noqa: E501

        :return: The onefs_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: int
        """
        return self._onefs_cpu_multiplier

    @onefs_cpu_multiplier.setter
    def onefs_cpu_multiplier(self, onefs_cpu_multiplier):
        """Sets the onefs_cpu_multiplier of this SmbSettingsGlobalExtended.

        Specify the number of OneFS driver worker threads per CPU.  # noqa: E501

        :param onefs_cpu_multiplier: The onefs_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: int
        """
        if onefs_cpu_multiplier is not None and onefs_cpu_multiplier > 4:  # noqa: E501
            raise ValueError("Invalid value for `onefs_cpu_multiplier`, must be a value less than or equal to `4`")  # noqa: E501
        if onefs_cpu_multiplier is not None and onefs_cpu_multiplier < 1:  # noqa: E501
            raise ValueError("Invalid value for `onefs_cpu_multiplier`, must be a value greater than or equal to `1`")  # noqa: E501

        self._onefs_cpu_multiplier = onefs_cpu_multiplier

    @property
    def onefs_num_workers(self):
        """Gets the onefs_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501

        Set the maximum number of OneFS driver worker threads.  # noqa: E501

        :return: The onefs_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: int
        """
        return self._onefs_num_workers

    @onefs_num_workers.setter
    def onefs_num_workers(self, onefs_num_workers):
        """Sets the onefs_num_workers of this SmbSettingsGlobalExtended.

        Set the maximum number of OneFS driver worker threads.  # noqa: E501

        :param onefs_num_workers: The onefs_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: int
        """
        if onefs_num_workers is not None and onefs_num_workers > 1024:  # noqa: E501
            raise ValueError("Invalid value for `onefs_num_workers`, must be a value less than or equal to `1024`")  # noqa: E501
        if onefs_num_workers is not None and onefs_num_workers < 0:  # noqa: E501
            raise ValueError("Invalid value for `onefs_num_workers`, must be a value greater than or equal to `0`")  # noqa: E501

        self._onefs_num_workers = onefs_num_workers

    @property
    def reject_unencrypted_access(self):
        """Gets the reject_unencrypted_access of this SmbSettingsGlobalExtended.  # noqa: E501

        If SMB3 encryption is enabled, reject unencrypted access from clients.  # noqa: E501

        :return: The reject_unencrypted_access of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._reject_unencrypted_access

    @reject_unencrypted_access.setter
    def reject_unencrypted_access(self, reject_unencrypted_access):
        """Sets the reject_unencrypted_access of this SmbSettingsGlobalExtended.

        If SMB3 encryption is enabled, reject unencrypted access from clients.  # noqa: E501

        :param reject_unencrypted_access: The reject_unencrypted_access of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._reject_unencrypted_access = reject_unencrypted_access

    @property
    def require_security_signatures(self):
        """Gets the require_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501

        Indicates whether the server requires signed SMB packets.  # noqa: E501

        :return: The require_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._require_security_signatures

    @require_security_signatures.setter
    def require_security_signatures(self, require_security_signatures):
        """Sets the require_security_signatures of this SmbSettingsGlobalExtended.

        Indicates whether the server requires signed SMB packets.  # noqa: E501

        :param require_security_signatures: The require_security_signatures of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._require_security_signatures = require_security_signatures

    @property
    def server_side_copy(self):
        """Gets the server_side_copy of this SmbSettingsGlobalExtended.  # noqa: E501

        Enable Server Side Copy.  # noqa: E501

        :return: The server_side_copy of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._server_side_copy

    @server_side_copy.setter
    def server_side_copy(self, server_side_copy):
        """Sets the server_side_copy of this SmbSettingsGlobalExtended.

        Enable Server Side Copy.  # noqa: E501

        :param server_side_copy: The server_side_copy of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._server_side_copy = server_side_copy

    @property
    def server_string(self):
        """Gets the server_string of this SmbSettingsGlobalExtended.  # noqa: E501

        Provides a description of the server.  # noqa: E501

        :return: The server_string of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: str
        """
        return self._server_string

    @server_string.setter
    def server_string(self, server_string):
        """Sets the server_string of this SmbSettingsGlobalExtended.

        Provides a description of the server.  # noqa: E501

        :param server_string: The server_string of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: str
        """
        if server_string is not None and len(server_string) > 511:
            raise ValueError("Invalid value for `server_string`, length must be less than or equal to `511`")  # noqa: E501
        if server_string is not None and len(server_string) < 1:
            raise ValueError("Invalid value for `server_string`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_string = server_string

    @property
    def service(self):
        """Gets the service of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify whether service is enabled.  # noqa: E501

        :return: The service of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SmbSettingsGlobalExtended.

        Specify whether service is enabled.  # noqa: E501

        :param service: The service of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._service = service

    @property
    def srv_cpu_multiplier(self):
        """Gets the srv_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501

        Specify the number of SRV service worker threads per CPU.  # noqa: E501

        :return: The srv_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: int
        """
        return self._srv_cpu_multiplier

    @srv_cpu_multiplier.setter
    def srv_cpu_multiplier(self, srv_cpu_multiplier):
        """Sets the srv_cpu_multiplier of this SmbSettingsGlobalExtended.

        Specify the number of SRV service worker threads per CPU.  # noqa: E501

        :param srv_cpu_multiplier: The srv_cpu_multiplier of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: int
        """
        if srv_cpu_multiplier is not None and srv_cpu_multiplier > 8:  # noqa: E501
            raise ValueError("Invalid value for `srv_cpu_multiplier`, must be a value less than or equal to `8`")  # noqa: E501
        if srv_cpu_multiplier is not None and srv_cpu_multiplier < 1:  # noqa: E501
            raise ValueError("Invalid value for `srv_cpu_multiplier`, must be a value greater than or equal to `1`")  # noqa: E501

        self._srv_cpu_multiplier = srv_cpu_multiplier

    @property
    def srv_num_workers(self):
        """Gets the srv_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501

        Set the maximum number of SRV service worker threads.  # noqa: E501

        :return: The srv_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: int
        """
        return self._srv_num_workers

    @srv_num_workers.setter
    def srv_num_workers(self, srv_num_workers):
        """Sets the srv_num_workers of this SmbSettingsGlobalExtended.

        Set the maximum number of SRV service worker threads.  # noqa: E501

        :param srv_num_workers: The srv_num_workers of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: int
        """
        if srv_num_workers is not None and srv_num_workers > 1024:  # noqa: E501
            raise ValueError("Invalid value for `srv_num_workers`, must be a value less than or equal to `1024`")  # noqa: E501
        if srv_num_workers is not None and srv_num_workers < 0:  # noqa: E501
            raise ValueError("Invalid value for `srv_num_workers`, must be a value greater than or equal to `0`")  # noqa: E501

        self._srv_num_workers = srv_num_workers

    @property
    def support_multichannel(self):
        """Gets the support_multichannel of this SmbSettingsGlobalExtended.  # noqa: E501

        Support multichannel.  # noqa: E501

        :return: The support_multichannel of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._support_multichannel

    @support_multichannel.setter
    def support_multichannel(self, support_multichannel):
        """Sets the support_multichannel of this SmbSettingsGlobalExtended.

        Support multichannel.  # noqa: E501

        :param support_multichannel: The support_multichannel of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._support_multichannel = support_multichannel

    @property
    def support_netbios(self):
        """Gets the support_netbios of this SmbSettingsGlobalExtended.  # noqa: E501

        Support NetBIOS.  # noqa: E501

        :return: The support_netbios of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._support_netbios

    @support_netbios.setter
    def support_netbios(self, support_netbios):
        """Sets the support_netbios of this SmbSettingsGlobalExtended.

        Support NetBIOS.  # noqa: E501

        :param support_netbios: The support_netbios of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._support_netbios = support_netbios

    @property
    def support_smb2(self):
        """Gets the support_smb2 of this SmbSettingsGlobalExtended.  # noqa: E501

        Support the SMB2 protocol on the server.  # noqa: E501

        :return: The support_smb2 of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._support_smb2

    @support_smb2.setter
    def support_smb2(self, support_smb2):
        """Sets the support_smb2 of this SmbSettingsGlobalExtended.

        Support the SMB2 protocol on the server.  # noqa: E501

        :param support_smb2: The support_smb2 of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._support_smb2 = support_smb2

    @property
    def support_smb3_encryption(self):
        """Gets the support_smb3_encryption of this SmbSettingsGlobalExtended.  # noqa: E501

        Support the SMB3 encryption on the server.  # noqa: E501

        :return: The support_smb3_encryption of this SmbSettingsGlobalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._support_smb3_encryption

    @support_smb3_encryption.setter
    def support_smb3_encryption(self, support_smb3_encryption):
        """Sets the support_smb3_encryption of this SmbSettingsGlobalExtended.

        Support the SMB3 encryption on the server.  # noqa: E501

        :param support_smb3_encryption: The support_smb3_encryption of this SmbSettingsGlobalExtended.  # noqa: E501
        :type: bool
        """

        self._support_smb3_encryption = support_smb3_encryption

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
        if not isinstance(other, SmbSettingsGlobalExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
