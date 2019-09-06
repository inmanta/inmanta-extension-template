import pytest

from inmanta import protocol


@pytest.mark.asyncio
async def test_hello_world(server):
    client = protocol.Client("client")
    result = await client.hello_world()
    assert result.code == 200
    assert result.result == {"data": "hello-world"}
