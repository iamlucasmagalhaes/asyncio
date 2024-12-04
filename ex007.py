import asyncio
import aioconsole

#imprime e apaga a mensagem na tela
async def msg_blink(text):
    #cria um loop inifinito para a impressão da mensagem
    while True:
        #end="\r" volta o cursor para o inicio da linha, imintando uma máquina de datilografar
        #flush=True força a liberação do conteúdo do buffer para o terminal
        print(text, end="\r", flush=True)  #exibe a mensagem
        await asyncio.sleep(0.5)  #aguarda 0.5 segundos
        print(" " * len(text), end="\r", flush=True)  #apaga a mensagem
        await asyncio.sleep(0.5)  #aguarda 0.5 segundos


async def main():
    #inicia a função msg_blink em uma tarefa assíncrona
    blink_task = asyncio.create_task(msg_blink("loading..."))

    # Espera até que o usuário pressione Enter
    await aioconsole.ainput("Pressione ENTER para parar o programa...\n")
    
    # Quando o ENTER for pressionado, cancela a tarefa do blink
    blink_task.cancel()
    await blink_task  # Aguarda a conclusão da tarefa do blink

asyncio.run(main())
