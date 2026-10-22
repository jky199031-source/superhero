# age
age = int(input("Madame Irma vous demande votre age"))
# prenom
name = input("maintenant elle exige votre nomination")
birthday = 2026 - age
# donner le prénom
print(f"ton nom est {name}")
# donner l'année de naissance appro
print(f"ton année de naissance appro est: {birthday}")
# donner l'age dans dix ans
print("dans 10 ans tu aura", age + 10, "ans")
# faire une prediction
if age < 18:
    print("attention au crs")
elif age >= 18 and age <= 30:
    print("tu vas regretter ton enfance")
elif age > 30 and age <= 60:
    print("tu va kiffer ta life")
elif age > 60:
    print("60 ans : encore jeune, mais avec une garantie limitée ! »")