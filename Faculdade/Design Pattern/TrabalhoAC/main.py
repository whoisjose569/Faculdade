#José Vitor de Araujo - 603317
#Isabelle Sepulveda - 603821
from classes2 import *
from classes3 import *

builder = notaFiscalBuilder()
builder.AdicionaAcao(enviadorDeEmail())
builder.AdicionaAcao(notaFiscalDao())
builder.AdicionaAcao(enviadorDeSms())
builder.AdicionaAcao(impressora())

nf = notaFiscalBuilder().paraEmpresa('UNIVEM').comCnpj('123.456.789/0001-10').comItem(ItemDaNota("item 1", 100)).comItem(ItemDaNota("item 2", 200)).comObservacoes('entregar nf pessoalmente').naDataAtual().constroi()