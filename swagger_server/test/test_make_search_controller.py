# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.search_request import SearchRequest  # noqa: E501
from swagger_server.models.search_response import SearchResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMakeSearchController(BaseTestCase):
    """MakeSearchController integration test stubs"""

    def test_search_files(self):
        """Test case for search_files

        Создать поиск файлов
        """
        body = SearchRequest()
        response = self.client.open(
            '/search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
