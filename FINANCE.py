# FINANCE

def cnvrt_n(n, tipo): # Conversor temporal
    assert type(n)==int and (tipo in ["A","S","T","M"])
    if tipo=="A": na=n; ns=n*2; nt=n*4; nm=n*12;
    elif tipo=="S": na=n/2; ns=n; nt=n*2; nm=n*6;
    elif tipo=="T": na=n/4; ns=n/2; nt=n; nm=n*3;
    elif tipo=="M": na=n/12; ns=n/6; nt=n/3; nm=n;
    return list((na, ns, nt, nm))


# JURO SIMPLES
def cnvrt_r_nom(r,tipo):
    assert type(r)==float and (tipo in ["A","S","T","M"])
    if tipo=="A": r_a=r; r_s=r/2; r_t=r/4; r_m=r/12;
    elif tipo=="S": r_a=r*2; r_s=r; r_t=r/2;  r_m=r/6;
    elif tipo=="T": r_a=r*4; r_s=r*2; r_t=r; r_m=r/3;
    elif tipo=="M": r_a=r*12; r_s=r*6; r_t=r*3; r_m=r;
    return list((r_a,r_s,r_t,r_m))

def Cap_js(Capital,r,n):
    assert type(Capital)==(int or float) and type(r)==float and type(n)==int
    res=[]; # func=(lambda i: r*i)
    for i in range(n+1):
        Cash = Capital*(1+(r*i))
        Juro_Total = Capital*r*i
        juro = Capital*r * int(i>0)
        res += [[i,juro,Juro_Total,Cash]]
    return res
def n_rjs_r(Ci, Ca, r):
    n = ((Ca/Ci)-1)/r
    return n
def r_rjs_n(Ci, Ca, n):
    r = ((Ca/Ci)-1)/n
    return r

# JURO COMPOSTO
def cnvrt_r_ef(r,tipo):
    assert type(r)==float and (tipo in ["A","S","T","M"])
    func=(lambda r,i: pow(1+r,i));
    if tipo=="A": r_a=r; r_s=(func(r,1/2))-1; r_t=(func(r,1/4))-1; r_m=(func(r,1/12))-1;
    elif tipo=="S": r_a=(func(r,2))-1; r_s=r; r_t=(func(r,1/2))-1; r_m=(func(r,1/6))-1;
    elif tipo=="T": r_a=(func(r,4))-1; r_s=(func(r,2))-1; r_t=r; r_m=(func(r,1/3))-1;
    elif tipo=="M": r_a=(func(r,12))-1; r_s=(func(r,6))-1; r_t=(func(r,3))-1; r_m=r;
    return list((r_a,r_s,r_t,r_m))

def Cap_jc(Capital,r,n):
    assert type(Capital)==(int or float) and type(r)==float and type(n)==int
    func=(lambda i: pow(1+r,i)); res=[[],[],[],[]]
    for i in range(n+1):
        Cash = Capital * func(i)
        Juro_Total = Capital * (func(i)-1)
        juro = Capital * ( (func(i)-1) - (func(i-1)-1) ) * int(i>0)
        res[0]+=[i]; res[1]+=[juro]; res[2]+=[Juro_Total]; res[3]+=[Cash]; 
        # print(i,juro,Juro_Total,Cash)
    return res
def r_rjc_n(Ci, Ca, n):
    r = pow(Ca/Ci, 1/n)-1
    return r



# Valor Presente/Atual e Futuro

FV = (lambda C0, r, t: C0*(1+r)**t) # Valor Futuro # Ct
PV = (lambda Ct, r, t: Ct*(1+r)**-t) # Valor Presente # C0

def K_times_compounding(Capital, rate, nr_periods, k_periods):
    # assert type(Capital)==(int or float) and type(r)==float and (type(n) and type(k))==int
    return (lambda C0,r,n,k: C0*pow(1+(r/k),k*n))(Capital, rate, nr_periods, k_periods)

def FV_n(Capital, rate, nr_periods):
    return (lambda C0,r,n: C0*pow(1+r,n))(Capital, rate, nr_periods)
def VA_n(Capital, rate, nr_periods):
    return (lambda C0,r,n: C0*pow(1+r,-n))(Capital, rate, nr_periods)

def FV_cont(Capital, rate, time):
    # assert type(Capital)==(int or float) and type(r)==float and type(T)==int
    return (lambda C0,r,t: C0*pow(e,r*t))(Capital, rate, time)
def VA_cont(Capital, rate, time):
    return (lambda C0,r,t: C0*pow(e,-r*t))(Capital, rate, time)


# Loans. Empréstimo, Rendas. Anuidade, perpetuidade. 
def emprestimo_prestacao(val_emprestimo, r, n):
    assert type(val_emprestimo)==(int or float) and type(r)==float and type(n)==int
    funcao=(lambda r,i: pow(1+r,i)); frn=funcao(r,n)
    prestacao = ((r*frn)/(frn-1))*val_emprestimo
    PV = ((frn-1)/(r*frn))*prestacao; FV = frn*((frn-1)/(r*frn))*prestacao
    res=[[],[],[]]
    for i in range(1,n+1):
        pv = prestacao * (funcao(r,-i)); fv = prestacao * (funcao(r,n-i))
        res[0]+=[i]; res[1]+=[pv]; res[2]+=[fv]; # print(i,pv,fv)
    return prestacao,PV==sum(res[1]),FV==sum(res[2])
def VA_perpetuidade(prestacao, r):
    Capital_inicial = prestacao/r # prestacao = Capital_inicial*r
    return prestacao, Capital_inicial

# ANUIDADE
Annuity = (lambda c, r, n: (c/r)*(1-(1/(1+r)**n))) # ANUIDADE
def VA_annuity(c, r, n):
    res = 0
    for i in range(1,n+1,1):
        res += c/((1+r)**i)
        print(i, c, c/((1+r)**i), res)
    #print(res)
    r1 = (c/r)*(1-(1/(1+r)**n))
    return res, r1


