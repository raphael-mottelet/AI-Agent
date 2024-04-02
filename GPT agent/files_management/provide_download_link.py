import sys
sys.path.append('..')

import os

def provide_download_link(filename):
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
