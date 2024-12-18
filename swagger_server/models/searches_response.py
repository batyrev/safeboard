# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SearchesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, search_id: str=None, paths: List[str]=None):  # noqa: E501
        """SearchesResponse - a model defined in Swagger

        :param search_id: The search_id of this SearchesResponse.  # noqa: E501
        :type search_id: str
        :param paths: The paths of this SearchesResponse.  # noqa: E501
        :type paths: List[str]
        """
        self.swagger_types = {
            'search_id': str,
            'paths': List[str]
        }

        self.attribute_map = {
            'search_id': 'search_id',
            'paths': 'paths'
        }
        self._search_id = search_id
        self._paths = paths

    @classmethod
    def from_dict(cls, dikt) -> 'SearchesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The searchesResponse of this SearchesResponse.  # noqa: E501
        :rtype: SearchesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def search_id(self) -> str:
        """Gets the search_id of this SearchesResponse.


        :return: The search_id of this SearchesResponse.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str):
        """Sets the search_id of this SearchesResponse.


        :param search_id: The search_id of this SearchesResponse.
        :type search_id: str
        """

        self._search_id = search_id

    @property
    def paths(self) -> List[str]:
        """Gets the paths of this SearchesResponse.


        :return: The paths of this SearchesResponse.
        :rtype: List[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths: List[str]):
        """Sets the paths of this SearchesResponse.


        :param paths: The paths of this SearchesResponse.
        :type paths: List[str]
        """

        self._paths = paths
