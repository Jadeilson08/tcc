#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Dialogo:
    def __init__(self):
        dialogoTXTA = open('./dialogos/saudacao.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTB = open('./dialogos/nome.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTC = open('./dialogos/1808.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTD = open('./dialogos/revolucaoporto.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTE = open('./dialogos/1821.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTF = open('./dialogos/josebonifacio.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTG = open('./dialogos/diafico.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTH = open('./dialogos/1822.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTI = open('./dialogos/1824.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTJ = open('./dialogos/1807.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTK = open('./dialogos/insurreicao.txt', 'r', encoding='utf-8').readlines()
        dialogoTXTL = open('./dialogos/noitegarrafadas.txt', 'r', encoding='utf-8').readlines()
        self.dialogoALL = dialogoTXTA+dialogoTXTB+dialogoTXTC+dialogoTXTD+dialogoTXTE+dialogoTXTF+dialogoTXTG+dialogoTXTH+dialogoTXTI+dialogoTXTJ+dialogoTXTK+dialogoTXTL

