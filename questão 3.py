import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analise_de_compras(x):
    # Declaração de variáveis a serem usadas
    minimo = np.inf
    maximo = -1 * minimo
    media = 0
    produtoMaisCaro = {}
    produtoMaisBarato = {}
    linhas, _ = x.shape

    # Vai linha a linha da tabela
    for i in range(linhas):
        valor = x.iat[i,5]
        media += valor

        # Verifica se é o maior valor encontrado
        if (valor > maximo):
            maximo = valor
            produtoMaisCaro = { x.iat[i, 4] }
        # Se tiver o mesmo valor do produto mais caro, ele vai aparecer nos resultados
        elif (valor == maximo):
            produtoMaisCaro.add(x.iat[i, 4])

        # Verifica se é o menor valor encontrado
        if (valor < minimo):
            minimo = valor
            produtoMaisBarato = { x.iat[i, 4] }
        # Se tiver o mesmo valor do produto mais barato, ele vai aparecer nos resultados
        elif (valor == minimo):
            produtoMaisBarato.add(x.iat[i, 4])

    # Calcula a média
    media = media / linhas

    return (media, minimo, maximo, produtoMaisBarato, produtoMaisCaro)

def segmentacao_por_genero(x):
    # Declaração de variáveis a serem usadas
    total = dict()
    linhas, _ = x.shape

    # Vai linha a linha
    for i in range(linhas):
        valor = x.iat[i,5]
        genero = x.iat[i,2]

        # Caso tenha encontrado um novo gênero
        if (genero not in total.keys()):
            total[genero] = [0, 0]

        # Soma o valor ao total do gênero e adiciona ao número de usuários de um gênero
        total[genero][1] += valor
        total[genero][0] += 1


    return total



if __name__ == '__main__':

    data = pd.read_json('dados_compras.json')

    if (np.where(pd.isnull(data))[0].size == 0):
        analise = analise_de_compras(data)
        segmentacao = segmentacao_por_genero(data)

        print("Análise de compras: ")
        print("Média de preços: ", analise[0])
        print("Produto mais barato: ", analise[3], " - $", analise[1])
        print("Produto mais caro: ", analise[4], " - $", analise[2])
        print()

        print("Segmentação por gênero:")
        print("Total gasto por homens: ", segmentacao['Masculino'][1])
        print("Total gasto por mulheres: ", segmentacao['Feminino'][1])
        print("Total gasto por outros: ", segmentacao['Outro / Não Divulgado'][1])


        y = np.array([segmentacao['Masculino'][0], segmentacao['Feminino'][0], segmentacao['Outro / Não Divulgado'][0]])
        mylabels = segmentacao.keys()

        plt.pie(y, labels = mylabels)
        plt.title('Distribuição por gênero')
        plt.show()