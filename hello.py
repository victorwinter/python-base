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
__version__ = "0.0.1"
__author__ = "Winter"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
        
print(msg)
