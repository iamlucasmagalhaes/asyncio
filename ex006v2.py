import asyncio
import random

#retorna um número aleatório entre 3 e 10
def time_generator():
    return random.randint(3, 10)

async def task(id):
    print(f'Task iniciada {id}')
    time = time_generator()
    await asyncio.sleep(time)
    
    print(f'Task finalizada: {id} em {time} segundos')

async def main():
    print('Aplicação iniciada')
    
    # Cria uma lista de tarefas
    tasks = []
    
    # Cria 30 tarefas
    for i in range(1, 31):
        task = asyncio.create_task(task(i))
        tasks.append(task)
    
    # Espera todas as tarefas terminarem
    await asyncio.gather(*tasks)

# Executa a função main
asyncio.run(main())
