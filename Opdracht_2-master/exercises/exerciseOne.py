#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de Valori FST intake opdracht. Werk zorgvuldig en netjes, succes!"

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    ("VFST is niet iets waar mijn hart ligt. Ik ga op zoek naar een andere chapter, Het ligt niet aan jou maar aan mij. Sorry dat ik via text met je verbreek en niet persoonlijk.")
    return None

if len(welcomeMessage) != 76:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())

print(printExercise())
