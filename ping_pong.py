from re import X
import pygame
from pygame.locals import *
from sys import exit
from random import choice, randint

clock = pygame.time.Clock()


largura , altura = 1000 , 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ping-Pong')

pontos_p1 = 0
pontos_p2 = 0

pygame.font.init()
fonte_letra = pygame.font.SysFont('arial', 40, True, False)

x_player1 = 3
y_player1 = 220

x_player2 = 990
y_player2= 220

x_bola = largura/2
y_bola = randint(105,495)

velocidade_x_bola = choice([-0.75,0.75])
velocidade_y_bola = choice([-0.75,0.75])



pygame.init()
while True:
    clock.tick(400)
    
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #placar
    mensagem1 = f"Player 1: {pontos_p1}"
    mensagem_p1 = fonte_letra.render(mensagem1, True, (255,255,255))

    mensagem2 = f'Player 2: {pontos_p2}'

    mensagem_p2 = fonte_letra.render(mensagem2, True, (255,255,255))


    tela.blit(mensagem_p1,(100,20))
    tela.blit(mensagem_p2,(700,20))


    #linha separadora jogo-placar
    pygame.draw.rect(tela, (255,255,255),(0, 98, largura, 1))

    #bola
    bola = pygame.draw.circle(tela, (255,255,255), (x_bola, y_bola), 5)

    #player 1
    player1 = pygame.draw.rect(tela, (0,0,255), (x_player1, y_player1, 7, 45))

    if pygame.key.get_pressed()[K_w]:
        y_player1 += -1
        if y_player1 <= 100:
            y_player1 = 100

    if pygame.key.get_pressed()[K_s]:
        y_player1 += 1
        if y_player1 >= 355:
            y_player1 = 355


    #player 2
    player2 = pygame.draw.rect(tela, (255,0,0), (x_player2, y_player2, 7, 45))
    if pygame.key.get_pressed()[K_UP]:
        y_player2 += -1
        if y_player2 <= 100:
            y_player2 = 100

    if pygame.key.get_pressed()[K_DOWN]:
        y_player2 += 1
        if y_player2 >= 355:
            y_player2 = 355

    #evitar travas no movimento
    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_UP]:
        y_player1 += -1
        y_player2 += 1
        if y_player1 <= 100:
            y_player1 = 100
        if y_player2 <= 100:
            y_player2 = 100


    if pygame.key.get_pressed()[K_DOWN] and pygame.key.get_pressed()[K_s]:
        y_player1 += 1
        y_player2 += 1
        if y_player1 >= 355:
            y_player1 = 355
        if y_player2 >= 355:
            y_player2 = 355

    if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_DOWN]:
        y_player1 += -1
        y_player2 += 1
        if y_player1 <= 100:
            y_player1 = 100
        if y_player2 >= 355:
            y_player2 = 355

    if pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_UP]:
        y_player1 += 1
        y_player2 += -1
        if y_player1 >= 355:
            y_player1 = 355
        if y_player2 <= 100:
            y_player2 = 100

    #movimento bola
    if y_bola >= altura or y_bola <= 100: velocidade_y_bola = velocidade_y_bola * (-1)

    if x_bola >= largura or x_bola <= 0: velocidade_x_bola = velocidade_x_bola * (-1)

    if x_bola <= x_player1 or x_bola >= 995: 
        velocidade_x_bola = 0
        velocidade_y_bola = 0
        
    if player1.colliderect(bola):
        velocidade_x_bola = velocidade_x_bola * (-1)

    if player2.colliderect(bola):
        velocidade_x_bola = velocidade_x_bola * (-1)


    y_bola += velocidade_y_bola
    x_bola += velocidade_x_bola

    if x_bola <= 10 or x_bola >= 990:
        if x_bola <= 10: 
            pontos_p2 += 1
            velocidade_x_bola = 1 
        else: 
            pontos_p1 += 1
            velocidade_x_bola = (-1)
        
        x_bola = largura/2
        y_bola = randint(105,395)

        velocidade_y_bola = choice([-1,1])

        y_bola += velocidade_y_bola
        x_bola += velocidade_x_bola

        x_player1 = 3
        y_player1 = 220

        x_player2 = 990
        y_player2= 220

    pygame.display.update()
