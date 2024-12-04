import asyncio
import random

#retorna um número aleatório entre 3 e 10
def time_generator():
    return random.randint(3, 10)

async def task(id):
    time = time_generator()
    await asyncio.sleep(time)
    print(f'Task finalizada: {id} em {time} segundos')

async def main():
    print('Aplicação iniciada')
    
    #cria uma lista de tarefas
    tasks = []
    
    #cria 30 tarefas
    for i in range(1, 31):
        task_obj = asyncio.create_task(task(i))
        tasks.append(task_obj) 

    #recebe a minha função tasks e retorna para o done as tarefas que foram completadas
    done = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

#executa a função main
asyncio.run(main())
