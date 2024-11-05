from typing import Iterable
from services.iposts_service import IPostsService
from repositories.iposts_repository import IPostsRepository


class PostsService(IPostsService):

    def __init__(self, repository: IPostsRepository):
        self.repository = repository

    async def get_and_save_posts(self) -> None:
        posts = await self.repository.get_all_posts()
        await self.repository.save_posts(posts=posts)

    async def filter_by_name(self, posts_filter: str) -> Iterable[dict]:
        return await self.repository.filter_by_title(posts_filter=posts_filter)

    async def get_all_posts(self) -> Iterable[dict]:
        return await self.repository.get_all_posts()
