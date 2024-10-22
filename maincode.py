import ttg
import random
import os
import time
import sys

def escrever_lentamente(texto, velocidade=0.05):
    """Escreve o texto letra por letra, simulando uma digitação lenta."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def gerar_tabela(papeis):
    """Gera uma tabela-verdade para os papéis na fase."""
    variaveis = [papel[1] for papel in papeis]
    tabela = ttg.Truths(variaveis, ints=False)
    return tabela

def verificar_proposicao(escolha, correta):
    """Verifica se a escolha do jogador é a correta."""
    return escolha == correta

def escolher_falas(personagens):
    """Escolhe aleatoriamente uma fala para cada personagem."""
    falas_escolhidas = []
    for personagem, falas in personagens.items():
        fala = random.choice(falas)
        falas_escolhidas.append(f"{personagem}: '{fala}'")
    return falas_escolhidas

def gerar_fase(papeis, personagens, opcoes, resposta_certa, fase_numero):
    """Executa uma fase do jogo e coleta uma preposição importante."""
    os.system("cls")
    time.sleep(1)
    escrever_lentamente(f"\n--- Fase {fase_numero}: Descubra algo importante ---")
    time.sleep(1)
    
    escrever_lentamente("Personagens nesta fase:")
    for papel, _ in papeis:
        escrever_lentamente(f"- {papel}")

    escrever_lentamente("\nPistas fornecidas:")
    falas = escolher_falas(personagens)
    for fala in falas:
        escrever_lentamente(fala)

    escrever_lentamente("")
    tabela = gerar_tabela(papeis)

    escrever_lentamente("\nEscolha uma preposição para seguir:")
    for i, opcao in enumerate(opcoes, 1):
        escrever_lentamente(f"{i}. {opcao}")

    escolha = input("\nDigite o número da preposição: ").strip()
    os.system("cls")
    if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
        escolha = int(escolha) - 1
        escrever_lentamente(f"\nVocê escolheu: {opcoes[escolha]}")
    else:
        escrever_lentamente("Escolha inválida. Seguiremos assim mesmo.")

    time.sleep(1)
    return opcoes[escolha]

def fase_final(pistas_reunidas, suspeitos):
    """Executa a fase final onde o jogador identifica o assassino."""
    os.system("cls")
    time.sleep(1)
    escrever_lentamente("\n--- Fase Final: Quem é o assassino? ---")
    time.sleep(1)
    escrever_lentamente("Pistas reunidas ao longo do jogo:")
    for i, pista in enumerate(pistas_reunidas, 1):
        escrever_lentamente(f"Fase {i}: {pista}")

    escrever_lentamente("\nSuspeitos:")
    for i, suspeito in enumerate(suspeitos, 1):
        escrever_lentamente(f"{i}. {suspeito}")

    assassino_correto = "Morganna"
    while True:
        escolha = input("\nDigite o número do assassino: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(suspeitos):
            escolha = int(escolha) - 1
            if verificar_proposicao(suspeitos[escolha], assassino_correto):
                escrever_lentamente("Parabéns! Você descobriu que Morganna era a culpada!")
                break
            else:
                escrever_lentamente("Errado! Tente novamente.")
        else:
            escrever_lentamente("Escolha inválida. Digite um número válido.")

def narrativa_inicial():
    os.system("cls")
    time.sleep(1)
    escrever_lentamente("No reino de Eldoria, onde o mistério e a magia se entrelaçam...")
    time.sleep(1.5)
    escrever_lentamente("A detetive Samantha, conhecida por seu intelecto afiado e perspicácia, foi chamada ao castelo.")
    time.sleep(2)
    escrever_lentamente("Um assassinato misterioso abalou a corte real.")
    time.sleep(1.5)
    escrever_lentamente("Agora, cabe a Samantha desvendar esse mistério sombrio.")
    time.sleep(1)
    escrever_lentamente("Com cada pista revelada, a verdade parece mais distante...")
    time.sleep(2)
    os.system("cls")

def narrativa_meio():
    escrever_lentamente("No dia seguinte, Samantha reuniu as pistas que coletou até o momento.")
    time.sleep(1.5)
    escrever_lentamente("Sua mente estava ocupada com as palavras enigmáticas dos suspeitos...")
    time.sleep(2)
    escrever_lentamente("Ela sabia que estava mais perto da verdade, mas o perigo também se aproximava.")
    time.sleep(2)
    os.system("cls")

def jogar():
    narrativa_inicial()
    
    escrever_lentamente("=== Bem-vindo ao Jogo de Detetive ===")
    time.sleep(1)
    
    pistas_reunidas = []

    for i, fase in enumerate(fases, 1):
        preposicao = gerar_fase(
            fase["papeis"],
            fase["personagens"],
            fase["opcoes"],
            fase["resposta_certa"],
            i
        )
        pistas_reunidas.append(preposicao)
        if i == 3:  # Adiciona uma narrativa extra no meio do jogo
            narrativa_meio()

    fase_final(pistas_reunidas, suspeitos)

# Configuração das 9 fases
fases = [
    # Fase 1: Cena do Crime - A Cozinha do Castelo
    {
        "papeis": [("Floris", "F"), ("Morganna", "M"), ("Aline", "A"), ("Sir Alaric", "SA")],
        "personagens": {
            "Floris": ["Uma sopa quente e uma morte fria... Que combinação, não acha?"],
            "Morganna": ["Quem fez isso já se foi há muito tempo."],
            "Aline": ["Há marcas frescas no chão."],
            "Sir Alaric": ["Precisamos agir rápido antes que a verdade desapareça."]
        },
        "opcoes": [
            "Se as facas estão ausentes, Bram está escondendo algo.",
            "Se Floris estava aqui, ele pode estar mentindo.",
            "As marcas no chão indicam que Sir Alaric sabe mais do que parece."
        ],
        "resposta_certa": 0
    },
    # Fase 2: Interrogatório com Bram
    {
        "papeis": [("Bram", "B"), ("Morganna", "M"), ("Lady Isolde", "LI")],
        "personagens": {
            "Bram": ["Baldwin sabia que algo ruim ia acontecer."],
            "Morganna": ["Não confie em Bram, ele esconde algo."],
            "Lady Isolde": ["Vamos nos concentrar no que importa."]
        },
        "opcoes": [
            "Se Bram está nervoso, ele esconde algo de Morganna.",
            "Bram sabia sobre o envenenamento.",
            "Bram viu Morganna na noite do assassinato."
        ],
        "resposta_certa": 1
    },
    
    # Adicionar mais fases depois
  
]

# Lista de suspeitos para a fase final
suspeitos = ["Floris", "Morganna", "Aline", "Sir Alaric", "Bram", "Lady Isolde"]

# Inicia o jogo
jogar()
