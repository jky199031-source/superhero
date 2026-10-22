# programme qui me permet dans la console d'ajouter un fruit
fruits = ["Kiwi", "Mangue", "Coco", "Pastèque", "Poire"]

# demander à l'utilisateur quel fruit il veut ajouter
new_fruit=input("Quel fruit voulez-vous ajouter ?")
# l'ajouter au tableau
fruits.append(new_fruit)
# afficher ce message à l'utilisateur
print(f"notre nouveau tableau de fruit est:{fruits}")
# "notre nouveau tableau de fruit est : XXXX"
# "nous avons XXX fruits dans notre panier"
print(f"nous avons {len(fruits)} fruits dans notre panier")



