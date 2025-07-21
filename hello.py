#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente tendo como base a variavel "LANG"
o programa ira exibir a mensagem com o idioma correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI argument `--lang`

Ou o usuário terá que digitar.

Execução:

   python3 hello.py
   ou
   ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Winter"
__license__ = "Unlicense"

import os 
import sys


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:    
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language: ")
        
current_language = current_language[:5]    

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

        
print(
    msg[current_language] * int(arguments["count"])
)
