# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SearchRequestCreationTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, value: str=None, operator: str=None):  # noqa: E501
        """SearchRequestCreationTime - a model defined in Swagger

        :param value: The value of this SearchRequestCreationTime.  # noqa: E501
        :type value: str
        :param operator: The operator of this SearchRequestCreationTime.  # noqa: E501
        :type operator: str
        """
        self.swagger_types = {
            'value': str,
            'operator': str
        }

        self.attribute_map = {
            'value': 'value',
            'operator': 'operator'
        }
        self._value = value
        self._operator = operator

    @classmethod
    def from_dict(cls, dikt) -> 'SearchRequestCreationTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The searchRequest_creation_time of this SearchRequestCreationTime.  # noqa: E501
        :rtype: SearchRequestCreationTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this SearchRequestCreationTime.


        :return: The value of this SearchRequestCreationTime.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this SearchRequestCreationTime.


        :param value: The value of this SearchRequestCreationTime.
        :type value: str
        """

        self._value = value

    @property
    def operator(self) -> str:
        """Gets the operator of this SearchRequestCreationTime.


        :return: The operator of this SearchRequestCreationTime.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str):
        """Sets the operator of this SearchRequestCreationTime.


        :param operator: The operator of this SearchRequestCreationTime.
        :type operator: str
        """

        self._operator = operator
