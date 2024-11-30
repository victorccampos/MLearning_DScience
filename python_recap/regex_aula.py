import re

telefone_regex: str = r'\(\d{2}\\d{4,5}-\d{4})'

frase: str = 'Olá, meu número de telefone é (98) 0000-0000'
print(re.search(pattern=telefone_regex, string=frase))
