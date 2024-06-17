import sys
sys.path.append('..')

import json
from openai import OpenAI
from context.agent_context import get_initial_context
from chat_history.chat_history import save_chat_history, load_chat_history
from context.context_manager import ContextManager
from context.keyword_manager import context_manager
<<<<<<< HEAD:conversation_features/run_conversation.py

OpenAI.api_key = "clef gpt"
=======
# Définir la clé API directement
OpenAI.api_key = ""
>>>>>>> a80262497cfe405b7c02edc1029e92eed6cc5820:GPT agent/conversation_features/run_conversation.py

def load_chat_history(messages):
    try:
        with open("history.json", "r") as file:
            chat_history = json.load(file)
            messages.extend(chat_history)
    except FileNotFoundError:
        print("Aucun historique de chat trouvé.")
    except Exception as e:
        print(f"Erreur lors du chargement de l'historique du chat : {e}")

def run_conversation(messages=[]):
        
    while True:
        try:
            user_message = input("Vous: ")

            if not context_manager.is_in_context(user_message):
                print("Gardez la conversation dans le contexte de la DGESCO.")
                continue

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

        if message_content == "Conversation terminée":
            break

        print(f"GPT: {message_content}")

        save_chat_history(messages)

if __name__ == "__main__":
    messages = get_initial_context()
    run_conversation(messages)
