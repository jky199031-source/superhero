# Je récupère l'info du nombre de pizza et je la transforme en nombre entier
nbPizzas =int(input("Combien de pizzas ?"))
# Je récupère le prix de la  pizza et je transforme le type de la réponse en décimal (float)
prix =float(input("Prix d'une pizza ?"))

# Total du prix
total = nbPizzas * prix

reduction =0.0
if nbPizzas > 5:
    reduction = total * 0.10
    total_apres_reduction = total - reduction

    if total_apres_reduction < 20:
        livraison = 3.0
    else: livraison = 0

    total_final = total_apres_reduction + livraison

    print()
    print(f" PIZZA TICKET")
    print(f"Pizzas : {nbPizzas} * {prix} €")
    print(f"Réduction : -{reduction} €")
    if livraison == 0:
        print("Livraison : gratuite")
        print(f"Livraison : {livraison} €")
        print(f"TOTAL : {total_final} €")