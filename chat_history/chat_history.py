import sys
sys.path.append('..')

import sys
sys.path.append('..')

import json

#fichier permettant  de sauvegarder l'historique des échanges entre gpt et user, sous la forme d'un fichier json.
def save_chat_history(messages, file_path="history.json"):
    try:
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'historique du chat : {e}")

def load_chat_history(file_path="history.json"):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement de l'historique du chat : {e}")
        return []
