import asyncio

async def wait_display() -> None:
    await asyncio.sleep(2)
    print("Oczekiwanie zakończone")

if __name__ == "__main__":
  asyncio.run(wait_display())  