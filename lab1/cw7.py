import asyncio

async def prep(activity) -> None:
    print(f"Starting {activity[0]}")
    await asyncio.sleep(activity[1])
    print(f"Finished {activity[0]}")

async def cooking(meal) -> None:
    for activity in meal:
        await prep(activity)

async def main():
    meals = [[("Krojenie mięsa", 2), ("Smażenie mięsa", 4), ("Arażacja talerza", 2)],
            [("Mycie warzyw", 3), ("Krojenie warzyw", 5), ("Pieczenie warzyw", 7)],
            [("Gotowanie makaronu", 4), ("Przygotowywanie sosu", 4), ("Połączenie składników", 2)]]
    await asyncio.gather(*(cooking(meals) for meals in meals))

if __name__ == "__main__":
    asyncio.run(main())