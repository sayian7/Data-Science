import requests
import feedparser
import pandas as pd

# URL do RSS do Financial Times
urls = ["https://www.ft.com/rss/home", "https://www.ft.com/rss/world", "https://www.ft.com/rss/markets", "https://www.ft.com/rss/companies", "https://www.ft.com/rss/technology", "https://www.ft.com/rss/middle-east-war"]
# Lista para armazenar os dados das notícias
news_data = []

# Cabeçalhos HTTP com User-Agent
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

# Cabeçalho com User-Agent
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
# }


# Recolha das notícias
for rss_url in urls:
    try:
        # Fazer o pedido HTTP ao RSS
        response = requests.get(rss_url, headers=headers, timeout=10)
        response.raise_for_status()  # Lança erro se o status não for 200

        # Interpretar o conteúdo do RSS
        feed = feedparser.parse(response.content)
        
        # Verificar se houve algum erro no parsing
        if feed.bozo:
            print(f"Erro ao processar o feed {rss_url}: {feed.bozo_exception}")
            continue

        print("Título do Feed:", feed.feed.get("title", "N/A"))
        print("Número de notícias encontradas:", len(feed.entries))

        # Percorrer cada notícia
        for entry in feed.entries:
            news_item = {
                
                "published": entry.get("published"),
                "title": entry.get("title"),
                "summary": entry.get("summary"),
                "link": entry.get("link"),
                "source": rss_url,
            }
            news_data.append(news_item)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao aceder ao RSS {rss_url}: {e}")



# Criar DataFrame inicial
df_news = pd.DataFrame(news_data)
df_news["published"] = pd.to_datetime(df_news["published"], errors="coerce") # Converter a coluna de datas para o formato datetime



# Visualizar as primeiras linhas
# print("\nDataFrame resultante:")
# print(df_news.head())

# Opcional: guardar em CSV
#df_news.to_csv("ft_news_middle_east.csv", index=False, encoding="utf-8-sig")




# -------------------------------
# 🔹 Remover duplicados mantendo fontes e links
# -------------------------------

# Agrupar por título (ou por link, se for sempre único)
df_unique = (
    df_news
    .groupby("title", as_index=False)
    .agg({
        "published": "first",      # Mantém a primeira data
        "summary": "first",        # Mantém o primeiro resumo
        "link": lambda x: list(set(x)),     # Lista de links únicos
        "source": lambda x: list(set(x))    # Lista de fontes únicas
    })
)



# =============================================================================
# Melhor abordagem: Combinação de campos: Para maior robustez, podes criar uma chave única combinando title e published:
# =============================================================================
df_news["news_id"] = (
    df_news["title"].str.strip().str.lower() + "_" +
    df_news["published"].astype(str)
)

df_unique = (
    df_news
    .groupby("news_id", as_index=False)
    .agg({
        "title": "first",
        "published": "first",
        "summary": "first",
        "link": lambda x: list(set(x)),
        "source": lambda x: list(set(x))
    })
    .drop(columns="news_id")
)



# Ordenar por data de publicação (opcional)
df_unique = df_unique.sort_values(by="published", ascending=False)

# Visualizar o resultado
print(df_unique.head())

# Guardar em CSV (opcional)
# df_unique.to_csv("ft_news_unique.csv", index=False, encoding="utf-8-sig")



