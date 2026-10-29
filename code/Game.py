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
        while True:                              # enquanto verdadeiro, o loop acontece
            menu = Menu(self.window)             # menu recebe a classe Menu
            menu.run()                           # roda a variavel menu
            pass
