import pytest

from etl.utils.http_requester import HTTPRequester


@pytest.mark.asyncio
async def test_http_requester():
    requester = HTTPRequester()

    response = await requester.request_from_page()

    assert response.status_code == 200
    assert response.html != ""
