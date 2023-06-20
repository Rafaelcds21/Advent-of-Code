"""
--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
import dados_day1

calorias_gerais_lista = dados_day1.lista_calorias_gerais.split("\n\n")

calorias_gerais_lista_sem_n = [x.replace("\n", " ") for x in calorias_gerais_lista]

calorias_gerais_agrupadas_lista = [x.split(" ") for x in calorias_gerais_lista_sem_n]

lista_da_lista_das_calorias_de_cada_elfo=[]

for x in calorias_gerais_agrupadas_lista:
    mini_list = []

    for i in x:
        if i!="":
            mini_list.append(i)

    lista_da_lista_das_calorias_de_cada_elfo.append(mini_list)

lista_total_calorias_geral = []

elfo = 1

for x in lista_da_lista_das_calorias_de_cada_elfo:
    soma_cada_elfo = 0

    lista_total_caloria_cada_elfo = []

    for i in x:
        soma_cada_elfo+=int(i)

    lista_total_caloria_cada_elfo.append(elfo)
    lista_total_caloria_cada_elfo.append(soma_cada_elfo)

    lista_total_calorias_geral.append(lista_total_caloria_cada_elfo)

    elfo+=1

maior = 0
elfo_com_mais_calorias = 0

for i in lista_total_calorias_geral:
    if i[1]>=maior:
        maior = i[1]
        elfo_com_mais_calorias = i[0]

print(f"O elfo com o maior número de calorias foi o {elfo_com_mais_calorias}° com {maior} calorias.")

"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
lista_total_calorias_geral_ordenada = sorted(lista_total_calorias_geral, key=lambda x: x[1], reverse=True)

top1 = lista_total_calorias_geral_ordenada[0]
top2 = lista_total_calorias_geral_ordenada[1]
top3 = lista_total_calorias_geral_ordenada[2]

soma_top_3 = top1[1] + top2[1] + top3[1]
print(f"O 1° lugar foi o {top1[0]}° elfo com {top1[1]} calorias, o 2° lugar foi o {top2[0]}° elfo com {top2[1]} calorias, o 3° lugar foi o {top3[0]}° elfo com {top3[1]} calorias e a soma total foi de {soma_top_3} calorias")