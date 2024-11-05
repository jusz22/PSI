from abc import ABC
from typing import Iterable


class IPostsRepository(ABC):

    async def save_posts(self, posts: Iterable[dict]) -> None:
        pass

    async def get_all_posts(self) -> Iterable[dict] | None:
        pass
    
    async def filter_by_title(self, posts_filter: str) -> Iterable[dict]:
        pass
    
    async def filter_by_content(self, posts_filter: str) -> Iterable[dict]:
        pass
