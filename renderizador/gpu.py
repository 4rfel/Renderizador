#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Simulador de GPU.

Desenvolvido por: Luciano Soares <lpsoares@insper.edu.br>
Disciplina: Computação Gráfica
Data: 31 de Agosto de 2020
"""

# Numpy
import numpy as np

# Pillow
from PIL import Image

class GPU:
    """
    Classe que representa o funcionamento de uma GPU.

    ...

    Atributos
    ----------
    width : int (static)
        largura tela
    height : int (static)
        altura tela
    image_file : str (static)
        nome do arquivo a ser salvo
    framebuffer : numpy.ndarray (static)
        matriz que armazena pixels no formato RGB

    Métodos
    -------
    parse():
        Realiza o parse e já realiza as rotinas de renderização.
    """

    width = 60
    height = 40
    image_file = None
    frame_buffer = None

    def __init__(self, width, height, image_file):
        """Criar um framebuffer e define o nome do arquivo para salvar o framebuffer."""
        # Mantem largura e altura
        GPU.width = width
        GPU.height = height
        GPU.image_file = image_file

        # Cria imagem
        GPU.frame_buffer = np.zeros((height, width, 3), dtype=np.uint8) # cria imagem c/fundo preto

    @staticmethod
    def set_pixel(coord_u, coord_v, color_r, color_g, color_b):
        """Troca a cor de um pixel no framebuffer."""
        GPU.frame_buffer[coord_v][coord_u] = [color_r, color_g, color_b] # altera um pixel da imagem
        # Perceba que a matriz é organizada em linhas e colunas, ou seja, y e x, ou v e u

    @staticmethod
    def save_image():
        """Método para salvar a imagem do framebuffer em um arquivo."""
        img = Image.fromarray(GPU.frame_buffer, 'RGB')
        img.save(GPU.image_file)

    @staticmethod
    def load_texture(textura):
        """Método para ler textura."""
        imagem = Image.open(textura)
        matriz = np.array(imagem)
        return matriz
