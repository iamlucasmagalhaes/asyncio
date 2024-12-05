import asyncio
from random import randint

async def deposito(valor):
    global saldo
    await asyncio.sleep(randint(1,3))
    saldo += valor

async def saque(valor):
    global saldo
    await asyncio.sleep(randint(1,3))
    saldo -= valor

async def main():
    print(f'Saldo atual: {saldo}')
    t1 = asyncio.create_task(deposito(400))
    t2 = asyncio.create_task(saque(300))
    t3 = asyncio.create_task(deposito(200))
    t4 = asyncio.create_task(saque(100))
    await t1,t2,t3,t4
    print(f'Saldo atual: {saldo}')

saldo = 0    
asyncio.run(main())

#O que está ocorrendo é o problema da condição de corrida, o qual acontece quando um processo sobrepõe outro. Mais detalhadamente, isso ocorre quando um processo começa a ser executado, é interrompido, e outro processo realiza a mesma operação, porém com outros valores. Após essa tarefa ser executada, a primeira tarefa volta a ter sua vez, continua de onde parou e altera o valor do cálculo, em vez de usar o valor atual. Ou seja, há um problema de sincronização.