class Pessoa:
    # Atributos
    __nome = 'Márcio'
    _idade = 35
    
    # Getters e Setters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    # Construtor
    def __init__(self,nome,idade):
        self.__nome = nome
        self._idade = idade
    
    # Métodos
    def exibir(self):
        print(self.__nome)
        print(self._idade)