"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        self.array = array_para_ordenar
        """Recebe o array com o conteudo a ser ordenado"""

    def ordena(self):
        array = self.array
        tamanho_do_array = len(array)
        
        for i in range(tamanho_do_array-1):
            for j in range(tamanho_do_array-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def toString(self):
        array = self.ordena()
        array_ordenado_string = ''
        for i in range(len(array)):
            if i == len(array)-1:
                array_ordenado_string += str(array[i])
            else:
                array_ordenado_string += str(array[i])+', '
        
        return array_ordenado_string

array = [255, 1, 9, 8, 0, 7, 7, 6, 3]        
ordenacao_instance = Ordenacao(array)
print(ordenacao_instance.toString())