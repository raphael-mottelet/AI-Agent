import sys
sys.path.append('..')

from context.context_manager import ContextManager  # type: ignore # Importation du gestionnaire de contexte

PYTHON_keywords = ["","code","python", "import", "from", "def", "return", "if", "else", "elif", "for", "while", "in", "not", "and", "or", "is", "None", "True", "False", "class", "try", "except", "raise", "assert", "with", "as", "lambda", "global", "nonlocal", "pass", "break", "continue", "yield", "del", "async", "await", "importation", "module", "package", "fonction", "méthode", "variable", "liste", "tuple", "dictionnaire", "ensemble", "itérable", "itérateur", "générateur", "compréhension de liste", "expression conditionnelle", "gestionnaire de contexte", "décorateur", "POO", "héritage", "polymorphisme", "encapsulation", "composition", "mixin", "introspection", "métaprogrammation", "programmation fonctionnelle", "map", "reduce", "filter", "lambda", "réflexion", "threading", "multiprocessing", "pickle", "JSON", "CSV", "XML", "SQLite", "unittest", "pytest", "logging", "debugging", "profilage", "optimisation", "virtualenv", "pip", "conda", "Anaconda", "Jupyter", "IDE", "PyCharm", "VSCode", "SublimeText", "Atom", "Spyder", "numpy", "pandas", "matplotlib", "scikit-learn", "tensorflow", "keras", "django", "flask", "web scraping", "API", "RESTful", "SOAP", "XML-RPC", "JSON-RPC", "ORM", "SQLAlchemy", "pep8", "docstring", "type hinting", "PEP", "GIL", "PEP8", "PEP20", "PEP257", "PEP484", "PEP526", "PEP572", "PEP8000"]

general_keywords = ["bonjour", "salut", "hello", "ça va", "comment ça va", "merci", "s'il vous plaît","historique des messages","tu te souviens de notre conversation ?","condensé","hstorique","donnees json","données json"]

all_keywords = PYTHON_keywords + general_keywords

context_manager = ContextManager(context_keywords=all_keywords)
