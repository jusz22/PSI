import asyncio

async def print_number(number: int) -> None:
    await asyncio.sleep(1)
    print(f"{number}")

async def main():
    args = [1, 2, 3, 4, 5]
    await asyncio.gather(*(print_number(i) for i in args))

if __name__ == "__main__":
    asyncio.run(main())
