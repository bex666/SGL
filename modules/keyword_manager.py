def edit_keywords(file_path="settings/mots_cles.txt"):
    print("✏️ Modification de la bibliothèque de mots-clés")
    with open(file_path, "r", encoding="utf-8") as f:
        keywords = f.read()
    print("Mots-clés actuels :")
    print(keywords)
    new_keywords = input("Entrez les nouveaux mots-clés (séparés par des retours à la ligne) :\n")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_keywords)
    print("✅ Mots-clés mis à jour.")