# Bond's / Obrigações
def Zero_Coupon_bond(FV,YTM,n):
    assert type(FV)==(int or float) and type(YTM)==float and type(n)==int
    func=(lambda r,i: pow(1+r,i))
    price = FV/func(YTM,n) # YTM = pow(FV/P,1/n)-1
    return price
def Coupon_bond_Price(FV,t_cpn,ytm,n):
    assert type(FV)==(int or float) and type(ytm)==float and type(n)==int
    func=(lambda r,i: pow(1+r,i))
    CPN = t_cpn*FV
    Price = (CPN*(1/ytm)*(1-(1/func(ytm,n)))) + FV/func(ytm,n)
    return Price
def Coupon_bond_Ytm(Price, FV, t_cpn, n):
    assert type(FV)==(int or float) and type(t_cpn)==float and type(n)==int
    f=(lambda r,i: pow(1+r,i))
    cpn = FV*t_cpn
    res=[[],[]]
    for y in arange(0.01,0.1,0.001):
        price = (cpn*(1/y)*(1-(1/f(y,n)))) + FV/f(y,n)
        res[0]+=[y]; res[1]+=[abs(Price-price)]; # print(y,Price,price,Price-price)
    return res


r = 0.1; n = 10; cpn = 10; FV = 100; 

Price_bond = (lambda FV, r, y, n: (((FV*r))/y)*(1-(1/(1+y)**n)) + (FV/(1+y)**n)) # B0
def Bond_Price(FV, r, y, n): # BOND PRICE (Coupon)
    res = 0 #cpn = FV*r
    for i in range(1,n+1,1):
        res += (FV*r)/((1+y)**i)
        print(i, FV*r, (FV*r)/((1+y)**i), res)
        if i == n:
            res += (FV/(1+y)**n)
    #print(res)
    r1 = (FV*r) * ( ((1+y)**n - 1 ) / (y * (1+y)**n) ) + (FV/(1+y)**n) #a1 = ( ((1+r)**n - 1 ) / (r * (1+r)**n) )
    r2 = (FV*r) * ( (1 - (1+y)**(-n)) / y ) + (FV/(1+y)**n) #a2 = ( (1 - (1+r)**(-n)) / r )
    r3 = (((FV*r))/y) * (1-(1/(1+y)**n)) + (FV/(1+y)**n)
    return res, r1, r2, r3

# Bond's
x,y,z,n=symbols("x"),symbols("y"),symbols("z"), symbols("n");
summation(x,(x,0,n)); 
# P, FV, CPN, N, YTM = symbols("P"),symbols("FV"),symbols("CPN"), symbols("N"), symbols("YTM"); 
# YTM = symbols("YTM"); P = 95; FV = 105; CPN = 5; N = 2;
# solve( P - ( (CPN/YTM)*(1-(1+YTM)**-N) + (FV*(1+YTM)**-N) ) , YTM )
def Zero_Coupon(FV,YTM,n):
    assert type(FV)==(int or float) and type(YTM)==float and type(n)==int
    func=(lambda r,i: pow(1+r,i))
    price = FV/func(YTM,n) # YTM = pow(FV/P,1/n)-1
    return price
def Coupon_bond_Ytm(Price,FV,t_cpn,n):
    assert type(FV)==(int or float) and type(t_cpn)==float and type(n)==int
    f=(lambda r,i: pow(1+r,i))
    cpn = FV*t_cpn
    res=[[],[]]
    for y in arange(0.01,0.1,0.001):
        price = (cpn*(1/y)*(1-(1/f(y,n)))) + FV/f(y,n)
        res[0]+=[y]; res[1]+=[abs(Price-price)]; # print(y,Price,price,Price-price)
    return res
def Coupon_bond_Price(FV,t_cpn,ytm,n):
    assert type(FV)==(int or float) and type(ytm)==float and type(n)==int
    func=(lambda r,i: pow(1+r,i))
    CPN = t_cpn*FV
    Price = (CPN*(1/ytm)*(1-(1/func(ytm,n)))) + FV/func(ytm,n)
    return Price



# Options / Opções : Stock, Call, Put: Long & Short


# Put-Call Parity: c + Ke^(-rt) = p + S0
def put_call_parity(S0, K, c, p, R, T):
    call = p + S0 - VA_cont(K, R, T);
    put = c - S0 + VA_cont(K, R, T);
    if call > c: print("Call is underpriced: Should Buy Call")
    elif not(call > c): print("Call is overpriced: Should Sell Call")
    elif put > p: print("Put is underpriced: Should Buy Put")
    elif not(put > p): print("Put is overpriced: Should Sell Put")
    return [["Call",c,call],["Put",p,put]]

def pcp_t0_1(CallQ, PutQ, c, p, S0, K, R, T):
    if CallQ == "Sell" and PutQ == "Buy":
        if c - p > 0:
            StockQ = "Buy"; BankQ = "Borrow";
            t0_call = c; t0_put = -p; t0_stock = -S0; t0_bank = VA_cont(K,R,T);
            t1_LST_call = 0; t1_LST_put = str(K)+"-ST"; t1_LST_stock = "ST"; t1_LST_bank = -K;
            t1_HST_call = "-ST+"+str(K); t1_HST_put = 0; t1_HST_stock = "ST"; t1_HST_bank = -K;
        else:
            StockQ = "Sell"; BankQ = "Lend";
            t0_call = c; t0_put = -p; t0_stock = S0; t0_bank = -VA_cont(K,R,T);
            t1_LST_call = 0; t1_LST_put = str(K)+"-ST"; t1_LST_stock = "-ST"; t1_LST_bank = K;
            t1_HST_call = "-ST+"+str(K); t1_HST_put = 0; t1_HST_stock = "-ST"; t1_HST_bank = K;
    elif CallQ == "Buy" and PutQ == "Sell":
        if -c+p<0:
            StockQ = "Sell"; BankQ = "Lend"
            t0_call=-c; t0_put=p; t0_stock=S0; t0_bank=-VA_cont(K,R,T);
            t1_LST_call=0; t1_LST_put=str(K)+"-ST"; t1_LST_stock="-ST"; t1_LST_bank=K;
            t1_HST_call="-ST+"+str(K); t1_HST_put=0; t1_HST_stock="-ST"; t1_HST_bank=K;
        else:
            StockQ = "Buy"; BankQ = "Borrow"
            t0_call=-c; t0_put=p; t0_stock=-S0; t0_bank=VA_cont(K,R,T);
            t1_LST_call=0; t1_LST_put=str(K)+"-ST"; t1_LST_stock="ST"; t1_LST_bank=-K;
            t1_HST_call="-ST+"+str(K); t1_HST_put=0; t1_HST_stock="ST"; t1_HST_bank=-K;
    
    print(CallQ+" "+"Call",t0_call,t1_LST_call,t1_HST_call)
    print(PutQ+" "+"Put",t0_put,t1_LST_put,t1_HST_put)
    print(StockQ+" "+"Stock",t0_stock,t1_LST_stock,t1_HST_stock)
    print(BankQ+" "+"Bank",t0_bank,t1_LST_bank,t1_HST_bank)

