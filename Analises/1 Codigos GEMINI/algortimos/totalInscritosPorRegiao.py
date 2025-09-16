# %%
# ANÁLISE: Total de Inscrições por Região e Período
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- 1. CARREGAMENTO E PREPARAÇÃO DOS DADOS ---
# (Esta parte é a mesma que o seu código já faz)
PASTA_DADOS = 'planilhas'
NOME_ARQUIVO = 'DfInscricoesOrganizadoUFComp.csv'
caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)

try:
    df_inscricoes = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{NOME_ARQUIVO}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
    exit()

colunas_nota = ['Média nota Enem', 'Nota Corte Grupo Preferência']
for col in colunas_nota:
    if pd.api.types.is_string_dtype(df_inscricoes[col]):
        df_inscricoes[col] = df_inscricoes[col].str.replace(',', '.', regex=False).astype(float)

df_inscricoes['Qualificado'] = df_inscricoes['Média nota Enem'] >= df_inscricoes['Nota Corte Grupo Preferência']
df_inscricoes['Qualificado'] = df_inscricoes['Qualificado'].map({True: 'Acima da Corte', False: 'Abaixo da Corte'})

mapa_regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}
df_inscricoes['Região'] = df_inscricoes['UF do Local de Oferta'].map(mapa_regioes)
df_inscricoes['periodo'] = df_inscricoes['Ano do processo seletivo'].astype(int).astype(str) + '-' + df_inscricoes['Semestre do processo seletivo'].astype(int).astype(str)

# --- 2. AGREGAÇÃO PARA OBTER O TOTAL DE INSCRITOS ---
print("\nGerando a tabela de resumo com o total de inscritos...")
contagem_detalhada = pd.crosstab(
    index=[df_inscricoes['Região'], df_inscricoes['periodo']],
    columns=df_inscricoes['Qualificado']
)

# --- MUDANÇA PRINCIPAL AQUI ---
# Criamos a coluna com a SOMA de inscritos, em vez do percentual
contagem_detalhada['Total Inscrições'] = contagem_detalhada['Acima da Corte'] + contagem_detalhada['Abaixo da Corte']

df_resumo_total = contagem_detalhada.reset_index()

# --- 3. PIVOTANDO PARA O FORMATO FINAL ---
# Agora usamos 'Total Inscrições' como os valores da tabela
df = pd.pivot_table(
    data=df_resumo_total,
    index=['periodo'],
    columns=['Região'],
    values='Total Inscrições' # <-- MUDANÇA AQUI
)

df.columns.name = None
df = df.reset_index()

print("\n--- DataFrame Final: Total de Inscrições por Região e Período ---")
display(df)

# Salva o novo CSV
df.to_csv('planilhas/totalInscritosCompPorRegiao.csv', index=False)
print("\nArquivo 'totalInscritosCompPorRegiao.csv' salvo com sucesso.")


# --- 4. GERANDO A IMAGEM DA NOVA TABELA ---
# Prepara os dados para a imagem (formatando como números inteiros)
df_para_imagem = df.fillna(0).astype({'Centro-Oeste': int, 'Nordeste': int, 'Norte': int, 'Sudeste': int, 'Sul': int})

fig, ax = plt.subplots(figsize=(12, 5)) 
ax.axis('off')
ax.axis('tight')

tabela = ax.table(
    cellText=df_para_imagem.values,
    colLabels=df_para_imagem.columns,
    loc='center',
    cellLoc='center'
)
tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.8) 
fig.suptitle('Total de Inscrições em Cursos de Computação por Região e Período', fontsize=16, y=0.9)

nome_arquivo_imagem = 'planilhas/tabela_total_inscritos.png'
plt.savefig(nome_arquivo_imagem, dpi=300, bbox_inches='tight', pad_inches=0.4)

print(f"\nImagem da tabela salva com sucesso em: '{nome_arquivo_imagem}'")
plt.show()

# %%