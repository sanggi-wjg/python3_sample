import asyncio


async def hello():
    print('Hello world')


async def add(a, b):
    print('a + b ?')
    # await asyncio.sleep(1.0)

    return a + b


async def print_add(a, b):
    result = await add(a, b)
    print('a + b = ', result)


loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
loop.run_until_complete(print_add(1, 2))
loop.close()