# Binomial Model : martingale_probability(u,d,r) & price_prob(payoff,S0,S,K,u,d,r)

def martingale_probability(u, d, r):
    qu = ((1+r)-d)/(u-d); qd = (u-(1+r))/(u-d);
    return qu, qd

def price_prob(payoff, S0, S, K, u, d, r): # T
    # payoff_call = (lambda S0,K: max(S0-K,0)) (s0,k)
    # payoff_put = (lambda S0,K: max(K-S0,0)) (s0,k)
    # payoff_asian = (lambda S0,ST,K: max(0.5*(S0+ST)-K,0)) (s0,st,k)
    qu, qd = martingale_probability(u,d,r);
    Su = S*u; Sd = S*d; 
    gu=payoff(Su,K); gd=payoff(Sd,K); # Asian call: gu=payoff(S0,Su,K); gd=payoff(S0,Sd,K);
    return [[Su,gu],[Sd,gd]]

# price tree
    S0=100; K=110; u=1.2; d=0.8; r=0.05; T=3;
    qu,qd = martingale_probability(u,d,r);
    S=[S0]; S+=[[S[0]*u,S[0]*d]];
    for i in range(1,T):
        for val in S[i]:
            S+=[[val*u,val*d]];
    print(S)

# def buy_stock(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         payoff = S-X
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def sell_stock(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         payoff = -(S-X)
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def buy_call(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         if not(S>X):
#             payoff=0
#         else:
#             payoff=S-X
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def sell_call(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         if not(S>X):
#             payoff=0
#         else:
#             payoff=-(S-X)
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def buy_put(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         if S<X:
#             payoff=X-S
#         else:
#             payoff=0
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def sell_put(X):
#     assert type(X)==(int or float)
#     r=[[],[]] # d={}
#     for S in range(101): # range(X-int(X/2),X+int(X/2)+1)
#         if S<X:
#             payoff=-(X-S)
#         else:
#             payoff=0
#         r[0]+=[S]; r[1]+=[payoff]; # d[S]=payoff
#     return r
# def Add_Ops(X,Y):
#     assert (type(X) and type(Y))==list
#     dx={}; dy={}; d={} # x1,x2 = X[0],X[1]; y1,y2 = Y[0],Y[1]; n = min(len(x1),len(x2)); # a = max(min(dx.keys()),min(dy.keys())); b = min(max(dx.keys()),max(dy.keys()))
#     for i1 in range(len(X[0])):
#         dx[X[0][i1]]=X[1][i1]
#     for i2 in range(len(Y[0])):
#         dy[Y[0][i2]]=Y[1][i2]
#     for i in range(101): # range(a,b+1)
#         d[i]=dx[i]+dy[i]
#     return [list(d.keys()),list(d.values())]
# def Show_Ops(X):
#     dataplot(X[0],X[1])


# STOCK PRICE

def f_d_p(avg, stdev): # Func Dist Prob
    fdp=(lambda u,s,x: (1/sqrt(2*pi*(pow(s,2)))*pow(e,-(1/(2*pow(s,2)))*(pow(x-u,2))))); # Func Dens Prob. Geral
    fdp_NR = (lambda x: fdp(0,1,x)); # Func Dens Prob. Norm Red # u=0; s=1;
    
    l=[fdp(avg,stdev,i) for i in arange(-100,100.5,0.5)];
    l_NR=list(map(fdp_NR,arange(-100,100+0.5,0.5)));
    
    s=0; r=[s]; # print(s,r);
    for y in l:
        s+=y; r+=[s]; # print(f_xi,s);
    return r #s # r # print(r); dataplot(r);



f = (lambda x: pow(e,pi*pow(x,2))); 
l = list(map(f,arange(-10,10,0.5))); # print(lista); 
plot(list(arange(-10,10,0.5)),lista)



from matplotlib.pyplot import plot
from random import random, randint
from numpy import e, pi, arange # import numpy as np
from math import sqrt, log # e, pi
# from decimal import *
from sympy import symbols, summation, solve # , cos, pi # from sympy import *


# Sn(t)
def plot_Sn_t(S0,u,s,n): # S0=0; n=10000; u=0; s=1; 
    S=[S0]; r_i=0; r_t=[0];
    w=[numpy.random.normal(0,1) for i in range(n)]; v=[-1,1];
    for i in range(1,n+1):
        t=i/n; r_t+=[t];
        r_i+=v[randint(0,len(v)-1)]*w[i-1]; 
        S+=[((s*n)**-0.5)*(r_i-u*i)];
    plot(r_t,S)


# Sn(t) NEW
def plot_Sn_t(S0,t0,u,s,n): # S0=0; t0=0; u=0; s=1; n=10000;
    S=[S0]; T=[t0]; ri=0; v=[-1,1];
    w=list(map((lambda x: numpy.random.normal(0,1)), range(1,n+1))); 
    T+=list(map((lambda x: x/n), range(1,n+1))); # t=i/n; T+=[t];
    # ((lambda : [-1,1][randint(0,len([-1,1])-1)])()); list(map((lambda x: [-1,1][randint(0,len([-1,1])-1)]),range(10))); 
    for i in range(1,n+1):
        ri += v[randint(0,len(v)-1)]*w[i-1]; 
        S += [((s*n)**-0.5)*(ri-u*i)];
    plot(T,S);


def plot_Sn_t(S0,t0,u,s,n): # S0=0; t0=0; u=0; s=1; n=10000;
    S=[S0]; T=[t0]; ri=0; v=[-1,1];
    w=list(map((lambda x: numpy.random.normal(0,1)),range(1,n+1))); 
    T+=list(map((lambda x: x/n),range(1,n+1))); # t=i/n; T+=[t];
    # ((lambda : [-1,1][randint(0,len([-1,1])-1)])()); list(map((lambda x: [-1,1][randint(0,len([-1,1])-1)]),range(10))); 
    for i in range(1,n+1):
        ri += v[randint(0,len(v)-1)]*w[i-1]; 
        S += [((s*n)**-0.5)*(ri-u*i)];
    plot(T,S);



import numpy as np
import matplotlib.pyplot as plt

def simulate_black_scholes(S0=100, mu=0.05, sigma=0.2, T=1.0, N=252, seed=None):
    if seed is not None: np.random.seed(seed)
    dt = T / N
    prices = np.zeros(N + 1)
    prices[0] = S0
    for t in range(1, N + 1):
        Z = np.random.normal(0, 1)
        prices[t] = prices[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return prices

# parâmetros
S0 = 100 # preço inicial
mu = 0.07 # retorno médio anual
sigma = 0.25 # volatilidade anual
T = 1 # horizonte temporal (anos)
N = 252 # número de passos

prices = simulate_black_scholes(S0, mu, sigma, T, N, seed=50)

# plot
plt.plot(prices)
plt.title("Simulação de preço de ação (Black-Scholes / GBM)")
plt.xlabel("Tempo")
plt.ylabel("Preço")
plt.show()



def monte_carlo_black_scholes(S0, mu, sigma, T, N, n_sim):
    dt = T / N
    paths = np.zeros((N + 1, n_sim))
    paths[0] = S0
    for t in range(1, N + 1):
        Z = np.random.normal(0, 1, n_sim)
        paths[t] = paths[t-1] * np.exp( (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return paths

paths = monte_carlo_black_scholes(100, 0.07, 0.25, 1, 252, 100)
plt.plot(paths)
plt.title("Monte Carlo - Simulação de preços")
plt.show()



    
# Black-Scholes formula
from statistics import NormalDist
# Normal_01 = NormalDist(0,1); 
# plot(list(arange(-5,5,1/10)),list(map(Normal_01.cdf,arange(-5,5,1/10)))); # Função distribuicao 
# plot(list(arange(-5,5,1/10)),list(map(Normal_01.pdf,arange(-5,5,1/10)))); # Função densidade de prob

def VA_n(Capital,rate,nr_periods):
    return (lambda C0,r,n: C0*pow(1+r,-n))(Capital,rate,nr_periods)

S0=50; K=50; t=0.5; r=0.1; s=1; # u=0;
N = NormalDist(0,1);
d1 = ( log(S0/K) + (r + (s**2)/2)*t ) / ( s*sqrt(t) ); d2 = d1 - s*sqrt(t);
Oc = ( (N.cdf(d1)) * S0 ) - ( (N.cdf(d1)) * VA_n(K,r,t) );


# Laplace aproximation of pi
def Laplace_aprox_pi(N):
    # N = 10000;
    c = 0;
    for i in range(N):
        x = numpy.random.uniform(-1,1);
        y = numpy.random.uniform(-1,1);
        if numpy.sqrt(x**2 + y**2) < 1:
            c += 1;
    p = c / float(N);
    print("Proportion inside: {}".format(p))







# import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json" # 1️ Endpoint da API pública
response = requests.get(url) # 2️ Fazer pedido à API
if response.status_code == 200: data = response.json(); price = data["bpi"]["USD"]["rate"]; #print(f"💰 Preço atual do Bitcoin: {price} USD") # 3️ Converter o resultado (JSON → dicionário Python)
else: print("Erro ao obter dados:", response.status_code)
    

# bitcoin_plot_statsmodels.py
# from statsmodels.tsa.seasonal import seasonal_decompose
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": "30"}  # últimos 30 dias
response = requests.get(url, params=params)
data = response.json()
# Converter para DataFrame
prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
prices["date"] = pd.to_datetime(prices["timestamp"], unit="ms")
prices = prices[["date", "price"]].set_index("date")
print(prices.head())


# ---------- 1. Obter dados históricos do Bitcoin (CoinDesk API) ----------
start_date, end_date = "2024-10-01", "2025-10-01" # Ajusta as datas conforme necessário (YYYY-MM-DD)
url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}"

resp = requests.get(url)
resp.raise_for_status()  # lança erro se o request falhar
js = resp.json()

prices = js.get("bpi", {}) # 'bpi' é um dicionário {date_string: price}

# ---------- 2. Transformar em DataFrame ----------
df = pd.DataFrame(list(prices.items()), columns=["date", "price"]); df["date"] = pd.to_datetime(df["date"]); df = df.set_index("date").sort_index()
# Garantir que a série é diária; se faltarem dias, podemos reindexar (opcional)
df = df.asfreq("D")             # dias ausentes terão NaN
df["price"] = df["price"].interpolate()  # interpolar valores faltantes (simples)

# ---------- 3. Decomposição da série temporal com statsmodels ----------
# Escolhemos um período semanal (7) — ajusta se fizer sentido (por exemplo, 30 para mensal)
period = 7
decomp = seasonal_decompose(df["price"], model="additive", period=period, extrapolate_trend='freq')

df["trend"] = decomp.trend; df["seasonal"] = decomp.seasonal; df["resid"] = decomp.resid

# ---------- 4. Visualização interativa com Plotly ----------
fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.03, subplot_titles=("Bitcoin Price (USD)", "Trend", "Seasonal", "Residuals"))
fig.add_trace(go.Scatter(x=df.index, y=df["price"], name="Price", mode="lines"), row=1, col=1) # Preço original
fig.add_trace(go.Scatter(x=df.index, y=df["trend"], name="Trend", mode="lines"), row=2, col=1) # Trend
fig.add_trace(go.Scatter(x=df.index, y=df["seasonal"], name="Seasonal", mode="lines"), row=3, col=1) # Seasonal
fig.add_trace(go.Scatter(x=df.index, y=df["resid"], name="Residuals", mode="lines"), row=4, col=1) # Residuals
fig.update_layout(height=900, title_text="Bitcoin Price & Time Series Decomposition", showlegend=True)
fig.update_xaxes(rangeslider_visible=True)  # mostra range slider para explorar
# Mostrar (em Jupyter use fig.show(); em script também abre uma tab no browser)
fig.show()
fig.write_html("bitcoin_plot.html", auto_open=True)
pio.renderers.default = 'browser'   # ou 'iframe_connected'
fig.show()

# ---------- 5. Exemplo simples de modelagem com statsmodels (opcional) ----------
# Aqui um exemplo muito simples de ajuste de tendência linear usando OLS (statsmodels.api)
# Se quiseres utilizar ARIMA/SARIMAX, podes usar statsmodels.tsa.arima.model.ARIMA ou SARIMAX.
if df["price"].notna().sum() > 30:
    import statsmodels.api as sm
    df2 = df.dropna(subset=["price", "trend"])
    # criar variável tempo
    df2["t"] = range(len(df2))
    X = sm.add_constant(df2["t"])
    y = df2["price"]
    model = sm.OLS(y, X).fit()
    print(model.summary().tables[1])  # coeficientes (intercept, slope)







# Portfolio Model

# import itertools
n = 3 # número de ações
j = 10 # partições
v = [round(x,2) for x in np.linspace(1, 0, j+1)] # Possíveis percentagens 
#N = (j+1)**n

#p = [(x,y,z,w) for x in v for y in v for z in v for w in v ]
#c = [x for x in p if sum(x)==1]; del p

combinacoes = list(itertools.product(v, repeat=n)) # Todas as combinações possíveis (com repetição)
cv = [c for c in combinacoes if sum(c) == 1]; del combinacoes # Filtrar apenas as que somam 1
#permutacoes = [(x,y,z) for x in range(2,5) for y in range(1,3) for z in range(2,4) ]
#combinacoes = [x for x in permutacoes if [sorted(y) for y in permutacoes].count(sorted(x)) == 1]

rs = {x: ( [round(x,2) for x in list(np.linspace(0.05,0.2,6))][np.random.randint(len([round(x,2) for x in list(np.linspace(0.05,0.2,6))])-1)] , [round(x,4) for x in list(np.linspace(0.01,0.06,11))] [np.random.randint(len([round(x,4) for x in list(np.linspace(0.01,0.06,11))])-1)] ) for x in range(1,n+1)}
cr = {x: round( list(np.linspace(-1,1,21))[np.random.randint(len(list(np.linspace(-1,1,21))))-1] , 2) for x in list(itertools.combinations(list(range(1,n+1)), 2))}
#returns = [round(x,2) for x in list(np.linspace(0.05,0.2,6))][np.random.randint(len([round(x,2) for x in list(np.linspace(0.05,0.2,6))])-1)]
#stdev = [round(x,4) for x in list(np.linspace(0.01,0.06,11))] [np.random.randint(len([round(x,4) for x in list(np.linspace(0.01,0.06,11))])-1)]

r = {x: 
     (round(sum([ x[i-1]*rs[i][0] for i in range(1,n+1) ]),4) , 
     round( np.sqrt( sum([ pow(x[i-1],2)*pow(rs[i][1],2) for i in range(1,n+1) ]) + sum( [ 2 * ( x[i-1]*x[j-1] ) * ( rs[i][1]*rs[j][1] ) * cr[(i,j)] for (i,j) in cr.keys() ] ) ) , 4 ) )
     for x in cv}

plt.plot( [x[1] for x in list(r.values())], [x[0] for x in list(r.values())] )






# import yfinance as yf
# Definir tickers: Ticker da ação: STM.PA; Índice de referência: ^STOXX50E. Ticker da ação: 0700.HK; Índice de referência: ^HSI
tesla = yf.download("TSLA", start="2025-01-01", end="2025-11-01")['Close']
# nvidia = yf.download("NVDA", start="2020-01-01", end="2025-01-01")['Close']
# ibm = yf.download("IBM", start="2020-01-01", end="2025-01-01")['Close']
# apple = yf.download("AAPL", start="2020-01-01", end="2025-01-01")['Close']
# amazon = yf.download("AMZN", start="2020-01-01", end="2025-01-01")['Close']
# walmart = yf.download("WMT", start="2020-01-01", end="2025-01-01")['Close']
# exxon = yf.download("XOM", start="2020-01-01", end="2025-01-01")['Close']
# microsoft = yf.download("MSFT", start="2020-01-01", end="2025-01-01")['Close']
market = yf.download("^GSPC", start="2020-01-01", end="2025-01-01")['Close']
risk_free = yf.download("^IRX", start="2020-01-01", end="2025-01-01")['Close']

tesla_ret = tesla.pct_change().dropna(); market_ret = market.pct_change().dropna() # Calcular retornos diários

# Converter taxa sem risco (3-month T-bill) para retorno diário aproximado
rf_daily = (risk_free / 100) / 252  # ^IRX está em percentagem anualizada
# rf_daily = (1 + (risk_free / 100)) ** (1/252) - 1

data = pd.concat([tesla_ret, market_ret, rf_daily], axis=1).dropna(); data.columns = ['Tesla', 'Market', 'Rf'] # Alinhar datas
data['Tesla_excess'] = data['Tesla'] - data['Rf']; data['Market_excess'] = data['Market'] - data['Rf'] # Calcular retornos em excesso (excess returns)
cov_matrix = np.cov(data['Tesla_excess'], data['Market_excess']); beta = cov_matrix[0,1] / cov_matrix[1,1] # Calcular beta da Tesla em relação ao mercado
market_mean = data['Market'].mean() * 252; rf_annual = data['Rf'].mean() * 252 # Retorno médio do mercado e taxa sem risco anualizadas

expected_return = rf_annual + beta * (market_mean - rf_annual) # CAPM: Retorno esperado da Tesla
print(f"Beta da Tesla: {beta:.2f}. Taxa sem risco (anual): {rf_annual:.2%}. Retorno esperado da Tesla (CAPM): {expected_return:.2%}")

for x in [tesla, nvidia, ibm, apple, amazon, walmart, exxon, microsoft]:
    plt.figure(); plt.plot(x.index.to_numpy(),x.to_numpy()); plt.title(f"{list(x.columns)[0]}"); plt.show()
    plt.figure(); plt.plot(x.pct_change().dropna().index.to_numpy(),x.pct_change().dropna().to_numpy()); plt.show()


ticker = "NVDA"; t = yf.Ticker(ticker) # Descarregar DFs
income, balance, cashflow = t.financials, t.balance_sheet, t.cashflow # anual (últimos anos)
q_income, q_balance, q_cashflow = t.quarterly_financials, t.quarterly_balance_sheet, t.quarterly_cashflow










# import calendar # from datetime import datetime, date, timedelta
# agora = datetime.now() # Data e hora atuais
# hoje = date.today() # Data de hoje
# natal = date(2025,12,25) # Criar uma data específica
# faltam = natal - hoje #print(f"Faltam {faltam.days} dias para o Natal!") # Diferença entre datas
# ontem, amanha = hoje - timedelta(days=1), hoje + timedelta(days=1) # Somar ou subtrair tempo
anos = list(range(2025,2025+1)) #ano = 2025
#data = date(ano, mes, dia); #dia_sem = data.isoweekday()
d = { (i,m,a): (date(a,m,i).isoweekday(), date(a,m,i).isocalendar().week) for a in anos for m in range(1,12+1) for i in range(1, calendar.monthrange(a, m)[1]+1)  }
s = {(a,i): [ (k[0], d[k][0]) for k in d.keys() if d[k][1] == i] for a in range(2025,2025+1) for i in range(1,53)}
#pd.DataFrame({j: [ i[j] for i in d.keys()] for j in range(3)})
#pd.DataFrame({j: [ d[i][j] for i in d.keys()] for j in range(2)})
r = {}
r.update({i: [k[i] for k in dw.keys()] for i in range(3)})
r.update({x: [dw[k][x] for k in dw.keys()] for x in dw[k]})
df = pd.DataFrame(r); df.to_clipboard()





# from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/markets/stocks/most-active/?start=200&count=200" # URL da página Yahoo Finance Most Active Stocks
# url = "https://finance.yahoo.com/markets/world-indices/"
# url = "https://finance.yahoo.com/markets/crypto/all/"
headers = {"User-Agent": "Mozilla/5.0"} # Cabeçalhos para simular um browser (evita bloqueio)
response = requests.get(url, headers=headers) # Fazer o pedido HTTP
response.raise_for_status()  # se houver erro, lança exceção
soup = BeautifulSoup(response.text, "lxml") # Usar BeautifulSoup para parsear o HTML
table = soup.find("table") # Encontra a tabela (Yahoo usa <table> com classes específicas)
df_list = pd.read_html(str(table)); df = df_list[0] # Converte diretamente em DataFrame se o pandas conseguir ler
print(df.columns); print(df.head()) # Ver os nomes das colunas
# if "Symbol" in df.columns and "Name" in df.columns: df_filtered = df[["Symbol", "Name"]] # Selecionar apenas colunas relevantes
# else:
#     df_filtered = df.iloc[:, :2]; df_filtered.columns = ["Symbol", "Name"] # tenta encontrar colunas parecidas (caso Yahoo altere ligeiramente os nomes)
# print("\nDataFrame com Ticker e Nome:") # print(df_filtered.head()) # Mostra o resultado
#df_filtered.to_csv("most_active_yahoo.csv", index=False) # Exportar para CSV (opcional)



urls = [
        "https://finance.yahoo.com/markets/commodities/",
        #"https://finance.yahoo.com/markets/crypto/all/"
        #"https://finance.yahoo.com/markets/bonds/"
        #"https://finance.yahoo.com/markets/world-indices/",
        #"https://finance.yahoo.com/markets/currencies/",
        #"https://finance.yahoo.com/markets/stocks/most-active/",
        #"https://finance.yahoo.com/markets/stocks/trending/",
        #"https://finance.yahoo.com/markets/stocks/gainers/",
        #"https://finance.yahoo.com/markets/stocks/losers/",
        #"https://finance.yahoo.com/markets/stocks/52-week-gainers/",
        #"https://finance.yahoo.com/markets/stocks/52-week-losers/",
        #"https://finance.yahoo.com/markets/stocks/highest-dividend/",
        #"https://finance.yahoo.com/markets/stocks/small-cap-stocks/",
        #"https://finance.yahoo.com/markets/stocks/large-cap-stocks/",
        #"https://finance.yahoo.com/markets/stocks/large-cap-stocks/",
        #"https://finance.yahoo.com/markets/stocks/most-expensive-stocks/",
        #"https://finance.yahoo.com/markets/stocks/highest-beta-stocks/"
        ]

headers = {"User-Agent": "Mozilla/5.0"}
#base_url = "https://finance.yahoo.com/markets/stocks/most-active/"
#dfr = pd.DataFrame()
for base_url in urls:
    dfs = []  # lista para juntar todas as tabelas
    # percorre as páginas de 200 em 200 resultados
    for start in range(0, 400, 200):  # 0, 200; ajusta se quiseres mais
        url = f"{base_url}?start={start}&count=200" #print(f"A ler: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find("table")
        if not table:
            print(f"Nenhuma tabela encontrada em {url}")
            break
        df_page = pd.read_html(str(table))[0]
        dfs.append(df_page)
    df = pd.concat(dfs, ignore_index=True) # junta todas as páginas num só dataframe
    #dfr = pd.concat([dfr, df], ignore_index=True)

# df = df.rename(columns=str.strip) # seleciona colunas relevantes
# cols = [c for c in df.columns if "Symbol" in c or "Name" in c]
# if len(cols) >= 2: df = df[cols[:2]]
# print(f"\nTotal de empresas recolhidas: {len(df)}") # print(df.head())
# df.to_csv("yahoo_most_active_all.csv", index=False) # guardar em CSV



r, s = {}, {}
for k in range(dfr.shape[0]):
    if dfr.Symbol.iloc[k] in r.keys() and not(dfr.Name.iloc[k] in r[dfr.Symbol.iloc[k]]): r[dfr.Symbol.iloc[k]] += [dfr.Name.iloc[k]]
    else: r[dfr.Symbol.iloc[k]] = [] + [dfr.Name.iloc[k]]
for k in range(dfr.shape[0]):
    if dfr.Name.iloc[k] in s.keys() and not(dfr.Symbol.iloc[k] in s[dfr.Name.iloc[k]]): s[dfr.Name.iloc[k]] += [dfr.Symbol.iloc[k]]
    else: s[dfr.Name.iloc[k]] = [] + [dfr.Symbol.iloc[k]]
del k     
pd.DataFrame(dict([(k, pd.Series(v)) for k, v in s.items()]))






# from matplotlib.pyplot import plot
# import matplotlib.pyplot as plt #%matplotlib inline
# plt.style.use('seaborn-v0_8-darkgrid')
# plt.style.use("seaborn-v0_8-whitegrid")
class empresa():
    def __init__(self, nome, ticker, tic, exchange, sector, country, currency):
        self._tk = tic
        # Informação geral
        self._info = pd.DataFrame({"Nome": [nome], "Ticker": [ticker], 'Exchange': [exchange], 'Setor': [sector], 'Country': [country], 'Currency': [currency]}) 
        self._info.index.name = "Info"
        self._ptemp = pd.DataFrame({}) # Por aqui de que datas a que datas é que se tem info da empresa
        self._ptemp.index.name = "Tempo"
        # Informação financeira
        self._bal = pd.DataFrame(index=["Total Assets", 
                                            "Current Assets", 
                                                #"Inventory",
                                                #"Receivables",
                                                #"Cash Cash Equivalents And Short Term Investments",
                                            "Total Non Current Assets",
                                                "Net PPE", 
                                                #"Goodwill And Other Intangible Assets", 
                                                #"Investments And Advances", 
                                        
                                        "Total Liabilities Net Minority Interest", 
                                            "Current Liabilities",
                                                #"Payables And Accrued Expenses", 
                                                #"Current Debt And Capital Lease Obligation", 
                                            
                                            "Total Non Current Liabilities Net Minority Interest", 
                                                #"Long Term Debt And Capital Lease Obligation", 
                                                #"Employee Benefits", 
                                                #"Derivative Product Liabilities", 

                                        "Total Equity Gross Minority Interest",
                                            "Stockholders Equity", 
                                            "Capital Stock", 
                                            "Retained Earnings", 
                                            
                                        "Total Capitalization", 
                                        "Common Stock Equity", 
                                        "Net Tangible Assets", 
                                        "Working Capital", 
                                        "Invested Capital", 
                                        "Tangible Book Value", 
                                        "Total Debt", 
                                        #"Net Debt", 
                                        "Share Issued", 
                                        "Ordinary Shares Number"]) #"Treasury Shares Number"])
                                        
        self._bal.index.name = "Balanco"
        self._dr = pd.DataFrame(index=["Total Revenue",
                                        "Cost Of Revenue",
                                        "Gross Profit",
                                        "Operating Expense",
                                        "Operating Income",
                                        "Net Non Operating Interest Income Expense",
                                        "Other Income Expense",
                                        "Pretax Income",
                                        "Tax Provision",
                                        "Net Income Common Stockholders",
                                        "Diluted NI Availto Com Stockholders",
                                        "Total Expenses",
                                        "Net Income From Continuing And Discontinued Operation",
                                        "Normalized Income",
                                        "Net Interest Income",
                                        "EBIT",
                                        "EBITDA",
                                        "Normalized EBITDA",
                                        "Tax Rate For Calcs",
                                        "Basic EPS",
                                        "Diluted EPS",
                                        "Basic Average Shares",
                                        "Diluted Average Shares",
                                        ])
        self._dr.index.name = "DR"
        self._rc = pd.DataFrame(index=["LG", "AF", "AT", "ROA", "SM", "PER"])
        self._rc.index.name = "RACIOS"
        # Informação de mercado
        #datas = pd.date_range(datetime.today() - timedelta(days=10), periods=10, freq='D')
        #preco = np.random.uniform(90, 120, size=10).round(2); volume = np.random.randint(10000, 100000, size=10)
        
        self._st = pd.DataFrame(columns=['Close', 'High', 'Low', 'Open', 'Volume'])
        self._st.index.name = "Preco"
    
    def info(self):
        return (self._info.loc[0,"Nome"], self._info.loc[0,"Ticker"])
    def nome(self):
        return self._info.loc[0,"Nome"]
    def ticker(self):
        return self._info.loc[0,"Ticker"]
    def setor(self):
        return # setor
    def balanco(self):
        return self._bal
    def resultados(self):
        return self._dr
    def precos_acao(self):
        return self._st[['Close', 'High', 'Low', 'Open']]
    
    def coloca_valores(self, df, tipo):
        if tipo == "Stock":
            df.columns = df.columns.droplevel(1) # Defeito do yfinance
            self._st = pd.DataFrame(columns=self._st.columns, index=df.index)
            for i in df.index:
                for j in df.columns:
                    self._st.loc[i,j]= df.loc[i,j]
        
        elif tipo == "DR":
            self._dr = pd.DataFrame(columns=df.columns, index=self._dr.index)
            for i in df.columns:
                for k in self._dr.index:
                    self._dr.loc[k,i] = df.loc[k,i]
                    
        elif tipo == "Bal":
            self._bal = pd.DataFrame(columns=df.columns, index=self._bal.index)
            for i in df.columns:
                for k in self._bal.index:
                    self._bal.loc[k,i] = df.loc[k,i]
                    
        #elif tipo == "RAC":
            
        tc = self._bal.columns if len(self._bal.columns)>=len(self._dr.columns) else self._dr.columns
        self._ptemp = pd.DataFrame(index=tc)
            
    def valores_tempo(self):
        return self._ptemp.index
    def valor_dr(self, date, rubrica):
        return self._dr.loc[rubrica,date]
    def valor_bal(self, date, rubrica):
        return self._bal.loc[rubrica,date]
    def valor_preco_acao(self, date, rubrica):
        return self._st.loc[date,rubrica]
    
    
    
    def calcula_rácios(self):
        # def div(a,b): return round(a/b,3) if b!=0 else None
        self._rc = pd.DataFrame(columns=self._ptemp.index, index= self._rc.index)
        for i in self._rc.columns:
            # Liquidez
            self._rc.loc["LG", i] = self._bal.loc["Current Assets",i] / self._bal.loc["Current Liabilities",i]
            # Solvabilidade / Endividamento / Estrutura Capital
            self._rc.loc["AF", i] = self._bal.loc["Total Equity Gross Minority Interest",i] / self._bal.loc["Total Assets",i]
            # Eficiência
            self._rc.loc["AT", i] = self._dr.loc["Total Revenue",i] / self._bal.loc["Total Assets",i]
            # Rendibilidade
            self._rc.loc["ROA", i] = self._dr.loc["Net Income Common Stockholders",i] / self._bal.loc["Total Assets",i]
            # Risco
            self._rc.loc["SM", i] = self._dr.loc["EBIT",i] / self._dr.loc["Gross Profit",i]
            # Mercado
            self._rc.loc["PER", i] =  self._bal.loc["Total Capitalization",i] / self._dr.loc["Net Income Common Stockholders",i]
    
    
    
    def show(self):
        # Mostra um resumo geral da empresa
        print(f"{self._info['Nome'].iloc[0]} ({self._info['Ticker'].iloc[0]})") #print(f"Setor: {self.info['Setor']} | País: {self.info['País']}")
        print("--------------- \n")
        print(f"\n {self._st}") 
        print("--------------- \n")
        print(f"\n {self._bal}")
        print("--------------- \n")
        print(f"\n {self._dr}")
        print("--------------- \n")
        print(f"\n {self._rc}")
        print("--------------- \n")

    def show_plot(self, tipo):
        print("Plot")

for i in [0]: #range(df.shape[0]):
    t = yf.Ticker(df["Symbol"].iloc[i])
    e = empresa(df["Name"].iloc[i], df["Symbol"].iloc[i], t.info["exchange"], t.info["sector"], t.info["country"], t.info["currency"])
    ds = yf.download(e.ticker(), start="2020-01-01", end="2025-11-01")
    e.coloca_valores(ds,"Stock") #ds.columns = ds.columns.droplevel(1)
    # Descarregar DFs
    # dr = t.financials # q_income = t.quarterly_financials
    # bal = t.balance_sheet # q_balance = t.quarterly_balance_sheet
    # cf = t.cashflow # q_cashflow = t.quarterly_cashflow
    e.coloca_valores(t.financials,"DR")
    e.coloca_valores(t.balance_sheet,"Bal")
    e.calcula_rácios()
    #e.show() #print("--------------- \n")
del i, ds, t


plt.figure(figsize=(15, 7)); e.precos_acao().plot(); plt.title(f"{e.nome()} Stock Price Data", fontsize=14); plt.ylabel('Price', fontsize=12) #plt.xlabel('Year-Month', fontsize=12) # Plot the close price

(e.precos_acao()/e.precos_acao().iloc[0]).plot() # Plot the absolute price series # Price change
plt.title(f"{e.nome()} Price Change", fontsize=14); plt.ylabel('Price Change', fontsize=12) # plt.legend() #plt.xlabel('Year-Month', fontsize=12)

ohlcv_dict = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'} # Aggregate function

ds = yf.download(tickers=e.ticker(), period="5d", interval="1m", auto_adjust=True, multi_level_index=False)
dsr = ds.resample('15T').agg(ohlcv_dict) # 15T for 15 minutes (H is for hour, D is for days, M is for months)
dsr.dropna(inplace=True); dsr.drop(columns=['Volume'], inplace=True)

ds.index = pd.to_datetime(ds.index) # Set the index to a datetime object

for i in list([df.shape[0]-1]): #range(df.shape[0]):
    #yf.download('EURUSD=X', period='5d', interval='1m')
    t = yf.Ticker(df.loc[i,"Symbol"])
    dfx = yf.download(df.loc[i,"Symbol"], start='2017-01-01', multi_level_index=False) # Set the ticker
    dfx.index = pd.to_datetime(dfx.index) # Set the index to a datetime object
    dfx.drop(columns=['Volume'], inplace=True); dfx.dropna(inplace=True);
    dfx['Close'].plot(); #plt.title(f"{di.loc[i,'Name']}", fontsize=14);
    #plt.legend([di.loc[i,"Symbol"] for i in range(dx.shape[0])])



t.options
t.option_chain(date=t.options[0]).calls.head()

# Calls
strike_prices = np.array(t.option_chain(date=t.options[0]).calls.strike)
last_prices = np.array(t.option_chain(date=t.options[0]).calls.lastPrice)

# Puts
strike_prices = np.array(t.option_chain(date=t.options[0]).puts.strike)
last_prices = np.array(t.option_chain(date=t.options[0]).puts.lastPrice)

plt.figure(figsize=(15, 7)); plt.plot(strike_prices, last_prices) # Plot call strike price vs call last traded price 
plt.xlabel('Strike Price', fontsize=12); plt.ylabel('Last Price', fontsize=12); plt.title('Microsoft Call/Put Options Last Price for Different Strike', fontsize=14)

t.get_earnings_dates() # Fetch the earnings calendar of the stock and store it in a DataFrame
t.get_earnings_dates().dropna(inplace=True) # Drop the NaN values

t.get_actions().tail(12) # Corporate actions # Print the last 10 corporate actions

