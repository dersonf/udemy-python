#!/usr/bin/python3.6
# Quantos porcentos do salario esta comprometido com despesa?

salario = float(input('\nQual e o salario ? :'))
despesas = float(input('Quanto esta comprometido (despesas)? :'))
porcentagem = float((despesas * 100) / salario)

print(f'\nSeu salario esta comprometido em {porcentagem}%\n')

