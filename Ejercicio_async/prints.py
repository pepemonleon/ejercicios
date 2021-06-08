import asyncio
import random
import decimal

BOOTS = 0
SECONDS = decimal.Decimal('0.00')

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




loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_seconds(),
                   worker())
)
loop.close()
