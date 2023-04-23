# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.search_request_creation_time import SearchRequestCreationTime  # noqa: F401,E501
from swagger_server.models.search_request_size import SearchRequestSize  # noqa: F401,E501
from swagger_server import util


class SearchRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, text: str=None, file_mask: str=None, size: SearchRequestSize=None, creation_time: SearchRequestCreationTime=None):  # noqa: E501
        """SearchRequest - a model defined in Swagger

        :param text: The text of this SearchRequest.  # noqa: E501
        :type text: str
        :param file_mask: The file_mask of this SearchRequest.  # noqa: E501
        :type file_mask: str
        :param size: The size of this SearchRequest.  # noqa: E501
        :type size: SearchRequestSize
        :param creation_time: The creation_time of this SearchRequest.  # noqa: E501
        :type creation_time: SearchRequestCreationTime
        """
        self.swagger_types = {
            'text': str,
            'file_mask': str,
            'size': SearchRequestSize,
            'creation_time': SearchRequestCreationTime
        }

        self.attribute_map = {
            'text': 'text',
            'file_mask': 'file_mask',
            'size': 'size',
            'creation_time': 'creation_time'
        }
        self._text = text
        self._file_mask = file_mask
        self._size = size
        self._creation_time = creation_time

    @classmethod
    def from_dict(cls, dikt) -> 'SearchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The searchRequest of this SearchRequest.  # noqa: E501
        :rtype: SearchRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this SearchRequest.


        :return: The text of this SearchRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this SearchRequest.


        :param text: The text of this SearchRequest.
        :type text: str
        """

        self._text = text

    @property
    def file_mask(self) -> str:
        """Gets the file_mask of this SearchRequest.


        :return: The file_mask of this SearchRequest.
        :rtype: str
        """
        return self._file_mask

    @file_mask.setter
    def file_mask(self, file_mask: str):
        """Sets the file_mask of this SearchRequest.


        :param file_mask: The file_mask of this SearchRequest.
        :type file_mask: str
        """

        self._file_mask = file_mask

    @property
    def size(self) -> SearchRequestSize:
        """Gets the size of this SearchRequest.


        :return: The size of this SearchRequest.
        :rtype: SearchRequestSize
        """
        return self._size

    @size.setter
    def size(self, size: SearchRequestSize):
        """Sets the size of this SearchRequest.


        :param size: The size of this SearchRequest.
        :type size: SearchRequestSize
        """

        self._size = size

    @property
    def creation_time(self) -> SearchRequestCreationTime:
        """Gets the creation_time of this SearchRequest.


        :return: The creation_time of this SearchRequest.
        :rtype: SearchRequestCreationTime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time: SearchRequestCreationTime):
        """Sets the creation_time of this SearchRequest.


        :param creation_time: The creation_time of this SearchRequest.
        :type creation_time: SearchRequestCreationTime
        """

        self._creation_time = creation_time
