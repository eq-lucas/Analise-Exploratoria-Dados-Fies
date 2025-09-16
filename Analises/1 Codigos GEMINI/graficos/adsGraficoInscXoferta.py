# %%
# ANÁLISE FINAL PARA "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS" (ADS)
# Gerando gráficos individuais, com eixo Y controlado e anotações para SP
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.ticker import MultipleLocator

# --- 1. CONFIGURAÇÃO ---
PASTA_DADOS = 'planilhas' 
NOME_ARQUIVO = 'adsanalise.csv' # Substitua se o nome do seu arquivo for diferente
PASTA_GRAFICOS = 'graficos_ads_finais' # Pasta para salvar os novos gráficos

# Cria a pasta de gráficos se ela não existir
os.makedirs(PASTA_GRAFICOS, exist_ok=True)

try:
    caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)
    df_ads = pd.read_csv(caminho_arquivo)
except FileNotFoundError:
    print(f"AVISO: Arquivo '{caminho_arquivo}' não encontrado.")
    if 'dfADS' in locals() or 'dfADS' in globals():
        df_ads = dfADS.copy()
    else:
        exit()

# --- 2. LOOP PARA GERAR GRÁFICOS SEPARADOS ---

anos = [2019, 2020, 2021]
semestres = [1, 2]
sns.set_theme(style="whitegrid")
print("Gerando gráficos individuais refinados para cada período...")

# Loop para criar um gráfico para cada período
for ano, sem in [(a, s) for a in anos for s in semestres]:
    
    # Filtra os dados para o período atual
    df_periodo = df_ads[(df_ads['Ano'] == ano) & (df_ads['Semestre'] == sem)]
    
    if df_periodo.empty:
        print(f"\nSem dados para o período {ano}/{sem}. Pulando.")
        continue
    
    # Ordena os estados alfabeticamente
    df_periodo_sorted = df_periodo.sort_values(by='UF do Local de Oferta', ascending=True)

    # Reformatando para o formato 'longo'
    df_plot_long = df_periodo_sorted.melt(
        id_vars='UF do Local de Oferta',
        value_vars=['VagasOfertadasCurso_UF', 'inscritosCurso_UF'],
        var_name='Métrica',
        value_name='Quantidade'
    )
    
    # --- CRIAÇÃO DA FIGURA INDIVIDUAL ---
    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(
        x='UF do Local de Oferta', 
        y='Quantidade', 
        hue='Métrica', 
        data=df_plot_long,
        palette='magma',
        ax=ax
    )
    
    # --- FORMATAÇÃO REFINADA ---
    ax.set_title(f'Análise ADS: Vagas Ofertadas vs. Inscrições - Período: {ano}/{sem}', fontsize=20)
    ax.set_xlabel('Estado (UF)', fontsize=14)
    ax.set_ylabel('Quantidade', fontsize=14)
    ax.tick_params(axis='x', rotation=45, labelsize=11)
    
    # DEFINE O LIMITE DO EIXO Y E OS INTERVALOS
    y_limit = 1000 
    ax.set_ylim(0, y_limit)
    ax.yaxis.set_major_locator(MultipleLocator(250))
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # LÓGICA PARA ADICIONAR ANOTAÇÃO EM SÃO PAULO (SP)
    if 'SP' in df_periodo_sorted['UF do Local de Oferta'].values:
        sp_data = df_periodo_sorted[df_periodo_sorted['UF do Local de Oferta'] == 'SP']
        sp_ofertadas = sp_data['VagasOfertadasCurso_UF'].iloc[0]
        sp_inscritos = sp_data['inscritosCurso_UF'].iloc[0]
        sp_x_position = df_periodo_sorted['UF do Local de Oferta'].tolist().index('SP')
        
        # Adiciona o texto com o valor real, em PRETO
        if sp_ofertadas > y_limit:
            ax.text(sp_x_position - 0.2, y_limit * 0.95, f'// {sp_ofertadas:,.0f}', ha='center', va='top', color='black', rotation=90, fontsize=12, weight='bold')
        if sp_inscritos > y_limit:
            ax.text(sp_x_position + 0.2, y_limit * 0.95, f'// {sp_inscritos:,.0f}', ha='center', va='top', color='black', rotation=90, fontsize=12, weight='bold')

    ax.legend(title='Métrica')
    plt.tight_layout()
    
    # --- SALVAR E MOSTRAR ---
    nome_arquivo_salvar = f'analise_ads_{ano}_{sem}_eixo_controlado.png'
    caminho_salvar = os.path.join(PASTA_GRAFICOS, nome_arquivo_salvar)
    
    plt.savefig(caminho_salvar)
    print(f"\nGráfico para {ano}/{sem} gerado e salvo como '{caminho_salvar}'")
    
    plt.show()
    plt.close(fig)

print("\nProcesso concluído. Todos os gráficos foram gerados e salvos.")
# %%