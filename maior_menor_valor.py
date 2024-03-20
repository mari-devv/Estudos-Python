primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor <= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'que {primeiro_valor=}'
    )