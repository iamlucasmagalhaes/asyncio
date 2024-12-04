import asyncio

def time_generator():
    

async def task1(id):
    print(f'Task iniciada {id}')
    if id % 2 == 0:
        await asyncio.sleep(4)
    await asyncio.sleep(6)
    
    print(f'Task finalizada: {id}')

async def main():
    print('Aplicação iniciada')
    
    # Cria uma lista de tarefas
    tasks = []
    
    # Cria 30 tarefas
    for i in range(1, 31):
        task = asyncio.create_task(task1(i))
        tasks.append(task)
    
    # Espera todas as tarefas terminarem
    await asyncio.gather(*tasks)

# Executa a função main
asyncio.run(main())
