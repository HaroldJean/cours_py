a = -1
b = 8
age = 21
majeur = False
if a > 0: #Si a est > à 0
    b += 1 #on incrémente la valeur de b
    print ("a =",a,"et b =",b)
    if a > 6:
        print ("a est sup à 6")
    else:  #sinon
            print ("a est inf à 6")
if a > 0:
    print ("a est positif.")
elif a < 0: #negatif
    print ("a est négatif.")
else: # Nul
    print ("a est nul.")
# est il majeur
if age >= 18:
    majeur = True
    print ("il est majeur")
else:
    print ("il est pas majeur")
if majeur is not True:
    print ("Reste chez toi")
else:
    print ("Tu peux sortir")
    
    
            
        
        
    

