#!/usr/bin/python
#-*- coding: utf-8
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, COLOR_ORANGE

class Menu:
    def __init__(self, window):                              # construtor inicia a instancia e 'window'
        self.window = window                                 # window recebe o parametro de window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # surf recebe a imagem carregada
        self.rect = self.surf.get_rect(left=0, top=0)        # posicionando um retangulo no topo a esquerda (no canto), aonde ficará a imagem

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')          # carrega o arquivo de musica do menu
        pygame.mixer_music.play(-1)                          # toca a musica, e o '-1' faz a musica repetir ao acabar

        while True:                             # loop infinito
            self.window.blit(source=self.surf, dest=self.rect)   # na janela faça um desenho (origem = imagem, destino = retangulo)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))  # texto na tela e suas dimenções
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))  # texto na tela e suas dimenções
            pygame.display.flip()                                # atualiza a tela

            for event in pygame.event.get():    # checa os eventos que forem "pegos"
                if event.type == pygame.QUIT:   # se o tipo do evento for 'sair'
                    pygame.quit()               # fecha a janela
                    quit()                      # fecha o jogo

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)        # escolhe a fonte que será utilizada
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()               # renderiza a imagem da fonte
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)                                # retangulo da imagem
        self.window.blit(source=text_surf, dest=text_rect)                                          # coloca a imagem no retangulo