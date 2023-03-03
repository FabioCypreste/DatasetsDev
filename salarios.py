#Primeiramente, faça o download do dataset1.

dataset1 = np.load('dataset1.npy')
dataset1[:5, :]

while True:
    f1 = int(input("Você deseja saber qual filtro? [1- Salários mínimos para salários dos Devs / 2- Amplitude Total / 3- Média salarial / 4 - Folha de pagamento / 5 - Lista de desenvolvedores]"))
    if f1 < 0 or f1 > 5:
        print('Por favor, selecione uma opção válida.')
    elif f1 == 1:
        print('Lista dos desenvolvedores com salário mais altos em salários minimos')
        for indice, sala in enumerate(datasetsala[:-6:-1,:]):
          print(f'Desenvolvedor {indice + 1}:')
          print(f'Matrícula: {sala[0]: .0f}')
          print(f'Salário(em salários mínimos): {(sala[1]/1112): .2f}')
          print(f'--------------------------------------------------------------')
        print('\n')
        print('Lista dos desenvolvedores com salário mais baixo em salários minimos')
        for indice, sala in enumerate(datasetsala[:5:,:]):
          print(f'Desenvolvedor {indice + 1}:')
          print(f'Matrícula: {sala[0]: .0f}')
          print(f'Salário(em salários mínimos): {(sala[1]/1112): .2f}')
          print(f'--------------------------------------------------------------')
    elif f1 == 2:
        salmin = dataset1[:,1]/1112
        print('A amplitude dos salários em reais:')
        print(f'{(np.max(dataset1[:,1]) - np.min(dataset1[:,1])): .2f} Reais')
        print('A amplitude em Salários minimos')
        print(f'{(np.max(salmin) - np.min(salmin)): .2f} Salário minimos')
    elif f1 == 3:
        print('A média dos 100 maiores salários do estado:')
        print(f'{np.mean(datasetsala[:-101:-1,:]): .2f}')
    elif f1 == 4:
        desc = dataset1[:,2] == 1
        comPlano = dataset1[desc,:]
        semPlano = dataset1[~(desc),:]
        comPlano[:,1] =  comPlano[:,1] - (comPlano[:,1] * 0.02) + comPlano[:,1] * 0.01 * comPlano[:,3]
        semPlano[:,1] =  semPlano[:,1] + semPlano[:,1] * 0.01 * semPlano[:,3] 
        print(f'A folha de pagamento total da empresa é de:{np.sum(comPlano[:,1]) + np.sum(semPlano[:,1]): .2f} R$')
    elif f1 == 5:
        print('Lista dos desenvolvedores')
        for indice, dev in enumerate(dataset1):
            print(f'Desenvolvedor {indice + 1}:')
            print(f'Matrícula: {dev[0]: .0f}')
            print(f'Salário: {dev[1]: .2f}')
            print(f'Plano de saúde: {dev[2]: .0f}')
            print(f'Dependentes: {dev[3]: .0f}\n')