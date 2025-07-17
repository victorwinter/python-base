#!/usr/bin/env python3

__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles), 
    ("Musica", aula_musica), 
    ("Dança", aula_danca),
]

for nome_atividade, atividade in atividades:
        
    print(f"Alunos da atividade {nome_atividade}\n")
    print("*" * 60 )
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("sala1 ", atividade_sala1 )
    print("sala2 ", atividade_sala2 )

    print()
    print("*" * 60)
