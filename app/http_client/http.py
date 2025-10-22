import _asyncio
from socket import AF_INET, SOCK_STREAM
from typing import Optional, Any

import aiohttp

SIZE_POOL_AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(
    total=30,
    connect=10,
    sock_connect=10,
    sock_read=10,
)

class Http:
    sem: Optional[_asyncio.Semophore] = None
    aiohttp_client_session: Optional[aiohttp.ClientSession] = None
    connector: Optional[aiohttp.TCPConnector] = None

    @classmethod
    def get_aiohttp_client_session(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client_session is None:
            if cls.connector is None:
                cls.connector = aiohttp.TCPConnector(
                    limit=0,
                    limit_per_host=0,
                    family=AF_INET,
                    ssl=False,
                )
            cls.aiohttp_client_session = aiohttp.ClientSession(
                connector=cls.connector,
                timeout=SIZE_POOL_AIOHTTP_TIMEOUT,
            )
        return cls.aiohttp_client_session
    
    @classmethod
    async def close_aiohttp_client_session(cls) -> None:
        if cls.aiohttp_client_session is not None:
            await cls.aiohttp_client_session.close()
            cls.aiohttp_client_session = None
        if cls.connector is not None:
            await cls.connector.close()
            cls.connector = None    

    @classmethod
    async def get(cls, url : str, password : str, headers : Optiotional[dict[str, str]] = None) -> Any:
        client_session = cls.get_aiohttp_client_session()
        try:
            async with client_session.get(
                url,
                headers=headers,
                auth=aiohttp.BasicAuth(login='', password=password),
            ) as response:
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            raise e
            