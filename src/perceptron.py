import string

"""
Classe Perceptron
"""


class Perceptron():

    epocas = 5

    contador = 0

    aprendizado = {}

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

        for j in range(len(data)):
            resultado = int(data[i][0])
            linha = data[i][1:]
            # Executa o teste de spam
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

    i = 0
    while treino and i < 1000 :
        linha = string.split(treino.readline())
        print linha
        data_train[i:i][:] = linha
        print "add %d" % i
        i += 1

    #for j in range(100) :
    print data_train

    perceptron = Perceptron()

    w = perceptron.perceptron_train(data_train)

    teste = open('spam_test.txt', 'r')
    data_test = []
'''
    i = 0
    while teste :
        data_test[i:i] = teste.readline()
        i += 1

    perceptron.perceptron_test(w, data_train)
'''
