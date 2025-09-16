# %%
# PROVA: Comparando o Total Nacional vs. o Total de Computação
import pandas as pd
import os

PASTA_DADOS = 'planilhas'

try:
    # Carrega o dataset com o total GERAL
    df_total_nacional = pd.read_csv(os.path.join(PASTA_DADOS, 'Total_Vagas_OfertadasTUDO.csv'))
    
    # Carrega o dataset com o total de COMPUTAÇÃO
    df_total_comp = pd.read_csv(os.path.join(PASTA_DADOS, 'Total_Vagas_OfertadasComp.csv'))

    # --- Análise para 2019, semestre 1 ---
    ano_analise = 2019
    semestre_analise = 1
    
    # Pega o valor total nacional
    vagas_nacional = df_total_nacional[
        (df_total_nacional['ano'] == ano_analise) & (df_total_nacional['semestre'] == semestre_analise)
    ]['VagasOfertadasTotais'].iloc[0]
    
    # Pega a linha de computação e soma todas as colunas de cursos
    vagas_comp = df_total_comp[
        (df_total_comp['ano'] == ano_analise) & (df_total_comp['semestre'] == semestre_analise)
    ].drop(columns=['ano', 'semestre']).sum(axis=1).iloc[0]
    
    # Calcula a porcentagem
    percentual = (vagas_comp / vagas_nacional) * 100
    
    print("-" * 60)
    print(f"Comparativo de Vagas Ofertadas em {ano_analise}/{semestre_analise}:")
    print(f"Total de Vagas Ofertadas (TODOS OS CURSOS NO BRASIL): {vagas_nacional:,.0f}")
    print(f"Total de Vagas Ofertadas (APENAS CURSOS DE COMPUTAÇÃO): {vagas_comp:,.0f}")
    print(f"\nOs cursos de Computação representaram {percentual:.2f}% do total de vagas ofertadas.")
    print("-" * 60)

except FileNotFoundError as e:
    print(f"ERRO: Arquivo não encontrado -> {e.filename}")

# %%