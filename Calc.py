# The input() function takes input from the user and returns it.
# A função input() recebe o input do utilizador e devolve.

sinal = input("Escolhe um sinal (+ - * /): ")

# A float is a floating point number which is a computers representation of a real number
# Um float é floating point number que é uma representação informática de um número real.

numero1 = float(input("Escolhe o primeiro número: "))
numero2 = float(input("Escolhe o segundo número "))

# This is read as if the signal is + then add numero1 to numero2 resulting in a sum and then print is used
# to show us the result. The "round" is used for rounding the numbers.

# Isto é lido como se o sinal fosse +, então adiciona o número1 ao número2, resultando numa soma
# e depois é utilizado o print para nos mostrar o resultado. O "round" é utilizado para arredondar os números.

if sinal == "+":
    result = numero1 + numero2
    print(round(result, 3))
# In here we have the elif, which means if the previous conditions were not true, then try this condition.
# Aqui temos o elif, que significa que se as condições anteriores não forem verdadeiras, então tenta esta condição.

# It's worth noting that in the "round" we're using 3, which means we're rounding to 3 decimal places.
# Vale a pena referir que no "round" estamos a utilizar 3 o que significa que estamos a arrondar para 3 casas decimais.
elif sinal == "-":
    result = numero1 - numero2
    print(round(result, 3))
elif sinal == "*":
    result = numero1 * numero2
    print(round(result, 3))
elif sinal == "/":
    result = numero1 / numero2
    print(round(result, 3))

# Here I find it difficult to understand the "f" string, with research I saw that F strings provide a convenient way
# of incorporating formatting expressions But even with this description I have a little trouble understanding.
# anyways it's used a print to display a message.
# Aqui demonstro dificuldade em perceber o "f" string, com pesquisa vi que a F strings fornecem uma forma conveniente
# de incorporar expressões formatação Mas mesmo com esta descrição tenho um pouco de dificuldade em perceber.
# de qualquer forma, é utilizado um print para mostrar uma mensagem.
else:
    print(f"{sinal} não é valido")