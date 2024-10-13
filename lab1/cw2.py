import asyncio

async def hello_world() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(1)
    print("world")

if __name__ == "__main__":
    asyncio.run(hello_world())