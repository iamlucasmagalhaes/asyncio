import requests
import time

#função para fazer a requisição HTTP
def requisicaoRest(id):
    url = f'https://api.restful-api.dev/objects/{id}'
    response = requests.get(url)  #realiza uma requisição HTTP GET para a API
    print(f"Status da requisição {id}: {response.status_code}")  #imprime o status da requisição
    print(response.json())  #i mprime o conteúdo da resposta em JSON

#função principal
def main():
    inicio = time.time()  #marca o tempo de início
    #faz as 10 requisições de forma síncrona
    for i in range(1, 11):
        requisicaoRest(i)
    
    #exibe o tempo total de execução
    print(f'Execução das 10 requisições terminou em: {time.time() - inicio:.2f} segundos')

main()
