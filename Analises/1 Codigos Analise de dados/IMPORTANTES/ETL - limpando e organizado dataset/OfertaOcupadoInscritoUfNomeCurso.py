# %%
import pandas as pd

pd.set_option('display.max_columns', None)

caminho_ins= "planilhas/DfInscricoesOrganizadoUFComp.csv"

caminho_of= "planilhas/DfOfertasOrganizadoUFCursosComp.csv"

df= pd.read_csv(caminho_ins)

dfo= pd.read_csv(caminho_of)


dfo_uf= "UF do Local de Oferta"
df_uf= "UF do Local de Oferta"


df_nomeCurso= "Nome do curso"
dfo_nomeCurso= "Nome do Curso"

df= (df.groupby(["Ano do processo seletivo","Semestre do processo seletivo","Nome do curso","UF do Local de Oferta"],as_index=False)
    .agg(

    inscritosCurso_UF=("Nome do curso",'count')


    ).sort_values(by=["Ano do processo seletivo","Semestre do processo seletivo","UF do Local de Oferta","inscritosCurso_UF"],ascending=[True,True,True,False])
    .reset_index(drop=True))


dfo=(dfo.groupby(["Ano","Semestre","Nome do Curso","UF do Local de Oferta"],as_index=False)
    .agg(

    VagasOcupadasCurso_UF=("Vagas ocupadas",'sum'),
    VagasOfertadasCurso_UF=('Vagas ofertadas FIES','sum')

    ).sort_values(by=["Ano","Semestre","UF do Local de Oferta","VagasOfertadasCurso_UF"],ascending=[True,True,True,False])
    .reset_index(drop=True))



df_final= pd.merge(

left=df,
right=dfo,
left_on=["Ano do processo seletivo","Semestre do processo seletivo","UF do Local de Oferta","Nome do curso",],
right_on=["Ano","Semestre","UF do Local de Oferta","Nome do Curso",],
how="outer",
suffixes=['INSCRITO','OFERTA']
)



colunas=[
    'Ano',
    'Semestre',
    'UF do Local de Oferta',
    'Nome do curso',
    'VagasOfertadasCurso_UF',
    'inscritosCurso_UF',
    'VagasOcupadasCurso_UF'
]

df_final=df_final[colunas].sort_values(by=colunas,ascending=[True,True,True,True,False,False,False,])


df_final
# %%
filtroADS= df_final['Nome do curso'] == 'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS'

colunas=[
    'Ano',
    'Semestre',
    'UF do Local de Oferta',
   # 'Nome do curso',
    'VagasOfertadasCurso_UF',
    'inscritosCurso_UF',
    'VagasOcupadasCurso_UF'
]


dfADS= df_final[filtroADS].sort_values(by=colunas,ascending=[True,True,True,False,False,False,])[colunas].reset_index(drop=True)


df_final.to_csv('OfertaOcupadoInscritoUfNomeCurso.csv',index=False)
# %%
