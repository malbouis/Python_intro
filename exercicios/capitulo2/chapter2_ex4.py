livro = 24.95
desconto = 0.4
preco_livro_unitario = livro*desconto
numero_total_livros = 60
primeiro_frete = 3.0
outros_fretes = 0.75

frete_total = (numero_total_livros - 1)*outros_fretes + primeiro_frete
custo_total_livros = preco_livro_unitario*numero_total_livros

custo_total = frete_total + custo_total_livros

print('O custo total da compra de 60 livros eh de ', custo_total, 'reais.')
print('O custo total da compra de 60 livros eh de {0:.5g} reais'.format(custo_total))
