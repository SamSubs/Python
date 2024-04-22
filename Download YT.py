from pytube import YouTube
from Apagar_Texto import Apagar
import time

try:
    arquivo = open('Sav.txt', 'r')
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    arquivo.close()
    print('Arquivo Carregado Com Sucesso\nVideos: {}Audios: {}\n'.format(linha1, linha2))

except FileNotFoundError as erro:
    erro = str(erro)
    print(f'{erro[37:]} Nao Encontrado!!\nCriando Arquivo...')
    dado = open('Sav.txt', 'a')
    dado.close()
    time.sleep(2.5)
    print('Reinicie o Codigo!')
    exit()

print(f'{"YouTube Download 2.0":^30}')

print('Baixar Video [1]\nBaixar Audio MP4 [2]\nCaminho [3]\nSair [4]')

try:
    user = int(input(': '))
except ValueError as Erro:
    print('Digite um Valor Valido\nErro {}'.format(Erro))
    exit()

if user == 1:
    try:
        url1 = input('Cole a URL: ')
        def baixar_video(url1, caminho_destino='.'):
            yt = YouTube(url1)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=caminho_destino)

    except Exception as l:
        erro = (f'{str(l)[14:34]}')
        if erro == 'could not find match':
            print('Erro ao Buscar a url, Tente Novamente')
        else:
            print('Ocorreu Um Erro, Tente Novamente')
        exit()

    if len(linha1) <= 5:
        user_sav = input('Onde Salvar o Video: ')
        print('Por Favor Aguarde...\n')
        caminho_destino = user_sav
        try:
            baixar_video(url1, caminho_destino)
            print(f'Salvo em {caminho_destino}')
        except Exception as erro:
            print('Ocorreu um Erro {}\nTente Novamente'.format(erro))
            exit()
    else:
        arquivo = open('Sav.txt', 'r')
        linha1 = arquivo.readline()
        print('Por Favor Aguarde...')
        filt = len(linha1) - 1
        caminho_destino = linha1[:filt]
        baixar_video(url1, caminho_destino)
        print(f'Salvo em {caminho_destino}')
elif user == 2:
    def Baixar_Audio(url1, caminho_destino='.'):
        try:
            yt = YouTube(url1)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=caminho_destino)
            print('Audio Baixado com Sucesso')
            print(f'Salvo em {caminho_destino}')

        except Exception as e:
            print(f'\nOcorreu um Erro {e}\nTente Novamente')
        exit()

    url1 = input('Cole a URL: ')

    if len(linha2) <= 4:
        user_sav = input('Onde Salvar o Video: ')
        print('Por Favor Aguarde...')
        caminho_destino = user_sav
        Baixar_Audio(url1, caminho_destino)
        print(f'Salvo em {caminho_destino}')
    else:
        arquivo = open('Sav.txt', 'r')
        linha2 = arquivo.readlines()
        #filt = len(linha2) - 1
        #caminho_destino = linha2[:filt]
        caminho_destino = linha2
        #print(linha2[1])
        Baixar_Audio(url1, linha2[1])#caminho_destino)

elif user == 3:
    print('Atenção Caminhos Conforme Video 1 e Audio em 2 Respectivamente')
    while True:
        user = int(input('Videos [1] Audios [2] Voltar [3]\n: '))
        if user == 1:
            while True:
                print('Mostrar Caminho [1]\nRenomear Caminho[2]\nApagar Caminho [3]\nSair [4]')
                user_inter = int(input(': '))

                if user_inter == 1:
                    arquivo = open('Sav.txt', 'r')
                    texto = arquivo.read()
                    arquivo.close
                    if len(texto) == 0:
                        print('Não Foi Encontrado Valores\n')
                    else:
                        print(f'\n{texto}\n')

                elif user_inter == 2:
                    arquivo = open('Sav.txt', 'r')
                    linha11 = arquivo.readline()
                    arquivo.close()

                    def main():
                        arquivo = "Sav.txt"
                        apagar = Apagar(arquivo)
                        apagar.apagar_texto_arquivo(linha11)

                    if __name__ == "__main__":
                        main()

                    novo = input('Novo Caminho : ')
                    arquivo = open('Sav.txt', 'a')
                    linha1 = arquivo.write(f'{novo}\n')
                    arquivo.close()
                    print('Renomeado Com Sucesso\n{} Para {}'.format(linha11, novo))

                elif user_inter == 3:
                    arquivo = open('Sav.txt', 'r')
                    linha11 = arquivo.readline()
                    arquivo.close()

                    def main():
                        arquivo = "Sav.txt"
                        apagar = Apagar(arquivo)
                        apagar.apagar_texto_arquivo(linha11)

                    if __name__ == "__main__":
                        main()

                    arquivo = open('Sav.txt', 'a')
                    arquivo.write('  ')
                    print('Apagado com Sucesso!\n')
                    arquivo.close()

                elif user_inter == 4:
                    print('Voltando...')
                    break
        elif user == 2:
            while True:
                print('\nMostrar Caminho [1]\nRenomear Caminho [2]\nApagar Caminho [3]\nSair [4]')
                user_inter = int(input(': '))

                if user_inter == 1:
                    arquivo = open('Sav.txt', 'r')
                    texto = arquivo.read()
                    if len(texto) == 0:
                        print('Não Foi Encontrado Valores')
                    else:
                        print(texto)
                    arquivo.close
                elif user_inter == 2:
                    arquivo = open('Sav.txt', 'r')
                    linha11 = arquivo.readline(20)
                    linha22 = arquivo.readline(20)
                    arquivo.close()
                    novo = input('Novo Caminho : ')

                    def main():
                        arquivo = "teste.txt"
                        apagar = Apagar(arquivo)
                        apagar.apagar_texto_arquivo(linha22)

                    if __name__ == "__main__":
                        main()

                    arquivo = open('Sav.txt', 'a')
                    linha1 = arquivo.write(f'{novo}')
                    #linha2 = arquivo.readline()
                    #arquivo.writelines(linha2)
                    arquivo.close()
                    print('Renomeado Com Sucesso\n{} Para {}'.format(linha22, novo))

                elif user_inter == 3:
                    arquivo = open('Sav.txt', 'r')
                    linha11 = arquivo.readline(20)
                    linha22 = arquivo.readline(20)
                    arquivo.close()


                    def main():
                        arquivo = "teste.txt"
                        apagar = Apagar(arquivo)
                        apagar.apagar_texto_arquivo(linha22)

                    if __name__ == "__main__":
                        main()

                    print('Apagado com Sucesso!')

                elif user_inter == 4:
                    print('Voltando...')
                    break
        elif user == 3:
            print('Saindo...')
            break
elif user == 4:
    print('Saindo..')
    exit()
