import sys
sys.path.append('..')

from context.context_manager import ContextManager  # type: ignore # Importation du gestionnaire de contexte

PYTHON_keywords = [" ","UFR SMBH", "UFR SEG", "UFR LLSHS",
    "Université Sorbonne Paris Nord", "campus de Bobigny", "campus de Villetaneuse", "campus d'Argenteuil",
    "santé", "médecine", "biologie humaine", "sciences économiques", "gestion", "lettres", "langues",
    "sciences humaines", "sciences sociales", "sciences du vivant", "sciences sanitaires", "sciences de l'éducation",
    "psychologie", "littérature", "linguistique", "histoire", "géographie", "langues",
    "premier cycle", "PACES", "licence", "deuxième cycle", "troisième cycle", "master", "doctorat",
    "formation professionnelle", "alternance", "comptabilité", "gestion", "finance",
    "laboratoire", "UMR", "INSERM", "CNRS", "ENSAM", "Équipe d'Accueil", "EA",
    "administration", "secrétariat", "direction", "scolarité",
    "Nathalie Charnaux", "Sandra Cochot", "Nathalie Coutinet", "Sabrina Juillet Garzon",
    "faculté de médecine", "Bobigny", "Villetaneuse", "Argenteuil",
    "numéro de téléphone", "adresse", "mail", "formation pluridisciplinaire"]

general_keywords = ["bonjour", "salut", "hello", "ça va", "comment ça va", "merci", "s'il vous plaît","historique des messages","tu te souviens de notre conversation ?","condensé","hstorique","donnees json","données json"]

all_keywords = PYTHON_keywords + general_keywords

context_manager = ContextManager(context_keywords=all_keywords)
