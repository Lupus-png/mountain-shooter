#!/usr/bin/python
#-*- coding: utf-8
import pygame

class Menu:
    def __init__(self, window):                              # construtor inicia a instancia e 'window'
        self.window = window                                 # window recebe o parametro de window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # surf recebe a imagem carregada
        self.rect = self.surf.get_rect(left=0, top=0)        # posicionando um retangulo no topo a esquerda (no canto), aonde ficará a imagem

    def run(self):
        self.window.blit(source=self.surf, dest=self.rect)   # na janela faça um desenho (origem = imagem, destino = retangulo)
        pygame.display.flip()                                # atualiza a tela
        pass