import asyncio

async def alert() -> None:
    await asyncio.sleep(3)
    print("Alert")

async def info() -> None:
    await asyncio.sleep(1)
    print("Information")

async def main() -> None:
    await asyncio.gather(alert(), info())

if __name__ == "__main__":
    asyncio.run(main())
