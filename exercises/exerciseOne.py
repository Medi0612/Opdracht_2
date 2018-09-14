#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de Valori FST intake opdracht. Werk zorgvuldig en netjes, succes!"
motivationMessage = "Na een prettig gesprek met Wieger, werd voor mij bevestigd dat deze baan precies bij mij past. Daarom solliciteer ik graag naar deze functie. Ik begrijp dat het voor klanten vervelend is als er iets niet naar behoren functioneert. Doordat ik altijd in oplossingen denk en mijn uitgebreide computerkennis combineer met mijn ruime ervaring in contact met klanten wordt elke vraag door mij snel en adequaat opgelost. Door mijn rustige karakter en communicatievaardigheden weet ik mensen op hun gemak te stellen. Daarnaast heb ik verschillende trainingen gevolgd om deze kwaliteit verder te ontplooien. Van kinds af aan werk ik al met computers er zijn weinig programma’s die ik niet beheers en anders pik ik die snel op. Voor meer informatie verwijs ik u naar mijn cv."

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printMotivationText():
    motivation = motivationMessage
    return None

if len(welcomeMessage) != 76:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
