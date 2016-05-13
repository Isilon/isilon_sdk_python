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

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.auth_users_api import AuthUsersApi


class TestAuthUsersApi(unittest.TestCase):
    """ AuthUsersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auth_users_api.AuthUsersApi()

    def tearDown(self):
        pass

    def test_create_user_member_of_item(self):
        """
        Test case for create_user_member_of_item

        
        """
        pass

    def test_delete_user_member_of_member_of(self):
        """
        Test case for delete_user_member_of_member_of

        
        """
        pass

    def test_list_user_member_of(self):
        """
        Test case for list_user_member_of

        
        """
        pass

    def test_update_user_change_password(self):
        """
        Test case for update_user_change_password

        
        """
        pass


if __name__ == '__main__':
    unittest.main()