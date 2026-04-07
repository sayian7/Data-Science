import os # print(os.getcwd())
import pathlib
from pathlib import Path #import os
# %whos, dir(), locals()
# import pwd  # Apenas para Linux/macOS (Para Windows, usaremos outra abordagem)

import json
import time
import calendar
from datetime import datetime, date, timedelta

import shutil

import requests
from bs4 import BeautifulSoup

from PIL import Image
import cv2

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mimetypes

import numpy as np
import pandas as pd

import yfinance as yf

import itertools

from scipy.stats import norm
import scipy.stats as stats

from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose

import pulp

import matplotlib.pyplot as plt #%matplotlib inline #from matplotlib.pyplot import plot
plt.style.use('seaborn-v0_8-darkgrid')
plt.style.use("seaborn-v0_8-whitegrid")

from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D plotting

import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

from numpy import e, arange # import numpy as np
from matplotlib.pyplot import plot # as dataplot # ?dataplot
# import matplotlib.pyplot as plt # ?plt
# dataplot(x,y) # fig,ax=plt.subplots(); ax.plot(x,y); plt.show(); plt.close();



from matplotlib.pyplot import plot
from random import random, randint
from decimal import *
from numpy import e, pi, arange # import numpy as np
from math import sqrt # e, pi
from functools import reduce # import matplotlib.pyplot as plt # ?plt
# from matplotlib.pyplot import plot as dataplot # ?dataplot
import pandas as pd

def pascal(n):
    def natQ(n):
        return n>0 and int(n)==n # isinstance(n, int)
    def linha(n):
        r=[]
        for l in range(1,n+1):
            rs=[]
            for p in range(1,l+1):
                if p==1 or p==l:
                    rs += [1]
                else:
                    rs += [ r[l-2][p-2] + r[l-2][p-1] ]
            r+=[rs]
        return r[n-1]
    assert (n>0 and int(n)==n) # natQ(n)
    return linha(n)


if True:# aproximaIntegral(g,0,1.5,5) = 1.0125276039749722; # aproximaIntegral(g,0,1.5,500000) = 0.9162916318762734;
    
    def aproximaIntegral_for_old(f,a,b,n):
        d=(b-a)/n; r=[0]; l=[f(a+(i-1)*d) for i in range(1,n+1)]; # for i in range(1,n+1): r+=f(a+(i-1)*d)
        for x in arange(a,b+d,d):
            r+=f(x); # print(x,f(x),r)
        return d*r
    
    def aproximaIntegral_for_new(f,a,b,n):
        # f=(lambda x: pow(1+x,-1)); a=0; b=1.5; n=500000; 
        d=(b-a)/n; s=0; r=[s]; # print(a,b,n,d,s,r);
        for x in arange(a,b,d): # for i in range(1,n+1): r+=f(a+(i-1)*d)
            s += ((f(x)) - ((d*(f(x)-f(x+d)))/2)); # s += d*f(x); # s += d*f(x+d);
            r+=[s]; # r+=[f(x)]; # print(x,s,r);
        sum(r)
        return s*d
    
    def aproximaIntegral_func_new(f,a,b,n):
        d=(b-a)/n;
        g=(lambda x: f(x) - ((d*(f(x)-f(x+d)))/2));
        s=sum(list(map(g,arange(a,b,d)))) # r=list(map(g,arange(a,b,d)))
        return s*d

if True: # Diferenciação e Integração de funções: Primitivas e Derivadas. # from sympy import *
    x,y,z=symbols("x"),symbols("y"),symbols("z"); # e+E;
    a,b,c,n=Symbol("a"),Symbol("b"),Symbol("c"),Symbol("n"); 
    diff(x**2+x+5,x), diff(1/x**2,x), diff(sin(x),x), diff(f(x)**2,x), diff(f(x)+g(x),x), diff(f(x)*g(x),x), diff(f(g(x)),x),
    integrate(x,x), integrate(1/(1+x**2),x), integrate(x*sin(x),x), integrate(x,(x,0,1)), integrate(sin(x),(x,0,pi)), integrate(E**-x,(x,0,oo))

