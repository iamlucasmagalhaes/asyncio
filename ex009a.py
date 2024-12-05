import asyncio
import aiohttp
import time

# Função assíncrona para fazer as requisições
async def requisicaoRest(id):
    #cria uma sessão HTTP
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.restful-api.dev/objects/{id}') as response: #realiza uma requisição HTTP GET para a API. A resposta é armazenada em response
            resposta = await response.json()  #transforma o response em JSON
            print(f"Status da requisição {id}: {response.status}") #imprime o status HTTP da requisição
            print(resposta)  #imprime o conteúdo da resposta JSON

# Função principal assíncrona
async def main():
    inicio = time.time()  #marca o tempo de início
    # Cria as tarefas para todas as requisições
    tarefas = [requisicaoRest(i) for i in range(1, 11)]
    
    # Executa todas as requisições em paralelo e espera pela conclusão
    await asyncio.gather(*tarefas)
    
    # Exibe o tempo total de execução
    print(f'Execução das 10 requisições terminou em: {time.time() - inicio:.2f} segundos')

asyncio.run(main())
