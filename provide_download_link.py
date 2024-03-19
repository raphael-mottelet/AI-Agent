import os

def provide_download_link(filename):
    """
    Crée un lien de téléchargement pour le fichier spécifié.
    Si le répertoire "download" n'existe pas, il sera créé.
    
    Args:
    - filename (str): Le nom du fichier à télécharger.
    
    Returns:
    - str: Le lien de téléchargement HTML.
    """
    download_dir = "download"
    file_path = os.path.join(download_dir, filename)
    
    # Vérifier si le répertoire "download" existe, sinon le créer
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Créer un fichier fictif pour les tests
    with open(file_path, "w") as f:
        f.write("Contenu fictif du fichier.")
    
    # Construire le lien de téléchargement
    file_basename = os.path.basename(file_path)
    download_link = f"<a href='{file_path}' download='{file_basename}'>Télécharger {file_basename}</a>"
    
    return download_link

# Exemple d'utilisation
download_link = provide_download_link("nom_prenom_fake_data.csv")
print(download_link)
