#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3
import pygame
#inicilizar o mixer
pygame.mixer.init()
#carregar o arquivo de música(verificar o caminho)
pygame.mixer.music.load('ex021.mp3')
#tocar a música
pygame.mixer.music.play()
#se quiser encerrar
input('Pressione ENTER para terminar')
pygame.mixer.music.stop()






