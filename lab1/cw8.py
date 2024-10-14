import asyncio

async def read(file_name) -> None:
    print(f"Reading file: {file_name}")
    await asyncio.sleep(2)
    await analyze(file_name)

async def analyze(file_name) -> None:
    print(f"Analyzing file: {file_name}")
    await asyncio.sleep(4)
    await write(file_name)

async def write(file_name) -> None:
    print(f"Writing file: {file_name}")
    await asyncio.sleep(1)

async def main():
    files = ("plans.txt", "dreams.txt", "requests.txt")
    await asyncio.gather(*(read(file) for file in files))

if __name__ == "__main__":
    asyncio.run(main())