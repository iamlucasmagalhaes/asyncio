import asyncio

#verifica se o número é primo
def prime(num):
    if num <= 1: #se o número for menor ou igual a 1 ele retorna falso
        return False
    #testa todos os números de 2 até a raiz quadrada de num, para verificar se ele possui um divisor exato
    for i in range(2, int(num ** 0.5) + 1): #ele vai começar o loop em 2, pois todo número é divisivel por 1
        if num % i == 0:
            #se o numero for divisivel por i então ele não é primo
            return False
    return True

#função geradora para os números primos a partir de um número N
async def prime_generator(start):
    num = start #atribui o parametro para uma variável, para que ela possa ser atualizada 
    while True:
        #para cada número primo que essa função encontrar ele vai retornar com yield
        if prime(num):
            yield num 
        num += 1 #atualiza o valor de num para que o proximo valor dele seja verificado
        await asyncio.sleep(0)

async def main():
    firstNumber = 10 #valor inicial
    async for is_prime in prime_generator(firstNumber):
        print(is_prime)
        await asyncio.sleep(1)


asyncio.run(main())