if True: # caminho = r"C:\Users\User\Desktop\asd.xlsx";
    import pandas as pd
    dados_excel = pd.read_excel(r"C:\Users\ASUS\OneDrive - Universidade de Lisboa\Desktop\Data_Worten_Sample.xlsx", sheet_name="SKU_INFO", usecols=[0,1,2]); # print(dados_excel)
    lista_dados = list(map(list,dados_excel.T.to_numpy())); # print(lista_dados); type(lista_dados) 
    
    xi=list(range(20)); yi=list(map((lambda x: e**x),range(20)));
    data_frame = pd.DataFrame(xi,yi);
    data_frame.to_excel(caminho) # print(data_frame)




if True: # caminho = r"C:\Users\User\Desktop\asd.xlsx"; 

    caminho1 = r"C:\Users\ASUS\OneDrive - Universidade de Lisboa\Desktop\EXEMPLO.xlsx";
    caminho2 = r"C:\Users\ASUS\OneDrive - Universidade de Lisboa\Desktop\EXEMPLO_OUT.xlsx";
    dados_excel = pd.read_excel(caminho);  # print(dados_excel)
    lista_dados = list(map(list,dados_excel.T.to_numpy()));
    # print(lista_dados); type(lista_dados) 
    
    xi=list(range(20)); yi=list(map((lambda x: e**x),range(20)));
    data_frame = pd.DataFrame(Lista);
    data_frame.to_excel(caminho2) # print(data_frame)
    
    Lista=[];
    for linha in ld_new:
        s=[];
        for x in linha:
            if x!=0: 
                s+=[x];
        Lista+=[s];

if True: # caminho = r"C:\Users\User\Desktop\asd.xlsx"; 

    caminho1 = r"C:\Users\ASUS\OneDrive - Universidade de Lisboa\Desktop\EX_IN.xlsx";
    caminho2 = r"C:\Users\ASUS\OneDrive - Universidade de Lisboa\Desktop\EX_OUT.xlsx";
    dados_excel = pd.read_excel(caminho1);  # print(dados_excel)
    lista_dados = list(map(list,dados_excel.T.to_numpy()));
    # print(lista_dados); type(lista_dados) 
    
    xi=list(range(20)); yi=list(map((lambda x: e**x),range(20)));
    data_frame = pd.DataFrame(L);
    data_frame.to_excel(caminho2) # print(data_frame)
    
    L=[];
    for x in l_new:
        if x<=0.1:
            L+=[0.1];
        elif x<=0.2:
            L+=[0.2];
        elif x<=0.3:
            L+=[0.3];
        elif x<=0.4:
            L+=[0.4];
        elif x<=0.5:
            L+=[0.5];
        elif x<=0.6:
            L+=[0.6];
        elif x<=0.7:
            L+=[0.7];
        elif x<=0.8:
            L+=[0.8];
        elif x<=0.9:
            L+=[0.9];
        elif x<=1:
            L+=[1];



s = ['a','b','c',]
l = [list(range(i,i+3)) for i in range(5)]; l
d = {lin[0] : {'a': lin[1], 'b': lin[2]} for lin in l}; d
[[d[x][y] for y in d[x].keys()] for x in d.keys()]
l_aux = [d[x][y] for y in d[x].keys() for x in d.keys()]; 
[d[x][y] for x in d.keys() for y in d[x].keys()]; 
[x for elem in w for x in elem]
reduce(lambda x,y:x+y,[[d[x][y] for y in d[x].keys()] for x in d.keys()],0)




from math import floor, ceil
import matplotlib.pyplot as plt # from matplotlib.pyplot import plot, hist
from random import random, randrange # randint
var_x = [int(random()*randrange(0,100,1)) for i in range(100)]; set(var_x) # var_x = [ random()*randrange(0,100,1) for i in range(100)];

