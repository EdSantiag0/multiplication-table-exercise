print('\033[1;32;40m-==-==-==- TESTE DE TABUADA!!! -==-==-==-\033[m')
from random import randint
quant = comp1 = comp2 = cont = resp = ponto = 0
quant = int(input('Digite quantas questões deseja responder? '))
while cont != quant:
    comp1 = randint(0, 10)
    comp2 = randint(0, 10)
    resp = int(input('{} X {} = '.format(comp1, comp2)))
    soma = comp1 * comp2
    cont += 1
    if resp == soma:
        print('\033[34mAcertou!\033[m')
    elif resp != soma:
        print('\033[31mErrou!\033[m a respota era {}'.format(soma))
    if resp == soma:
        ponto += 1
print('De {} questões você certou {}'.format(quant, ponto))
media = quant - ponto
if quant == ponto:
    print('PARABÉNS! você acertou todas')
elif media <= quant/2:
    print('Muito Bem! você ficou na média')
else:
    print('Precisa estudar mais')