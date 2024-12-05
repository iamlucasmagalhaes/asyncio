import asyncio
from random import randint
import aiohttp
from aioconsole import aprint, ainput

async def msg_blink(text):
    #cria um loop inifinito para a impressão da mensagem
    while True:
        #end="\r" volta o cursor para o inicio da linha, imintando uma máquina de datilografar
        #flush=True força a liberação do conteúdo do buffer para o terminal
        print(text, end="\r", flush=True)  #exibe a mensagem
        await asyncio.sleep(0.5)  #aguarda 0.5 segundos
        print(" " * len(text), end="\r", flush=True)  #apaga a mensagem
        await asyncio.sleep(0.5)  #aguarda 0.5 segundos

#função que retorna meu ip
async def endIP():
    #usa o aiohttp.ClientSession() para fazer uma requisição GET ao https://api.ipify.org, que retorna um IP público 
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.ipify.org') as response:
            ip = await response.text() #pega o IP retornado pela API
    await asyncio.sleep(randint(3, 10)) #pausa aleatória
    await aprint(" " * len(ip), end="\r", flush=True)  #limpa a tela
    return ip

async def main():
    tasks = {asyncio.create_task(endIP()), asyncio.create_task(msg_blink("loading"))} #cria uma tarefa assíncrona que mostra o loading e o IP
    respostas, pendentes = await asyncio.wait(tasks, timeout=None, return_when="FIRST_COMPLETED") #espera até que uma das tarefas esteja completa

    for task in pendentes:
        task.cancel() #cancela as tarefas pendentes no caso a função que pisca a mensagem

    task = next(iter(respostas)) #armazena o ip

    print(f"O IP é: {task.result()}") #imprime o ip

asyncio.run(main()) 