import pandas as pd # Biblioteca para manipulação e organização dos dados
import feedparser # Biblioteca para ler RSS feeds de notícias
import requests # Biblioteca para realizar pedidos HTTP a APIs (opcional, mas útil)
import os
import re

# Dicionário com os URLs de cada Website onde se extraem/leêm notícias financeiras + Section de onde está exposta essa noticia
URLs = {"Financial Times": , "Bloomberg": , "Reuters": , "Yahoo": , "S&P": , "Fitch": }

# Links de Websites de News
rss_url = "https://www.ft.com/rss/home" # URL do RSS feed do Financial Times
# Exemplos de RSS Feeds do Financial Times: Notícias principais: https://www.ft.com/rss/home . Mundo: https://www.ft.com/rss/world . Mercados: https://www.ft.com/rss/markets . Empresas: https://www.ft.com/rss/companies . Tecnologia: https://www.ft.com/rss/technology . 


# Definir uma função logo a partir daqui que recebe como entrada o link; Dar os links como dicionário para repetir as mesmas operações para cada link através de um ciclo; Registar a fonte proveniente das noticias numa coluna do DataFrame
# Código para Ler o RSS Feed: O objetivo deste passo é aceder ao feed e visualizar as informações básicas das notícias (antes de as organizar num DataFrame).
def create_news_df_by_link(df: DataFrame | None = None, rss_url: str = "", source: str = ""):
    feed = feedparser.parse(rss_url) # Aceder ao RSS Feed do Financial Times e Ler o conteúdo do RSS feed #O que é um RSS Feed? Um RSS (Really Simple Syndication) é um formato padronizado que permite aos websites de notícias disponibilizar os seus conteúdos mais recentes de forma estruturada (O Financial Times disponibiliza vários RSS feeds para diferentes secções do seu site.). Cada item do feed normalmente inclui:📰 Título , 📅 Data de publicação , 📝 Resumo (summary) , 🔗 Link para a notícia , 👤 Autor (quando disponível) .
    #print("Título do Feed:", feed.feed.title, "\nN.º de notícias encontradas:", len(feed.entries)) # Verificar o título do feed
    
    # Create DataFrame
    news_data = [] # Criar uma lista para armazenar os dados das notícias
    for entry in feed.entries: # Percorrer cada notícia no feed
        news_item = {
            "source": source,
            "published": entry.get("published", None),
            "title": entry.get("title", None),
            "summary": entry.get("summary", None),
            "link": entry.get("link", None),
            #"author": entry.get("author", "N/A")  # Caso o autor não esteja disponível
        }
        news_data.append(news_item)
    df_news = pd.DataFrame(news_data) # Criar DataFrame com as notícias
    df_news["published"] = pd.to_datetime(df_news["published"], errors="coerce") # Converter a coluna de datas para o formato datetime

    print(df_news.head()) # Visualizar as primeiras linhas do DataFrame
    # Visualizar as primeiras 3 notícias
    # for i, entry in enumerate(feed.entries[:3], start=1):
    #     print(f"\nNotícia {i} : Data de publicação {entry.published}")
    #     #print("Author:", entry.author) # When available
    #     print("Título:", entry.title)
    #     print("Resumo:", entry.summary)
    #     print("Link:", entry.link)
    
    return df

# df_news = df_news.sort_values(by="published", ascending=False) # Ordenar por data
# df_filtered = df_news[df_news["title"].str.contains("market", case=False, na=False)] # Filtrar notícias por palavra-chave



#3. Filtrar Notícias com Base em Palavras-Chave

# Definir Palavras-Chave / Keywords

# Tirar keywords de livros por exemplo
# Indicadores/Conceitos/Termos Financeiros/Risco [Literacia Financeira] (Rácios, profits/Losses, VaR, Delta, Spread, Ratings, Greeks, etc)
financial_terms = []


