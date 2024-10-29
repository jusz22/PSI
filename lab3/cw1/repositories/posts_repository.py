import aiohttp

from utils import consts
from typing import Iterable

from repositories.iposts_repository import IPostsRepository

class PostsRepository(IPostsRepository):
    async def get_all_posts(self) -> Iterable[dict]:
        all_posts = await self._get_posts()
        
        return all_posts
    
    async def filter_by_name(self, filter: str) -> Iterable[dict]:
        posts = await self._get_posts()

async def _get_posts(self) -> Iterable[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(consts.API_URL) as response:
            if response.status != 200:
                return None

            return await response.json()
    