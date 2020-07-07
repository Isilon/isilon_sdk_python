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


class SnmpSettingsExtended(object):
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
        'read_only_community': 'str',
        'service': 'bool',
        'snmp_v1_v2c_access': 'bool',
        'snmp_v3_access': 'bool',
        'snmp_v3_auth_protocol': 'str',
        'snmp_v3_password': 'str',
        'snmp_v3_priv_password': 'str',
        'snmp_v3_priv_protocol': 'str',
        'snmp_v3_read_only_user': 'str',
        'snmp_v3_security_level': 'str',
        'system_contact': 'str',
        'system_location': 'str'
    }

    attribute_map = {
        'read_only_community': 'read_only_community',
        'service': 'service',
        'snmp_v1_v2c_access': 'snmp_v1_v2c_access',
        'snmp_v3_access': 'snmp_v3_access',
        'snmp_v3_auth_protocol': 'snmp_v3_auth_protocol',
        'snmp_v3_password': 'snmp_v3_password',
        'snmp_v3_priv_password': 'snmp_v3_priv_password',
        'snmp_v3_priv_protocol': 'snmp_v3_priv_protocol',
        'snmp_v3_read_only_user': 'snmp_v3_read_only_user',
        'snmp_v3_security_level': 'snmp_v3_security_level',
        'system_contact': 'system_contact',
        'system_location': 'system_location'
    }

    def __init__(self, read_only_community=None, service=None, snmp_v1_v2c_access=None, snmp_v3_access=None, snmp_v3_auth_protocol=None, snmp_v3_password=None, snmp_v3_priv_password=None, snmp_v3_priv_protocol=None, snmp_v3_read_only_user=None, snmp_v3_security_level=None, system_contact=None, system_location=None):  # noqa: E501
        """SnmpSettingsExtended - a model defined in Swagger"""  # noqa: E501

        self._read_only_community = None
        self._service = None
        self._snmp_v1_v2c_access = None
        self._snmp_v3_access = None
        self._snmp_v3_auth_protocol = None
        self._snmp_v3_password = None
        self._snmp_v3_priv_password = None
        self._snmp_v3_priv_protocol = None
        self._snmp_v3_read_only_user = None
        self._snmp_v3_security_level = None
        self._system_contact = None
        self._system_location = None
        self.discriminator = None

        if read_only_community is not None:
            self.read_only_community = read_only_community
        if service is not None:
            self.service = service
        if snmp_v1_v2c_access is not None:
            self.snmp_v1_v2c_access = snmp_v1_v2c_access
        if snmp_v3_access is not None:
            self.snmp_v3_access = snmp_v3_access
        if snmp_v3_auth_protocol is not None:
            self.snmp_v3_auth_protocol = snmp_v3_auth_protocol
        if snmp_v3_password is not None:
            self.snmp_v3_password = snmp_v3_password
        if snmp_v3_priv_password is not None:
            self.snmp_v3_priv_password = snmp_v3_priv_password
        if snmp_v3_priv_protocol is not None:
            self.snmp_v3_priv_protocol = snmp_v3_priv_protocol
        if snmp_v3_read_only_user is not None:
            self.snmp_v3_read_only_user = snmp_v3_read_only_user
        if snmp_v3_security_level is not None:
            self.snmp_v3_security_level = snmp_v3_security_level
        if system_contact is not None:
            self.system_contact = system_contact
        if system_location is not None:
            self.system_location = system_location

    @property
    def read_only_community(self):
        """Gets the read_only_community of this SnmpSettingsExtended.  # noqa: E501

        The read-only community name.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The read_only_community of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._read_only_community

    @read_only_community.setter
    def read_only_community(self, read_only_community):
        """Sets the read_only_community of this SnmpSettingsExtended.

        The read-only community name.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param read_only_community: The read_only_community of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if read_only_community is not None and len(read_only_community) < 1:
            raise ValueError("Invalid value for `read_only_community`, length must be greater than or equal to `1`")  # noqa: E501

        self._read_only_community = read_only_community

    @property
    def service(self):
        """Gets the service of this SnmpSettingsExtended.  # noqa: E501

        Whether the SNMP service is enabled.  # noqa: E501

        :return: The service of this SnmpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SnmpSettingsExtended.

        Whether the SNMP service is enabled.  # noqa: E501

        :param service: The service of this SnmpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._service = service

    @property
    def snmp_v1_v2c_access(self):
        """Gets the snmp_v1_v2c_access of this SnmpSettingsExtended.  # noqa: E501

        Whether SNMP v1 and v2c protocols are enabled.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v1_v2c_access of this SnmpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._snmp_v1_v2c_access

    @snmp_v1_v2c_access.setter
    def snmp_v1_v2c_access(self, snmp_v1_v2c_access):
        """Sets the snmp_v1_v2c_access of this SnmpSettingsExtended.

        Whether SNMP v1 and v2c protocols are enabled.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v1_v2c_access: The snmp_v1_v2c_access of this SnmpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._snmp_v1_v2c_access = snmp_v1_v2c_access

    @property
    def snmp_v3_access(self):
        """Gets the snmp_v3_access of this SnmpSettingsExtended.  # noqa: E501

        Whether SNMP v3 is enabled.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_access of this SnmpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._snmp_v3_access

    @snmp_v3_access.setter
    def snmp_v3_access(self, snmp_v3_access):
        """Sets the snmp_v3_access of this SnmpSettingsExtended.

        Whether SNMP v3 is enabled.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_access: The snmp_v3_access of this SnmpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._snmp_v3_access = snmp_v3_access

    @property
    def snmp_v3_auth_protocol(self):
        """Gets the snmp_v3_auth_protocol of this SnmpSettingsExtended.  # noqa: E501

        SNMPv3 authentication protocol. May only be SHA or MD5.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_auth_protocol of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_auth_protocol

    @snmp_v3_auth_protocol.setter
    def snmp_v3_auth_protocol(self, snmp_v3_auth_protocol):
        """Sets the snmp_v3_auth_protocol of this SnmpSettingsExtended.

        SNMPv3 authentication protocol. May only be SHA or MD5.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_auth_protocol: The snmp_v3_auth_protocol of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["SHA", "MD5"]  # noqa: E501
        if snmp_v3_auth_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_v3_auth_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(snmp_v3_auth_protocol, allowed_values)
            )

        self._snmp_v3_auth_protocol = snmp_v3_auth_protocol

    @property
    def snmp_v3_password(self):
        """Gets the snmp_v3_password of this SnmpSettingsExtended.  # noqa: E501

        This field allows a client to change the SNMP v3 authentication password. There is always a password set.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_password of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_password

    @snmp_v3_password.setter
    def snmp_v3_password(self, snmp_v3_password):
        """Sets the snmp_v3_password of this SnmpSettingsExtended.

        This field allows a client to change the SNMP v3 authentication password. There is always a password set.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_password: The snmp_v3_password of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if snmp_v3_password is not None and len(snmp_v3_password) > 39:
            raise ValueError("Invalid value for `snmp_v3_password`, length must be less than or equal to `39`")  # noqa: E501
        if snmp_v3_password is not None and len(snmp_v3_password) < 8:
            raise ValueError("Invalid value for `snmp_v3_password`, length must be greater than or equal to `8`")  # noqa: E501

        self._snmp_v3_password = snmp_v3_password

    @property
    def snmp_v3_priv_password(self):
        """Gets the snmp_v3_priv_password of this SnmpSettingsExtended.  # noqa: E501

        This field allows a client to change the SNMP v3 privacy password. There is always a password set.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_priv_password of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_priv_password

    @snmp_v3_priv_password.setter
    def snmp_v3_priv_password(self, snmp_v3_priv_password):
        """Sets the snmp_v3_priv_password of this SnmpSettingsExtended.

        This field allows a client to change the SNMP v3 privacy password. There is always a password set.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_priv_password: The snmp_v3_priv_password of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if snmp_v3_priv_password is not None and len(snmp_v3_priv_password) > 39:
            raise ValueError("Invalid value for `snmp_v3_priv_password`, length must be less than or equal to `39`")  # noqa: E501
        if snmp_v3_priv_password is not None and len(snmp_v3_priv_password) < 8:
            raise ValueError("Invalid value for `snmp_v3_priv_password`, length must be greater than or equal to `8`")  # noqa: E501

        self._snmp_v3_priv_password = snmp_v3_priv_password

    @property
    def snmp_v3_priv_protocol(self):
        """Gets the snmp_v3_priv_protocol of this SnmpSettingsExtended.  # noqa: E501

        SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_priv_protocol of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_priv_protocol

    @snmp_v3_priv_protocol.setter
    def snmp_v3_priv_protocol(self, snmp_v3_priv_protocol):
        """Sets the snmp_v3_priv_protocol of this SnmpSettingsExtended.

        SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_priv_protocol: The snmp_v3_priv_protocol of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["AES", "DES"]  # noqa: E501
        if snmp_v3_priv_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_v3_priv_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(snmp_v3_priv_protocol, allowed_values)
            )

        self._snmp_v3_priv_protocol = snmp_v3_priv_protocol

    @property
    def snmp_v3_read_only_user(self):
        """Gets the snmp_v3_read_only_user of this SnmpSettingsExtended.  # noqa: E501

        The read-only user for SNMP v3 read requests.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_read_only_user of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_read_only_user

    @snmp_v3_read_only_user.setter
    def snmp_v3_read_only_user(self, snmp_v3_read_only_user):
        """Sets the snmp_v3_read_only_user of this SnmpSettingsExtended.

        The read-only user for SNMP v3 read requests.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_read_only_user: The snmp_v3_read_only_user of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if snmp_v3_read_only_user is not None and len(snmp_v3_read_only_user) < 1:
            raise ValueError("Invalid value for `snmp_v3_read_only_user`, length must be greater than or equal to `1`")  # noqa: E501

        self._snmp_v3_read_only_user = snmp_v3_read_only_user

    @property
    def snmp_v3_security_level(self):
        """Gets the snmp_v3_security_level of this SnmpSettingsExtended.  # noqa: E501

        SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The snmp_v3_security_level of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._snmp_v3_security_level

    @snmp_v3_security_level.setter
    def snmp_v3_security_level(self, snmp_v3_security_level):
        """Sets the snmp_v3_security_level of this SnmpSettingsExtended.

        SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value.  # noqa: E501

        :param snmp_v3_security_level: The snmp_v3_security_level of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["noAuthNoPriv", "authNoPriv", "authPriv"]  # noqa: E501
        if snmp_v3_security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_v3_security_level` ({0}), must be one of {1}"  # noqa: E501
                .format(snmp_v3_security_level, allowed_values)
            )

        self._snmp_v3_security_level = snmp_v3_security_level

    @property
    def system_contact(self):
        """Gets the system_contact of this SnmpSettingsExtended.  # noqa: E501

        Contact information for the system owner.  This must be a valid email address.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The system_contact of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._system_contact

    @system_contact.setter
    def system_contact(self, system_contact):
        """Sets the system_contact of this SnmpSettingsExtended.

        Contact information for the system owner.  This must be a valid email address.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param system_contact: The system_contact of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if system_contact is not None and len(system_contact) < 1:
            raise ValueError("Invalid value for `system_contact`, length must be greater than or equal to `1`")  # noqa: E501
        if system_contact is not None and not re.search('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$', system_contact):  # noqa: E501
            raise ValueError("Invalid value for `system_contact`, must be a follow pattern or equal to `/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$/`")  # noqa: E501

        self._system_contact = system_contact

    @property
    def system_location(self):
        """Gets the system_location of this SnmpSettingsExtended.  # noqa: E501

        A location name for the SNMP system.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :return: The system_location of this SnmpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._system_location

    @system_location.setter
    def system_location(self, system_location):
        """Sets the system_location of this SnmpSettingsExtended.

        A location name for the SNMP system.  @DEFAULT reverts this field to its default value.  # noqa: E501

        :param system_location: The system_location of this SnmpSettingsExtended.  # noqa: E501
        :type: str
        """
        if system_location is not None and len(system_location) < 1:
            raise ValueError("Invalid value for `system_location`, length must be greater than or equal to `1`")  # noqa: E501

        self._system_location = system_location

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
        if not isinstance(other, SnmpSettingsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
