# yield usado para grandes volumes de dados e vc nao precisar importar toda a informação ocupando assim a memória

def ler_csv(nome_arquivo):
	for linha in open(nome_arquivo, 'r'):
		yield linha
	# Para a situação acima podemos abreviar para o codigo abaixo
	# yield from open(nome_arquivo, 'r')


# Nao é gerado uma lista que vai ocupar a memoria e sim um gerador
vendas = ler_csv('vendas.csv')
print(vendas) # <generator object ler_csv at 0x7f9f6c0b5b50>
	
# Forma de uso mais comum do gerador dentro de um loop
for venda in vendas:
	print(venda)


