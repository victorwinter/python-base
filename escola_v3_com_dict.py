#!/usr/bin/env python3

__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Ingles": aula_ingles, 
    "Musica": aula_musica, 
    "Dança": aula_danca
}

for nome_atividade, atividade in atividades.items():
        
    print(f"Alunos da atividade {nome_atividade}\n")
    print("*" * 60 )

    # Todos os alunos da sala1 que tem interção com a atividade:
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))


    print("Sala 1: ", atividade_sala1 )
    print("Sala 2: ", atividade_sala2 )

    print()
    print("*" * 60)
