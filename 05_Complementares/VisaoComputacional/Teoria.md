# Visão Computacional  
-  Detecção de faces e objetos
-  Reconhecimento facial
-  Rastreamento de objetos 

## Detecção de faces e objetos  
### Classficador Cascade
1º Conjuto de faces  
2º Conjunto de não-faces  
> __Treinamento com AdaBoost__  
> - Seleção de Características (aplicação dos filtros)   
> - Uma imagem 24x24 tem mais de 160 000 combinações
> - Aplicação no formato de "cascata"  


[Artigo do Medium: Detectando objetos com métodos clássicos — OpenCV (cascades)](https://medium.com/ensina-ai/detectando-objetos-com-métodos-clássicos-opencv-cascades-440e29913b1b)
 
 
### LBPH (Local Binary Patterns Histograms)

[Understanding the Local Binary Pattern (LBP): A Powerful Method for Texture Analysis in Computer Vision](https://aihalapathirana.medium.com/understanding-the-local-binary-pattern-lbp-a-powerful-method-for-texture-analysis-in-computer-4fb55b3ed8b8)

É uma forma de descrever a estrutura local de uma imagem de uma forma que seja invariante às mudanças na iluminação, pois os binários do pixel escolhido serão os mesmos.

O histograma é o da contagem de cores de um pixel. O algoritmo classifica em borda ou canto com base nesse histograma.


## Rastreamento de Objetos  

- Mais rápidos que os algortimos de detecção  
- Algoritmo de detecção sempre "começa do zero"
- Rastreamento usa a informação _anterior_.


### Algoritmo CSRT (Discriminative Correlation Filter With Channel and Spatial Reliability)  
1. Da esquerda para a direita: patch de treinamento com a caixa delimitadora do objeto a ser rastreado
2. HOG para extrair informação útil da imagem
3. Probabilidade de objeto posterior após o teste aleatório de Markov
4. Patch de treinamento mascarado com o mapa final de confiabilidade  

[What is computer vision? - IBM](https://www.ibm.com/topics/computer-vision)

