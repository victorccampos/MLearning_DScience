<h1> Redução de Dimensionalidade - 10/11/2024 </h1>

> 1. Principal Component Analysis (PCA)
> 2. Linear Discriminant Analysis (LDA)
> 3. Kernel PCA
 
Diminuir o tamanho da base de dados para **otimizar** o processamento de uma base de dados muito grande.

<h2>PCA</h2>  

- Seleção de característica x Extração de Característica

`Seleção`: usa os atributos mais importantes  
`Extração`: cria novos atributos, como união, combinação de atributos com base na relação entre eles.

-  Um dos principais algoritmos de aprendizagem de máquina não supervisionada (não depende da classe).
-  Identifica a correlação entre variáveis, e caso haja uma forte correlação _é possível reduzir a dimensionalidade_
-  Das $m$ variáveis independentes, _PCA_ extrai $p \le m$ novas variáveis independentes que _explica melhor_ a variação na base de dados _sem considerar a variável dependente_
-  O usuário escolhe o número $p \rightarrow$  componentes principais.
  
---


<H2>LDA</H2>  

- Além de encontrar os componentes principais, LDA também encontra os eixos que maximizam a separação entre múltiplas classes.
- Algoritmo supervisionado por causa da relação com a classe
- Das $m$ variáveis independentes, LDA extrai $p \le m$ novas variáveis independentes que mais _separam as classes_ da variável dependente.

---  

<H2>Kernel PCA </H2>  

- PCA e LDA são utilizados quando os dados são _linearmente separáveis_
- É uma versão do PCA que os dados são mapeados para uma dimensão maior usando algum **kernel trick**.
- Os componentes principais são extraídos dos dados com dimensionalidade maior (após a aplicação do kernel).


