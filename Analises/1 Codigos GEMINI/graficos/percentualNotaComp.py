# %%
# ANÁLISE DE PERFIL: Qualificação dos Candidatos por Região (Gráfico de Barras Agrupadas)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CARREGAMENTO E CONFIGURAÇÃO ---
PASTA_DADOS = 'planilhas'
NOME_ARQUIVO = 'DfInscricoesOrganizadoUFComp.csv'
caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)

try:
    df_inscricoes = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{NOME_ARQUIVO}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
    exit()

# --- 2. LIMPEZA E PREPARAÇÃO DOS DADOS (Mesma lógica da análise anterior) ---
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

# --- 3. AGREGAÇÃO DOS DADOS POR REGIÃO E PERÍODO ---
contagem_detalhada = pd.crosstab(
    index=[df_inscricoes['Região'], df_inscricoes['periodo']],
    columns=df_inscricoes['Qualificado']
)
contagem_detalhada['Percentual Acima da Corte'] = (
    contagem_detalhada['Acima da Corte'] / (contagem_detalhada['Acima da Corte'] + contagem_detalhada['Abaixo da Corte'])
) * 100
df_plot = contagem_detalhada.reset_index()


# --- 4. GERAÇÃO DO GRÁFICO DE BARRAS AGRUPADAS ---
plt.figure(figsize=(20, 10))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    data=df_plot,
    x='periodo',
    y='Percentual Acima da Corte',
    hue='Região',
    # Garante a ordem alfabética das regiões na legenda e nas cores
    hue_order=sorted(df_plot['Região'].unique()),
    palette='Set2'
)

ax.set_title('Evolução do Percentual de Candidatos Qualificados por Região', fontsize=20)
ax.set_xlabel('Período (Ano-Semestre)', fontsize=14)
ax.set_ylabel('Candidatos Acima da Corte (%)', fontsize=14)
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Região', fontsize=12)
plt.tight_layout()
plt.show()






# %%
# CÓDIGO PARA GERAR O DATAFRAME DE RESUMO: Qualificação dos Candidatos por Região e Período
import pandas as pd
import os

# --- 1. CARREGAMENTO E CONFIGURAÇÃO ---
PASTA_DADOS = 'planilhas'
NOME_ARQUIVO = 'DfInscricoesOrganizadoUFComp.csv'
caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)

try:
    df_inscricoes = pd.read_csv(caminho_arquivo)
    print(f"Arquivo '{NOME_ARQUIVO}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
    # Adicionando um fallback para o código não quebrar se o arquivo não for encontrado no seu ambiente
    if 'df_inscricoes_comp' in locals() or 'df_inscricoes_comp' in globals():
        df_inscricoes = df_inscricoes_comp.copy()
    else:
        exit()

# --- 2. LIMPEZA E PREPARAÇÃO DOS DADOS ---
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

# --- 3. AGREGAÇÃO DOS DADOS POR REGIÃO E PERÍODO ---
print("\nGerando a tabela de resumo...")
# Cria uma tabela cruzada para contar as inscrições
contagem_detalhada = pd.crosstab(
    index=[df_inscricoes['Região'], df_inscricoes['periodo']],
    columns=df_inscricoes['Qualificado']
)

# Calcula o percentual de candidatos 'Acima da Corte'
contagem_detalhada['Percentual Acima da Corte'] = (
    contagem_detalhada['Acima da Corte'] / (contagem_detalhada['Acima da Corte'] + contagem_detalhada['Abaixo da Corte'])
) * 100

# Prepara o DataFrame final para visualização
df_resumo_qualificacao = contagem_detalhada.reset_index().sort_values(by=['Região', 'periodo'])




df=pd.pivot_table(

    data=df_resumo_qualificacao,
    index=['periodo'],
    columns=['Região'],
    values= 'Percentual Acima da Corte'

)

df.columns.name=None
df=df.reset_index()

df.to_csv('percentualCompAcimaCorte.csv',index=False)

df

# %%
# SOLUÇÃO DEFINITIVA: Gerando a imagem da tabela com Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Etapa 1: Preparar o DataFrame 'df' ---
# (Incluí o código de preparação para que esta célula seja independente)
try:
    PASTA_DADOS = 'planilhas'
    NOME_ARQUIVO = 'DfInscricoesOrganizadoUFComp.csv'
    caminho_arquivo = os.path.join(PASTA_DADOS, NOME_ARQUIVO)
    df_inscricoes = pd.read_csv(caminho_arquivo)
    
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
    
    contagem_detalhada = pd.crosstab(
        index=[df_inscricoes['Região'], df_inscricoes['periodo']],
        columns=df_inscricoes['Qualificado']
    )
    contagem_detalhada['Percentual Acima da Corte'] = (
        contagem_detalhada['Acima da Corte'] / (contagem_detalhada['Acima da Corte'] + contagem_detalhada['Abaixo da Corte'])
    ) * 100
    df_resumo_qualificacao = contagem_detalhada.reset_index()

    df = pd.pivot_table(
        data=df_resumo_qualificacao,
        index=['periodo'],
        columns=['Região'],
        values='Percentual Acima da Corte'
    )
    print("DataFrame 'df' final pronto para ser desenhado.")
except Exception as e:
    print(f"Ocorreu um erro ao preparar o DataFrame: {e}")
    df = pd.DataFrame({'Coluna Exemplo': [1, 2]}) # Fallback para o código não quebrar
# --- Fim da preparação do df ---


# --- Etapa 2: Desenhar e Salvar a Tabela com Matplotlib ---

# 1. Prepara os dados para a tabela (formatando como texto com '%')
df_para_imagem = df.fillna('-').applymap(lambda x: f'{x:.1f}%' if isinstance(x, (int, float)) else x)

# 2. Cria uma figura e um eixo vazios
fig, ax = plt.subplots(figsize=(12, 5)) 

# Esconde os eixos do gráfico (não queremos um gráfico, só a tabela)
ax.axis('off')
ax.axis('tight')

# 3. "Desenha" a tabela no eixo
tabela = ax.table(
    cellText=df_para_imagem.values,
    colLabels=df_para_imagem.columns,
    rowLabels=df_para_imagem.index,
    loc='center',
    cellLoc='center'
)
tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.8) # Ajusta o tamanho da tabela

# Adiciona um título à figura
fig.suptitle('Percentual de Candidatos Qualificados por Região e Período', fontsize=16, y=0.9)

# 4. Salva a figura como uma imagem
nome_arquivo_imagem = 'planilhas/tabela_matplotlib.png'
plt.savefig(nome_arquivo_imagem, dpi=300, bbox_inches='tight', pad_inches=0.4)

print(f"\nImagem da tabela salva com sucesso em: '{nome_arquivo_imagem}'")
plt.show()

# %%