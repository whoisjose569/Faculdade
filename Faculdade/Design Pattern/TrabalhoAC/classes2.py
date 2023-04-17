class Orcamento:
    def __init__(self) -> None:
        self.items = {}
        self.orcamento = 0
        self.estadoAtual = emAprovacao()
    
    def addItem(self, nome, preco):
        self.items [nome] = preco
    
    def mostraItens(self):
        for nome, preco in self.items.items():
            print(f"{nome}: {preco}")
    
    def somaTotal(self):
        self.orcamento = sum(self.items.values())
        return sum(self.items.values())
    
    def realizaCalculo(self, orcamento , imposto):
        impost = imposto.calcula(orcamento)
        print(impost)
    
    def qtdItens(self):
        return len(self.items)
    
    def aplicaDescontoExtra(self):
        self.estadoAtual.aplicaDescontoExtra(self)
    
    def Aprova(self):
        self.estadoAtual.Aprova(self)
    
    def Reprova(self):
        self.estadoAtual.Reprova(self)
    
    def Finaliza(self):
        self.estadoAtual.Finaliza(self)
        
    def temItensDuplicados(self):
        nomes = []
        for nome, preco in self.items.items():
            if nome in nomes:
                return True
            nomes.append(nome)
        return False
    

class calculadorImpostos:
    def realizaCalculo(self ,orcamento , imposto):
        if imposto.nome == 'icms':
            icms = imposto.calcula(orcamento)
            print(f"Valor do Imposto: {icms}")
        if imposto.nome == 'iss':
            iss = imposto.calcula(orcamento)
            print(f'Valor do Imposto: {iss}')
        if imposto.nome == 'pis':
            pis = imposto.calcula(orcamento)
            print(f"Valor do Imposto: {pis}")
        if imposto.nome == 'cofins':
            cofins = imposto.calcula(orcamento)
            print(f"Valor do Imposto: {cofins}")

class Imposto:
    def __init__(self, outroImposto) -> None:
        self._outroImposto = outroImposto
        

    @property
    def outroImposto(self):
        return self._outroImposto
    
    @outroImposto.setter
    def outroImposto(self, outroImposto):
        self._outroImposto = outroImposto
    
    def calcula(self, orcamento):
        pass
    
    def calculoDoOutroImposto(self, orcamento):
        if self._outroImposto is None:
            return 0
        return self._outroImposto.calcula(orcamento)

class ICMS(Imposto):
    def __init__(self, outroImposto=None) -> None:
        super().__init__(outroImposto)
        self.nome = "icms"
        
    
    def calcula(self , orcamento):
        return orcamento.orcamento * 0.06 + self.calculoDoOutroImposto(orcamento)
    
    def calculoDoOutroImposto(self, orcamento):
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)
    

class ISS(Imposto):
    def __init__(self, outroImposto=None) -> None:
        super().__init__(outroImposto)
        self.nome = "iss"

    def calcula(self, orcamento):
        return orcamento.orcamento * 0.1 + self.calculoDoOutroImposto(orcamento)
    
    def calculoDoOutroImposto(self, orcamento):
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)
    

class PIS(Imposto):
    def __init__(self, outroImposto=None) -> None:
        super().__init__(outroImposto)
        self.nome = 'pis'
        
    def calcula(self , orcamento):
        return orcamento.orcamento * 0.16 + self.calculoDoOutroImposto(orcamento)
    
    def calculoDoOutroImposto(self, orcamento):
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)

class COFINS(Imposto):
    def __init__(self, outroImposto=None) -> None:
        super().__init__(outroImposto)
        self.nome = 'cofins'
    
    def calcula(self , orcamento):
        return orcamento.orcamento * 0.02 + self.calculoDoOutroImposto(orcamento)
    
    def calculoDoOutroImposto(self, orcamento):
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)

class Desconto:
    def desconta(orcamento):
        pass
    
    @property
    def proximo(self):
        pass
    
    @proximo.setter
    def proximo(self, proximo):
        pass
    
        
class desconto5itens(Desconto):   
    @property
    def proximo(self):
        pass
    
    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo
    
    def desconta(self, orcamento):
        if orcamento.qtdItens() > 5:
            print(f'Baseado na quantidade de itens Desconto de : {orcamento.somaTotal() * 0.1}')
            return orcamento.somaTotal() * 0.1
        return self._proximo.desconta(orcamento)

