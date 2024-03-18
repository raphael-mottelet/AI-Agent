from openai import OpenAI
import json

import gpt_functions

# Set your OpenAI API key here
OpenAI.api_key = "add your key in here"

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

def run_conversation(message, messages=[]):
    messages.append(message)

    try:
        client = OpenAI(api_key=OpenAI.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
    except Exception as e:
        print(f"Erreur lors de la création de la completion : {e}")
        return

    if response.choices:
        message_content = response.choices[0].message.get("content", response.choices[0].message.get("text"))
        messages.append({"role": "system", "content": message_content})

        if "function_call" in message:
            function_name, function_response = parse_function_response(message)
            message = {
                "role": "function",
                "name": function_name,
                "content": function_response
            }
        else:
            user_message = input("GPT: " + message_content + "\nYou: ")
            message = {
                "role": "user",
                "content": user_message
            }

        run_conversation(message, messages)

if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "You are an AI bot that can do everything using function calls. When you are asked to do something, use the function call you have available and then respond with a message confirming what you have done."
        }
    ]

    user_message = input("GPT: What do you want to do?\nYou: ")
    message = {
        "role": "user",
        "content": user_message
    }

    run_conversation(message, messages)
