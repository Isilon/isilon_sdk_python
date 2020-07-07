# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_9_0_0
from isi_sdk_9_0_0.api.auth_roles_api import AuthRolesApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestAuthRolesApi(unittest.TestCase):
    """AuthRolesApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.auth_roles_api.AuthRolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role_member(self):
        """Test case for create_role_member

        """
        pass

    def test_create_role_privilege(self):
        """Test case for create_role_privilege

        """
        pass

    def test_delete_role_member(self):
        """Test case for delete_role_member

        """
        pass

    def test_delete_role_privilege(self):
        """Test case for delete_role_privilege

        """
        pass

    def test_list_role_members(self):
        """Test case for list_role_members

        """
        pass

    def test_list_role_privileges(self):
        """Test case for list_role_privileges

        """
        pass


if __name__ == '__main__':
    unittest.main()
