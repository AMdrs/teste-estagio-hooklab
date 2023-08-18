def main(x):
    # Declaração de variáveis para evitar programar um primeiro caso específico
    # Dependendo da fonte dos dados, será necessário mudar os valores das 2 últimas variáveis
    media = 0
    piorNota = 100000.0
    melhorNota = -100000.0

    for i in x:
        # Soma as notas para calcular a média depois
        media += i["avaliacao"]

        # Busca o melhor filme
        if (i["avaliacao"] > melhorNota):
            melhorNota = i["avaliacao"]
            melhorFilme = [ i["titulo"] ]
        # Caso 2 ou mais filmes tenham a mesma nota, ambos aparecem no resultado
        elif (i["avaliacao"] == melhorNota):
            melhorFilme.append(i["titulo"])

        # busca o ano com o pior filme
        if (i["avaliacao"] < piorNota):
            piorNota = i["avaliacao"]
            piorAno = [ i["ano"] ]
        # Caso 2 ou mais filmes tenham a mesma nota, ambos os anos de lançamento aparecem no resultado
        elif (i["avaliacao"] == piorNota):
            piorAno.append(i["ano"])

    # Calcula a média
    media = media / len(x)

    return (media, melhorFilme, piorAno)

if __name__ == '__main__':

    # Lista de filmes
    filmes = [
        {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
        {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
        {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
    ]

    # Chamada de função
    mediaNotas, melhorFilme, piorFilmeAno = main(filmes)

    # Mostra os resultados
    print("Média das notas: ", mediaNotas)
    print("Melhores Filmes: ", melhorFilme)
    print("Anos com o pior lançamento: ", piorFilmeAno)