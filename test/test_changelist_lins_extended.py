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
from swagger_client.models.changelist_lins_extended import ChangelistLinsExtended


class TestChangelistLinsExtended(unittest.TestCase):
    """ ChangelistLinsExtended unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangelistLinsExtended(self):
        """
        Test ChangelistLinsExtended
        """
        model = swagger_client.models.changelist_lins_extended.ChangelistLinsExtended()


if __name__ == '__main__':
    unittest.main()