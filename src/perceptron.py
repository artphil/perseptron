"""
Classe Perceptron
"""


class Perceptron():

    epocas = 0

    contador = 0

    aprendizado = {}

    # Executa o teste
    def perceptron_execute(w):
        # 
        saida =

    # Treina o perceptor
    def perceptron_train(data):
        # Para cada epoca
        for i in range(epocas):
            # Para cada entrada
            for j in range(len(data)):
                resultado = int(data[i][0])
                w = data[i][1:]
                # Executa o teste de spam
                saida = perceptron_execute(w, data)

                if saida != data[i][0]:
                    novoPeso(i, saida)
                    treinou = false

            contador += 1

    if treinou == false & & contador < epocas
    perceptron_train(data)

    # Testa o
    def perceptron_test(w, data):
        ocorrencias = 0

        for i in range(1, len(data)):

        somarorio = (data[0] * w[0]) + (data[1] * w[1]) + ((-1) * w[2])

        if somarorio >= 0:
            return 1

        return 0

    def novoPeso(i, saida):
        w[0] = w[0] + (1 * (aprendizado[i][2] - saida) * aprendizado[i][0])
        w[1] = w[1] + (1 * (aprendizado[i][2] - saida) * aprendizado[i][1])
        w[2] = w[2] + (1 * (aprendizado[i][2] - saida) * (-1))
