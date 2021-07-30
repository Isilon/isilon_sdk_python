# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_9_1_0
from isi_sdk_9_1_0.api.performance_api import PerformanceApi  # noqa: E501
from isi_sdk_9_1_0.rest import ApiException


class TestPerformanceApi(unittest.TestCase):
    """PerformanceApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_1_0.api.performance_api.PerformanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_performance_dataset(self):
        """Test case for create_performance_dataset

        """
        pass

    def test_delete_performance_dataset(self):
        """Test case for delete_performance_dataset

        """
        pass

    def test_get_performance_dataset(self):
        """Test case for get_performance_dataset

        """
        pass

    def test_get_performance_metric(self):
        """Test case for get_performance_metric

        """
        pass

    def test_get_performance_metrics(self):
        """Test case for get_performance_metrics

        """
        pass

    def test_get_performance_settings(self):
        """Test case for get_performance_settings

        """
        pass

    def test_list_performance_datasets(self):
        """Test case for list_performance_datasets

        """
        pass

    def test_update_performance_dataset(self):
        """Test case for update_performance_dataset

        """
        pass

    def test_update_performance_settings(self):
        """Test case for update_performance_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
