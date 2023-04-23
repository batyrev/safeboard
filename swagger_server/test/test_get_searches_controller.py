# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.search_response_not_finished import SearchResponseNotFinished  # noqa: E501
from swagger_server.models.searches_response import SearchesResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetSearchesController(BaseTestCase):
    """GetSearchesController integration test stubs"""

    def test_get_search_results(self):
        """Test case for get_search_results

        Получить результаты поиска
        """
        response = self.client.open(
            '/searches/{search_id}'.format(search_id='search_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
