#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu                       # importantando a classe Menu de Meny.py

class Game:
    def __init__ (self):
        pygame.init()                                                # inicia o pygame
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))     # window recebe pygame display, que é uma janela, com o tamanho passado como parametro        

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')                  # carrega o arquivo de musica do menu
        pygame.mixer_music.play(-1)                                # toca a musica, e o '-1' faz a musica repetir ao acabar

        while True:                              # enquanto verdadeiro, o loop acontece
            menu = Menu(self.window)             # menu recebe a classe Menu
            menu.run()                           # roda a variavel menu
            pass


            # check for all events
            #for event in pygame.event.get():    # checa os eventos que forem "pegos"
            #    if event.type == pygame.QUIT:   # se o tipo do evento for 'sair'
            #        pygame.quit()               # close window
            #        quit()                      # end pygame

