import pygame

print('Setup Start')
pygame.init();
window = pygame.display.set_mode(size = (600, 480))     # window recebe pygame display, que é uma janela, com o tamanho passado como parametro
print('Setup End')

print('Loop Start')
while True:                             # enquanto verdadeiro, o loop acontece
    # check for all events
    for event in pygame.event.get():    # checa os eventos que forem "pegos"
        if event.type == pygame.QUIT:   # se o tipo do evento for 'sair'
            pygame.quit()               # close window
            quit()                      # end pygame

