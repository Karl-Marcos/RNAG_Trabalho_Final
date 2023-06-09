<h1 align="center"> Algoritmo Genético aplicado para Regressão Simbólica </h1>

<p align="center"> Repositório dedicado ao trabalho final da disciplina de Redes Neurais e Algoritmos Genéticos do curso Bacharelado em Ciência e Tecnologia da Ilum Escola de Ciência, Campinas, SP - Brasil. </p>

<p align="center"> <img src="https://github.com/aaaaclarinha/aaaaclarinha/assets/106619091/b0a94d54-b3a7-4373-afc6-b1fbf1d26b2c", width=900, height=300></p>
<p align="center"> Fonte: Fabiana da Fonte

<details><summary><h3 align="justify"> Quem somos? </h3></summary>
  
<p align="justify"> Somos alunos da <a href="https://ilum.cnpem.br/"> Ilum Escola de Ciência</a>! Nosso curso é voltado para uma formação interdisciplinar em Ciência e Tecnologia. Por aqui exploramos diversas áreas do conhecimento e somos convidados a pensar ciência de forma independente e inovadora. </p>

<p align="justify"> Com base nisto, trazemos projetos multidisciplinares, incrementados principalmente em Python, para a plataforma do GitHub. Para conhecer um pouco mais de nosso trabalho, visite nossos perfis:</p>

- <a href="https://github.com/aaaaclarinha"> Ana Clara Brandão </a>
- <a href="https://github.com/Vendedor-de-Automoveis"> Heitor R. Bernardes </a>
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
Além disso, podem ser acessadas também algumas funções úteis para o deselvimento do nosso trabalho, como as funções correspondentes às equações diferenciais e a função que resolve o problema da análise numericamente, usando o método de Runge-Kutta. Estas se encontram definidas no arquivo <a href="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/funcoes.py"> funcoes.py </a> 
</p>

</details>

<h3> Regressão Simbólica </h3>

<p align="justify"> Um dos principais obstáculos enfrentados na área de ciência analítica nos dias atuais envolvem um entendimento de relações numéricas entre conjuntos de dados pretencentes a um determinado sistema. Por isso, diversos modelos e técnicas foram desenvolvidas com o intuito de tentar gerar um vínculo quantitativo para estas variáveis, oferecendo uma interpretação coerente que é feita de acordo com o sistema que está sendo trabalhado. Nesse sentido, a forma mais usual de se realizar a solução de um problema como é através de combinações lineares, que são expressões baseadas em informações já coletadas para gerar um novo dado relacionado às propriedades do sistema estudado. Esse tipo de regressão oferece vantagens como a facilidade na interpretação do modelo e na relação com conceitos ligados aos dados, bem como possue um baixo custo computacional para o processamento de dados, comparado a redes neurais, por exemplo [1]. </p>

<p align="justify"> A regressão simbólica, por sua vez, procura relacionar essas variáveis de forma simbólica, utilizando de diversos recurso matemáticos para manipular expressões desconhecidas, que vão desde operações básicas, como adição e multiplicação, até funções mais complexas, como logaritmos e exponenciais. O uso desse método é amplamente aplicado em Aprendizado de Máquina para predizer variáveis de saída a partir das relações das variáveis de entrada fornecidas através de um banco de dados, de forma a aproximar a expressão da melhor forma possível. Essa ferramenta tecnológica permite identificar padrões de comportamento em conjuntos de dados, podendo até auxiliar na descrição matemática de propriedades físicas, o qual funciona de um modo muito complexo de ser alcançado, pois um dos principais desafios para a realização da regressão simbólica está em encontrar um expressão curta e interpretável para tais variáveis [2].</p>

<h3> Dinâmica Populacional e Equações Diferenciais </h3>

<p align='justify'> Em dinâmica populacional, existe uma forma interessante e válida de se representar modelos populacionais reais expressos de forma matemática, usando equações diferencias. Estes modelos, então, são usados para descrever um sistema populacional real, levando em conta as condições em que ele se encontra, de forma a permitir um estudo experimental simulador que prevê o que pode acontecer com as dinâmicas de fenômenos. </p>

