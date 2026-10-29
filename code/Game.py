#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Menu import Menu                       # importantando a classe Menu de Meny.py

class Game:
    def __init__ (self):
        pygame.init()                                           # inicia o pygame
        self.window = pygame.display.set_mode(size = (600, 480))     # window recebe pygame display, que é uma janela, com o tamanho passado como parametro        

    def run(self):
        while True:                              # enquanto verdadeiro, o loop acontece
            menu = Menu(self.window)
            menu.run()
            pass


            # check for all events
            #for event in pygame.event.get():    # checa os eventos que forem "pegos"
            #    if event.type == pygame.QUIT:   # se o tipo do evento for 'sair'
            #        pygame.quit()               # close window
            #        quit()                      # end pygame

