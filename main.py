import colorsys

print("Olá mundo!")
# idade = int(input("Fala sua idade ai?"))
# print("A sua idade é : %i" %idade);
# nasci = 2022 - idade;
# print("vove nasce em %i" %nasci);
# print(type(idade))
# print(type(nasci))
# fruta = "Manga";
# nome = "Carlos alberto";
# print("Sua fruta favorita é {} acertei né e o seu nome é {} acertei de novo né".format(fruta, nome) );


#print("Oi Vamos saber se você ja pode tirar sua cnh? ")
#nome = input("Informe seu nome: ")
#idade = int(input("Digite sua idade: "))
#
#if(idade < 18):
#    print("Você não possui idade ainda sr.{0} sua idade é {1}".format(nome, idade));
#elif(idade >= 18):
#    print("Você possui idade para tirar sua cnh sr.{0} sua idade é {1}".format(nome, idade));



#    print("Vamos calcular o fatorial de um numero")
#    numero = int(input("Digite um numero: "))
#    fatorial = numero;
#    contator = 1;
#    while (numero-contator)>1:
#        fatorial = fatorial*(numero-contator)
#        contator += 1
#        print("O fatorial de {0} = {1} = {2}".format(numero, fatorial, contator))
#
#
#def parabens():
#    print(' Parabéns para você\n Nessa data querida\n Muitas felicidades\n Muitos anos de vida')
#
#parabens()
#
#def temLetraU():
#    frase = input("Digite uma frase: ")
#    if 'u' in frase:
#        print('Você utilizou a letra U')
#    else:
#        print('Você não utilizou a letra U')
#temLetraU()
#
#def somaQuadrados(a, b):
#    somaQ = a**2 + b**2
#    return somaQ
#
#print(somaQuadrados(2, 3))

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
musicas = ('Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
indice = np.arange(len(musicas))
acessos = [1068254, 866216, 849895, 763652, 758198]
plt.bar(indice, acessos)
plt.xticks(indice, musicas, color='red')
plt.ylabel('Acessos')
plt.title('Ranking do Spotify 31.dez.2019')
plt.show()








    


