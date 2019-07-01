#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from dialogos import Dialogo

bot = ChatBot('Anetha')
conversa = Dialogo().dialogoALL
aprender = ListTrainer(bot)
aprender.train(conversa)

def descobrirResposta(pergunta):
	perg = pergunta.lower()
	resp = bot.get_response(perg)
	resposta = str(resp)
	return resposta
