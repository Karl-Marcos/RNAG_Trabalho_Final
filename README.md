<h1 align="center"> Algoritmo Genético aplicado para Regressão Simbólica </h1>

<p align="center"> Repositório dedicado ao trabalho final da disciplina de Redes Neurais e Algoritmos Genéticos do curso Bacharelado em Ciência e Tecnologia da Ilum Escola de Ciência, Campinas, SP - Brasil. </p>

<p align="center"> <img src="https://github.com/aaaaclarinha/aaaaclarinha/assets/106619091/b0a94d54-b3a7-4373-afc6-b1fbf1d26b2c", width=900, height=300></p>
<p align="center"> Fonte: Fabiana da Fonte

<details><summary><h3 align="justify"> Quem somos? </h3></summary>
  
<p align="justify"> Somos alunos da Ilum Escola de Ciência! Nosso curso é voltado para uma formação interdisciplinar em Ciência e Tecnologia. Por aqui exploramos diversas áreas do conhecimento e somos convidados a pensar ciência de forma independente e inovadora. </p>

<p align="justify"> Com base nisto, trazemos projetos multidisciplinares, incrementados principalmente em Python, para a plataforma do GitHub. Para conhecer um pouco mais de nosso trabalho, visite nossos perfis:</p>

- Ana Clara Brandão - https://github.com/aaaaclarinha
- Heitor Ribeiro - https://github.com/Vendedor-de-Automoveis
- Marcos de Cerqueira - https://github.com/Karl-Marcos
- Sophia Michel - https://github.com/Sophlechim
  
</details>

<details><summary><h3><b>Como se guiar nesse GitHub?</h3></b></summary>
<p align="justify">
Os experimentos de regressão simbólica estão separados em três notebooks jupyter (.ipynb), cada um aplicado a uma das equações diferenciais dos modelos populacionais: </p>
 
- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Malthus.ipynb"> Modelo de Malthus </a>

- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Verhulst.ipynb"> Modelo de Verhulst </a>

- <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/R_S%20-%20Gompertz.ipynb"> Modelo de Gompertz </a>

<p align="justify">
Além disso, algumas funções úteis, como as funções correspondentes às equações diferenciais em si, assim como a função que reslolve numericamente usando o método de Runge-Kutta, estão definidas no arquivo <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/funcoes.py"> funcoes.py 
</p>

</details>

<h3> Regressão Simbólica </h3>

<p align="justify"> Um dos principais obstáculos enfrentados na área de ciência analítica nos dias atuais envolvem um entendimento de relações numéricas entre conjuntos de dados pretencentes a um determinado sistema. Por isso, diversos modelos e técnicas foram desenvolvidas com o intuito de tentar gerar um vínculo quantitativo para estas variáveis, oferecendo uma interpretação coerente que é feita de acordo com o sistema que está sendo trabalhado. Nesse sentido, a forma mais usual de se realizar a solução de um problema como é através de combinações lineares, que são expressões baseadas em informações já coletadas para gerar um novo dado relacionado às propriedades do sistema estudado. Esse tipo de regressão oferece vantagens como facilidade na interpretação do modelo e na relação com conceitos ligados aos dados, bem como possue um baixo custo computacional para o processamento de dados, comparado a redes neurais, por exemplo [1]. </p>

<p align="justify"> A regressão simbólica, por sua vez, procura relacionar essas variáveis de forma simbólica, utilizando de diversos recurso matemáticos, que vão desde operações básicas, como soma e multiplicação, até funções mais complexas, como logaritmos e exponenciais, afim de encontrar uma representação matemática capaz de descrever os dados fornecidos. Essa ferramenta tecnológica permite identificar padrões de comportamento em conjuntos de dados e pode até auxiliar a descrição matemática de propriedades físicas, apesar de ser um propósito muito dificil de ser alcaçado, isto porque um dos principais desafios para a regressão simbólica é encontrar um expressão curta e interpretável para tais variáveis [2].</p>

<p align="justify"> Desta forma, o presente trabalho foi desenvolvido com a interção de aplicar um método de regressão simbólica para aproximar soluções para equações diferenciais ordenadas (EDOs), as quais descrevem dinâmicas de modelos populacionais, segundo os modelos de Malthuls, Verhulst e Gompertz. </p>

<h3> Dinâmica Populacional e Equações Diferenciais </h3>

<p align="justify"> </p>

    
  <h3> Referências </h3>
    
<p align="justify"> [1] <a href='https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b'> LUCIANOSPHERE. A better symbolic regression method, by explicitly considering units. Disponível em: https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b. Acesso em: 18 jun. 2023. </a>
‌</p>
<p align="justify"> [2] <a href='https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95'> RUGGIERO, R. Symbolic Regression: The Forgotten Machine Learning Method. Disponível em: https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95. Acesso em: 20 jun. 2023. </a>
</p>
    