def dummy_fun(var_x, n, start):
    # start = 0; n = 5; # var_x = [ random()*randrange(0,100,1) for i in np.arange(0,100,1)];
    #var_x = [int(random()*randrange(0,100,1)) for i in range(100)]; set(var_x)
    d = (max(var_x)-min(var_x))/n; 
    dummy_labels = [ (i,floor(start+(d*i))) if i<n else (i,ceil(max(var_x))) for i in range(n+1) ]; 
    #print("gen var_dummy = 0 // var2")
    #for i,x in dummy_labels: print("replace var_dummy = ", i, " if var_x >= ", x)
    #print("replace var_dummy = . if var_x == .  // treats missing values")
    var_dummy = []; r = [[] for i in range(len(dummy_labels))]; 
    for i,x in enumerate(var_x):
        q=False; j=0; 
        while not(q) and j <= len(dummy_labels): 
            if x <= dummy_labels[j][1] and j <= len(dummy_labels)-1: 
                r[j] += [[i,x,dummy_labels[j][1],dummy_labels[j][0]]]; 
                var_dummy += [dummy_labels[j][0]]; 
                q=True;
            elif x > dummy_labels[j-1][1] and j==len(dummy_labels): 
                r[j] += [[i,x,dummy_labels[j][1],dummy_labels[j][0]]]; 
                var_dummy += [dummy_labels[j][0]]; 
                q=True;
            j+=1
    """
    # var_x
    plt.hist(var_x, bins=20, edgecolor='black') # Create a histogram # Adjust the number of bins as needed
    plt.xlabel('Value'); plt.ylabel('Frequency'); plt.title('Histogram Example'); # Add labels and title
    plt.show() # Show the histogram
    
    # var_dummy
    plt.hist(dummy_fun(var_x,n,start), bins=10, edgecolor='black') # Create a histogram # Adjust the number of bins as needed
    plt.xlabel('Value'); plt.ylabel('Frequency'); plt.title('Histogram Example'); # Add labels and title
    plt.show() # Show the histogram
    
    """
    return var_dummy

def mostra_dummy_fun(var_x,n,start):
    # start = 0; n = 5; # var_x = [int(random()*randrange(0,100,1)) for i in range(100)]; set(var_x) # var_x = [ random()*randrange(0,100,1) for i in np.arange(0,100,1)];
    d = (max(var_x)-min(var_x))/n; 
    dummy_labels = [ (i,floor(start+(d*i))) if i<n else (i,ceil(max(var_x))) for i in range(n+1) ]; 
    print("gen var_dummy = 0 // var2")
    for i,x in dummy_labels: print("replace var_dummy = ", i, " if var_x >= ", x)
    print("replace var_dummy = . if var_x == .  // treats missing values")

def histogram_dummy(var_x):
    # var_x = [random()*randrange(0,100,1) for i in np.arange(0,100,1)]; set(var_x)
    for i in range(1,10,1): # Passos de 1
        plt.hist(dummy_fun(var_x,i,0), bins=i, edgecolor='black'); plt.xlabel('Value'); plt.ylabel('Frequency'); plt.title('Histogram Example'); plt.show() # Create a histogram # Adjust the number of bins as needed # Add labels and title # Show the histogram
        mostra_dummy_fun(var_x,i,0)
    for i in range(10,51,5): # Passos de 5
        plt.hist(dummy_fun(var_x,i,0), bins=i, edgecolor='black'); plt.xlabel('Value'); plt.ylabel('Frequency'); plt.title('Histogram Example'); plt.show() # Create a histogram # Adjust the number of bins as needed # Add labels and title # Show the histogram
        mostra_dummy_fun(var_x,i,0)





def permutacoes(w):
    result=[[]]
    for x in w:
        new_result=[]
        for u in result:
            #print(u)
            for i in range(len(u)+1):
                novo = u[:]; #print(novo)
                novo.insert(i,x); #print(novo)
                new_result += [novo]; #print(new_result)
        result = new_result; #print(result)
    return result


from itertools import combinations
def combinações(w):
    #from itertools import combinations
    #w = list(range(3)); r=[]; #s=[]; 
    result = []; 
    for i in range(1,len(w)+1): 
        combinacoes = combinations(w,i); r_combinacoes = []; 
        for combinacao in combinacoes: 
            r_combinacao = []; 
            for x in combinacao: 
                r_combinacao += [x]; 
            r_combinacoes += [r_combinacao]
        result += [r_combinacoes]; 
        #s += list(combinations(lista,i));
    #print(r,s) # print(s)
    return result
#combinações([chr(i) for i in range(65,71)])



if True: # Chat GPT: Combinations
    from itertools import combinations
    def generate_combinations(input_list):
        all_combinations = []
        for r in range(1, len(input_list) + 1):
            
            combinations_r = combinations(input_list, r) # Generate combinations of length r
            all_combinations.extend(combinations_r)
        return all_combinations
    # Example usage:
    my_list = ['A', 'B', 'C']
    result = generate_combinations(my_list)
    # Print the result
    for combination in result:
        print(combination)