<p align="justify"> A escolha dos modelos aplicados foi inspirada pela disciplina de Equações Diferencias e Análise Numérica, ministradas pelo professor Doutor Vinícius F. Wasques, na Ilum Escola de Ciência, Campinas - Brasil, nos anos de 2022 e 2023. Os modelos foram estudado dos pontos de vista análitico e numérico, e agora serão discutidos com esta nova abordagem. </p>

<h4> O Modelo de Malthus </h4>

<p align="justify"> Um dos modelos mais clássicos, foi proposto pelo economista inglês Thomas Malthus em 1798, afim de descrever o crescimento de uma população. Ele avaliou que o número de indivíduos de uma população em um determinado instante $t$ é uma proporção da população total.
</p>

$$ \frac{\partial{x}}{\partial{t}} = \lambda x $$

<h4> O Modelo de Verhulst </h4>

<p align="justify"> Verhulst, por sua vez, propos que, para um modelo mais geral, considera-se uma taxa atrelada a limitações de recursos, desta forma, uma população só cresceria até alcançar um limite máximo sustentável, após isso, ela se estabilizaria.
</p>

$$ \frac{\partial{x}}{\partial{t}} = \lambda x (1-x) $$

<h4> O Modelo de Gompertz </h4>

<p align="justify"> O mais recente modelo (1938) foi originalmente considerado para análisar o crescimento de células tumorais. Elaborado por Benjamin Gompertz, este modelo considera também uma taxa atrelada a capacidade máxima que uma população pode alcançar.

$$ \frac{\partial{x}}{\partial{t}} = \lambda x \ ln (\frac{1}{x})$$

<p align="justify"> A todos os modelos foi aplicada uma regressão simbólica, que tinha o intuito de encontrar representações válidas como resoluções numéricas de possíveis soluções de cada um desses modelos. Foram usados como parâmetro, portanto, soluções numéricas respectivas a cada modelo que foram obtidas pelo método análise numérica de Runge-Kutta, o qual consiste na discretização temporal da equação diferencial. Esse é um método muito eficaz para descrever aproximações de equações não lineares, como é o caso dos dos três modelos demonstrados acima. </p>

<p align="justify"> Desta forma, o presente trabalho foi desenvolvido com a intenção de usar um algoritmo genético para aplicar um método de regressão simbólica para encontrar soluções para equações diferenciais ordenadas (EDOs), as quais descrevem dinâmicas de modelos populacionais, segundo os modelos de Malthuls, Verhulst e Gompertz. Usando o módulo de Python `DEAP`, buscamos uma representação matemática capaz de descrever os dados fornecidos através de uma aproximação. </p>

<h3> Resultados e Discussões </h3>

Na aba Resultados desse repositório é possível ver os gráficos de funções aproximadas da solução analítica de cada um dos três modelos populacionais apresentados neste trabalho, bem como alguns exemplos de regressões simbólicas encontradas pelo algoritmo genético.

Aqui, temos algumas soluções que o grupo julgou como sendo boas aproximações, considerando as limitações do código:


<p align="justify"> As melhores soluções para o modelo de Malthus </p>

<table>
  <tr>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Malthus_ana.jpeg?raw=true" width=540 height=240 alt="Imagem 1">
      </figure>
      <p>$$x(t) = 3e^{t}$$</p>
    </td>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Malthus_2.jpeg?raw=true" width=540 height=240 alt="Imagem 2">
      </figure>
      <p>$$x(t) = \frac{e^{t}}{ee^{e-1}} + ee^t $$</p>
    </td>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Malthus_3.jpeg?raw=true" width=540 height=240 alt="Imagem 3">
      </figure>
      <p>$$x(t) = \frac{t}{e} + ee^t = e^{-1}$$ </p>
    </td>
  </tr>
</table>

