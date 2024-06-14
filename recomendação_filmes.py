import random

lista_filmes = [
    "O Poderoso Chefão",
    "Forrest Gump",
    "Pulp Fiction",
    "Os Bons Companheiros",
    "A Origem",
    "Clube da Luta",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Matrix",
    "Star Wars: Episódio IV - Uma Nova Esperança",
    "O Silêncio dos Inocentes"
] 

lista_series = [
    "Breaking Bad",
    "Game of Thrones",
    "Friends",
    "Stranger Things",
    "The Office",
    "Sherlock",
    "House of Cards",
    "Westworld",
    "Black Mirror",
    "The Mandalorian"
]

lista_desenhos = [
    "Rick and Morty",
    "Os Simpsons",
    "Hora de Aventura",
    "Bob Esponja",
    "Futurama",
    "South Park",
    "Avatar: A Lenda de Aang",
    "Scooby-Doo",
    "Tom e Jerry",
    "Dragon Ball Z"
]

escolha1 = random.choice(lista_filmes)
escolha2 = random.choice(lista_series)
escolha3 = random.choice(lista_desenhos)

digite = input("\noq vc deseja assitir?\n\n- Filmes\n- Series\n- Desenhos\n\nEscreva sua opção: ").lower()

if digite == 'filmes':
    print(f'\nVoce esolheu {digite} - ' + escolha1)
elif digite == 'series':
    print(f'\nVoce esolheu {digite} - ' + escolha2)
else:
    print(f'\nVoce esolheu {digite} - ' + escolha3)