#Oppgave 3-9, program for å beregne farge på tall i ruletten
#Alternativ 1, nøsting av hvis-setninger med tanke på intervall og farge

#Steg 1, avgjøre gyldig tall
#Steg 2, finne riktig intervall

#Brukeren oppgir verdi på ruletten
tall=int(input('Hva er tallet på ruletten? '))

#Tester om gyldig verdi og beregner riktig farge for gyldige verdier
if tall>=0 and tall<=36:
    print('Gyldig tall.')

    if tall==0:
        print('Tallet er',tall,'og er markert "Grønn" på ruletten')
    else:
        if tall<=10:
            print('Tallet er ',tall,'og er i intervallet [1,10]')
        else:
            if tall<=18:
                print('Tallet er',tall,'og er i intervallet [11,18]')
            else:
                if tall<=28:
                    print('Tallet er',tall,'og er i intervallet [19,28]')
                else:
                    if tall<=36:
                        print('Tallet er',tall,'og er i intervallet [29,36]')
                        

else:
    print('Ugyldig tall.')
