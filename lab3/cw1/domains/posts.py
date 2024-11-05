from dataclasses import dataclass


@dataclass
class PostsRecord:
    user_id: int
    post_id: int
    title: str
    body: str
