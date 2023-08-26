class Series:
    # calculando o o valor do n-nésimo termo da sequencia de Fibonacci utilizando recursividade
    # usei o decorator @staticmethod pois este é um método que não necessita necessariamente de uma instancia
    @staticmethod
    def fibonacci(n:int):
        if n <= 0:
            return 0

        elif n == 1:
            return 1

        else:
            return Series.fibonacci(n-1) + Series.fibonacci(n-2)
    # calculando o fatorial de um número usando recursividade, também um método estático por não depender de uma instancia
    @staticmethod
    def factorial(n:int):
        if n == 0 or n == 1:
            return 1

        else:
            return n * Series.factorial(n-1)

    @staticmethod
    def prime_number(n:int):
        if n <= 1:
            return f'{n} não é um número primo!'
        if n <= 3:
            return f'{n} é um número primo!'
        
        if n % 2 == 0 or n % 3 == 0:
            return f'{n} não é um número primo!'
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return f'{n} não é um número primo!'
            i += 6
        
        return f'{n} é um número primo!'

    @staticmethod 
    def fibonarial(n:int):
        return Series.fibonacci(n) * Series.factorial(n)


print(Series.fibonacci(10))
print(Series.prime_number(10))
print(Series.factorial(10))
print(Series.fibonarial(10))
