from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iposts_service import IPostsService


async def main(
        service: IPostsService = Provide[Container.service],
) -> None:
    await service.get_and_save_posts()
    posts = await service.get_all_posts()
    posts_filter = "ma"
    filtered_posts = await service.filter_by_name(posts_filter=posts_filter)
    print(posts)
    print(filtered_posts)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
