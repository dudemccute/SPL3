# parkhaus.py 
# Angabe für das Beispiel: siehe Moodle

p = 0
print("Linienbus-Simulator")

Haltestellen = input("Wie viele Haltestellen gibt es ? ")

Haltestellen = int(Haltestellen)
i = 0

while (i < Haltestellen):
    i = i+1
    print("Sie sind an der:",i,".Haltstelle,Wie viele Personen steigen ein ")
    einsteiger = input()
    inside =int (einsteiger)

    print("Wv Austeiger?")
    Austeiger = input()
    out = int(Austeiger)

    p = p + inside
    p = p - out
     
    if(p > 60):
        print("Es sind zu viele im Bus ")
        r = p - 60
        print("Es sind ",r,"Personen zu viel ")
        p = 60
        print("Es sind nun",p,"Menschen im Bus")
    elif(p < 0):
        print("Es sind zu wenig im Bus ")
        i = i-1
        p = p-inside
        p = p+out
        
    else:
        print("Es sind nun",p,"Menschen im Bus ")
    



