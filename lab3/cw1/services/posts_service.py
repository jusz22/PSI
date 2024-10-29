from typing import Iterable
from services.iposts_service import IPostsService
from repositories.iposts_repository import IPostsRepository


class PostsService(IPostsService):
    repository: IPostsRepository

def __init__(self, repository: IPostsRepository) -> None:
    self.repository = repository

async def filter_by_name(self, filter: str) -> Iterable[dict]:
    posts = await self.repository.get_all_posts()