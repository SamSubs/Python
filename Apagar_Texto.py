class Apagar:
    def __init__(self, arquivo):
        self.arquivo = arquivo
    def apagar_texto_arquivo(self, texto_para_apagar):
        # Ler o conteúdo do arquivo
        with open(self.arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Remover o texto específico das linhas
        linhas_modificadas = [linha.replace(texto_para_apagar, '') for linha in linhas]

        # Sobrescrever o arquivo com o novo conteúdo
        with open(self.arquivo, 'w') as arquivo:
            arquivo.writelines(linhas_modificadas)

    # Exemplo de uso
    # nome_arquivo = 'arquivo.txt'
    # texto_para_apagar = 'Texto a ser apagado'

    # Chamar a função para apagar o texto do arquivo
    #apagar_texto_arquivo(nome_arquivo, texto_para_apagar)
