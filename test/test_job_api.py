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
from swagger_client.apis.job_api import JobApi


class TestJobApi(unittest.TestCase):
    """ JobApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.job_api.JobApi()

    def tearDown(self):
        pass

    def test_create_job_job(self):
        """
        Test case for create_job_job

        
        """
        pass

    def test_create_job_policy(self):
        """
        Test case for create_job_policy

        
        """
        pass

    def test_delete_job_policy(self):
        """
        Test case for delete_job_policy

        
        """
        pass

    def test_get_job_events(self):
        """
        Test case for get_job_events

        
        """
        pass

    def test_get_job_job(self):
        """
        Test case for get_job_job

        
        """
        pass

    def test_get_job_job_summary(self):
        """
        Test case for get_job_job_summary

        
        """
        pass

    def test_get_job_policy(self):
        """
        Test case for get_job_policy

        
        """
        pass

    def test_get_job_recent(self):
        """
        Test case for get_job_recent

        
        """
        pass

    def test_get_job_reports(self):
        """
        Test case for get_job_reports

        
        """
        pass

    def test_get_job_statistics(self):
        """
        Test case for get_job_statistics

        
        """
        pass

    def test_get_job_type(self):
        """
        Test case for get_job_type

        
        """
        pass

    def test_get_job_types(self):
        """
        Test case for get_job_types

        
        """
        pass

    def test_list_job_jobs(self):
        """
        Test case for list_job_jobs

        
        """
        pass

    def test_list_job_policies(self):
        """
        Test case for list_job_policies

        
        """
        pass

    def test_update_job_job(self):
        """
        Test case for update_job_job

        
        """
        pass

    def test_update_job_policy(self):
        """
        Test case for update_job_policy

        
        """
        pass

    def test_update_job_type(self):
        """
        Test case for update_job_type

        
        """
        pass


if __name__ == '__main__':
    unittest.main()