def comb_reg_lin(lista,lista_var): 
    # Fazer as combinações possíveis para fazer todas as regressões lineares entre n variáveis
    from random import random, randrange # randint
    
    l = list(range(6)); v1 = l[0]; 
    ld = [l[i] for i in range(len(l)-1) if i!=0]
    r = []; 
     
    for i,x in enumerate(l): 
        ld = [l[j] for j in range(len(l)-1) if j!=i]; 
        rd = []; 
        for k,y in enumerate(ld): 
            print("")
    
    return l














from random import randint
import statistics
statistics.mean([ list(range(1,6))[randint(0,4)] for i in range(7774)]) #[list(range(1,6))[randint(0,4)] for i in range(7774)]
statistics.mean([ list(range(1,6))[randint(0,4)] for i in range(7774)]) #[list(range(1,6))[randint(0,4)] for i in range(90049)]



# Triangular Distribution
a=200; c=1060; b=2050; # Media = (a + b + c) / 3
p_c = 2/(b-a); P_c = (c-a)/(b-a); 
r=[]; 
for x in range(a,b+((b-a)/10),(b-a)/10): 
    p_x = ((x<=c)*((2*(x-a))/((b-a)*(c-a)))) + ((x>c)*((2*(b-x))/((b-a)*(b-c)))); # pdf
    P_x = ((x<=c)*(((x-a)**2)/((b-a)*(c-a)))) + ((x>c)*(1-(((b-x)**2)/((b-a)*(b-c))))); # cdf
    r+=[(x,p_x,P_x)]; 
r
del p_x, P_x, p_c, P_c, x, a, b, c, r

from sympy import symbols, solve
x,y=symbols("x"),symbols("y")
a,b,c = symbols("a"),symbols("b"),symbols("c"); 
solve((((x-a)**2)/((b-a)*(c-a)))-y, x) # CDF_INV_1 = [a - sqrt(y*(a - b)*(a - c)), a + sqrt(y*(a - b)*(a - c))]; 
solve((1-(((b-x)**2)/((b-a)*(b-c))))-y, x) # CDF_INV_2 = [b - sqrt((a - b)*(b - c)*(y - 1)), b + sqrt((a - b)*(b - c)*(y - 1))]; 



if True: # Modulo obsrand
    # Modulo obsrand: Disponibiliza uma função para gerar observações de uma variavel aleatoria com distribuicao exponencial # %load modules/obsrand
    import numpy as np; import matplotlib.pyplot as plt # %matplotlib notebook
    t = np.arange(0.0, 6.0, 0.01); s = 1-np.e**(-t/2); plt.plot(t, s) #1-np.e**(-6/2) #(lambda t: 1-np.e**(-t/2))(np.arange(0.0, 6.0, 0.01)) #f_x = (lambda t: 1-np.e**(-t/2)) #for i in range(15): plt.plot(np.arange(0.0, 10+1, 1) , 1-np.e**(-np.arange(0.0, 10+1, 1)/2) ); 
    from random import random; from math import log
    def exprandom(m):
        x=random()
        return -m*log(x)
    import obsrand; [obsrand.exprandom(2),obsrand.exprandom(2),obsrand.exprandom(2),obsrand.exprandom(100),obsrand.exprandom(100)] #for i in range(15): plt.plot(np.arange(0.0, 10+1, 1) , [ exprandom(i) for i in np.arange(0.0, 10+1, 1)] ); 



import math
from statistics import NormalDist
def kde_normal(sample, h):
    "Create a continuous probability density function from a sample."
    # Smooth the sample with a normal distribution of variance h.
    kernel_h = NormalDist(0.0, math.sqrt(h)).pdf
    n = len(sample)
    def pdf(x):
        return sum(kernel_h(x - x_i) for x_i in sample) / n
    return pdf
sample = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
f_hat = kde_normal(sample, h=2.25)
xarr = [i/100 for i in range(-750, 1100)]
yarr = [f_hat(x) for x in xarr]




def f_d_p(avg, stdev): # Func Dist Prob
    fdp = (lambda u,s,x: (1/sqrt(2*pi*(pow(s,2)))*pow(e,-(1/(2*pow(s,2)))*(pow(x-u,2))))); # Func Dens Prob. Geral
    l = [fdp(avg,stdev,i) for i in arange(-100,100.5,0.5)];
    fdp_NR = (lambda x: fdp(0,1,x)); # Func Dens Prob. Norm Red # u=0; s=1;
    l_NR = list(map(fdp_NR, arange(-100,100+0.5,0.5)));
    s=0; r=[s]; # print(s,r);
    for y in l:
        s+=y; r+=[s]; # print(f_xi,s);
    return s # r # print(r); dataplot(r);














