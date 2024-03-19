import os
import json
from openai import OpenAI
import gpt_functions
from agent_context import get_initial_context
from chat_history import save_chat_history, load_chat_history

# Définir la clé API directement
OpenAI.api_key = "insert key in here"

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

def parse_function_response(message):
    function_call = message.get("function_call")
    if function_call:
        function_name = function_call.get("name")

        print("GPT: Called function " + function_name )

        try:
            arguments = json.loads(function_call.get("arguments", "{}"))

            if hasattr(gpt_functions, function_name):
                function_response = getattr(gpt_functions, function_name)(**arguments)
            else:
                function_response = "ERROR: Called unknown function"
        except Exception as e:
            function_response = "ERROR: Invalid arguments - " + str(e)
    else:
        function_name = None
        function_response = None

    return function_name, function_response

def run_conversation(messages=[]):
    while True:
        try:
            user_message = input("Vous: ")
            message = {
                "role": "user",
                "content": user_message
            }
            messages.append(message)

            client = OpenAI(api_key=OpenAI.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
        except Exception as e:
            print(f"Erreur lors de la création de la completion : {e}")
            return

        message_obj = response.choices[0].message
        if hasattr(message_obj, 'content'):
            message_content = message_obj.content
        elif hasattr(message_obj, 'text'):
            message_content = message_obj.text
        else:
            message_content = "No content available."
        messages.append({"role": "system", "content": message_content})

        # Condition de sortie de la boucle
        if message_content == "Conversation terminée":
            break

        print(f"GPT: {message_content}")

        # Sauvegarder l'historique après chaque interaction
        save_chat_history(messages)

if __name__ == "__main__":
    messages = get_initial_context()  # Initialize the agent with the context in French
    run_conversation(messages)
