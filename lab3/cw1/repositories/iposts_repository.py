from abc import ABC
from typing import Iterable
from domains.posts import PostsRecord

class IPostsRepository(ABC):
    async def get_all_posts(self) -> Iterable[dict] | None:
        pass
    
    async def filter_by_name(self, filter: str) -> Iterable[dict]:
        pass
    
    async def filter_by_content(self, filter: str) -> Iterable[dict]:
        pass