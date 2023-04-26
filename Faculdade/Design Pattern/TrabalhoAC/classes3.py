import datetime
class ItemDaNota:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
class notaFiscal:
    def __init__(self, razaoSocial, cnpj, data, valorTotal, impostos, todosItens, observacoes):
        self.razaoSocial = razaoSocial
        self.cnpj = cnpj
        self.data = data
        self.valorTotal = valorTotal
        self.impostos = impostos
        self.todosItens = todosItens
        self.observacoes = observacoes
        
class notaFiscalBuilder:
    def __init__(self) -> None:
        self._razaoSocial = ''
        self._cnpj = ''
        self._valorTotal = 0
        self._impostos = 0
        self.data = ''
        self.observacoes = ''
        self._todosItens=[]
        self.todasAcoesASeremExecutadas=[]
    
    def AdicionaAcao(self, novaAcao):
        self.todasAcoesASeremExecutadas.append(novaAcao)
        
    @property
    def razaoSocial(self):
        return self._razaoSocial
    
    @property
    def cnpj(self):
        return self._cnpj
    
    def paraEmpresa(self, razaoSocial):
        self._razaoSocial = razaoSocial
        return self
    
    def comCnpj(self, cnpj):
        self._cnpj = cnpj
        return self
    
    def comObservacoes(self, observacoes):
        self.observacoes = observacoes
        return self
    
    def naDataAtual(self):
        self.data = datetime.datetime.now()
        return self
        
    def comItem(self, item):
        self._todosItens.append(item)
        self._valorTotal += item.valor
        self._impostos += item.valor * 0.05
        return self

    def constroi(self):
        notaFiscal = (self.razaoSocial, self.cnpj, self._valorTotal, self._impostos, self.data, self.observacoes)
        
        for acao in self.todasAcoesASeremExecutadas:
            acao.executa(notaFiscal)

        return notaFiscal
    
class acaoAposGerarNota:
    def executa(self, notaFiscal):
        pass

class enviadorDeEmail(acaoAposGerarNota):
    def executa(self, notaFiscal):
        print('Enviando por e-mail')

class notaFiscalDao(acaoAposGerarNota):
    def executa(self, notaFiscal):
        print('Salvando no banco')

class enviadorDeSms(acaoAposGerarNota):
    def executa(self, notaFiscal):
        print('Enviando por SMS')

class impressora(acaoAposGerarNota):
    def executa(self, notaFiscal):
        print('Imprimindo Nota Fiscal')

