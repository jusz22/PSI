import asyncio

async def fib(n: int) -> None:
    first = 0
    second = 1
    i = 0
    while i < n:
        print(first)
        await asyncio.sleep(1)
        result = first + second
        first = second
        second = result
        i += 1

if __name__ == "__main__":
    asyncio.run(fib(10))