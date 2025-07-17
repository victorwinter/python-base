clientes = ["Maria", "João", "Carlos"]

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é otimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponivel.

Preço promocional %(preco).2f
"""

for cliente in clientes:
    print(email_tmpl % {
        "nome": cliente,
        "produto": "caneta",
        "texto": "Caneta para apagar riscos nas paredes",
        "link": "https://canetaslegais.com",
        "quantidade": 1,
        "preco": 50.5
    })
    
