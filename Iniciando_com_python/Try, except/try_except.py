"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que você digitar: '
)
#quando o try "erra", cai direto no except
# serve para capturar erros na exeção
try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
    
except:
    print('Isso não é um número')



#isdigit checa se o usuário digitou apenas números
#if numero_str.isdigit():
#   
#else:
#   