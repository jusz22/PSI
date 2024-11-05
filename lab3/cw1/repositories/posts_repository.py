import asyncio
from typing import Iterable

import aiohttp
from repositories.iposts_repository import IPostsRepository


async def _get_posts() -> Iterable[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
            if response.status != 200:
                return None

            return await response.json()


class PostsRepository(IPostsRepository):

    def __int__(self):
        self._posts: Iterable[dict] = []

    async def get_all_posts(self) -> Iterable[dict]:
        all_posts = await _get_posts()

        return all_posts

    async def save_posts(self, posts: Iterable[dict]) -> None:
        self._posts = posts

    async def filter_by_title(self, posts_filter: str) -> Iterable[dict]:
        return [post for post in self._posts if posts_filter in post["title"].lower()]

    async def filter_by_content(self, posts_filter: str) -> Iterable[dict]:
        return [post for post in self._posts if posts_filter in post["body"].lower()]


async def main():
    repo = PostsRepository()
    posts = await PostsRepository.filter_by_title(repo, "m")
    print(posts)


if __name__ == "__main__":
    asyncio.run(main())
