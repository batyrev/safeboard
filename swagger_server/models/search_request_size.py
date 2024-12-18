# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SearchRequestSize(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, value: int=None, operator: str=None):  # noqa: E501
        """SearchRequestSize - a model defined in Swagger

        :param value: The value of this SearchRequestSize.  # noqa: E501
        :type value: int
        :param operator: The operator of this SearchRequestSize.  # noqa: E501
        :type operator: str
        """
        self.swagger_types = {
            'value': int,
            'operator': str
        }

        self.attribute_map = {
            'value': 'value',
            'operator': 'operator'
        }
        self._value = value
        self._operator = operator

    @classmethod
    def from_dict(cls, dikt) -> 'SearchRequestSize':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The searchRequest_size of this SearchRequestSize.  # noqa: E501
        :rtype: SearchRequestSize
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> int:
        """Gets the value of this SearchRequestSize.


        :return: The value of this SearchRequestSize.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this SearchRequestSize.


        :param value: The value of this SearchRequestSize.
        :type value: int
        """

        self._value = value

    @property
    def operator(self) -> str:
        """Gets the operator of this SearchRequestSize.


        :return: The operator of this SearchRequestSize.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str):
        """Sets the operator of this SearchRequestSize.


        :param operator: The operator of this SearchRequestSize.
        :type operator: str
        """

        self._operator = operator
