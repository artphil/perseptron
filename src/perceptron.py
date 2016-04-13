import string
from collections import Counter

"""
Classe Perceptron
"""


class Perceptron():

    testes = 4000   # Numero de testes a considerar
    pesos = list()  # Peso de aprendizagem
    ocorrencias = Counter()
    lista_palavras = set()
    resultados = list()
    matriz = list()

    # Construtor que iinicializa um w ja treinado
    def __init__ (self, *treino) :

        pass

    # cria a lista de palavras que mais repetem
    def pega_palavras (self, data) :
        # lista de palavras unicas
        linha = list()
        emails = list()

        for i in range(self.testes) :
            palavras = set()
            linha = string.split(data.readline())

            self.resultados.append(int(linha[0]))
            emails.append(linha)
            for item in linha[1:] :
                palavras.add(item)

            for item in palavras :
                self.ocorrencias[item] += 1
                if self.ocorrencias[item] >= 30 :
                    self.lista_palavras.add(item)

        return emails

    def treino (self, data) :
        emails = self.pega_palavras (data)
        lista_palavras = list(self.lista_palavras)

        for i in range(self.testes) :
            incidencia = [0] * len(lista_palavras)
            for item in emails[i] :
                if item in lista_palavras :
                    indice = lista_palavras.index(item)
                    incidencia[indice] = 1

            self.matriz.append((self.resultados[i], incidencia[:]))

        print self.matriz


    # Executa o teste
    def perceptron_execute(w, linha) :
        # Teste para cada linha

        tamanho = len(linha)
        for i in range(0, tamanho) :
            if w.has_key(linha[i]) :
                if w[linha[i]] > 0 :
                    spam += 1

        print "spam %d \nn palav %d \nrazao %f" % (spam, tamanho, float(spam)/tamanho)
        return float(spam) / tamanho

    # Treina o perceptor
    def perceptron_train(data):
        # Para cada epoca
        w = {}

        print "W inicial = " + w

        ##for j in range(len(data)):
        i = 0
        while data and i < 1000 :
            linha = string.split(data.readline())
            print linha
            print "treino %d" % i
            i += 1
            resultado = int(linha[0])
            del linha[0]
            saida = perceptron_execute(w, linha)

            if saida != resultado:
                novoPeso(w, linha, saida)

                print "Novo W = " + w

        return w
    # Testa a entrada no perceptron
    def perceptron_test(w, data):

        contador = 0
        for j in range(len(data)):
            resultado = int(data[i][0])
            linha = data[i][1:]
            # Executa o teste de spam
            saida = perceptron_execute(w, linha)

            if saida != resultado:
                contador += 1

            print "Contados %d " % contador
            print  "Razao %d "% contador / len(data)
        return contador / len(data)

    def mudaPeso(w, linha, saida):
        for i in range(0, len(linha)):
            if saida > 0 :
                w[linha[i]] += 1
            elif w.has_key(linha[i]) :
                if w[linha[i]] > 0 :
                    aprendizado[w[i]] -= 1
            else :
                w[linha[i]] = 0

        print "Novo W = " + w

"""
Programa principal
"""

if __name__ == "__main__":

    treino = open('spam_train.txt', 'r')
    data_train = []

    """i = 0
    while treino and i < 1000 :
        linha = string.split(treino.readline())
        print linha
        data_train[i:i][:] = linha
        print "add %d" % i
        i += 1"""

    #for j in range(100) :
    print data_train

    perceptron = Perceptron()

    # w = perceptron.perceptron_train(treino)
    words = perceptron.treino(treino)

    print perceptron.lista_palavras
    print "numero de palavras = %d " % len(perceptron.lista_palavras)
    treino.close()
'''
    teste = open('spam_test.txt', 'r')
    data_test = []

    i = 0
    while teste :
        data_test[i:i] = teste.readline()
        i += 1

    perceptron.perceptron_test(w, data_train)
'''
