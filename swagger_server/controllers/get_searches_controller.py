from swagger_server.models.searches_response import SearchesResponse  # noqa: E501
from swagger_server.services.db_service import get_paths_by_search_id  # noqa: E501


def get_search_results(search_id):  # noqa: E501
    """Получить результаты поиска

    Ответом на получение результатов поиска должен быть либо список путей к файлам,
    либо информация о том, что поиск ещё не завершился # noqa: E501

    :param search_id: Идентификатор поиска
    :type search_id: str

    :rtype: SearchesResponse
    """
    paths = get_paths_by_search_id(search_id)
    return SearchesResponse(search_id=search_id, paths=paths)
