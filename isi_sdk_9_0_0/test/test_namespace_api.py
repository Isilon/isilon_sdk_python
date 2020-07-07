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
from isi_sdk_9_0_0.api.namespace_api import NamespaceApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestNamespaceApi(unittest.TestCase):
    """NamespaceApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.namespace_api.NamespaceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_directory(self):
        """Test case for copy_directory

        """
        pass

    def test_copy_file(self):
        """Test case for copy_file

        """
        pass

    def test_create_access_point(self):
        """Test case for create_access_point

        """
        pass

    def test_create_directory(self):
        """Test case for create_directory

        """
        pass

    def test_create_directory_with_access_point_container_path(self):
        """Test case for create_directory_with_access_point_container_path

        """
        pass

    def test_create_file(self):
        """Test case for create_file

        """
        pass

    def test_delete_access_point(self):
        """Test case for delete_access_point

        """
        pass

    def test_delete_directory(self):
        """Test case for delete_directory

        """
        pass

    def test_delete_directory_with_access_point_container_path(self):
        """Test case for delete_directory_with_access_point_container_path

        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        """
        pass

    def test_get_acl(self):
        """Test case for get_acl

        """
        pass

    def test_get_directory_attributes(self):
        """Test case for get_directory_attributes

        """
        pass

    def test_get_directory_contents(self):
        """Test case for get_directory_contents

        """
        pass

    def test_get_directory_metadata(self):
        """Test case for get_directory_metadata

        """
        pass

    def test_get_directory_with_access_point_container_path(self):
        """Test case for get_directory_with_access_point_container_path

        """
        pass

    def test_get_file_attributes(self):
        """Test case for get_file_attributes

        """
        pass

    def test_get_file_contents(self):
        """Test case for get_file_contents

        """
        pass

    def test_get_file_metadata(self):
        """Test case for get_file_metadata

        """
        pass

    def test_get_worm_properties(self):
        """Test case for get_worm_properties

        """
        pass

    def test_list_access_points(self):
        """Test case for list_access_points

        """
        pass

    def test_move_directory(self):
        """Test case for move_directory

        """
        pass

    def test_move_directory_with_access_point_container_path(self):
        """Test case for move_directory_with_access_point_container_path

        """
        pass

    def test_move_file(self):
        """Test case for move_file

        """
        pass

    def test_query_directory(self):
        """Test case for query_directory

        """
        pass

    def test_set_acl(self):
        """Test case for set_acl

        """
        pass

    def test_set_directory_metadata(self):
        """Test case for set_directory_metadata

        """
        pass

    def test_set_file_metadata(self):
        """Test case for set_file_metadata

        """
        pass

    def test_set_worm_properties(self):
        """Test case for set_worm_properties

        """
        pass


if __name__ == '__main__':
    unittest.main()
