# Dados o tempo gasto por um veículo em uma viagem e sua velocidade média, calcular a quantidade de litros de combustível gasto pelo veículo, 
# considerando que o veículo faz um quilômetro por litro. 
# Para isso, determine primeiramente a distância percorrida pelo veículo 
# (com base no tempo gasto por ele e na sua velocidade média) e depois a quantidade de combustível que ele utilizou.

# criando a funcao
def calculoCombustivel():    
    tempo = float(input("Quanto tempo levou a viagem? (em horas) "))

    vmedia = float(input("Velocidade média: (em km/h) "))

    distancia = vmedia * tempo
    print(f"O combustível gasto foi de {distancia}L na viagem. ")

# chamando' a funcao
calculoCombustivel()

