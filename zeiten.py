# zeiten.py
 
import sys

def zeitInSekunden(h,m,s):
    return int(s) + (int(m)*60) + (int(h)*3600)

#beginnZeit = input("Beginnzeit: ")
#endZeit = input("Endezeit: ")

p = sys.argv

beginnZeit = p[1]
endZeit = p[2]

#Zeit im Format HH:MM:SS
beginn = beginnZeit.split(":")
end = endZeit.split(":")

print(zeitInSekunden(end[0], end[1], end[2]) - zeitInSekunden(beginn[0], beginn[1], beginn[2]))