# Commodities
commodities_kws = ["commodities", "commodity market", "oil", "crude oil", "brent", "WTI", "natural gas", "LNG", "coal", "gold", "silver", "copper", "aluminium", "nickel", "zinc", "iron ore", "steel", "lithium", "cobalt", "rare earths", "agriculture", "agricultural commodities", "wheat", "corn", "soybeans", "sugar", "coffee", "cocoa", "cotton", "palm oil", "OPEC", "OPEC+", "energy prices", "metals", "mining", "futures", "spot price", "commodity trading"]

# Stocks # Stocks, Futuros e ETFs # Options # Crypto
stocks_kws = [
        # Termos gerais do mercado acionista
        "stock", "stocks", "equity", "equities", "share", "shares", "stock market", "equity market", "listed company", "market capitalization", "market cap",

        # Instrumentos financeiros
        "ETF", "exchange-traded fund", "index fund", "futures", "equity futures", "options", "derivatives", "ADR", "GDR", "warrants", "contracts for difference", "CFD",

        # Atividade de mercado
        "IPO", "initial public offering", "secondary offering", "listing", "delisting", "trading volume", "liquidity", "bull market", "bear market", "rally", "sell-off", "price-to-earnings", "P/E", "earnings per share", "EPS", "dividend", "dividend yield", "share buyback", "capital raise",

        # Setores e estilos de investimento
        "growth stocks", "value stocks", "small cap", "mid cap", "large cap", "blue chip", "sector rotation", "momentum", "volatility", "VIX"
    ]


# Bolsas de Valores (Exchanges)
exchanges_kws = ["stock exchange", "exchange", "bourse", "trading venue", "IPO", "initial public offering", "listing", "delisting", "equity trading", "market capitalization", "shares", "equities", "New York Stock Exchange", "NYSE", "Nasdaq Exchange", "London Stock Exchange", "LSE", "Euronext", "Deutsche Börse", "Hong Kong Exchange", "HKEX", "Shanghai Stock Exchange", "Tokyo Stock Exchange", "TSE", "B3 Brazil"]


# Índices (Indexes) # Índices acionistas (-> Retirar do Excel YF) # Adicionar indices de spread de crédito, indices de interest rates (yield curves), etc
indexes_kws = ["stock index", "equity index", "benchmark index", "S&P 500", "Dow Jones", "Nasdaq", "Nasdaq 100", "FTSE 100", "FTSE 250", "Euro Stoxx 50", "Stoxx Europe 600", "DAX", "CAC 40", "IBEX 35", "PSI 20", "Nikkei 225", "Hang Seng", "Shanghai Composite", "MSCI", "MSCI World", "MSCI Emerging Markets", "VIX", "volatility index"]


# Interest Rates / Risk-free rates

# Obrigações (Bonds & Fixed Income)
bonds_kws = ["bond", "bonds", "government bond", "sovereign bond", "corporate bond", "treasury", "Treasury yield", "yield", "bond yield", "yield curve", "inverted yield curve", "fixed income", "debt securities", "note", "bill", "gilts", "bund", "OAT", "BTP", "municipal bond", "emerging market debt", "duration", "coupon", "bond issuance", "primary market", "secondary market", "spread tightening", "spread widening"]


# Mercados de Crédito (Credit Markets)
credit_kws = ["credit", "credit market", "credit risk", "credit spread", "spreads", "high yield", "high-yield", "junk bonds", "investment grade", "leveraged loans", "loan market", "syndicated loans", "credit default swap", "CDS", "default", "distressed debt", "refinancing", "debt issuance", "corporate debt", "sovereign debt", "private credit", "structured credit", "collateralized loan obligation", "CLO", "collateralized debt obligation", "CDO", "securitization", "asset-backed securities", "ABS", "mortgage-backed securities", "MBS", "liquidity", "leverage", "deleveraging", "covenant", "covenant-lite", "rating", "credit rating", "downgrade", "upgrade", "Moody's", "S&P", "Fitch"]


# Empresas (Companies & Corporate Activity) -> Ler a lista de Excel sobre empresas (Tentar encontrar mais se for necessário) # Incluir Tickers
companies_kws = ["company", "corporate", "earnings", "revenue", "profit", "net income", "EBITDA", "guidance", "outlook", "merger", "acquisition", "M&A", "takeover", "buyout", "private equity", "venture capital", "IPO", "spin-off", "dividend", "share buyback", "capital increase", "restructuring", "bankruptcy", "insolvency", "shareholder", "stake", "valuation", "market cap"]

