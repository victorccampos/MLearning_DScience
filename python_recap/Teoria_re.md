# Expressões Regulares  

- Busca sofisticada por padrões
- Procurar todas as palavras que começam com letra _maiúscula_ ou que começam com _maiúscula_ e terminam com _minúscula_
- Que começam com 'a' e terminam com 'e'
- Procurar e-mails, números de telefone, CEPs, etc  
- Padrões de buscas são ilimitados  
---

Extrair todas as palavras que:  
1. Começam com vogais e terminam com consoantes
2. Possuem de 5 a 9 letras
3. Trechos separados por ponto "."
4. Começam com _c_, possuem 'r', 'e' ou 'u' no meio e terminam com 'a', 'l' ou 'x'


## Métodos
1. ```search```: encontrar as posições de padrões dentro de uma string, se estes estiverem presentes
2. ```match```: Encontrar se o começo de uma string é igual a um determinado padrão  
3.```findall``` Encontrar todas as substrings em uma string que correspondam a um padrão.


---



### Usos Comuns de Regex
1. Validação de entrada: Verificar se um texto segue um formato específico (ex.: emails, números de telefone, CEPs).

   - Exemplo: Validar um email: r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
2. Busca por padrões: Encontrar partes específicas de texto, como datas ou URLs.

   - Exemplo: Procurar datas no formato YYYY-MM-DD: r"\d{4}-\d{2}-\d{2}"
3. Substituição de texto: Alterar ou remover partes de um texto com base em um padrão.

   - Exemplo: Remover espaços extras: re.sub(r"\s+", " ", text)
4. Extração de dados: Capturar partes específicas de texto usando grupos.

   - Exemplo: Capturar o nome de domínio de um email: r"@([a-zA-Z0-9.-]+)\."


<table><thead><tr><th>Metacaractere</th><th>Significado</th><th>Exemplo</th></tr></thead><tbody><tr><td><code>.</code></td><td>Qualquer caractere (exceto nova linha)</td><td><code>a.b</code> → Combina "acb", "a9b"</td></tr><tr><td><code>^</code></td><td>Início da string</td><td><code>^abc</code> → Combina "abc" no início</td></tr><tr><td><code>$</code></td><td>Final da string</td><td><code>xyz$</code> → Combina "xyz" no final</td></tr><tr><td><code>*</code></td><td>Zero ou mais repetições do caractere anterior</td><td><code>ba*</code> → Combina "b", "ba", "baa"</td></tr><tr><td><code>+</code></td><td>Uma ou mais repetições do caractere anterior</td><td><code>ba+</code> → Combina "ba", "baa"</td></tr><tr><td><code>?</code></td><td>Zero ou uma repetição do caractere anterior</td><td><code>ba?</code> → Combina "b" ou "ba"</td></tr><tr><td><code>{n,m}</code></td><td>Entre <code>n</code> e <code>m</code> repetições</td><td><code>a{2,4}</code> → Combina "aa", "aaa", "aaaa"</td></tr><tr><td><code>[]</code></td><td>Conjunto de caracteres</td><td><code>[aeiou]</code> → Combina qualquer vogal</td></tr><tr><td><code>\</code></td><td>Escape para caracteres especiais</td><td><code>\.</code> → Combina literalmente "."</td></tr><tr><td>`</td><td>`</td><td>Operador OR</td></tr><tr><td><code>()</code></td><td>Grupo de captura</td><td><code>(ab)+</code> → Combina "ab", "abab"</td></tr></tbody></table>