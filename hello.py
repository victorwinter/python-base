#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente tendo como base a variavel "LANG"
o programa ira exibir a mensagem com o idioma correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

   python3 hello.py
   ou
   ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Winter"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

        
print(msg[current_language])
