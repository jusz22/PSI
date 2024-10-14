import asyncio

async def packaging_machine(max_operation_time: int) -> None:
    timer = 0
    while(timer <= max_operation_time):
        print("Packaged one box")
        timer += 3
        await asyncio.sleep(3)

async def burner_machine(max_operation_time: int) -> None:
    timer = 0
    while(timer <= max_operation_time):
        print("Burned one item")
        timer += 6
        await asyncio.sleep(6)

async def etching_machine(max_operation_time: int) -> None:
    timer = 0
    while(timer <= max_operation_time):
        print("Etched one glass pane")
        timer += 1
        await asyncio.sleep(1)

async def main(max_operation_time: int) -> None:
    await asyncio.gather(packaging_machine(max_operation_time), burner_machine(max_operation_time), etching_machine(max_operation_time))

if __name__ == "__main__":
    asyncio.run(main(15))