# MULTIPLE / LINEAR REGRESSION : DATA SCIENCE

# Import necessary libraries #pip install scikit-learn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(42); X1 = np.random.rand(100, 1) * 10; X2 = np.random.rand(100, 1) * 10; # Generate some sample data
df = pd.read_csv('your_dataset.csv') # Assuming you have a dataset in a CSV file, load it into a pandas DataFrame # Replace 'your_dataset.csv' with the actual filename
X = df[['X1', 'X2', 'X3', '...']]; y = df['y'] # Assuming your dataset has columns 'X1', 'X2', ..., 'Xn' as independent variables and 'y' as the dependent variable # Replace these column names with your actual column names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) # Split the data into training and testing sets
model = LinearRegression() # Create a linear regression model
model.fit(X_train, y_train) # Fit the model on the training data
y_pred = model.predict(X_test) # Make predictions on the test data
# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred, squared=False))
coefficients = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.coef_}); print(coefficients) # Print the coefficients
print('Intercept:', model.intercept_) # Print the intercept








np.random.seed(42); num_points = 50 # Generate random data # For reproducibility
x,y,z = np.random.rand(num_points) * 10, np.random.rand(num_points) * 10, np.random.rand(num_points) * 10 # Coordinates for 3D scatterplot Random values for X, Y, Z
categories = np.random.choice([0, 1, 2], size=num_points) # Fourth variable to categorize points (e.g., 0, 1, 2)
colors = np.array(["red", "green", "blue"]); point_colors = colors[categories] # Map categories to colors # One color for each category
fig = plt.figure(figsize=(20, 10)) # Increase figure size (width, height in inches)
ax = fig.add_subplot(111, projection='3d'); scatter = ax.scatter(x, y, z, c=point_colors, marker='o') # Create 3D scatter plot
for i, color in enumerate(colors): ax.scatter([], [], [], c=color, label=f"Category {i}") # Add legend to identify categories
ax.legend(loc="upper right"); ax.set_xlabel("X Axis"); ax.set_ylabel("Y Axis"); ax.set_zlabel("Z Axis"); ax.set_title("3D Scatter Plot with Categories") # Add labels and title
#fig.subplots_adjust(left=0.1, right=2, bottom=0.1, top=0.9)
ax.set_zlabel("Z Axis", labelpad=0)
plt.show() # Show the plot #plt.savefig("3d_scatter_plot.png", dpi=300)  # Save the plot with higher quality (optional) # Higher dpi for better quality















cmnho = str(os.getcwd())
def path(caminho, string):
    if not(isinstance(string,str)): string = str(string)
    return str(caminho+string)
path = "C:/Users/João Paulo/Desktop/DS/data/"






# Lixo -> Conversor de imagem

from PIL import Image
Image.MAX_IMAGE_PIXELS = None

# Open the PNG file # Input and output file paths
input_path = "C:/Users/João Paulo/Desktop/Part 1/scatterplots.png"
output_path = "C:/Users/João Paulo/Desktop/Part 1/scatterplots_converted_file.jpg"

# Convert and save as JPEG
image = Image.open(input_path).convert("RGB")  # Remove transparency
image.save(output_path, "JPEG", optimize=True, quality=50)  # Save as JPEG

image = Image.open(input_path) # Open the PNG file
new_size = (image.width // 2, image.height // 2); image = image.resize(new_size, Image.ANTIALIAS) # Resize the image to 50% of its original size # Adjust scale if needed
image = image.convert("RGB"); image.save(output_path, "JPEG", optimize=True, quality=85) # Convert and save as JPEG # Remove transparency if present


from PIL import Image
Image.MAX_IMAGE_PIXELS = None

input_path = "C:/Users/João Paulo/Desktop/scatterplots.png"; output_path = "C:/Users/João Paulo/Desktop/scatterplots_converted_file.jpg" # Open the PNG file # Input and output file paths

image = Image.open(input_path) # Open the PNG file
new_size = (image.width // 2, image.height // 2); image = image.resize(new_size, Image.Resampling.LANCZOS) # Resize the image to 50% of its original size # Adjust scale if needed
image = image.convert("RGB"); image.save(output_path, "JPEG", optimize=True, quality=65) # Convert and save as JPEG # Remove transparency if present




import cv2
image = cv2.imread(input_path) # Read the PNG image
cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 30])  # Quality: 1-100 # Save as JPEG with compression

