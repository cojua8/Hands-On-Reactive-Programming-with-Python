import datetime
import asyncio


async def wait(delay):
    now = datetime.datetime.now()
    print(f"wait for {delay} seconds at {now.strftime('%H:%M:%S')}")
    await asyncio.sleep(delay)
    now = datetime.datetime.now()
    print(f"waited for {delay} seconds at {now.strftime('%H:%M:%S')}")
    return True


loop = asyncio.get_event_loop()
loop.run_until_complete(wait(2))
