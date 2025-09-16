# %%
# CÓDIGO APENAS PARA GERAR O DATAFRAME de Nota de Corte por Período e Região
import pandas as pd
import os

# --- 1. CARREGAMENTO E CONFIGURAÇÃO ---
PASTA_DADOS = 'planilhas'
NOME_ARQUIVO = 'DfOfertasOrganizadoUFCursosComp.csv' 
caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)

try:
    df_ofertas = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{NOME_ARQUIVO}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
    exit()

# --- 2. LIMPEZA E PREPARAÇÃO DOS DADOS ---
df_ofertas.columns = df_ofertas.columns.str.strip() 

# Converte a coluna de nota de corte para número
df_ofertas['Nota de Corte Grupo Preferência'] = pd.to_numeric(
    df_ofertas['Nota de Corte Grupo Preferência'].astype(str).str.replace(',', '.'), 
    errors='coerce'
)
df_ofertas.dropna(subset=['Nota de Corte Grupo Preferência'], inplace=True)

# Mapeia os estados (UF) para as 5 grandes regiões (USANDO O .map())
mapa_regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}
df_ofertas['Região'] = df_ofertas['UF do Local de Oferta'].map(mapa_regioes)

# Cria a coluna 'periodo' para usar como eixo X
df_ofertas['periodo'] = df_ofertas['Ano'].astype(int).astype(str) + '-' + df_ofertas['Semestre'].astype(int).astype(str)

# --- 3. EXIBIÇÃO DO DATAFRAME FINAL ---
print("\n--- DataFrame final, pronto para a visualização ---")
# Selecionando as colunas mais relevantes para a exibição
colunas_relevantes = [
    'periodo', 
    'Região', 
    'UF do Local de Oferta', 
    'Nome do Curso', 
    'Nota de Corte Grupo Preferência'
]

display(df_ofertas[colunas_relevantes])


# %%
# CÓDIGO PARA GERAR O GRÁFICO de Nota de Corte por Período e Região
import matplotlib.pyplot as plt
import seaborn as sns

# Supondo que o DataFrame 'df_ofertas' já foi criado e preparado na célula anterior
# com as colunas 'periodo', 'Região' e 'Nota de Corte Grupo Preferência'

# --- GERAÇÃO DO GRÁFICO DE BOXPLOT AGRUPADO ---
plt.figure(figsize=(20, 10))
sns.set_theme(style="whitegrid")

ax = sns.boxplot(
    data=df_ofertas,
    x='periodo',
    y='Nota de Corte Grupo Preferência',
    hue='Região', # <-- Agrupa as 5 regiões dentro de cada período
    hue_order=['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'], # Ordem na legenda
    palette='viridis'
)

# --- MELHORANDO O LAYOUT E OS TÍTULOS ---
ax.set_title('Evolução da Distribuição da Nota de Corte por Período e Região', fontsize=20)
ax.set_xlabel('Período (Ano-Semestre)', fontsize=14)
ax.set_ylabel('Nota de Corte', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
ax.legend(title='Região')

plt.tight_layout()
plt.show()

# %%