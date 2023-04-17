#José Vitor de Araujo - 603317
#Isabelle Sepulveda - 603821
from classes2 import *
from classes3 import *

iss = ISS()
icms = ICMS()
pis = PIS()
cofins = COFINS()

t = Orcamento()
t.addItem('Calça', 500)

#calculador = calculadorImpostos()
#calculador2 = calculadorDescontos()


#t.mostraItens()
#print(f'Valor TOTAL: {t.somaTotal()}')
#calculador.realizaCalculo(t , icms)
#calculador.realizaCalculo(t , iss)
#calculador.realizaCalculo(t , pis)
#calculador.realizaCalculo(t , cofins)

#desconto = calculador2.calcula(t)
#print(desconto)
#impostoComplexo = ISS(PIS())
#valor = impostoComplexo.calcula(t)
#print(valor)

#t.aplicaDescontoExtra()
#print(t.orcamento)
#t.Aprova

#t.aplicaDescontoExtra()
#print(t.orcamento)

#t.Finaliza()

''' criador = notaFiscalBuilder()
criador.paraEmpresa('UNIVEM')
criador.comCnpj("123.456.789/0001-10")

criador.comItem(ItemDaNota('item 1', 100))
criador.comItem(ItemDaNota('item 2', 200))
criador.comItem(ItemDaNota('item 3', 300))
criador.comObservacoes('entregar nf pessoalmente')
criador.naDataAtual()

nf = criador.constroi()'''

nf = notaFiscalBuilder().paraEmpresa('UNIVEM').comCnpj('123.456.789/0001-10').comItem(ItemDaNota("item 1", 100)).comItem(ItemDaNota("item 2", 200)).comObservacoes('entregar nf pessoalmente').naDataAtual().constroi()
























