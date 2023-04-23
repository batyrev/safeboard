import hashlib
import threading

import connexion
import six

from swagger_server.models.search_request import SearchRequest  # noqa: E501
from swagger_server.models.search_response import SearchResponse  # noqa: E501
from swagger_server import util

from swagger_server.services.db_service import add_new_search
from swagger_server.services.search_service import find_files_by_mask


def search_files(body):  # noqa: E501
    """Создать поиск файлов

    Ответом на создание поиска файлов должен быть идентификатор поиска # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SearchResponse
    """
    search_id = generate_id(body)
    if connexion.request.is_json:
        body = SearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
        add_new_search(search_id)
        thread = threading.Thread(target=find_files_by_mask,
                                  args=(search_id, body.file_mask))
        thread.start()
    return SearchResponse(search_id=search_id)


def generate_id(body) -> str:
    """Generate hash"""
    body_str = body["text"]
    body_str += body["file_mask"]
    body_str += body["creation_time"]["operator"]
    body_str += body["creation_time"]["value"]
    body_str += body["size"]["operator"]
    body_str += str(body["size"]["value"])
    return hashlib.md5(str.encode(body_str)).hexdigest()
