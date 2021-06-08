import asyncio
import random
import os
import decimal

BOOTS = 0
SECONDS = decimal.Decimal('0.00')

env_var_value = input('Please enter workers value:\n')
os.environ["workers"] = env_var_value

async def print_seconds():
    global SECONDS
    print("Seconds: " + str(SECONDS) + " boots: " + str(BOOTS))
    while True:
        await asyncio.sleep(1)
        SECONDS += 1
        print("Seconds: " + str(SECONDS) + " boots: " + str(BOOTS))



async def make_boots():
    global BOOTS
    manufacturing_time = random.choice([1, 3, 5])
    await asyncio.sleep(manufacturing_time)
    BOOTS += 1

async def worker():
        while True:
            await make_boots()

async def update_workers(numbers):
    for item in range(numbers):
        asyncio.create_task(worker())

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_seconds(),
                   update_workers(int(os.environ["workers"])))
)
loop.close()
