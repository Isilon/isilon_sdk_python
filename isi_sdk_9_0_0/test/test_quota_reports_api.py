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
from isi_sdk_9_0_0.api.quota_reports_api import QuotaReportsApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestQuotaReportsApi(unittest.TestCase):
    """QuotaReportsApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.quota_reports_api.QuotaReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_report_about(self):
        """Test case for get_report_about

        """
        pass


if __name__ == '__main__':
    unittest.main()