# Resize the image (optional)
scale_percent = 50  # Resize to 50% of the original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Save as JPEG with aggressive compression
cv2.imwrite(output_path, resized_image, [int(cv2.IMWRITE_JPEG_QUALITY), 30])  # Quality: 1-100













# Histograms with different bin numbers (symbolic)

d = {f"{i}-{i+7-1}": int( (i+6)/7 ) for i in range(1,49,7) }
counts = {i: 0 for i in range(1,7+1)}
levels = [ i for i in range(1,49,7) ]


# Equal width discretization -> Consequência é que a distribuição muda

var = "var1"
n_min = 1 #min(data[var])
n_max = 37 #max(data[var])
bin_size = 5
lvars = []
dvars_in = {}
for k in range(n_min, n_max//2 + 4, bin_size): # Se o k for parametro fixo (à escolha), necessário por para fora e tirar o ciclo for e ainda adaptar o código se necessário
    data[var+"_bin="+str(k)] = data.apply(lambda x: 0 * ( x[var] ), axis=1); lvars += [var+"_bin="+str(k)]
    ints = [i for i in range(n_min,n_max+1,k)]; ints_nomes = [f"{i}-{i+k-1}" for i in range(n_min,n_max+1,k)]
    dvars_in[var+"_bin="+str(k)] = [f"{i}-{i+k-1}" for i in range(n_min,n_max+1,k)]
    for j in range(data.shape[0]):
        val = data[var].loc[j]
        for i in range(len(ints)):
            if i < (len(ints)-1) and ( val >= ints[i] and val < ints[i+1] ) : data[var+"_bin="+str(k)][j] = ints_nomes[i] #if val >= ints[i] and val < ints[i+1] : data[var+"_bin="+str(k)][j] = ints_nomes[i]
            elif i == (len(ints)-1) and val >= ints[i]: data[var+"_bin="+str(k)][j] = ints_nomes[i]



rows, cols = 2,3 # define_grid(len(symbolic))
fig, axs = subplots(rows, cols, figsize=(cols * 5, rows * 5), squeeze=False)
i, j = 0, 0
for n in range(rows*cols):
    if n < len(lvars):
        counts: Series = data[lvars[n]].value_counts()
        
        lx = dvars_in[lvars[n]] #lx = list(data[symbolic[n]].unique()); lx = [int(x) for x in lx]; lx.sort(); lx = [str(int(x)) for x in lx] #ly = [counts[x] for x in lx]
        # lista = [str(np.random.randint(0,i+1)) for i in range(10)]; lista.sort(); print(lista)
        
        plot_bar_chart([s.split("-")[0] for s in lx], [counts[x] for x in lx], ax=axs[i, j], title="Histogram for %s" % lvars[n], percentage=False)
        #plot_bar_chart(lx, [counts[x] for x in lx], ax=axs[i, j], title="Histogram for %s" % symbolic[n], xlabel=symbolic[n], percentage=False)
        
        i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
        
    else: axs[i, j].hist([]); axs[i, j].set_xticks([]);  axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False)





# Equal frequency discretization -> Consequência/limitação de alterar a distribuição original dos dados, e provocar alterações profundas nos resultados das descoberta de padrões
# Partitions the range of variable A into k intervals containing aproximately the same number of points.
# Each interval with 1/k of the probability mass computed by the inverse cumulative distribution functuin, F_A(-1)
# i_th interval boundary v_i given by: v_i = F_A(-1) (i/k), Vi 1,...,k-1

import numpy as np
l = [np.random.randint(15) for i in range(30)]; l.sort() #lista = list(range(100))
lx = list(set(l))

k = 5 # Nr de intervalos a dividir com igual/semelhante distribuição; Pode ser feito um ciclo para testar a variação do k
N = len(l)
cs = N // k # resto = n_counts_int % k
#n_min = min(lista); n_max = max(lista)

dc = {v: len([x for x in l if x==v]) for v in lx}
d = {i: lx[i] for i in range(len(lx))}

n=0
r = {i: [0,[]] for i in range(1,k+1,1)}
for i in range(1,k+1,1):
    c = 0; lc = []
    for j in range(n,len(lx)):
        if c < cs:
            val = d[j]; lc += [val]
            c += dc[val]
        else:
            break
    n = j
    r[i] = [c, lc]




























