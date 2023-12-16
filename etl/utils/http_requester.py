import httpx
from dataclasses import dataclass


@dataclass
class HTTPRequesterResponse:
    status_code: int
    html: str


class HTTPRequester:
    __URL: str

    def __init__(self) -> None:
        self.__URL = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"  # noqa E501

    async def request_from_page(self) -> HTTPRequesterResponse:
        """Busca o HTML da url base da classe.

        https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm

        Returns
        -------
        HTTPRequesterResponse
            Retorna o status_code e o html.
        """
        async with httpx.AsyncClient(base_url=self.__URL) as client:
            response = await client.get("/")

            return HTTPRequesterResponse(
                status_code=response.status_code, html=response.text
            )
