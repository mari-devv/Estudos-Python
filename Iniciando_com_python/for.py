"""
Utilizamos "while"" quando não sabemos quantas repetições vão ter
while = enquanto
"""
"""
Utilizamos o "for" quando sabemos a quantas repetições vão ter
para = for
"""
texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