# Setores / Sectores -> Retirar do Excel YF ou arranjar um dataset universal para esta nomenclatura (CAE, ICB, GICS, S&P, etc)
sectors_kws = ["energy"] 








# Financial Institutions / Bancos
financial_institutions_kws = [
        # Termos gerais
        "bank", "banks", "banking", "lender", "lenders", "financial institution", "commercial bank", "investment bank", "retail bank", "universal bank", "credit institution", "depositary institution",

        # Tipos de entidades financeiras
        "asset manager", "wealth manager", "private bank", "hedge fund", "pension fund", "insurance company", "reinsurance", "broker", "dealer", "custodian", "clearing house", "prime broker",

        # Atividades bancárias
        "loan", "lending", "mortgage", "deposit", "capital adequacy", "liquidity ratio", "net interest margin", "NIM", "non-performing loan", "NPL", "provisions", "capital buffer", "Tier 1", "CET1",

        # Regulação e supervisão
        "Basel III", "Basel IV", "stress test", "banking regulation", "prudential regulation", "resolution", "bail-in", "bailout",

        # Exemplos de bancos globais
        "JPMorgan", "Goldman Sachs", "Morgan Stanley", "Citigroup", "Bank of America", "HSBC", "Barclays", "Deutsche Bank", "BNP Paribas", "Credit Agricole", "Santander", "BBVA", "UBS", "Credit Suisse", "ING", "UniCredit", "Intesa Sanpaolo", "Wells Fargo", "Standard Chartered"
    ]


# Política Monetária e Bancos Centrais (Opcional mas Relevante) # Eventos Macroeconómicos
macro_kws = ["central bank", "monetary policy", "interest rate", "interest rates", "rate hike", "rate cut", "inflation", "deflation", "recession", "economic growth", "quantitative easing", "QE", "quantitative tightening", "QT"]
    [
        # Conflitos e geopolítica
        "war", "conflict", "military conflict", "geopolitics", "geopolitical", "invasion", "sanctions", "trade war", "ceasefire", "peace talks", "NATO", "United Nations", "UN", "Middle East", "Ukraine", "Russia", "China-Taiwan", "South China Sea", "Gaza", "Israel", "Iran",

        # Choques económicos e crises
        "economic shock", "financial crisis", "banking crisis", "sovereign debt crisis", "credit crunch", "market turmoil", "market volatility", "systemic risk", "contagion", "recession", "economic downturn", "slowdown", "stagflation", "depression", "default", "sovereign default",

        # Política económica e monetária
        "stimulus", "fiscal policy", "government spending", "austerity", "budget deficit", "public debt", "interest rate decision", "rate hike", "rate cut", "quantitative easing", "QE", "quantitative tightening", "QT",

        # Instituições e bancos centrais
        "Federal Reserve", "Fed", "European Central Bank", "ECB", "Bank of England", "BoE", "Bank of Japan", "BoJ", "People's Bank of China", "PBOC", "IMF", "International Monetary Fund", "World Bank", "WTO", "OECD"
    ]


# Countries/Países/Regiões Geográficas (Procurar lista na web) Site UNSD
countries_kws = ["Portugal"] 


# Themes/Keyword Categories: 
    # Financial concepts/terms/names:
    # Commodities:
    # Stocks/Ações (Stocks, Futures e ETFs):
    # Indexes/Índices:
    # Exchanges/Currencies:
    # Bonds/Obrigações:
    # Credit/Crédito:
    # Companies/Empresas:
    # Sectors/Setores:
    # Financial Institutions / Banks:
    # Countries/Regions/Geographic Locations: 
    # Macro:
    # Governments Policies/Laws:
    # Regulation/Normative Agencies/Institutions:
    # Non-Governamental Organizations (ONGs):


