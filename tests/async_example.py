import asyncio

async def test(alias:str, first=False):
    
    for i in range(0, 10):
        if first : await asyncio.sleep(1)
        print(alias+" : "+str(i)) 

async def call_tests():
    tasks = [test("alias_"+str(_), _ < 1) for _ in range(0, 10)]

    await asyncio.gather(*tasks)

asyncio.run(call_tests())
