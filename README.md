# Analise-Exploratoria-Dados-Fies
Este repositório contém um projeto completo de análise de dados sobre os microdados públicos do FIES (Fundo de Financiamento Estudantil), com foco no desempenho e na dinâmica dos cursos da área de Computação no Brasil.


O objetivo principal foi transformar um grande volume de dados brutos e inconsistentes em datasets agregados e visualizações claras, permitindo a extração de insights estratégicos sobre o programa.

As principais etapas do projeto incluíram:

    Limpeza e Preparação de Dados (Data Wrangling):

        Leitura e concatenação de múltiplos arquivos CSV (mais de 1.5 GB de dados brutos).

        Tratamento de inconsistências nos dados, como nomes de colunas variáveis entre os anos, linhas duplicadas e padronização de nomes de cursos.

        Criação de novas variáveis (features) para enriquecer a análise, como a categorização de candidatos por "Região" e a classificação de "Qualificados" (nota do ENEM acima ou abaixo da nota de corte).

    Análise Exploratória de Dados (EDA):

        Agregação de dados para calcular métricas-chave, como total de vagas ofertadas, número de inscrições, candidatos únicos e vagas ocupadas.

        Análise detalhada por múltiplas dimensões: por curso, por período (ano/semestre) e por localização (UF/Região).

    Visualização de Dados (Data Visualization):

        Criação de um painel de visualizações para comunicar os resultados, incluindo:

            Gráficos de Funil para demonstrar a competitividade do processo.

            Boxplots para analisar a distribuição e variação das notas de corte.

            Heatmaps (Mapas de Calor) para visualizar a performance (ex: "potencial desperdiçado") por curso e período.

            Gráficos de Barras Agrupadas para comparar a performance entre regiões e semestres.

            Tabelas Estilizadas para exportação de relatórios em formato de imagem.

Tecnologias Utilizadas:

    Linguagem: Python

    Bibliotecas Principais: Pandas (para manipulação de dados), Matplotlib e Seaborn (para visualização).

    Ambiente: Jupyter Notebook / VS Code com extensão Jupyter.
