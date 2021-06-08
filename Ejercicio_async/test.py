import asyncio
import random
import time

BOOTS = 0
SECONDS = 0
async def print_seconds():
    global SECONDS
    while True:
        time.sleep(1)
        SECONDS += 1
        print("Seconds: " + str(SECONDS) + " boots: " + str(BOOTS))

async def test(text):
    while True:
        time.sleep(1)
        print(text)

async def test_2(text):
    for i in range(5):
        time.sleep(1)
        print(text)


async def test_3(text):
    for i in range(5):
        time.sleep(1)
        print(text)

async def make_boot():
    global BOOTS
    manufacturing_time = random.choice([1,3,5])
    # await asyncio.sleep(manufacturing_time)
    # await asyncio.sleep(manufacturing_time)
    time.sleep(manufacturing_time)
    BOOTS += 1
    print("HELLOOOOOOO")


async def worker():
    while 1:
        await make_boot()


async def main():
    # task_test = asyncio.create_task(print_seconds())
    # task_test_3 = asyncio.create_task(print_seconds())
    #task_3 = asyncio.create_task(worker())


    task_adios = asyncio.create_task(test_2("ADIOS"))
    # task_bye = asyncio.create_task(test_3("BYE"))

    # L = asyncio.gather(
    #     # test("Hola"),
    #     test_2("ADIOS"),
    #     test_3("BYEEE"),
    # )
    # print(L)

    print("THIRD")


#asyncio.run(main())

loop = asyncio.get_event_loop()
loop.create_task(test_2("HOLA"))
loop.create_task(test_3("ADIOS"))
loop.run_forever()
loop.close()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


