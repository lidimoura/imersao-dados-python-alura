import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Configuracao da Pagina ---
st.set_page_config(page_title="Data Science Salary Analytics", layout="wide")

# --- Estilizacao CSS (Insight Box e Tons Profissionais) ---
st.markdown("""
    <style>
    .main { background-color: #faf8f5; color: #2c1e1a; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-size: 16px; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #5d4037; }
    h1, h2, h3 { color: #5d4037; font-family: 'Segoe UI', sans-serif; }
    .insight-box { 
        background-color: #f4ede4; 
        padding: 18px; 
        border-radius: 8px; 
        border-left: 5px solid #8b4513; 
        color: #3e2723; 
        font-size: 15px;
        margin-top: 10px; 
        margin-bottom: 20px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CARREGAMENTO DOS DADOS ---
@st.cache_data
def load_data():
    if os.path.exists("dados-imersao-final.csv"):
        return pd.read_csv("dados-imersao-final.csv")
    return pd.DataFrame()

df = load_data()

# --- SIDEBAR: IDIOMA, BIO E LINKS ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

if lang == "PT-BR":
    st.sidebar.title("Lídi Moura")
    st.sidebar.markdown("""
    **Arquiteta de Solucoes e Especialista em Dados**
    
    Especialista em Data Science pelo programa **ONE (Alura/Oracle)**. 
    Em especializacao de **IA (Alura/Santander)** e preparacao para certificacoes internacionais **OCI** e **MySQL**.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Acessos e Contato")
    st.sidebar.link_button("Repositorio no GitHub", "https://github.com/lidimoura/nome-do-seu-repo-de-salarios")
    st.sidebar.link_button("Relatorio Tecnico (Colab)", "https://lidimoura.github.io/nome-do-seu-repo-de-salarios/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    
    title = "Dashboard de Analise de Salarios - Data Science"
    subtitle = "Inteligencia Competitiva e Tendencias de Mercado"
    
    sec_context_title = "Visao Geral e Metodologia"
    sec_context_text = """
    **Objetivo:** Gerar insights estrategicos sobre as tendencias salariais globais na area de dados, fornecendo inteligencia competitiva para profissionais e recrutadores.
    
    **Stack Tecnologica e ETL:** O projeto utilizou Python e Pandas para a limpeza rigorosa de dados, tratamento de nulos e normalizacao de categorias estruturais (como a correcao da coluna 'senoridade'). A analise permite avaliar variaveis criticas como distribuicao por senioridade, modelo de trabalho (remoto/presencial) e localizacao geografica.
    """
    
    rec_title = "Insights e Resultados Criticos"
    rec_text = """
    **Padroes de Mercado Identificados:**
    * **Gap de Senioridade:** Disparidades salariais significativas entre niveis (Senior vs. Junior apresentam diferenca media de ~$80k USD).
    * **Contratos:** O modelo Full-Time domina as ofertas de maior valorizacao financeira.
    * **Flexibilidade:** A variacao de salarios esta fortemente atrelada ao pais de residencia e ao formato remoto.
    """
    
    tab1_label = "Distribuicao Salarial"
    tab2_label = "Top Cargos"
    tab3_label = "Modelos de Trabalho"
    tab4_label = "Mapa Global"
    tab5_label = "Dados Detalhados"
    
    filter_header = "Filtros Interativos"
    footer_text = "Transparencia e Vibe Coding: Analise tecnica, estrategia de limpeza e interpretacao de dados sao de autoria de Lidi Moura (orientada pela Imersao Alura). Estruturacao otimizada com IA."

else:
    st.sidebar.title("Lídi Moura")
    st.sidebar.markdown("""
    **Solutions Architect and Data Specialist**
    
    Data Science Specialist through the **ONE program (Alura/Oracle)**. 
    Currently specializing in **AI (Alura/Santander)** and preparing for **OCI** and **MySQL** international certifications.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Links and Contact")
    st.sidebar.link_button("Project Repository", "https://github.com/lidimoura/nome-do-seu-repo-de-salarios")
    st.sidebar.link_button("Technical Report (Colab)", "https://lidimoura.github.io/nome-do-seu-repo-de-salarios/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    
    title = "Data Science Salary Analytics Dashboard"
    subtitle = "Competitive Intelligence and Market Trends"
    
    sec_context_title = "Overview and Methodology"
    sec_context_text = """
    **Objective:** Generate strategic insights on global salary trends in the data field, providing competitive intelligence for professionals and recruiters.
    
    **Tech Stack and ETL:** The project used Python and Pandas for rigorous data cleaning, handling nulls, and normalizing structural categories. The analysis evaluates critical variables such as seniority distribution, work models (remote/on-site), and geographic location.
    """
    
    rec_title = "Critical Insights and Results"
    rec_text = """
    **Identified Market Patterns:**
    * **Seniority Gap:** Significant salary disparities between levels (Senior vs. Junior show an average difference of ~$80k USD).
    * **Contracts:** The Full-Time model dominates the highest financial valuation offers.
    * **Flexibility:** Salary variation is strongly linked to the country of residence and remote work formats.
    """
    
    tab1_label = "Salary Distribution"
    tab2_label = "Top Roles"
    tab3_label = "Work Models"
    tab4_label = "Global Map"
    tab5_label = "Detailed Data"
    
    filter_header = "Interactive Filters"
    footer_text = "Transparency & Vibe Coding: Technical analysis, cleaning strategy, and data interpretation by Lidi Moura. Structure optimized with AI."

# --- FILTROS NA SIDEBAR ---
st.sidebar.header(filter_header)

if not df.empty:
    anos_disponiveis = sorted(df['ano'].unique())
    anos_selecionados = st.sidebar.multiselect("Ano / Year", anos_disponiveis, default=anos_disponiveis)

    senioridades_disponiveis = sorted(df['senoridade'].unique())
    senioridades_selecionadas = st.sidebar.multiselect("Senioridade / Seniority", senioridades_disponiveis, default=senioridades_disponiveis)

    contratos_disponiveis = sorted(df['contrato'].unique())
    contratos_selecionados = st.sidebar.multiselect("Contrato / Contract Type", contratos_disponiveis, default=contratos_disponiveis)

    tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
    tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa / Company Size", tamanhos_disponiveis, default=tamanhos_disponiveis)

    df_filtrado = df[
        (df['ano'].isin(anos_selecionados)) &
        (df['senoridade'].isin(senioridades_selecionadas)) &
        (df['contrato'].isin(contratos_selecionados)) &
        (df['tamanho_empresa'].isin(tamanhos_selecionados))
    ]
else:
    df_filtrado = pd.DataFrame()

# --- CABECALHO ---
st.title(title)
st.markdown(f"### {subtitle}")
st.divider()

# --- SITUACAO E TRATAMENTO ---
st.header(sec_context_title)
st.write(sec_context_text)
st.divider()

# --- RECOMENDACAO E KPIs ---
col_rec, col_kpi = st.columns([1.5, 1])
with col_rec:
    st.header(rec_title)
    st.info(rec_text)

with col_kpi:
    st.header("KPIs Globais" if lang == "PT-BR" else "Global KPIs")
    if not df_filtrado.empty:
        salario_medio = df_filtrado['usd'].mean()
        salario_maximo = df_filtrado['usd'].max()
        total_registros = df_filtrado.shape[0]
        cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
    else:
        salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

    col_k1, col_k2 = st.columns(2)
    col_k1.metric("Media / Average", f"${salario_medio:,.0f}")
    col_k1.metric("Maximo / Maximum", f"${salario_maximo:,.0f}")
    col_k2.metric("Registros / Records", f"{total_registros:,}")
    col_k2.metric("Cargo Frequente / Top Role", cargo_mais_frequente)

st.divider()

# --- ABAS DE GRAFICOS (PLOTLY) ---
if not df_filtrado.empty:
    tab1, tab2, tab3, tab4, tab5 = st.tabs([tab1_label, tab2_label, tab3_label, tab4_label, tab5_label])

    with tab1:
        st.subheader(tab1_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'O grafico abaixo demonstra a distribuicao de frequencia dos salarios anuais em USD, revelando a concentracao de profissionais em faixas especificas e ajudando a identificar benchmarks de mercado.' if lang == 'PT-BR' else 'The chart below demonstrates the frequency distribution of annual salaries in USD, revealing professional concentration in specific ranges.'}</div>", unsafe_allow_html=True)
        grafico_hist = px.histogram(df_filtrado, x='usd', nbins=30, 
                                    color_discrete_sequence=['#8b4513'],
                                    labels={'usd': 'Faixa Salarial (USD)' if lang == 'PT-BR' else 'Salary Range (USD)'})
        st.plotly_chart(grafico_hist, use_container_width=True)

    with tab2:
        st.subheader(tab2_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Aqui, podemos visualizar os cargos com maior remuneracao media, destacando oportunidades de carreira com melhor potencial salarial.' if lang == 'PT-BR' else 'Here we can visualize the roles with the highest average compensation, highlighting career opportunities with the best salary potential.'}</div>", unsafe_allow_html=True)
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(top_cargos, x='usd', y='cargo', orientation='h',
                                color='usd', color_continuous_scale='YlOrBr',
                                labels={'usd': 'Media Anual (USD)' if lang == 'PT-BR' else 'Annual Average (USD)', 'cargo': ''})
        st.plotly_chart(grafico_cargos, use_container_width=True)

    with tab3:
        st.subheader(tab3_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Este grafico evidencia a proporcao do trabalho remoto na area de dados, um fator cada vez mais importante na tomada de decisao profissional e retencao de talentos.' if lang == 'PT-BR' else 'This chart shows the proportion of remote work in the data field, an increasingly important factor in professional decision-making and talent retention.'}</div>", unsafe_allow_html=True)
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(remoto_contagem, names='tipo_trabalho', values='quantidade', hole=0.5, color_discrete_sequence=['#8b4513', '#cd853f', '#f4a460'])
        grafico_remoto.update_traces(textinfo='percent+label')
        st.plotly_chart(grafico_remoto, use_container_width=True)

    with tab4:
        st.subheader(tab4_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Mapa mundial evidenciando a distribuicao geografica dos salarios medios (USD) para Cientistas de Dados.' if lang == 'PT-BR' else 'World map highlighting the geographic distribution of average salaries (USD) for Data Scientists.'}</div>", unsafe_allow_html=True)
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            grafico_paises = px.choropleth(media_ds_pais, locations='residencia_iso3', color='usd',
                                           color_continuous_scale='YlOrBr',
                                           labels={'usd': 'Media (USD)' if lang == 'PT-BR' else 'Average (USD)'})
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("Nenhum Cientista de Dados encontrado com os filtros atuais." if lang == "PT-BR" else "No Data Scientists found with current filters.")

    with tab5:
        st.subheader(tab5_label)
        st.dataframe(df_filtrado, use_container_width=True)

else:
    st.error("Erro: Arquivo 'dados-imersao-final.csv' nao encontrado no repositorio." if lang == "PT-BR" else "Error: 'dados-imersao-final.csv' not found in repository.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 13px; line-height: 1.5;'><b>{footer_text}</b><br>Desenvolvendo tecnologia sustentavel para reflorestar o digital.</div>", unsafe_allow_html=True)