keywords_dict = {
    "Financial terms": ,
    "Commodities": ,"Stocks": ,"Currencies": ,"Exchanges": ,"Indexes": ,
    "Bonds": ,"Credit": ,
    "Companies": ,
    "Macro": 
    }





# Criar um Padrão de Pesquisa Global : Caso desejes criar um padrão regex que inclua todas as palavras-chave:


all_keywords = [ kw for kws in keywords_dict.values() for kw in kws ]

pattern = "|".join(keywords) # Criar um padrão de pesquisa com as palavras-chave
pattern = "|".join(re.escape(keyword) for keyword in all_keywords)







df_combined["relevant"] = ( df_combined["title"].str.contains(pattern, case=False, na=False) | df_combined["summary"].str.contains(pattern, case=False, na=False) ) # alternativamente, podes manter todas as notícias e adicionar uma coluna indicadora: Assim, poderás filtrar facilmente no Excel.
df_filtered = df_combined[df_combined["relevant"]] # Manter apenas as notícias relevantes (opcional)

df_filtered = df_combined[  df_combined["title"].str.contains(pattern, case=False, na=False) | df_combined["summary"].str.contains(pattern, case=False, na=False) ] # Filtrar notícias cujo título ou resumo contenham as palavras-chave
#df_filtered.to_excel("financial_times_news_filtered.xlsx", index=False) # Guardar Apenas as Notícias Filtradas



# 6. (Opcional) Identificar a Categoria da Notícia : Se quiseres uma análise mais avançada, podes também identificar a categoria associada a cada notícia:
# Graças ao uso do dicionário, a função de categorização torna-se muito mais simples e escalável:
    

def categorize_news(text, keywords_dict):
    """
    Categoriza uma notícia com base nas palavras-chave.
    
    Parameters:
        text (str): Texto da notícia (título + resumo).
        keywords_dict (dict): Dicionário com categorias e palavras-chave.
    
    Returns:
        list: Lista de categorias correspondentes.
    """
    text = text.lower()
    matched_categories = []

    for category, keywords in keywords_dict.items():
        for keyword in keywords:
            if keyword.lower() in text:
                matched_categories.append(category)
                break  # Evita múltiplas correspondências na mesma categoria

    return matched_categories if matched_categories else ["Other"]



# Aplicar a Categorização ao DataFrame

# Combinar título e resumo
df_combined["text"] = ( df_combined["title"].fillna('') + " : " + df_combined["summary"].fillna('') )

# Aplicar a categorização
df_combined["categories"] = df_combined["text"].apply(
    lambda x: categorize_news(x, keywords_dict)
)



# (Opcional) Converter a lista de categorias em texto
df_combined["categories"] = df_combined["categories"].apply(
    lambda x: ", ".join(x)
)

df_combined["category"] = ( df_combined["title"].fillna('') + " " + df_combined["summary"].fillna('') ).apply(categorize_news)



# Filtrar Notícias por Categoria
# Exemplo: selecionar apenas notícias sobre instituições financeiras
#Filtrar Notícias com Base em Palavras-Chave: Para evitar notícias irrelevantes, podemos filtrar os artigos com base em um conjunto de palavras-chave presentes no título ou no resumo.


df_financials = df_combined[
    df_combined["categories"].str.contains("Financial_Institutions", na=False)
]





























# Exportar para Excel

file_name = "financial_times_news.xlsx" # Nome do ficheiro Excel
# Verificar se o ficheiro já existe
if os.path.exists(file_name):
    df_existing = pd.read_excel(file_name)
    df_existing["published"] = pd.to_datetime(df_existing["published"], errors="coerce")
    df_combined = pd.concat([df_existing, df_news], ignore_index=True) # Combinar dados antigos com os novos
else: df_combined = df_news
df_combined = df_combined.drop_duplicates(subset="link") # Remover duplicados com base no link
df_combined = df_combined.sort_values(by="published", ascending=False) # Ordenar por data (mais recentes primeiro)
df_combined.to_excel(file_name, index=False) # Exportar/Guardar para Excel: Guardar os dados permite utilizá-los posteriormente
print(f"Ficheiro '{file_name}' atualizado com sucesso!")




