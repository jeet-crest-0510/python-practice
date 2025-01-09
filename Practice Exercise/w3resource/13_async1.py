import asyncio
import time

async def coffee():
    print("Start Coffee()")
    await asyncio.sleep(3)
    print("End Coffee()")
    
    return "Coffee Ready"

async def Toast():
    print("Start Toast()")
    await asyncio.sleep(3)
    print("End Toast()")
    
    return "Toast Ready"

async def main():
    start = time.time()
    f1 = asyncio.create_task(coffee())
    f2 = asyncio.create_task(Toast())
    r1 = await f1
    r2 = await f2
    end = time.time()
    print(f"Elapsed Time: {end - start} s")

if __name__ == "__main__":
    asyncio.run(main())