# Parameters for the normal distribution
mean, std_dev = 0, 1  # Mean (μ) # Standard deviation (σ)
x = np.linspace(-5, 5, 100) # Example x-values
pdf_values = norm.pdf(x, loc=mean, scale=std_dev) # Calculate PDF
print(pdf_values) # Print or visualize results
def normal_pdf(x, mean=0, std_dev=1):
    return (1 / (np.sqrt(2 * np.pi * std_dev**2))) * np.exp(-((x - mean)**2) / (2 * std_dev**2))
pdf_values = normal_pdf(x, mean=0, std_dev=1)

#x = pd.Series(np.linspace(-5, 5, 100))
#pdf_values = x.apply(lambda v: norm.pdf(v, loc=0, scale=1))

plt.plot(np.linspace(-5, 5, 100),norm.pdf(np.linspace(-5, 5, 100), loc=0, scale=1))


plt.plot(x, pdf_values, label="Normal PDF")
plt.title("Normal Distribution PDF", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Density", fontsize=12)

#f = (lambda x, u, s: norm.pdf(x, loc=u, scale=s))

h = 5
rows, cols = 1, 2
fig, ax = plt.subplots(rows, cols, figsize=(cols * h, rows * h), dpi=300)
for i in range(rows*cols):
    ax[i].plot(x, norm.pdf(np.linspace(-5, 5, 100), loc=0, scale=1+i), label="Normal PDF")
    ax[i].set(title="Normal Distribution PDF", xlabel="x", ylabel="Density") #ax.grid(True)
    ax[i].legend(["PDF"]) #plt.show()

rows, cols = 1,1
legend=[]
fig, ax = plt.subplots(rows, cols, figsize=(cols * h, rows * h), dpi=300)
for i in range(2):
    #ax.plot(x, norm.pdf(np.linspace(-5, 5, 100), loc=0, scale=1+i), label="Normal PDF")
    ax.bar(x, norm.pdf(np.linspace(-5, 5, 100), loc=0, scale=1+i), label="Normal PDF")
    #ax.scatter(x, norm.pdf(np.linspace(-5, 5, 100), loc=0, scale=1+i), label="Normal PDF")
    legend.append(f"x{i}")
ax.set(title="Normal Distribution PDF", xlabel="x", ylabel="Density") #ax.grid(True)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(legend) #plt.show()






# a, b = True, True; (a and not b) or (not a and b) # XOR



data = [np.random.normal(10,1) for i in range(10)] # Sample data
n = len(data) # Sample size
mean = np.mean(data) # Mean of the data
std_dev = np.std(data, ddof=1) # Sample standard deviation (ddof=1 for sample)
confidence_level = 0.95 # Confidence level
df = n - 1 # Degrees of freedom
t_critical = stats.t.ppf((1 + confidence_level) / 2, df) # Critical t-value for the confidence level
margin_of_error = t_critical * (std_dev / np.sqrt(n)) # Margin of error
Confidence_Interval = [mean - margin_of_error, mean + margin_of_error] # Confidence Interval #lower_bound, upper_bound = mean - margin_of_error, mean + margin_of_error
print(mean, margin_of_error, Confidence_Interval)

















def multivariate_gaussian_pdf(x, y, mean, covariance): # Function to compute the multivariate Gaussian PDF
    pos = np.dstack((x, y))  # Combine x and y into position vectors
    size = mean.shape[0]
    det = np.linalg.det(covariance)
    inv_cov = np.linalg.inv(covariance)
    norm_const = 1 / (np.sqrt((2 * np.pi) ** size * det))
    diff = pos - mean
    exponent = -0.5 * np.einsum('...i,ij,...j', diff, inv_cov, diff)
    return norm_const * np.exp(exponent)
# Parameters for the 2D Gaussian
#mean = np.array([0, 0])  # Mean vector (center)
#covariance = np.array([[1, 0.5], [0.5, 1]])  # Covariance matrix
#print("Mean Vector:"); print(mean_vector) #print("\nCovariance Matrix:"); print(covariance_matrix) # Output the results

# Generate 100 random points for x and y
#np.random.seed(42) # For reproducibility
data1 = np.random.rand(100, 2)  # 100 points with (x, y) coordinates
data2 = np.random.randn(100, 2)  # 100 points with (x, y) coordinates

#mean = np.mean(data, axis=0) # Compute the mean vector
#covariance = np.cov(data, rowvar=False) # Compute the covariance matrix

x = np.linspace(0, 1, 100); y = np.linspace(0, 1, 100); x, y = np.meshgrid(x, y) # Create a grid of x and y values

z1 = multivariate_gaussian_pdf(x, y, np.mean(data1, axis=0), np.cov(data1, rowvar=False)) # Compute the PDF1
z2 = multivariate_gaussian_pdf(x, y, np.mean(data2, axis=0), np.cov(data2, rowvar=False)) # Compute the PDF2

fig = plt.figure(figsize=(12, 8)); ax = fig.add_subplot(111, projection='3d'); 
surf1 = ax.plot_surface(x, y, z1, cmap='viridis', alpha=0.8, edgecolor='none', label="Gaussian 1") # Plot the 3D surface
surf2 = ax.plot_surface(x, y, z2, cmap='plasma', alpha=0.8, edgecolor='none', label="Gaussian 2") # Surface for the second Gaussian


#ax.set_title('Multivariate Gaussian PDFs'); ax.set_xlabel('X-axis'); ax.set_ylabel('Y-axis'); ax.set_zlabel('PDF value'); # Customize the plot
# Turn off visual noise
ax.axis('off')  # Turns off the entire axis (grid, ticks, labels)
ax.grid(False)  # Ensure the grid is off




# from sklearn.linear_model import LinearRegression
df = pd.read_excel("C:/Users/João Paulo/Desktop/Proj/Homework II.xlsx", sheet_name="DS_Order", header=0, na_values="")
numeric = ['unsafe', 'session', 'reg', 'hot', 'massage_cl', 'provider_second', 'llength', 'age', 'asq', 'school', 'exper', 'exper_sq', 'race', 'marr_status', 'bmi', 'lnw', 'age_cl', 'asq_cl', 'appear_cl', 'race_cl']
plt.scatter(df["X"], df["Y"], color='blue', label="Data points")
X = df['X'].values.reshape(-1,1); y = df['Y'].values
model = LinearRegression(); model.fit(X,y); y_pred = model.predict(X)
plt.plot(df['X'], y_pred, color='red', label = "Regression line")
plt.xlabel('X'); plt.ylabel('Y'); plt.title('Scatter plot with Regression Line'); plt.legend(); #plt.show()

ids = list(df['id'].unique()); ids.sort()
l = df[['id','session']].to_numpy()
d = {i: [] for i in ids}
for i, x in enumerate(l): d[x[0]] += [x[1]]
for i in d.keys(): d[i].sort()
r = {i: (1,1,1,1) if len(d[i]) == 1 and d[i][0] == 1 else (2,len(d[i]),min(d[i]),max(d[i])) for i in d.keys() }
# rn = {i: r[i] for i in r.keys() if r[i]!=0}
lr = [[],[],[],[]]; 
for i in df['id'].to_numpy(): lr[0] += [r[i][0]]; lr[1] += [r[i][1]]; lr[2] += [r[i][2]]; lr[3] += [r[i][3]]
df = pd.concat([df, pd.DataFrame({'First_session': lr[0], 'Nr_sessions': lr[1], 'First': lr[2], 'Last': lr[3]})], axis = 1)
df.to_clipboard(index=False)



ds = pd.read_clipboard(index_col=0)

d = {}
for i in ds.columns:
    for j in ds.index:
        d[(i,j)] = ds[i][j]
vals = [x for x in d.values() if not np.isnan(x)]; vals.sort()


def vals_abs(lista):
    r = []
    pos = [x for x in lista if x>=0]; pos.sort()
    neg = [x for x in lista if x<0]; neg.sort()
    for i in range(len(lista)):
        if len(pos) > 0 and len(neg) > 0:
            if abs(neg[0]) > pos[-1]: r+=[neg[0]]; neg = neg[1:]
            else: r+=[pos[-1]]; pos = pos[:-1]
        elif len(pos) == 0 and len(neg) > 0:
            r+=[neg[0]]; neg = neg[1:]
        elif len(pos) > 0 and len(neg) == 0:
            r+=[pos[-1]]; pos = pos[:-1]
    return r

lvals = vals_abs(vals)

r = {}
for i,x in enumerate(lvals):
    for k in d.keys():
        if d[k] == x:
            r[k] = x

ddf = pd.Series(r)
ddf.to_clipboard()
