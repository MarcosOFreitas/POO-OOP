
#TODO: Programação Orientada a Objetos (POO) em Python
# A POO é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes.
# Os principais pilares da POO são: Classes e Objetos, Encapsulamento, Herança, Polimorfismo, Abstração e Composição.

#? 1. Classes e Objetos
# Uma classe é como um molde que define as características (atributos) e comportamentos (métodos) de um objeto.
# Um objeto é uma instância de uma classe, ou seja, um elemento criado a partir desse molde.

class Carro:
    def __init__(self, marca, modelo, cor, ano):
        # Atributos que definem as características do carro
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_info(self):
        print(f"\nMarca: {self.marca}; \nModelo: {self.modelo};\nCor: {self.cor};\nAno: {self.ano}")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", "Preto", "2024")
meu_carro.exibir_info()

#? 2. Encapsulamento
# O encapsulamento é a prática de proteger os dados de uma classe, tornando-os privados.
# Isso é feito usando atributos e métodos privados (prefixados com "__"), que só podem ser acessados dentro da classe.

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def ver_saldo(self):
        return self.__saldo

# Exemplo de uso do encapsulamento
conta = ContaBancaria(1000)
conta.depositar(500)
print(f"Saldo atual: {conta.ver_saldo()}")

#? 3. Herança
# A herança permite que uma classe (classe filha) herde atributos e métodos de outra classe (classe pai).
# Isso promove a reutilização de código e facilita a extensão de funcionalidades.

class Veiculo:
    def __init__(self, rodas):
        self.rodas = rodas

    def exibir_rodas(self):
        print(f"Este veículo tem {self.rodas} rodas.")

class Carro(Veiculo):
    def __init__(self, rodas, marca):
        super().__init__(rodas)  # Chama o construtor da classe pai
        self.marca = marca

    def exibir_info(self):
        print(f"Carro da marca {self.marca} com {self.rodas} rodas.")

# Exemplo de herança
carro = Carro(4, "Honda")
carro.exibir_info()

#? 4. Polimorfismo
# O polimorfismo permite que diferentes classes tenham métodos com o mesmo nome, mas comportamentos distintos.
# Isso facilita o uso de funções genéricas que podem trabalhar com diferentes tipos de objetos.

class Passaro:
    def falar(self):
        print("Piu")

class Gato:
    def falar(self):
        print("Miau")

def som_animal(animal):
    animal.falar()

# Exemplo de polimorfismo
passaro = Passaro()
gato = Gato()

som_animal(passaro)  # Saída: Piu
som_animal(gato)     # Saída: Miau

#? 5. Abstração
# A abstração é o processo de esconder detalhes complexos e expor apenas o essencial.
# Em Python, isso pode ser feito usando classes base abstratas (ABC - Abstract Base Classes).

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Exemplo de abstração
retangulo = Retangulo(5, 10)
print(f"Área do retângulo: {retangulo.calcular_area()}")

#? 6. Composição
# A composição é uma relação "tem-um", onde uma classe contém objetos de outra classe como parte de seus atributos.
# Isso promove a modularidade e reutilização de código.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def exibir_potencia(self):
        print(f"Potência do motor: {self.potencia} cavalos.")

class CarroComMotor:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # Composição: o carro "tem um" motor

    def exibir_info(self):
        print(f"Carro da marca {self.marca}")
        self.motor.exibir_potencia()

# Exemplo de composição
motor = Motor(150)
carro = CarroComMotor("Ford", motor)
carro.exibir_info()