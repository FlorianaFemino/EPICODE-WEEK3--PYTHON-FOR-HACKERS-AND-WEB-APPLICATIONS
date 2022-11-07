# Esercizio: calcolare il perimetro di alcune figure geometriche e la circonferenza di un cerchio

# ------------------------------- #

# importo la classe math, che permette di svolgere operazioni con pi greco

import math

# definizione delle funzioni perimetro e circonferenza

def perimetro_quadrato(): # Definizione della funzione per il calcolo del perimetro di un quadrato
    perimetro_1 = int (input ("Inserisci la lunghezza del lato: "))
    print ("\nPerimetro: ", perimetro_1 * 4, "\n--------------------------------------")

def circonferenza(): # Definizione della funzione per il calcolo della circonferenza
    circ_1 = int (input ("Inserisci la misura del raggio: "))
    print ('\nCirconferenza: ', circ_1*math.pi*2, "\n--------------------------------------")

def perimetro_rettangolo(): # Definizione della funzione per il calcolo del perimetro del rettangolo
    base = int (input ("Inserisci il valore della base: "))
    altezza = int (input ("Inserisci il valore dell'altezza: "))
    print ("\nPerimetro: ", base*2+altezza*2, "\n--------------------------------------")

# Menu principale

while 1:
    scelta = input ("Benvenuto! Scegli cosa vuoi calcolare:\n\n1. Perimetro di un quadrato\n\n2. Circonferenza\n\n3. Perimetro di un rettangolo\n\nOppure digita qualsiasi altro tasto per uscire\n")

    if scelta == '1':
        perimetro_quadrato()
    elif scelta == '2':
        circonferenza()
    elif scelta == '3':
        perimetro_rettangolo()
    elif scelta != '1' and scelta != '2' and scelta != '3':
        print ("A presto!")
        break