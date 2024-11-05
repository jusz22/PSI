from abc import ABC
from typing import Iterable


class IPostsService(ABC):
    async def get_and_save_posts(self) -> None:
        pass

    async def filter_by_name(self, posts_filter: str) -> Iterable[dict]:
        pass

    async def get_all_posts(self) -> Iterable[dict]:
        pass