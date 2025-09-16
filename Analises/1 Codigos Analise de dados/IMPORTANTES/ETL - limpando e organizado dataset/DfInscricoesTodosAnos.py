# %%
import pandas as pd
import os

pd.set_option('display.max_columns', None)


ano = [2019, 2020, 2021]
sem = [1, 2]

lista_DF = []


for year in ano: 
    for semestre in sem:

        caminho_inscricoes = f'dataset/inscricoes CORRIGIDAS/fies_{semestre}_inscricao_{year}.csv'

        df_bruto = pd.read_csv(caminho_inscricoes)



        mapa_nomes_corretos = {

            'ANÃLISE E DESENVOLVIMENTO DE SISTEMAS': 'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS',
            'CIÊNCIAS DA COMPUTAÇÃO': 'CIÊNCIA DA COMPUTAÇÃO',
            'SISTEMA DE INFORMAÇÃO': 'SISTEMAS DE INFORMAÇÃO',
            'ENGENHARIA DE COMPUTAÇÃO': 'ENGENHARIA DA COMPUTAÇÃO'
        }

        df_bruto['Nome do curso'] = df_bruto['Nome do curso'].replace(mapa_nomes_corretos)



        # Filtra o DataFrame para manter apenas os cursos de computação
        cursosComputacao = [

            'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS',
            'CIÊNCIA DA COMPUTAÇÃO',
            'SISTEMAS DE INFORMAÇÃO',
            'REDES DE COMPUTADORES',
            'ENGENHARIA DA COMPUTAÇÃO',
            'ENGENHARIA DE SOFTWARE'
        ]

        filtro_computacao = df_bruto['Nome do curso'].isin(cursosComputacao)
        df_temporario = df_bruto[filtro_computacao]
        


        lista_DF.append(df_temporario)

df_concat = pd.concat(lista_DF, ignore_index=True)







# Define a ordem de classificação, com UF em primeiro, como solicitado
desempate = [

'Ano do processo seletivo',
'Semestre do processo seletivo',
'UF do Local de Oferta',
'Cod. do Grupo de preferência',
'Código do curso',
'Turno'
]
df_organizado = df_concat.sort_values(by=desempate, ascending=True)


df_organizado

# %%
df_organizado.to_csv('DfInscricoesOrganizadoUFComp.csv', index=False)
# %%