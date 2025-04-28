# Programação Orientada a Objetos (POO) em Python

Este projeto é um guia prático e comentado sobre os principais pilares da Programação Orientada a Objetos (POO) utilizando a linguagem **Python**.

O conteúdo é dividido em seis seções principais:  
**Classes e Objetos, Encapsulamento, Herança, Polimorfismo, Abstração e Composição**.

---

## 📚 Conteúdo

### 1. Classes e Objetos
- Definição de uma **classe** `Carro`.
- Criação de **objetos** a partir da classe.
- Uso de atributos e métodos para exibir informações do objeto.

### 2. Encapsulamento
- Definição de atributos **privados** (`__saldo`) na classe `ContaBancaria`.
- Métodos públicos para **depositar valores** e **consultar saldo**, protegendo o acesso direto aos dados.

### 3. Herança
- Criação de uma **classe base** `Veiculo`.
- Criação de uma **classe derivada** `Carro` que herda atributos e métodos da classe `Veiculo`.
- Utilização da função `super()` para acessar a classe pai.

### 4. Polimorfismo
- Definição de múltiplas classes (`Passaro` e `Gato`) com métodos `falar` de mesmo nome, mas comportamentos diferentes.
- Uso de uma função genérica `som_animal` para chamar o método `falar`, demonstrando polimorfismo.

### 5. Abstração
- Uso do módulo `abc` para criar uma **classe abstrata** `Forma`.
- Definição de um **método abstrato** `calcular_area`.
- Implementação de uma subclasse `Retangulo` que concretiza o método abstrato.

### 6. Composição
- Criação de uma classe `Motor` representando a potência de um motor.
- Criação de uma classe `CarroComMotor`, que contém um objeto `Motor` como um dos seus atributos, demonstrando a relação de **composição**.
