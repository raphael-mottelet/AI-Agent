from agent_context import get_initial_context
from run_conversation import run_conversation

if __name__ == "__main__":
    messages = get_initial_context() #ici on initialise notre agent avec le contexte. Vu que le contexte est par défaut en français, l'agent s'initialise en français.
    run_conversation(messages)
