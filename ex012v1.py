import asyncio
from random import randint

saldo = 0
lock = asyncio.Lock()

async def deposito(valor):
    global saldo
    await asyncio.sleep(randint(1, 3))
    async with lock:
        saldo += valor
        print(f'Saldo atual: {saldo}')

async def saque(valor):
    global saldo
    await asyncio.sleep(randint(1, 3))
    async with lock:
        saldo -= valor
        print(f'Saldo atual: {saldo}')

async def main():
    global saldo
    saldo = 0  
    print(f'Saldo atual: {saldo}')
    
    t1 = asyncio.create_task(deposito(400))
    t2 = asyncio.create_task(saque(300))
    t3 = asyncio.create_task(deposito(200))
    t4 = asyncio.create_task(saque(100))
    
    await t1 
    await t2
    await t3
    await t4
    print(f'Saldo atual: {saldo}')

asyncio.run(main())