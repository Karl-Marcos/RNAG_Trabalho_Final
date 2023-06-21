<h1 align="center"> Algoritmo Genético aplicado para Regressão Simbólica </h1>

<p align="center"> Repositório dedicado ao trabalho final da disciplina de Redes Neurais e Algoritmos Genéticos do curso Bacharelado em Ciência e Tecnologia da Ilum Escola de Ciência, Campinas, SP - Brasil. </p>

<p align="center"> <img src="https://github.com/aaaaclarinha/aaaaclarinha/assets/106619091/b0a94d54-b3a7-4373-afc6-b1fbf1d26b2c", width=900, height=300></p>
<p align="center"> Fonte: Fabiana da Fonte

<details><summary><h3 align="justify"> Quem somos? </h3></summary>
  
<p align="justify"> Somos alunos da <a href="https://ilum.cnpem.br/"> Ilum Escola de Ciência</a>! Nosso curso é voltado para uma formação interdisciplinar em Ciência e Tecnologia. Por aqui exploramos diversas áreas do conhecimento e somos convidados a pensar ciência de forma independente e inovadora. </p>

<p align="justify"> Com base nisto, trazemos projetos multidisciplinares, incrementados principalmente em Python, para a plataforma do GitHub. Para conhecer um pouco mais de nosso trabalho, visite nossos perfis:</p>

- <a href="https://github.com/aaaaclarinha"> Ana Clara Brandão </a>
- <a href="https://github.com/Vendedor-de-Automoveis"> Heitor Ribeiro</a>
- <a href="https://github.com/Karl-Marcos"> Marcos de Cerqueira</a>
- <a href="https://github.com/Sophlechim"> Sophia Michel </a>

<p align="justify"> Esse repositório é parte da disciplina de Redes Neurais e Algoritmos Genéticos, ministrada pelo <a href="https://github.com/drcassar"> Prof. Daniel R. Cassar </a> </p>
  
</details>

<details><summary><h3><b>Como se guiar nesse GitHub?</h3></b></summary>
<p align="justify">
Os experimentos de regressão simbólica por algoritmos genéticos estão separados em três Notebooks Jupyter (.ipynb), sendo cada um aplicado a uma equação diferencial dos modelos populacionais: </p>
 
- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Malthus.ipynb"> Modelo de Malthus (R_S_Malthus) </a>

- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Verhulst.ipynb"> Modelo de Verhulst (R_S_Verhulst) </a>

- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Gompertz.ipynb"> Modelo de Gompertz (R_S_Gompertz) </a>

<p align="justify">
Além disso, podem ser acessadas também algumas funções úteis para o deselvimento do nosso trabalho, como as funções correspondentes às equações diferenciais e a função que resolve o problema da análise numericamente, usando o método de Runge-Kutta. Estas se encontram definidas no arquivo '.py' <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/funcoes.py"> funcoes.py </a> 
</p>

</details>

<h3> Regressão Simbólica </h3>

<p align="justify"> Um dos principais obstáculos enfrentados na área de ciência analítica nos dias atuais envolvem um entendimento de relações numéricas entre conjuntos de dados pretencentes a um determinado sistema. Por isso, diversos modelos e técnicas foram desenvolvidas com o intuito de tentar gerar um vínculo quantitativo para estas variáveis, oferecendo uma interpretação coerente que é feita de acordo com o sistema que está sendo trabalhado. Nesse sentido, a forma mais usual de se realizar a solução de um problema como é através de combinações lineares, que são expressões baseadas em informações já coletadas para gerar um novo dado relacionado às propriedades do sistema estudado. Esse tipo de regressão oferece vantagens como a facilidade na interpretação do modelo e na relação com conceitos ligados aos dados, bem como possue um baixo custo computacional para o processamento de dados, comparado a redes neurais, por exemplo [1]. </p>

<p align="justify"> A regressão simbólica, por sua vez, procura relacionar essas variáveis de forma simbólica, utilizando de diversos recurso matemáticos para manipular expressões desconhecidas, que vão desde operações básicas, como adição e multiplicação, até funções mais complexas, como logaritmos e exponenciais. O uso desse método é amplamente aplicado em Aprendizado de Máquina para predizer variáveis de saída a partir das relações das variáveis de entrada fornecidas através de um banco de banco de dados, de forma a aproximar a expressão da melhor forma possível uma representação matemática capaz de descrever os dados fornecidos através de uma aproximação. Essa ferramenta tecnológica permite identificar padrões de comportamento em conjuntos de dados e pode até auxiliar a descrição matemática de propriedades físicas, o qual é um propósito muito complexo de ser alcaçado, isto porque um dos principais desafios para a regressão simbólica é encontrar um expressão curta e interpretável para tais variáveis [2].</p>

<p align="justify"> Desta forma, o presente trabalho foi desenvolvido com a interção de aplicar um método de regressão simbólica para aproximar soluções para equações diferenciais ordenadas (EDOs), as quais descrevem dinâmicas de modelos populacionais, segundo os modelos de Malthuls, Verhulst e Gompertz. </p>

<h3> Dinâmica Populacional e Equações Diferenciais </h3>

<p align="justify"> </p>

    
  <h3> Referências </h3>
    
<p align="justify"> [1] <a href='https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b'> LUCIANOSPHERE. A better symbolic regression method, by explicitly considering units. Disponível em: https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b. Acesso em: 18 jun. 2023. </a>
‌</p>
<p align="justify"> [2] <a href='https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95'> RUGGIERO, R. Symbolic Regression: The Forgotten Machine Learning Method. Disponível em: https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95. Acesso em: 20 jun. 2023. </a>
</p>
    