class descontoMais500Reais(Desconto):
    @property
    def proximo(self):
        pass

    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo

    def desconta(self, orcamento):
        if orcamento.somaTotal() >= 500:
            print(f'Baseado no valor total Desconto de: {orcamento.orcamento * 0.07}')
            return orcamento.orcamento * 0.07
        return self._proximo.desconta(orcamento)


class semDesconto(Desconto):
    @property
    def proximo(self):
        pass

    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo
    def calcula(orcamento):
        print('Sem Desconto')
        return 0    
        
class calculadorDescontos:
    def calcula(self, orcamento):
        d1 = desconto5itens()
        d2 = descontoMais500Reais()
        
        d1.proximo = d2
        
        return d1.desconta(orcamento)

class estadoDeUmOrcamento:
    def aplicaDescontoExtra(self, orcamento):
        pass
    
    def Aprova(self, orcamento):
        pass
    
    def Reprova(self, orcamento):
        pass
    
    def Finaliza(self, orcamento):
        pass

class emAprovacao(estadoDeUmOrcamento):
    def aplicaDescontoExtra(self, orcamento):
        orcamento.orcamento -= orcamento.orcamento * 0.05
    
    def Aprova(self, orcamento):
        orcamento.estadoAtual = Aprovado()
    
    def Reprova(self, orcamento):
        orcamento.estadoAtual = Reprovado()
    
    def Finaliza(self, orcamento):
        raise Exception("Orcamento em aprovação não podem ir para finalizado diretamente")

class Aprovado(estadoDeUmOrcamento):
    def aplicaDescontoExtra(self, orcamento):
        orcamento.orcamento -= orcamento.orcamento * 0.02
    
    def Aprova(self, orcamento):
        raise Exception("Orçamento já está em estado de aprovação")

    def Reprova(self, orcamento):
        raise Exception("Orçamento está em estado de aprovação e não pode ser reprovado")
    
    def Finaliza(self, orcamento):
        orcamento.estadoAtual = Finalizado()

class Reprovado(estadoDeUmOrcamento):
    def aplicaDescontoExtra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra!")
    
    def aprova(self, orcamento):
        raise Exception("Orçamentos reprovados não podem ser aprovados")
        
    def reprova(self, orcamento):
        raise Exception("Orçamento já está reprovado")
        
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(estadoDeUmOrcamento):
    def aplicaDescontoExtra(self, orcamento):
        raise Exception("Orçamentos finalizados não recebem desconto extra!")

    def aprova(self, orcamento):
        raise Exception("Orçamentos finalizados não podem ser aprovados")
        
    def reprova(self, orcamento):
        raise Exception("Orçamentos finalizados não podem ser reprovados")
        
    def finaliza(self, orcamento):
        raise Exception("Orçamento já está finalizado")

class templateDeImpostoCondicional(Imposto):
    def calcula(self, orcamento):
        if(self.deveUsarMaximaTaxacao(orcamento)):
            return self.maximaTaxacao(orcamento)
        else:
            return self.minimaTaxacao(orcamento)

    def deveUsarMaximaTaxacao(self, orcamento):
        pass
    
    def maximaTaxacao(self, orcamento):
        pass
    
    def minimaTaxacao(self, orcamento):
        pass

class IKCV(templateDeImpostoCondicional):
    def deveUsarMaximaTaxacao(self, orcamento):
        return orcamento.orcamento > 500 and self.temItemMaiorQue100ReaisNo(orcamento)
    
    def maximaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.10
    
    def minimaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.06
    
    def temItemMaiorQue100ReaisNo(self, orcamento):
        for item, valor in self.items.items():
            if valor > 100:
                return True
        return False

class ICPP(templateDeImpostoCondicional):
    def deveUsarMaximaTaxacao(self, orcamento):
        return orcamento.orcamento >= 500
    
    def maximaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.07
    
    def minimaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.05
    

class IHIT(templateDeImpostoCondicional):
    def deveUsarMaximaTaxacao(self, orcamento):
        if orcamento.temItensDuplicados():
            return orcamento.orcamento * 0.13 + 100
        else:
            return orcamento.qtdItens()* 0.01
        
    def maximaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.09
    
    def minimaTaxacao(self, orcamento):
        return orcamento.orcamento * 0.02