<p align="justify"> As melhores soluções para o modelo de Verhulst </p>

<table>
  <tr>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Verhulst_ana.jpeg?raw=true" width=540 height=240 alt="Imagem 1">
        <figcaption>$$x(t) = \frac{1}{1+e^{-t}}$$</figcaption>
      </figure>
    </td>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Verhulst_2.jpeg?raw=true" width=540 height=240 alt="Imagem 2">
        <figcaption>$$x(t) = 3e^{-e^{-t}e^{-\frac{e^t}{e}}}$$</figcaption>
      </figure>
    </td>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Verhulst_3.jpeg?raw=true" width=540 height=240 alt="Imagem 3">
        <figcaption>$$x(t) = e^{e^{-te^{te^{-t}}}}$$</figcaption>
      </figure>
    </td>
  </tr>
</table>


<p align="justify"> As melhores soluções para o modelo de Gompertz </p>

<table>
  <tr>
    <td>
      <figure>
          <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Gompertz_ana.jpeg?raw=true" width=540 height=240 alt=" Solução 1 (análitica">
        <figcaption align="center">$$x(t) = x_0 \  e^{-e^{-t}}$$</figcaption>
      </figure>
      </td>
    <td>
      <figure>
        <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Gompertz_2.jpeg?raw=true" width=540 height=240 alt="Solução 2">
        <figcaption>$$x(t) = -t + \frac{e^t}{e}+ e^{e^{-t}}$$</figcaption>
      </figure>
    </td>
    <td>
      <figure>
      <img src="https://github.com/Karl-Marcos/RNAG_Trabalho_Final/blob/main/resultados/Gompertz_3.jpeg?raw=true" width=540 height=240 alt="Solução 3">
      <figcaption>$$x(t) = e^{\frac{1}{t + \frac{e^t}{t+1}}}$$</figcaption> 
      </figure>
    </td>
  </tr>
</table>


  <h3> Referências </h3>
    
<p align="justify"> [1] <a href='https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b'> LUCIANOSPHERE. A better symbolic regression method, by explicitly considering units. Disponível em: https://towardsdatascience.com/a-better-symbolic-regression-method-by-explicitly-considering-units-35b3630165b. Acesso em: 18 jun. 2023. </a>
‌</p>
<p align="justify"> [2] <a href='https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95'> RUGGIERO, R. Symbolic Regression: The Forgotten Machine Learning Method. Disponível em: https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95. Acesso em: 20 jun. 2023. </a>
</p>

<p align="justify"> [3] <a href='https://moodle-ilum.cnpem.br/pluginfile.php/256647/mod_resource/content/15/Equa__es_Diferenciais___Ilum_2022%20%2817%29.pdf'> WASQUES, Vinícius Francisco. Notas Matemáticas: Equações Diferenciais. Ilum Escola de Ciência, 2022. </a>
</p>

<p align="justify"> [4] <a href='https://towardsdatascience.com/symbolic-regression-the-forgotten-machine-learning-method-ac50365a7d95](https://www.fc.unesp.br/Home/Departamentos/Matematica/revistacqd2228/v02n02a09-os-modelos-de-crescimento-populacional.pdf)'> TAVONI, R.; ZOTIN G. DE OLIVEIRA, R. Os modelos de crescimento populacional de Malthus e Verhulst - uma motivação para o ensino de logaritmos e exponenciais. C.Q.D.- Revista Eletrônica Paulista de Matemática, v. 2, p. 86–99, 2013.</a>
</p>

<p align="justify"> [5] <a href='https://www.if.ufrj.br/~carlos/infoenci/notasdeaula/roteiros/aula06.pdf'> CEDERJ -CENTRO DE EDUCAÇÃO SUPERIOR A DISTÂNCIA DO ESTADO DO RIO DE JANEIRO. [s.l: s.n.]. Disponível em: <https://www.if.ufrj.br/~carlos/infoenci/notasdeaula/roteiros/aula06.pdf>. </a>
</p>



‌
    
