
class Conta:

    def __init__(self, cliente, saldo):

        self.titular = cliente
        self.__saldo = saldo
        self.historico = []

    property
    def saldo(self):
        return self.__saldo

    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append(f'Depósito de {valor}')
            print("Depósito: R$", valor)
            print("Saldo total", self.__saldo)
            print('*'*15)
        else:
            print("Erro! Você precisa depositar alguma quantia.")
            print('*'*15)

    def sacar(self, valor):
        if self.__saldo - valor < 0:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor
            self.historico.append(f'Saque de {valor}')
            print("Saque: R$", valor)
            print("Saldo atual: R$", self.__saldo)


    def consulta_saldo(self):
        return self.__saldo

class ChequeEspecial(Conta):
    def __init__(self, cliente, saldo):
        Conta.__init__(self, cliente, saldo):
        self._limite = cliente.renda
        self.__saldo_especial = saldo


    def saldo(self, saque):
        self.__saldo_especial = self._limite - saque
        return self.__saldo_especial

    def sacar(self):
        valor = float(input('Digite o valor do saque na conta especial: '))
        if self._limite > 0:
            print('Saque realizado.')
            self.__saldo_especial -= valor
            return self.__saldo_especial

        else:
            print('Limite ultrapassado')
    
    
    def mostrarSaldo(self):

        print(f'Limite disponivel no cheque especial: {self.limite}, valor disponivel para saque {self.__saldo_especial}')

    def __str__(self)-> str:
        return f"limite: {self.limite}  \nsaldo: R$ {self.__saldo_especial}"


class Cliente:

    def __init__(self, nome, renda, telefone, sexo):
        self.__nome = nome
        self.__renda = renda
        self.__telefone = telefone
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def renda(self):
        return self.__renda
    
    @property
    def sexo(self):
        return self.__sexo

    def __str__(self)-> str:
        return f"Nome: {self.__nome}  \nRenda: R$ {self.__renda}  \nTelefone: {self.__telefone} \nSexo: {self.__sexo}"






cliente1 = Cliente('Raquel Domingos', 5000, '383747', 'F')
print(cliente1)

if cliente1.sexo == "f"
    conta1 = ChequeEspecial(cliente1, 100)
    print('colocando 100 reais na conta e consultando saldo')
    print(conta1.consulta_saldo())
else
    conta1 = Conta(cliente1, 100)

print('depositando 1000 reais e conferindo o saldo')
conta1.depositar(1000)

print(conta1.saldo())
print('sacando 50 reais, depositando mais 1200, e sacando 500')
conta1.sacar(50)
conta1.depositar(1000)
conta1.depositar(200)
conta1.sacar(500)
print(conta1.historico)

conta1.sacar(2000)
ce.sacar()