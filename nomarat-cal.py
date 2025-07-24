#Hi today we are going to calculate your final result at your exam!

name = input ('what is your name ? ')
madrese_name = input ('what is your madrese name ? ')
kelas_name = input ('shomare kelasi: ')

nomre_1 = int (input ("nomre riazi benevis "))
nomre_2 = int (input ("nomre programming benevis "))
nomre_3 = int (input ("nomre dini benevis "))
nomre_4 = int (input ("nomre farsi benevis "))
nomre_5 = int (input ("nomre english benevis "))

zarib = {"riazi" : 3 , 
    "programming" : 3 , 
    "dini" : 2 , 
    "farsi" : 2 , 
    "english" : 3
}

nomrat = {"riazi" : nomre_1 , 
    "programming" : nomre_2 , 
    "dini" : nomre_3 , 
    "farsi" : nomre_4 ,
    "english" : nomre_5
}

majmoe_zaribdar = 0
majmoe_zarib = 0

for dars in nomrat:
    majmoe_zaribdar += nomrat[dars] * zarib[dars]
    majmoe_zarib += zarib[dars]

miangin = majmoe_zaribdar / majmoe_zarib

print(f"hi {name} you were studing at {madrese_name} in {kelas_name} Miangin nomarat: {miangin : 1.2f}")
# this is amin safari booooooooooooy!!!