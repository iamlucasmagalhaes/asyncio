import asyncio
from random import randint
from aioconsole import aprint

#função para verificar se um número é primo
async def is_prime(number):
    await asyncio.sleep(0.1)

    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Função de animação "loading"
async def msg_blink(text):
    while True:
        print(text, end="\r", flush=True)  # Exibe a mensagem
        await asyncio.sleep(0.5)  # Aguarda 0.5 segundos
        print(" " * len(text), end="\r", flush=True)  # Apaga a mensagem
        await asyncio.sleep(0.5)  # Aguarda 0.5 segundos

async def main():
    # Número a ser verificado
    number = 5_000_111_000_222_021

    # Cria uma tarefa assíncrona que verifica se o número é primo e outra para a animação
    tasks = {
        asyncio.create_task(is_prime(number)), 
        asyncio.create_task(msg_blink("loading..."))
    }

    # Espera até que uma das tarefas seja concluída
    respostas, pendentes = await asyncio.wait(tasks, timeout=None, return_when="FIRST_COMPLETED")

    # Cancela as tarefas pendentes (a animação "loading")
    for task in pendentes:
        task.cancel()

    # A primeira tarefa completada é o cálculo do número primo
    task = next(iter(respostas))

    # Exibe o resultado
    result = task.result()
    print(f"O número {number} {'é primo' if result else 'não é primo'}.")


asyncio.run(main())
