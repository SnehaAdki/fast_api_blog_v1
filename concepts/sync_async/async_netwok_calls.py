import time
import asyncio
import aiohttp

async def make_request(session,req_n):
    url = "https://httpbin.org/get"
    print(f"Making session call {req_n}")
    async with session.get(url) as resp : 
        if resp.status == 200:
            await resp.text()

async def main():
    req_cnt = 10
    async with aiohttp.ClientSession() as session:
        await asyncio.gather( *[make_request(session,i) for i in range(0,req_cnt)])

  
start = time.time()
asyncio.run(main())
end = time.time()
print(f"Total time taken {end - start}")