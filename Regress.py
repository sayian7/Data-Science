from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math



# nomes únicos (linhas)
nomes = ["Ana", "Bruno", "Carla", "Diogo", "Eva"]

# meses (colunas)
meses = list(range(1,6+1)) #["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# ano atual
ano = pd.Timestamp.today().year
# intervalo de datas (1 Jan até 30 Jun)
datas = pd.date_range(
    start=f"{ano}-01-01",
    end=f"{ano}-06-30",
    freq="D"
)
print(datas)




# gerar dados aleatórios entre 0 e 4
dados = np.random.randint(0, 5, size=(len(nomes), len(meses)))
df1 = pd.DataFrame(dados, index=nomes, columns=meses)
print(df1)


# variáveis (colunas)
variaveis = ["x1", "x2", "x3", "x4"]

# gerar valores aleatórios entre 0 e 100
dados = np.random.randint(0, 101, size=(len(datas), len(variaveis)))
df2 = pd.DataFrame(dados, index=datas, columns=variaveis)
print(df2)

# gerar valores aleatórios entre 0 e 100
dados = np.random.randint(0, 101, size=(len(datas), len(nomes)))
df3 = pd.DataFrame(dados, index=datas, columns=nomes)
print(df3)



# df1 -> dataframe com valores 0–4 (index = nomes, colunas = meses)
# df2 -> dataframe com x1..x4 (index = meses)
# df3 -> dataframe com nomes (index = meses)

resultado = pd.DataFrame(index=df3.index, columns=df3.columns)

for data in df3.index:
    for nome in df3.columns:
        mes = data.month
        var_idx = df1.loc[nome, mes]  # valor entre 0 e 4
        
        if var_idx == 0:
            resultado.loc[data, nome] = (df3.loc[data, nome], None)
        else:
            var_nome = f"x{var_idx}"
            resultado.loc[data, nome] = (
                df3.loc[data, nome],
                df2.loc[data, var_nome]
            )
print(resultado)



# # resultado = dataframe com tuplos (y, x)
# params = {}
# for nome in resultado.columns:
#     xs = []
#     ys = []
#     for val in resultado[nome]:
#         y, x = val
#         if x is not None:
#             xs.append(x)
#             ys.append(y)
#     # só faz regressão se tiver pelo menos 2 pontos
#     if len(xs) >= 2:
#         a, b = np.polyfit(xs, ys, 1)  # y = a*x + b
#         params[nome] = {"slope": a, "intercept": b}
#     else:
#         params[nome] = {"slope": None, "intercept": None}
# # transformar em dataframe
# df_params = pd.DataFrame(params)
# print(df_params)


params = {}
for nome in resultado.columns:
    xs = []
    ys = []
    for val in resultado[nome]:
        y, x = val
        if x is not None:
            xs.append(x)
            ys.append(y)
    # só faz regressão se tiver pelo menos 2 pontos
    if len(xs) >= 2:
        res = linregress(xs, ys)
        params[nome] = {
            "slope": res.slope,
            "intercept": res.intercept,
            "r2": res.rvalue**2,
            "p_value": res.pvalue
        }
    else:
        params[nome] = {
            "slope": None,
            "intercept": None,
            "r2": None,
            "p_value": None
        }
# transformar em dataframe
df_params = pd.DataFrame(params)
print(df_params)

# Todas as regressões no mesmo gráfico
# plt.figure()
# for nome in resultado.columns:
#     xs = []
#     ys = []
#     for val in resultado[nome]:
#         y, x = val
#         if x is not None:
#             xs.append(x)
#             ys.append(y)
#     if len(xs) >= 2:
#         # pontos
#         plt.scatter(xs, ys, label=nome)
#         # regressão
#         a, b = np.polyfit(xs, ys, 1)
#         x_line = np.linspace(min(xs), max(xs), 100)
#         y_line = a * x_line + b
#         plt.plot(x_line, y_line)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.title("Regressões lineares por nome")
# plt.show()

# Gráfico individual por regressão 
# nomes = list(resultado.columns)
n = len(nomes)

# grelha "quadrada"
ncols = math.ceil(math.sqrt(n))
nrows = math.ceil(n / ncols)

plt.figure(figsize=(4*ncols, 4*nrows))
for i, nome in enumerate(nomes, 1):
    xs, ys = [], []
    for val in resultado[nome]:
        y, x = val
        if x is not None:
            xs.append(x)
            ys.append(y)
    ax = plt.subplot(nrows, ncols, i)
    if len(xs) >= 2:
        # pontos
        ax.scatter(xs, ys, label=nome)
        
        # regressão + stats
        res = linregress(xs, ys)
        a = res.slope
        b = res.intercept
        r2 = res.rvalue**2
        pval = res.pvalue
        
        x_line = np.linspace(min(xs), max(xs), 100)
        y_line = a * x_line + b
        ax.plot(x_line, y_line)
        
        ax.set_title(
            #f"{nome}\n"
            f"a={a:.2f}, b={b:.2f}, R²={r2:.2f}, p={pval:.3f}"
        )
    else:
        ax.set_title(f"{nome}\nSem dados suficientes")
    # ax.set_xlabel("x")
    # ax.set_ylabel("y")
    ax.legend()
plt.tight_layout()
plt.show()
