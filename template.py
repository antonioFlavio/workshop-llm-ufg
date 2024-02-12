
def _get_template_1():
    return """Atue como um especialista em extrair palavras complexas de textos jurídicos. Considere como público alvo pessoas com baixa escolaridade, com idade de 18 anos.
Não considere como complexo: nomes de pessoas, entidades, números.
Considere apenas as palavras existentes no trecho. Se não houver palavras complexas, deixe vazio.
Não exagere, não selecione como palavra complexa mais do que 40% das palavras do trecho. Dê preferência para as mais complexas.
Uma palavra complexa não deve ser considerada como simplificação de outra palavra complexa.

Extraia palavras complexas e suas respectivas palavras simples substitutas: {trecho}.

Considere o gênero e grau das palavras ao redor da palavra complexa para sugerir a palavra simples substituta.
Na palavra simples, faça o ajuste morfológico necessário para que a frase permaneça coesa e coerente.
"""

def _get_template_2():
    return """Atue como um especialista em extrair palavras complexas de textos jurídicos. Considere como público alvo pessoas com baixa escolaridade, com idade de 20 anos.
Não considere como complexo: nomes de pessoas, entidades, números.
Considere apenas as palavras existentes no trecho. Se não houver palavras complexas, deixe vazio.
Não selecione palavras simples como complexas e dê preferência para as mais complexas.
Uma palavra complexa não deve ser considerada como simplificação de outra palavra complexa.

Extraia palavras complexas e suas respectivas palavras simples substitutas: {trecho}.

Considere o gênero e grau das palavras ao redor da palavra complexa para sugerir a palavra simples substituta. Na palavra simples, faça o ajuste morfológico necessário para que a frase permaneça coesa e coerente.
"""

def _get_template_3():
    return """Atue como um especialista em extrair palavras complexas de textos jurídicos. Considere como público alvo pessoas com baixa ou média escolaridade, com idade de 24 anos.
Não considere como complexo: nomes de pessoas, entidades, números.
Considere apenas as palavras existentes no trecho. Se não houver palavras complexas, deixe vazio.
Não selecione palavras simples como complexas e dê preferência para as mais complexas.
Uma palavra complexa não deve ser considerada como simplificação de outra palavra complexa.

Extraia palavras complexas e suas respectivas palavras simples substitutas: {trecho}.

Considere o gênero e grau das palavras ao redor da palavra complexa para sugerir a palavra simples substituta. Na palavra simples, faça o ajuste morfológico necessário para que a frase permaneça coesa e coerente.
"""

def _get_template_4():
    return """Atue como um especialista em extrair palavras complexas de textos jurídicos.
Não considere como complexo: nomes de pessoas, entidades, números.
Considere apenas as palavras existentes no trecho. Se não houver palavras complexas, deixe vazio.
Não selecione palavras simples como complexas e dê preferência para as mais complexas.
Uma palavra complexa não deve ser considerada como simplificação de outra palavra complexa.
Considere como complexa palavras do juridiquês ou palavras formais.

Extraia palavras complexas e suas respectivas palavras simples substitutas: {trecho}.

Considere o gênero e grau das palavras ao redor da palavra complexa para sugerir a palavra simples substituta. Na palavra simples, faça o ajuste morfológico necessário para que a frase permaneça coesa e coerente.
"""

def _get_template_5():
    return """Atue como um especialista em extrair palavras complexas de textos jurídicos.
Não considere como complexo: nomes de pessoas, entidades, números ou datas
Considere apenas as palavras existentes no trecho. Se não houver palavras complexas, deixe vazio.
Não selecione palavras simples como complexas e dê preferência para as mais complexas.
Uma palavra complexa não deve ser considerada como simplificação de outra palavra complexa.
Considere como complexa palavras do juridiquês ou palavras formais.
Se a simplificação de uma palavra for ela mesma, não considere como palavra complexa.

Extraia palavras complexas e suas respectivas palavras simples substitutas: {trecho}.

Considere o gênero e grau das palavras ao redor da palavra complexa para sugerir a palavra simples substituta. Na palavra simples, faça o ajuste morfológico necessário para que a frase permaneça coesa e coerente.
"""

templates = {}

templates["template_1"] = _get_template_1()
templates["template_2"] = _get_template_2()
templates["template_3"] = _get_template_3()
templates["template_4"] = _get_template_4()
templates["template_5"] = _get_template_5()

def get_template(template_id):
    return templates[template_id]