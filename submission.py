# submission.py 
#Level2 - korrekte Lösung ermittlen

abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:0 correct"

t = abgabe.split(" ")
startzeit = t[0]
submissions = t[1]
bestezeit = "23:59:59"
besteruser = -1



for x in range (2, len(t), 3):
   user = t[position]
   zeit = t[position+1]
   loesung = t[position+2]
   print"Abgabe:",user,zeit,loesung =="correct")
   if(zeit < bestezeit):
       bestezeit = zeit
       besteruser = user
    
print(besteruser, bestezeit)

    
