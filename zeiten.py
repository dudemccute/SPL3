# zeiten.py
 
def zeitInSekunden(h,m,s):
    return int(s) + (int(m)*60) + (int(h)*3600)

beginnZeit = input("Beginnzeit: ")
endZeit = input("Endezeit: ")


#Zeit im Format HH:MM:SS
beginn = beginnZeit.split(":")

print("Stunden",h)
print("Minuten",m)
print("Sekunden",s)

print(zeitInSekunden(beginnZeit[0], beginnZeit[1], beginnZeit[2]) - zeitInSekunden(endZeit[0], endZeit[1], endZeit[2]) )

print("Gesamt Sekunden Beginn:",beginnSekunden)
