#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from funcao import * # importando as funções com perguntas e respostas
import telepot 
from chatbot import *

telegram = telepot.Bot("875776312:AAGc6GYNU88kyeY1UUkTH9FlG2IYfpz3y6U")

print("pode digitar")
def receberMensagem(msg):
	pergunta = msg['text'] #salvando a pergunta
	resposta = descobrirResposta(pergunta) #métoda para descobrir a resposta
	chatID = msg['chat']['id'] #criar um método para enviar a msg
	telegram.sendMessage(chatID, resposta)

telegram.message_loop(receberMensagem)

while True:
	pass


