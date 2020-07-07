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


class ProvidersDuoExtended(object):
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
        'autopush': 'bool',
        'enabled': 'bool',
        'failmode': 'str',
        'fallback_local_ip': 'bool',
        'groups': 'str',
        'host': 'str',
        'http_proxy': 'str',
        'https_timeout': 'int',
        'ikey': 'str',
        'prompts': 'int',
        'pushinfo': 'bool',
        'skey': 'str'
    }

    attribute_map = {
        'autopush': 'autopush',
        'enabled': 'enabled',
        'failmode': 'failmode',
        'fallback_local_ip': 'fallback_local_ip',
        'groups': 'groups',
        'host': 'host',
        'http_proxy': 'http_proxy',
        'https_timeout': 'https_timeout',
        'ikey': 'ikey',
        'prompts': 'prompts',
        'pushinfo': 'pushinfo',
        'skey': 'skey'
    }

    def __init__(self, autopush=None, enabled=None, failmode=None, fallback_local_ip=None, groups=None, host=None, http_proxy=None, https_timeout=None, ikey=None, prompts=None, pushinfo=None, skey=None):  # noqa: E501
        """ProvidersDuoExtended - a model defined in Swagger"""  # noqa: E501

        self._autopush = None
        self._enabled = None
        self._failmode = None
        self._fallback_local_ip = None
        self._groups = None
        self._host = None
        self._http_proxy = None
        self._https_timeout = None
        self._ikey = None
        self._prompts = None
        self._pushinfo = None
        self._skey = None
        self.discriminator = None

        if autopush is not None:
            self.autopush = autopush
        if enabled is not None:
            self.enabled = enabled
        if failmode is not None:
            self.failmode = failmode
        if fallback_local_ip is not None:
            self.fallback_local_ip = fallback_local_ip
        if groups is not None:
            self.groups = groups
        if host is not None:
            self.host = host
        if http_proxy is not None:
            self.http_proxy = http_proxy
        if https_timeout is not None:
            self.https_timeout = https_timeout
        if ikey is not None:
            self.ikey = ikey
        if prompts is not None:
            self.prompts = prompts
        if pushinfo is not None:
            self.pushinfo = pushinfo
        if skey is not None:
            self.skey = skey

    @property
    def autopush(self):
        """Gets the autopush of this ProvidersDuoExtended.  # noqa: E501

        Specifies if Duo automatically sends a push login request to the users phone.  # noqa: E501

        :return: The autopush of this ProvidersDuoExtended.  # noqa: E501
        :rtype: bool
        """
        return self._autopush

    @autopush.setter
    def autopush(self, autopush):
        """Sets the autopush of this ProvidersDuoExtended.

        Specifies if Duo automatically sends a push login request to the users phone.  # noqa: E501

        :param autopush: The autopush of this ProvidersDuoExtended.  # noqa: E501
        :type: bool
        """

        self._autopush = autopush

    @property
    def enabled(self):
        """Gets the enabled of this ProvidersDuoExtended.  # noqa: E501

        Specifies if the Duo provider is enabled.  # noqa: E501

        :return: The enabled of this ProvidersDuoExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProvidersDuoExtended.

        Specifies if the Duo provider is enabled.  # noqa: E501

        :param enabled: The enabled of this ProvidersDuoExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def failmode(self):
        """Gets the failmode of this ProvidersDuoExtended.  # noqa: E501

        Specifies if Duo will fail \"safe\" (allow access) or \"secure\" (deny access) on configuration or service errors.  # noqa: E501

        :return: The failmode of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._failmode

    @failmode.setter
    def failmode(self, failmode):
        """Sets the failmode of this ProvidersDuoExtended.

        Specifies if Duo will fail \"safe\" (allow access) or \"secure\" (deny access) on configuration or service errors.  # noqa: E501

        :param failmode: The failmode of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["safe", "secure"]  # noqa: E501
        if failmode not in allowed_values:
            raise ValueError(
                "Invalid value for `failmode` ({0}), must be one of {1}"  # noqa: E501
                .format(failmode, allowed_values)
            )

        self._failmode = failmode

    @property
    def fallback_local_ip(self):
        """Gets the fallback_local_ip of this ProvidersDuoExtended.  # noqa: E501

        Specifies if Duo will report the server IP if the client IP cannot be detected.  # noqa: E501

        :return: The fallback_local_ip of this ProvidersDuoExtended.  # noqa: E501
        :rtype: bool
        """
        return self._fallback_local_ip

    @fallback_local_ip.setter
    def fallback_local_ip(self, fallback_local_ip):
        """Sets the fallback_local_ip of this ProvidersDuoExtended.

        Specifies if Duo will report the server IP if the client IP cannot be detected.  # noqa: E501

        :param fallback_local_ip: The fallback_local_ip of this ProvidersDuoExtended.  # noqa: E501
        :type: bool
        """

        self._fallback_local_ip = fallback_local_ip

    @property
    def groups(self):
        """Gets the groups of this ProvidersDuoExtended.  # noqa: E501

        Specifies a list of groups Duo is required for (default is all groups).  # noqa: E501

        :return: The groups of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ProvidersDuoExtended.

        Specifies a list of groups Duo is required for (default is all groups).  # noqa: E501

        :param groups: The groups of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        if groups is not None and len(groups) > 1024:
            raise ValueError("Invalid value for `groups`, length must be less than or equal to `1024`")  # noqa: E501
        if groups is not None and len(groups) < 0:
            raise ValueError("Invalid value for `groups`, length must be greater than or equal to `0`")  # noqa: E501

        self._groups = groups

    @property
    def host(self):
        """Gets the host of this ProvidersDuoExtended.  # noqa: E501

        Specifies the API hostname.  # noqa: E501

        :return: The host of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ProvidersDuoExtended.

        Specifies the API hostname.  # noqa: E501

        :param host: The host of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        if host is not None and len(host) > 256:
            raise ValueError("Invalid value for `host`, length must be less than or equal to `256`")  # noqa: E501
        if host is not None and len(host) < 0:
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `0`")  # noqa: E501

        self._host = host

    @property
    def http_proxy(self):
        """Gets the http_proxy of this ProvidersDuoExtended.  # noqa: E501

        Specifies the HTTP proxy to use.  # noqa: E501

        :return: The http_proxy of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """Sets the http_proxy of this ProvidersDuoExtended.

        Specifies the HTTP proxy to use.  # noqa: E501

        :param http_proxy: The http_proxy of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        if http_proxy is not None and len(http_proxy) > 1024:
            raise ValueError("Invalid value for `http_proxy`, length must be less than or equal to `1024`")  # noqa: E501
        if http_proxy is not None and len(http_proxy) < 0:
            raise ValueError("Invalid value for `http_proxy`, length must be greater than or equal to `0`")  # noqa: E501

        self._http_proxy = http_proxy

    @property
    def https_timeout(self):
        """Gets the https_timeout of this ProvidersDuoExtended.  # noqa: E501

        Specifies the number of seconds to wait for HTTPS responses from Duo Security.  # noqa: E501

        :return: The https_timeout of this ProvidersDuoExtended.  # noqa: E501
        :rtype: int
        """
        return self._https_timeout

    @https_timeout.setter
    def https_timeout(self, https_timeout):
        """Sets the https_timeout of this ProvidersDuoExtended.

        Specifies the number of seconds to wait for HTTPS responses from Duo Security.  # noqa: E501

        :param https_timeout: The https_timeout of this ProvidersDuoExtended.  # noqa: E501
        :type: int
        """
        if https_timeout is not None and https_timeout > 600:  # noqa: E501
            raise ValueError("Invalid value for `https_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if https_timeout is not None and https_timeout < 0:  # noqa: E501
            raise ValueError("Invalid value for `https_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._https_timeout = https_timeout

    @property
    def ikey(self):
        """Gets the ikey of this ProvidersDuoExtended.  # noqa: E501

        Specifies the integration key.  # noqa: E501

        :return: The ikey of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._ikey

    @ikey.setter
    def ikey(self, ikey):
        """Sets the ikey of this ProvidersDuoExtended.

        Specifies the integration key.  # noqa: E501

        :param ikey: The ikey of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        if ikey is not None and len(ikey) > 256:
            raise ValueError("Invalid value for `ikey`, length must be less than or equal to `256`")  # noqa: E501
        if ikey is not None and len(ikey) < 0:
            raise ValueError("Invalid value for `ikey`, length must be greater than or equal to `0`")  # noqa: E501
        if ikey is not None and not re.search('^[A-Za-z0-9]*$', ikey):  # noqa: E501
            raise ValueError("Invalid value for `ikey`, must be a follow pattern or equal to `/^[A-Za-z0-9]*$/`")  # noqa: E501

        self._ikey = ikey

    @property
    def prompts(self):
        """Gets the prompts of this ProvidersDuoExtended.  # noqa: E501

        Specifies the maximum number of authentication prompts to display (1-3 default is 3).  # noqa: E501

        :return: The prompts of this ProvidersDuoExtended.  # noqa: E501
        :rtype: int
        """
        return self._prompts

    @prompts.setter
    def prompts(self, prompts):
        """Sets the prompts of this ProvidersDuoExtended.

        Specifies the maximum number of authentication prompts to display (1-3 default is 3).  # noqa: E501

        :param prompts: The prompts of this ProvidersDuoExtended.  # noqa: E501
        :type: int
        """
        if prompts is not None and prompts > 3:  # noqa: E501
            raise ValueError("Invalid value for `prompts`, must be a value less than or equal to `3`")  # noqa: E501
        if prompts is not None and prompts < 1:  # noqa: E501
            raise ValueError("Invalid value for `prompts`, must be a value greater than or equal to `1`")  # noqa: E501

        self._prompts = prompts

    @property
    def pushinfo(self):
        """Gets the pushinfo of this ProvidersDuoExtended.  # noqa: E501

        Specifies to include information in the Duo Push message.  # noqa: E501

        :return: The pushinfo of this ProvidersDuoExtended.  # noqa: E501
        :rtype: bool
        """
        return self._pushinfo

    @pushinfo.setter
    def pushinfo(self, pushinfo):
        """Sets the pushinfo of this ProvidersDuoExtended.

        Specifies to include information in the Duo Push message.  # noqa: E501

        :param pushinfo: The pushinfo of this ProvidersDuoExtended.  # noqa: E501
        :type: bool
        """

        self._pushinfo = pushinfo

    @property
    def skey(self):
        """Gets the skey of this ProvidersDuoExtended.  # noqa: E501

        Specifies the secret key.  # noqa: E501

        :return: The skey of this ProvidersDuoExtended.  # noqa: E501
        :rtype: str
        """
        return self._skey

    @skey.setter
    def skey(self, skey):
        """Sets the skey of this ProvidersDuoExtended.

        Specifies the secret key.  # noqa: E501

        :param skey: The skey of this ProvidersDuoExtended.  # noqa: E501
        :type: str
        """
        if skey is not None and len(skey) > 256:
            raise ValueError("Invalid value for `skey`, length must be less than or equal to `256`")  # noqa: E501
        if skey is not None and len(skey) < 0:
            raise ValueError("Invalid value for `skey`, length must be greater than or equal to `0`")  # noqa: E501
        if skey is not None and not re.search('^[A-Za-z0-9]*$', skey):  # noqa: E501
            raise ValueError("Invalid value for `skey`, must be a follow pattern or equal to `/^[A-Za-z0-9]*$/`")  # noqa: E501

        self._skey = skey

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
        if not isinstance(other, ProvidersDuoExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
