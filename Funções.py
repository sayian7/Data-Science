"""     # NB 1: Funções Básicas

escreve_percentagem(25,11),w # ?escreve_percentagem
x=percentagem(88,20); x, percentagem(20,14)
alunos=102; avaliados=78; aprovados=64; percentagens(alunos,avaliados,aprovados)
estatistica([10,20,0,0,9,6,14])
"""
"""     # NB 3 Funções - Listas e tipos de iteráveis

pares([1,2,10,44,33,1,2,45,71]),contapares([1,2,10,44,33,1,2,45,71]), [parQ(2),parQ(3),conta([1,2,10,44,33,1,2,45,71],parQ),selecciona([1,2,10,44,33,1,2,45,71],parQ)]
[imparQ(2), imparQ(3), conta([1,2,10,44,33,1,2,45,71],imparQ), selecciona([1,2,10,44,33,1,2,45,71],imparQ)]
aplana([[1,2,3],[4,5],[6],[7,8,9]])
listacresc([1,2,3]), listacresc([2,1,2]), linhascresc([[1,2,3],[4,2,1],[5,2,7],[4,5,6],[1,1,1]])
matriz=[[1,2,3],[4,5,6],[7,8,9]]; [matriz[i][i] for i in range(len(matriz))], diagonal([[1,2,3],[4,2,1],[5,2,7],[4,5,6],[1,1,1]]), diagonalcresc([[1,2,3],[4,2,1],[5,2,7],[4,5,6],[1,1,1]])
m=[[1,2],[3,4],[5,6]]; [[linha[i] for linha in m] for i in range(len(m[1]))], transposta([[1,2],[3,4],[5,6]]), colunascresc([[1,5,2,6],[1,4,3,6],[1,7,4,2]])
grafo([1,12,14,32,5,1,10]), [segpospar([0,1]),segpospar([1,12])], pospares([1,12,14,32,5,1,10])
grafo([1,12,14,32,5,1,10]), selecciona(grafo([1,12,14,32,5,1,10]),segpospar), transposta(selecciona(grafo([1,12,14,32,5,1,10]),segpospar)), transposta(selecciona(grafo([1,12,14,32,5,1,10]),segpospar))[0]
indlinhascresc([[1,2,3],[3,4,1],[1,2,2],[4,2,1]]), [seglistacresc([0,[1,2,3]]),seglistacresc([1,[3,2,4]])]
a=5; b=[4,5,6]; [fun(a),a],[fun(b),b]
lista=[1,2,3]; valor=5; newfun(lista,valor),lista,valor
sumprod(5,6)
t=(1,2,3); f(5,6,7,10), f(5,*t)
v=(1,1); d={"b":100,"c":10,"a":1}; g(1,1,a=8,b=23), g(1,*v,**d)
"""
"""     # NB 4 - Funções Recursivas.

[exponencial(0,10),exponencial(2,10),2**10], [factorial(7),factorial(4.3)]
[factorial_robusto(5),factorial_robusto(-7)], [factorial_robusto2(0),factorial_robusto2(3.1)]
mdc(234,1108), compr([4,5,6]), media([1,2,4]), ate(10), flista([5,7,10])
[prefixoQ([1,2,3],[1,2,3,4,5]),prefixoQ([2,3],[1,2,3,4,5])], todosQ([2,4,6],parQ), algumQ([1,3,5,7],parQ)
palindromoQ([True,True,False]), digitos(1073), capicuaQ(12321)
primoQ(223), primosate(111), [n for n in ate(10) if primoQ(n)], [primo(n+1) for n in ate(10)], primo(100) # ?proxprimos
pesqzero(s1), pesqzero(s2), pesqzero(s3)
nposdig(4,3,mp.fraction(3,7)), nposdig(9,1,mp.pi), nposdig(9,20,mp.pi), nposdig(1,1,10**-100)
sqrmult(2,10)
[fibonacci(i) for i in range(8)]
flistaiter([7,8,9])
recpi(10),recpi(100),recpi(1000),recpi(10000),recpi(10000),recpi(10000)
iterpi(10000), iterpi(10000)

%time sqrmult(2,1000)
%time exponencial(2,1000)

%time fibonacci(20)
%time fibonacci(35)
%time fib2(100)

%time maxlista(ate(25))
%time maxlista(ate(26))
%time max2(ate(26))

%time max3(ate(26))
%time max3(ate(260))

%time max4(ate(26))
%time max3(ate(260))

"""
"""     # NB 5 - Funções Imperativas.

[factorial(400),factorial(-2),factorial(4)], factorial(4), maufactorial(4), piorfactorial(4), factorial(7)
[flista([3,5,4]),flista2([3,5,4])], flista([7,8])
list2num([1,0,7,3]), list2num_v2([1,0,7,3,8,0])
valores=[1,2,3,4]; media(valores),resultado,valores
maximin([[3,4,8],[7,0,0],[0,6,0]])
hondt([100,80,30,20],9), gauss([[2,1,-1],[-3,-1,2],[-2,-1,1]],[8,-11,-3]), gauss([[2,1,-1],[4,2,-2],[-2,1,2]],[8,-11,-3]), biss(cos,0,pi,10**(-10)), biss(lambda x:x*cos(x)-log(x),1,2,.0001)
sudokuQ([[1,5,4,8,7,3,2,9,6],[3,8,6,5,9,2,7,1,4],[7,2,9,6,4,1,8,3,5],[8,6,3,7,2,5,1,4,9],[9,7,5,3,1,4,6,2,8],[4,1,2,9,6,8,3,5,7],[6,3,1,4,5,7,9,8,2],[5,9,8,2,3,6,4,7,1],[2,4,7,1,8,9,5,6,3]])
sudokuQ([[5,1,4,8,7,3,2,9,6],[3,8,6,5,9,2,7,1,4],[7,2,9,6,4,1,8,3,5],[8,6,3,7,2,5,1,4,9],[9,7,5,3,1,4,6,2,8],[4,1,2,9,6,8,3,5,7],[6,3,1,4,5,7,9,8,2],[5,9,8,2,3,6,4,7,1],[2,4,7,1,8,9,5,6,3]])
pares([4,5,6]), tuplos(3,[0,1]), partes([1,2,3]), permutacoes([1,2,3,4])

"""
"""     # NB 6 - Algoritmos de ordenação

w=list(range(1000)); %time binsearch(999,w)
w=list(range(2000)); %time binsearch(1999,w)
w=list(range(4000)); %time binsearch(3999,w)
w=list(range(8000)); %time binsearch(7999,w)

from random import *
w=list(range(20)); shuffle(w); %time slowsort(w)

shufflecaseiro(list(range(10))), shufflecaseiro(list(range(10)))

%time luckysort(shufflecaseiro(list(range(10)))), %time luckysort(shufflecaseiro(list(range(10))))

%time insertsort(shufflecaseiro(list(range(10))))
%time insertsort(shufflecaseiro(list(range(100))));None
%time insertsort(shufflecaseiro(list(range(1000))));None

%time selectsort(shufflecaseiro(list(range(10))))
%time selectsort(shufflecaseiro(list(range(100))));None
%time selectsort(shufflecaseiro(list(range(1000))));None

%time quicksort(shufflecaseiro(list(range(10))))
%time quicksort(shufflecaseiro(list(range(100))));None
%time quicksort(shufflecaseiro(list(range(1000))));None

%time mergesort(shufflecaseiro(list(range(10))))
%time mergesort(shufflecaseiro(list(range(100))));None
%time mergesort(shufflecaseiro(list(range(1000))));None

%time countsort(shufflecaseiro(list(range(10))),0,10)
%time countsort(shufflecaseiro(list(range(100))),0,100);None
%time countsort(shufflecaseiro(list(range(1000))),0,1000);None
%time sorted(shufflecaseiro(list(range(1000))));None
%time shufflecaseiro(list(range(1000))).sort()

"""
"""     # NB 7 - Programação Funcional

from math import factorial
from random import *

from functools import reduce
from functools import partial
?reduce, ?partial

from time import sleep

import sys
sys.setrecursionlimit(2100)

# type(quadrado), ?map, ?filter, ?range
def quadrado(x):
    return x**2
g=(lambda x,y:x*y); g(7,9), quadrado(5), (lambda x:x**2)(5) 

%time any(map(lambda x:f_sleep(x)==0,range(100)))
%time any([f_sleep(x)==0 for x in range(100)])

quadrados([5,6,7]), quadrados([5,6,7]), qperfeitos([1,7,0,9,0.3,25]), powers([4,5,6,2,0,2])
algumperfeito([3,3,3,5]), todosperfeitos([9,100,49]), quantosperfeitos([8,100,49])
pertenceQ(1,[3,2,1]), transposta([[1,2,3],[4,5,6]])
media([3,6,12]), factfun(0), factlist(range(10))
mymap(lambda x:x+1,[3,4,5]), myany([False,False,False]), nest(lambda x:x+1,5,10)
minimo([4,1,7,-10,5,3]), fixedpoint(lambda x:x+1 if x<5 else x,0), fechotrans([[0,1],[1,2],[2,3],[3,4]])
dobro = mymult(2); triplo = mymult(3); mymult(7)(8),dobro(10)+triplo(5)
somatrescurryed=curryfun(somatres,3), somatrescurryed(5)(6)(7), 
somatresuncurryed=uncurryfun(somatrescurryed), somatresuncurryed(5,6,7)

Y(FACT)(5)
replica([5,6,7],3), Y(REP)([5,6,7],3), Y(REP_v2)([5,6,7])(3)

list(map_imperativo(lambda x:x+1,[3,4,5])), reduce_imperativo(lambda x,y:x+y,[3,4,5],0)
list(i**2 for i in range(10) if i%2==0), list(compreens_imperativo(lambda i:i**2,range(10),lambda i:i%2==0))

factrec(5)

def disp_f(w):
    a=0
    for i in w:
        a=a+i
        print(a)
disp_f([3,4,5])

para([3,4,5],prog,{"a":0});

wsmall=[randrange(200,250) for i in range(1000)]; wmedium=[randrange(1900,2000) for i in range(100)]; wlarge=[randrange(40000,50000) for i in range(10)]
%time x=[factorial_rec(x) for x in wsmall];None
%time x=[factorial_rec(x) for x in wmedium];None
%time x=[factorial_rec(x) for x in wlarge];None
%time x=[factorial_iter(x) for x in wsmall];None
%time x=[factorial_iter(x) for x in wmedium];None
%time x=[factorial_iter(x) for x in wlarge];None
%time x=[factorial_imp_while(x) for x in wsmall];None
%time x=[factorial_imp_while(x) for x in wmedium];None
%time x=[factorial_imp_while(x) for x in wlarge];None
%time x=[factorial_imp_for(x) for x in wsmall];None
%time x=[factorial_imp_for(x) for x in wmedium];None
%time x=[factorial_imp_for(x) for x in wlarge];None
%time x=[factorial_func(x) for x in wsmall];None
%time x=[factorial_func(x) for x in wmedium];None
%time x=[factorial_func(x) for x in wlarge];None
%time x=[factorial(x) for x in wsmall];None
%time x=[factorial(x) for x in wmedium];None
%time x=[factorial(x) for x in wlarge];None

"""

if True: # Funções úteis
    if True:
        
        def nest(f,n,x):
            return reduce(lambda a,b:f(a),range(n),x)
        
        def reduce_imperativo(f,iterable,x):
            r=x
            for y in iterable:
                r=f(r,y)
            return r
        def compreens_imperativo(expr,iterable,cond):
            for i in iterable:
                if cond(i):
                    yield expr(i)
        
        def permutacoes(w):
            res=[[]]
            for x in w:
                nres=[]
                for u in res:
                    for i in range(len(u)+1):
                        novo=u[:]
                        novo.insert(i,x)
                        nres+=[novo]
                res=nres
            return res
        def pares(w):
            res=[]
            for i in range(len(w)):
                for j in range(len(w)):
                    res.append([w[i],w[j]])
            return res
        def tuplos(n,w):
            res=[[]]
            for i in range(n):
                new=[]
                for j in range(len(res)):
                    for k in range(len(w)):
                        new.append(res[j]+[w[k]])
                res=new
            return res
        def partes(S):
            todos=tuplos(len(S),[0,1])
            res=[]
            for car in todos:
                sub=[]
                for i in range(len(S)):
                    if car[i]==1:
                        sub.append(S[i])
                res.append(sub)
            return res     
        def split(w):
            x=w[0]
            left=[]
            right=[]
            for i in range(1,len(w)):
                if w[i]<=x:
                    left+=[w[i]]
                else:
                    right+=[w[i]]
            return left,x,right
        def fusao(u,v):
            res=[]
            i=0
            j=0
            for k in range(len(u)+len(v)):
                if i<len(u) and (j==len(v) or u[i]<v[j]):
                    res.append(u[i])
                    i=i+1
                else:
                    res.append(v[j])
                    j=j+1
            return res
        def shufflecaseiro(w):
            for i in range(len(w)):
                j=randrange(i,len(w))
                w[i],w[j]=w[j],w[i]
            return w
        def slowsort(w):
            poss=permutacoes(w)
            i=0
            while not ordQ(poss[i]):
                i=i+1
            return poss[i]
        def quicksort(w):
            if len(w)<2:
                return w
            else:
                w1,x,w2=split(w)
                return quicksort(w1)+[x]+quicksort(w2)
        def luckysort(w):
            while not(ordQ(w)):
                shufflecaseiro(w)
            return w
        def insere(x,w):
            i=0
            while i<len(w) and w[i]<x:
                i=i+1
            w.insert(i,x)
            return w
        def insertsort(w):
            res=[]
            for i in range(len(w)):
                insere(w[i],res)
            return res
        def posmin(w,pos):
            for i in range(pos+1,len(w)):
                if w[i]<w[pos]:
                    pos=i
            return pos
        def selectsort(w):
            for i in range(len(w)-1):
                j=posmin(w,i)
                if j!=i:
                    x=w.pop(j)
                    w.insert(i,x)
            return w
        def mergesort(w):
            if len(w)<2:
                return w
            else:
                m=len(w)//2
                w1=mergesort(w[:m])
                w2=mergesort(w[m:])
                return fusao(w1,w2)
        def countsort(w,a,b):
            space=range(a,b+1)
            cont=[0 for val in space]
            for i in range(len(w)):
                cont[w[i]-a]+=1
            res=[]
            for val in space:
                res+=[val for quant in range(cont[val-a])]
            return res
        
        def curryfun(f,n):
            def curryult(h,i):
                def newh(*args):
                    return partial(h,*args)
                return newh
            return reduce(curryult,range(n-1),f)
        def uncurryfun(f):
            def g(*args):
                return reduce(aplica,args,f)
            return g
        
        def enquanto(cond,prog,estado):
            if cond(estado):
                return enquanto(cond,prog,prog(estado))
            else:
                return estado
        def para(iterable,prog,estado):
            iterador=iter(iterable)
            go=True
            while go:
                i=next(iterador,None)
                if i!=None:
                    estado=prog(i,estado)
                else:
                    go=False
            return estado
        def prog(i,estado):
            estado["a"]=estado["a"]+i
            print(estado["a"])
            return estado
    
    if True: # aplana(w)
        
        def aplana(w):
            return [x for elem in w for x in elem]
        def aplana_rec(m):
            def aplana_lista_aux(w):
                if w==[]:
                    return []
                else:
                    return [w[0]]+aplana_lista_aux(w[1:])
            if m==[]:
                return []
            else:
                return aplana_lista_aux(m[0])+aplana_rec(m[1:]) if isinstance(w[0],list) else [m[0]]+aplana_rec(m[1:])
    
    if True: # diagonal(m)
        
        def diagonal(m):
            return [m[i][i] for i in range(len(m))]
        def diagonal_rec(m):
            if m==[]:
                return []
            else:
                return diagonal_rec(m[:len(m)-1])+[m[len(m)-1][len(m)-1]]
    
    if True: # transposta(m)
        
        def transposta(m):
            return [[linha[i] for linha in m] for i in range(len(m[1]))]
        def transposta_(m):
            return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    
    if True: # map(f,w)
        
        def mymap(f,w):
            return reduce(lambda r,x:r+[f(x)],w,[])
        def map_imperativo(f,iterable):
            for x in iterable:
                yield f(x)
    
    if True: # myany(w) e myall(w)
        
        def myany(w):
            return reduce(lambda x,y:x or y,w,False)
        def myany_rec(w):
            if w==[]:
                return False
            else:
                return w[0] or myany_rec(w[1:])
        
        def myall(w):
            return reduce(lambda x,y:x and y,w,True)
        def myall_rec(w):
            if w==[]:
                return True
            else:
                return w[0] and myany_rec(w[1:])
    
    if True: # grafo(w)
        
        def grafo(w):
            return [[i,w[i]] for i in range(len(w))]
        def grafo_rec(w):
            if w==[]:
                return []
            else:
                return grafo_rec(w[:len(w)-1])+[[len(w)-1,w[len(w)-1]]]
    
    if True: # selecciona(w,p)
        
        def selecciona(w,p):
            return [x for x in w if p(x)]
        def selecciona_func(w,p):
            return list(filter(p,w))
        def selecciona_rec(w,p):
            if w==[]:
                return []
            else:
                return [w[0]]+selecciona_rec(w[1:],p) if p(w[0]) else selecciona_rec(w[1:],p)
    
    if True: # conta(w,p)
        
        def conta(w,p):
            return len([x for x in w if p(x)])
        
        def conta_rec(w,p):
            if w==[]:
                return []
            else:
                return 1+conta_rec(w[1:],p) if p(w[0]) else conta_rec(w[1:],p)
    
    if True: # ate(n)
        
        def ate(n):
            if n==0:
                return []
            else: 
                return ate(n-1)+[n-1]
        def ate_func(n):
            return list(range(n))
    
    if True: # comprimento(w)
        
        def comprimento(w):
            if w==[]:
                return 0
            else:
                return 1+comprimento(w[1:])
        def comprimento_func(w):
            return len(w)
    
    if True: # digitos(n)
        
        def digitos(n):
            if n<10:
                return [n]
            else:
                return digitos(n//10)+[n%10]
        def digitos_fun(n):
            return [int(str(x)) for x in str(n)]
        def digitos_func(n):
            return list(map(int,str(n)))
        def nposdig(d,n,num):
            def contar(d,n,num,pos,i):
                if floor(num*(10**pos))%10==d:
                    if i==n:
                        return pos
                    else:
                        return contar(d,n,num,pos+1,i+1)
                else:
                    return contar(d,n,num,pos+1,i)
            return contar(d,n,num,1,1)
    
    if True: # list2num_rec(w)
        
        def list2num_rec(w):
            if w==[]:
                return 0
            else:
                return (w[0]*10**(len(w)-1))+list2num_rec(w[1:])
        def list2num(w):
            r=0
            while len(w)!=0:
                r=w[0]+10*r
                w=w[1:]
            return r
        def list2num_v2(w):
            r=0
            i=len(w)
            while i!=0:
                r=r+w[i-1]*(10**(len(w)-i))
                i=i-1
            return r
        def list2num_v3(w):
            r=0
            for i in range(len(w)):
                r+=w[i]*(10**(len(w)-i-1))
            return r
        def list2num_v4(w):
            r=0
            for i,x in enumerate(w):
                r+=x*(10**(len(w)-i-1))
            return r
    
    if True: # replica(w,n)
        
        def replica(w,n):
            if w==[]:
                return []
            else:
                return [w[0] for i in range(n)]+replica(w[1:],n)
        def REP(f):
            def rep(w,n):
                if w==[]:
                    return []
                else:
                    return [w[0] for i in range(n)]+f(w[1:],n)
            return rep
        def REP_v2(f):
            def rep(w,n):
                if w==[]:
                    return []
                else:
                    return [w[0] for i in range(n)]+uncurryfun(f)(w[1:],n)
            return curryfun(rep,2)    

if True: # Funções auxiliares
    if True: # Funções Q
        
        if True: # temdivisorQ(n,i,j), primoQ(n)
            
            def temdivisorQ(n,i,j):
                if i>j:
                    return False
                elif n%i==0:
                    return True
                else:
                    return temdivisorQ(n,i+1,j)
            def primoQ(n):
                return n>1 and not(temdivisorQ(n,2,n-1))
            def primosate(n):
                if n<3:
                    return []
                elif primoQ(n-1):
                    return primosate(n-1)+[n-1]
                else:
                    return primosate(n-1)
            def primo(n):
                
                def proxprimos(i,k):
                    if k==1 and primoQ(i):
                        return i
                    elif k>1 and primoQ(i):
                        return proxprimos(i+1,k-1)
                    else:
                        return proxprimos(i+1,k)
                
                return proxprimos(2,n)
        
        if True: # parQ(n), pares(w), pospares(w)
            
            def parQ(n):
                return n%2==0
            def contapares(w):
                return len([x for x in w if x%2==0])
            def pares(w):
                return [x for x in w if x%2==0]
            def segundaposparQ(p):
                return p[1]%2==0
            def pospares(w):
                return transposta(selecciona(grafo(w),segundaposparQ))[0]
        
        if True: # quadradoperfeitoQ(x), quadradosperfeitosQ(w)
            
            def quadradoperfeitoQ(x):
                return ceil(sqrt(x))**2==x
            def quadradosperfeitosQ(w):
                return list(map(quadradoperfeitoQ,w))
            def algumperfeitoQ(w):
                return any(list(map(quadradoperfeitoQ,w)))
            def todosperfeitosQ(w):
                return all(list(map(quadradoperfeitoQ,w)))
            def quantosquadradosperfeitosQ(w):
                return len(list(filter(quadradoperfeitoQ,w)))
        
        if True: # listacrescQ(w)
            
            def listacrescQ(w):
                w1=w[:]
                list.sort(w1)
                return w==w1
            def diagonalcrescQ(m):
                return listacrescQ(diagonal(m))
            def seglistacrescQ(w):
                return listacresc(w[1])
            def linhascresc(m):
                return selecciona(m,listacrescQ)
            def colunascresc(m):
                return selecciona(transposta(m),listacrescQ)
            def indlinhascresc(m):
                return transposta(selecciona(grafo(m),seglistacrescQ))[0]
            def indcolunascresc(m):
                return transposta(selecciona(grafo(transposta(m)),seglistacrescQ))[0]
        
        if True: # prefixoQ(t,T), todosQ(w,p), algumQ(w,p)
            
            def prefixoQ(t,T):
                if len(t)==0:
                    return True
                elif len(T)==0:
                    return False
                elif t[0]!=T[0]:
                    return False
                else: 
                    return prefixoQ(t[1:],T[1:])
            def todosQ(w,p):
                if len(w)==0:
                    return True
                else:
                    return p(w[0]) and todosQ(w[1:],p)
            def algumQ(w,p):
                if len(w)==0:
                    return False
                else:
                    return p(w[0]) or algumQ(w[1:],p)
        
        if True: # palindromoQ(w), capicuaQ(n), ordQ(w), pertenceQ(x,w)
            
            def palindromoQ(w):
                if len(w)<2:
                    return True
                elif w[0]!=w[-1]:
                    return False
                else:
                    return palindromoQ(w[1:len(w)-1])
            def capicuaQ(n):
                return palindromoQ(digitos(n))
            def ordQ(w):
                i=1
                ok=True
                while ok and i<len(w):
                    if w[i]<w[i-1]:
                        ok=False
                    else:
                        i=i+1
                return ok
            def pertenceQ(x,w):
                def igualx(y):
                    return x==y
                return any(list(map(igualx,w)))
    
    if True: # Funções Matemáticas
        
        if True: # aplica(f,x)
            
            def aplica(f,x):
                return f(x)
        
        if True: # mymult(x)
            
            def mymult(x):
                def multx(y):
                    return x*y
                return multx
        
        if True: # max_div_comum(x,y) # from math import gcd # gcd(x,y)
            
            def mdc(x,y):
                if x==0 or y==0:
                    return x+y
                else:
                    return mdc(y,x%y)
        
        if True: # sumprod(x,y), somatres(x,y,z)
            
            def sumprod(x,y):
                return x+y,x*y
            def somatres(x,y,z):
                return x+y+z
            
            def f(x,*ys):
                for y in ys:
                    x=x+y
                return x
            def g(x,*ys,**zs):
                for y in ys:
                    x=x+y
                return zs["a"]+x
        
        if True: # f_sleep(x), fun(x), newfun(w,x)
            
            def f_sleep(x): # a função f_sleep devolve o argumento com um delay de 0.5 segundos
                sleep(0.5)
                return x
            def fun(x):
                x=x+x
                return x
            def newfun(w,x):
                w.append(x)
                return w
        
        if True: # somalista(w), media(w)
            
            def somalista_rec(w):
                if w==[]:
                    return 0
                else:
                    return w[0]+somalista_rec(w[1:])
            def somalista_func(w):
                return reduce(lambda x,y:x+y,w,0)
            
            def media(w):
                if w==[]:
                    print("erro, lista vazia")
                else:
                    return somalista_rec(w)/len(w)
            def media_imp(w):
                compr=len(w)
                if compr==0:
                    return False
                else:
                    global resultado
                    soma=0
                    while w!=[]:
                        soma=soma+w.pop()
                    resultado=soma/compr
                    return True
        
        if True: # max(w)
            
            def maxlista_rec(w):
                if w==[]:
                    print("erro")
                elif len(w)==1:
                    return w[0]
                elif w[0]>maxlista_rec(w[1:]):
                    return w[0]
                else:
                    return maxlista_rec(w[1:])
            def max2(w):
                if w==[]:
                    print("erro")
                elif len(w)==1:
                    return w[0]
                else:
                    x=max2(w[1:])
                    if x>w[0]:
                        return x
                    else:
                        return w[0]
            def max3(w):
                def maior(x,y):
                    if x>y:
                        return x
                    else:
                        return y
                
                if w==[]:
                    print("erro")
                elif len(w)==1:
                    return w[0]
                else:
                    return maior(w[0],max3(w[1:]))
            def max4(w):
                def maxparcial(u,m):
                    if u==[]:
                        return m
                    elif u[0]>m:
                        return maxparcial(u[1:],u[0])
                    else:
                        return maxparcial(u[1:],m)
                
                if w==[]:
                    print("erro")
                else:
                    return maxparcial(w[1:],w[0])
            def max_func(w):
                def fora(u):
                    return u[1:] if u[0]<u[1] else [u[0]]+u[2:]
                return nest(fora,len(w)-1,w)[0]
            def pos_max(lista):
                assert lista!=[]
                max=lista[-1]
                pmax=len(lista)-1
                for pos in range(pmax-1,-1,-1):
                    val=lista[pos]
                    if val>max:
                        max=val
                        pmax=pos
                return pmax
            def maximin(m):
                max=m[0][0]
                min=m[0][0]
                imin=0
                for i in range(len(m)):
                    for j in range(len(m[0])):
                        x=m[i][j]
                        if x>max:
                            max=x
                        elif x<min:
                            min=x
                            imin=i
                return max,imin
        
        if True: # percentagem(tot,val)
            
            def percentagem(tot,val):
                return int(100*val/tot)
            def escreve_percentagem(tot,val):
                global w
                w=int(100*val/tot)
                print(w,"%")
            def percentagens(val1,val2,val3):
                return [percentagem(val1,val3),percentagem(val2,val3),percentagem(val1,val2)]
            def estatistica(w):
                avals=[x for x in w if x!=0]
                return sum(w)/len(avals),percentagens(len(w),len(avals),len([x for x in avals if x>9.4]))
        
        if True: # quadrado(x)
            
            def quadrado(x):
                return x**2
            def quadrados(w):
                return list(map(lambda x:x**2,w))
        
        if True: # exponencial(x,n)
            
            def exp(b,e):
                return b**e
            def exponencial(x,n):
                assert x!=0
                if n==0:
                    return 1
                else:
                    return x*exponencial(x,n-1)
            def sqrmult(x,e):
                if e==0:
                    return 1
                elif (e%2)==0:
                    return sqrmult(x*x,e/2)
                else:
                    return x*sqrmult(x,e-1)
            def powers(w):
                return list(map(exp,w,range(len(w))))
        
        if True: # fatorial(n), flista(w)
            
            def factorial_rec(n):
                if n==0:
                    return 1
                else:
                    return n*factorial_rec(n-1)
            def factrec(n):
                def cond(estado):
                    return estado["n"]>1
                def passo(estado):
                    estado["r"]*=estado["n"]
                    estado["n"]+=-1
                    return estado
                return enquanto(cond,passo,{"n":n,"r":1})["r"]
            def factorial_iter(n):
                def factorialaux(i,r):
                    if i==0:
                        return r
                    else:
                        return factorialaux(i-1,r*i)
                return factorialaux(n,1)
            def factorial_iter_v2(n):
                def factorial_iter_aux(n,r):
                    if n==0:
                        return r
                    else:
                        return factorial_iter_aux(n-1,n*r)    
                return factorial_iter_aux(n,1)
            def factorial_imp_while(n):
                r=1
                while n!=0:
                    r=r*n
                    n=n-1
                return r
            def factorial_imp_while_v2(n):
                r=1
                while n!=0:
                    r*=n
                    n-=1
                return r
            def factorial_imp_while_v3(n):
                r=1
                while n>1:
                    r*=n
                    n+=-1
                return r
            def factorial_imp_for(n):
                r=1
                for i in range(n):
                    r*=(i+1)
                return r   
            def factorial_func(n):
                return reduce(lambda x,y:x*y,range(1,n+1),1)
            def Y(h):
                def W(f):
                    def r(x):
                        return h(f(f))(x)
                    return r
                return W(W)
            def FACT(f):
                def fact(n):
                    if n==0:
                        return 1
                    else:
                        return n*f(n-1)
                return fact
            
            def flista_rec(w):
                if w==[]:
                    return w
                else:
                    return [factorial(w[0])]+flista(w[1:])
            def flista_iter(w):
                
                def flistaaux(wfalta,wfeito):
                    if wfalta==[]:
                        return wfeito
                    else:
                        return flistaaux(wfalta[1:],wfeito+[factorial(wfalta[0])])
                    
                return flistaaux(w,[])
            def flista_imp(w):
                wfeito=[]
                while w!=[]:
                    wfeito=wfeito+[factorial(w[0])]
                    w=w[1:]
                return wfeito
            def flista_imp_v2(w):
                wfeito=[]
                while w!=[]:
                    wfeito+=[factorial(w[0])]
                    w=w[1:]
                return wfeito
            def flista_imp_2(w):
                wfeito=[]
                while w!=[]:
                    wfeito=[factorial(w[-1])]+wfeito
                    w=w[:-1]
                return wfeito
            def flista_imp_for(w):
                r=[]
                for x in w:
                    r+=[factorial(x)]
                return r
            def flista_func(w):
                return list(map(factorial_func,w))
            
            def factorial_robusto(x):
                if isinstance(x,int) and x>=0:
                    return factorial(x)
                else:
                    print("erro, factorial de argumento inválido")
            def factorial_robusto2(x):
                assert isinstance(x,int) and x>=0
                return factorial(x)
            def maufactorial(n):
                r=1
                while True:
                    if n!=0:
                        r=r*n
                        n=n-1
                    else:
                        return r
            def piorfactorial(n):
                r=1
                while 1:
                    if n!=0:
                        r=r*n
                        n=n-1
                    else:
                        break
                return r
    
    if True: # Funções Matemática aplicada
        
        if True: # pesqzero(s)
            
            def pesqzero(s):
                def tenta(n):
                    if s(n)==0:
                        return n
                    else:
                        return tenta(n+1)
                return tenta(0)
            def s1(n):
                return n-5
            def s2(n):
                return cos(n*pi/100)
            def s3(n):
                return 1
        
        if True: # fibonacci(n)
            
            def fibonacci_rec(n):
                if n<2:
                    return 1
                else:
                    return fibonacci_rec(n-1)+fibonacci_rec(n-2)
            def fibonacci_iter(n):
                
                def fibgo(a,b,k):
                    if k==0:
                        return a
                    else:
                        return fibgo(b,a+b,k-1)
                    
                return fibgo(1,1,n)
        
        if True: # pi(n)
            
            def pi_rec(n):
                def hits(k):
                    if k==0:
                        return 0
                    elif random()**2+random()**2<1:
                        return 1+hits(k-1)
                    else:
                        return hits(k-1)                
                return 4*hits(n)/n
            def pi_iter(n):
                def hits(c,i):
                    if i==0:
                        return c
                    elif random()**2+random()**2<1:
                        return hits(c+1,i-1)
                    else:
                        return hits(c,i-1)
                return 4*hits(0,n)/n
        
        if True: # bisseccao(f,a,b,e)
            
            def biss(f,a,b,e):
                assert a<b and f(a)*f(b)<0
                while b-a>e:
                    x=(a+b)/2
                    if f(a)*f(x)<0:
                        b=x
                    else:
                        a=x
                return (a+b)/2
        
        if True: # binsearch(x,w)
            
            def binsearch(x,w):
                found=False
                left=0
                right=len(w)-1
                while not(found) and left<=right:
                    mid=(left+right)//2
                    if x==w[mid]:
                        found=True
                    elif x<w[mid]:
                        right=mid-1
                    else:
                        left=mid+1
                if found:
                    return mid
                else:
                    return False
        
        if True: # fixedpoint(f,x), fechotrans(R)
            
            def fixedpoint(f,x):
                while x!=f(x):
                    x=f(x)
                return x
            def fixedpoint_(f,x):
                found=False
                while not(found):
                    y=f(x)
                    if y==x:
                        found=True
                    else:
                        x=y
                return x
            def fechotrans(R):
                def fecho(S):
                    return S+[[a[0],b[1]] for a in S for b in R if a[1]==b[0] and [a[0],b[1]] not in S]
                return fixedpoint(fecho,R)
        
        if True: # Gauss
            
            # Gauss # todas as definições agem por efeito colateral sobre a matriz # apenas `pivot` devolve um resultado, Booleano, indicando se foi encontrado
            def aumenta(m,a): # constrói a matriz aumentada
                for i in range(len(m)):
                    m[i].append(a[i])
            def pivot(m,i): # procura pivot diferente de zero # devolve Booleano mas troca linhas por efeito colateral sobre a matriz
                j=i
                while j<len(m) and m[j][i]==0:
                    j=j+1
                if j==len(m):
                    return False
                else:
                    m[i],m[j]=m[j],m[i]
                    return True
            def normaliza(m,i): # divide a linha pelo pivot
                x=m[i][i]
                for j in range(len(m[i])):
                    m[i][j]=m[i][j]/x
            def somamult(m,j,i): # soma à linha j um múltiplo adequado da linha i, anulando a entrada # age por efeito colateral sobre a matriz
                x=m[j][i]
                for k in range(i,len(m[j])):
                    m[j][k]=m[j][k]-x*m[i][k]
            def ultvec(m): # extrai vector resultado
                for i in range(len(m)):
                    m[i]=m[i][-1]
            def gauss(m,a):
                assert len(m)==len(a)
                aumenta(m,a)
                i=0
                ok=True
                while i<len(m) and ok:
                    ok=pivot(m,i)
                    if ok:
                        normaliza(m,i)
                        for j in range(i+1,len(m)):
                            somamult(m,j,i)
                    i=i+1
                i=i-1
                while i>=0 and ok:
                    for j in range(i-1,-1,-1):
                        somamult(m,j,i)
                    i=i-1
                if ok:
                    ultvec(m)
                    return m
                else:
                    print("erro")
        
        if True: # hondt(votos,lugares)
            
            def hondt(votos,lugares):
                res=[0 for i in range(len(votos))]
                coefs=votos[:]
                for disp in range(lugares,0,-1):
                    prox=posmax(coefs)
                    res[prox]=res[prox]+1
                    coefs[prox]=votos[prox]/(res[prox]+1)
                return res
        
        if True: # pos(a,b), sudoku(m)
            
            def pos(a,b):
                if a<9:
                    return (a,b)
                elif a<18:
                    return (b,a-9)
                else:
                    return (3*((a-18)//3)+b//3,3*((a-18)%3)+b%3)
            def sudokuQ(m):
                t=[]
                for n in range(10):
                    t=t+[0]
                ok=True
                a=0
                while ok and a<27:
                    b=0
                    while ok and b<9:
                        (i,j)=pos(a,b)
                        x=m[i][j]
                        if t[x-1]==a:
                            t[x-1]=a+1
                        else:
                            ok=False
                        b=b+1
                    a=a+1
                return ok

if True: # Exercícios
    
    if True: # soma_nat(n)
        
        def soma_nat(n):
            if n==1:
                return 1
            else:
                return n+soma_nat(n-1)
        
        def soma_nat_iter(n):
            def soma_nat_aux(x,s):
                if x==0:
                    return s
                else:
                    return soma_nat_aux(x-1,s+x)
            return soma_nat_aux(n,0)
        
        def soma_nat_for(n):
            r=0
            for i in range(n+1):
                r+=i
            return r
        
        def soma_nat_while(n):
            r=0
            while n!=0:
                r+=n
                n-=1
            return r
        
        def soma_nat_iter(n):
            return sum(range(1,n+1))
        
        def soma_nat_iter_v2(n):
            return sum([i for i in range(1,n+1)])
        
        def soma_nat_func(n):
            return reduce(lambda a,b: a+b, range(n+1))
        
        soma_nat(5),soma_nat(1000)
    
    if True: # temdivisorQ(n,i,j)
        
        def temdivisorQ(n,i,j):
            if i>j:
                return False
            elif n%i==0:
                return True
            else:
                return temdivisorQ(n,i+1,j)
        
        def temdivisorQ_iter(n):
            def tem_div_aux(n,i,r):
                if not (i>1):
                    return r
                elif n%i==0:
                    return tem_div_aux(n,i-1,True)
                else:
                    return tem_div_aux(n,i-1,r)
            return tem_div_aux(n,n-1,False)
        
        def temdivisorQ_for(n,i,j):
            r=False
            for k in range(i,j+1):
                if n%k==0:
                    r=True
            return r
        
        def temdivisorQ_while(n,i,j):
            r=False
            while not(r) and not(i>j):
                if n%i==0:
                    r=True
                i+=1
            return r
        
        def temdivisorQ_iter(n,i,j):
            return sum([n%k==0 for k in range(i,j+1)])>=1
        
        def tem_divisorQ_func(n,i,j):
            return any(list(map(lambda x: n%x==0,range(i,j+1))))
    
    if True: # div(m,n)
        
        def div(m,n): 
            if m<n:
                return 0
            else:
                return 1+div(m-n,n)
        
        def div_iter(m,n):
            def div_aux(m,n,x):
                if m<(x*n):
                    return x
                else:
                    return div_aux(m,n,x+1)
            return div_aux(m,n,0)
        
        def div_for(m,n):
            r=0
            for i in range(1,(m//n)+1):
                r+=1
            return r
        
        def div_while(m,n):
            r=0
            while m>n:
                m-=n
                r+=1
            return r
        
        def div_iter(m,n):
            return sum(range(1,(m//n)+1))
        
        def div_func(m,n):
            return reduce((lambda a,b: a+b),list(map((lambda x: m-(n*x)>0),range(1,(m//n)+1))))
        
        def div_func(m,n):
            return (lambda x,y: x//y)(m,n)
        
        def div_func(m,n):
            def div_int(m,n):
                return [1 for x in range(1,(m//n)+1)]
            return reduce(lambda a,b: a+b,div_int(m,n))
        
        div(7,2), div(3,4)
    
    if True: # resto_div_int(m,n)
        
        def resto_div_int(m,n):
            return m-(div(m,n)*n)
        
        def resto_div_inteira_func(m,n):
            return m-reduce((lambda a,b: a+b),list(map((lambda x: m-(n*x)>0),range(1,(m//n)+1))))
        
        def resto_div_int_func(m,n):
            return (lambda x,y: x-(x//y))(m,n)
        
        resto_div_int(7,2),resto_div_int(3,4)
    
    if True: # nr_digitos(n)
        
        def nr_digitos(n):
            if n<10:
                return 1
            else:
                return 1+nr_digitos(n//10)
        
        def digitos_iter(n):
            def nr_digitos_aux(x,s):
                if x<1:
                    return s
                else:
                    return nr_digitos_aux(x//10,s+1)
            return digitosaux(n,0)
        
        def nr_digitos_while(n):
            c=0
            while n!=0:
                n=n//10
                c+=1
            return c
        
        def nr_digitos_for(n):
            r=[]
            for i in range(len(str(n))):
                r+=[int(str(n)[i])]
            return len(r)
        
        def nr_digitos_iter(n):
            return len([int(x) for x in str(n)])
        
        def nr_digitos_func(n):
            return len(list(map(int,str(n))))
        
        nr_digitos(5629),nr_digitos(7)
    
    if True: # prim_alg(n)
        
        def prim_alg(n):
            if n<10:
                return n
            else:
                return prim_alg(int(n//10))
        
        def prim_alg_iter(n):
            def prim_alg_aux(x,s):
                if x<10:
                    return s
                else:
                    return prim_alg(n//10,n-n//10)
            return prim_alg_aux(n,n)
        
        def prim_alg_while(n):
            while n>=10:
                n=n//10
            return n
        
        def prim_alg_for(n):
            r=[]
            for i in range(len(str(n))):
                r+=[int(str(n)[i])]
            return r[0]
        
        def prim_alg_iter(n):
            return [int(x) for x in str(n)][0]
        
        def prim_alg_func(n):
            return list(map(int,str(n)))[0]
        
        prim_alg(5629),prim_alg(7)
    
    if True: # media_digitos(n)
        
        def media_digitos(n): 
            def soma_digitos(n):
                if n<10:
                    return n
                else: 
                    return n%10+soma_digitos(n//10)
            def nr_digitos(n):
                if n<10:
                    return 1
                else:
                    return 1+nr_digitos(n//10)
            return soma_digitos(n)/nr_digitos(n)
        
        def media_digitos_iter(n):
            def media_aux(x,c,s):
                if x<1:
                    return s/c
                else:
                    return media_aux(x//10,c+1,s+(x%10))
            return media_aux(n,0,0)
        
        def media_digitos_while(n):
            def soma_digitos_while(n):
                s=0
                while n!=0:
                    n=n//10
                    s+=n%10
                return s
            return soma_digitos_while(n)/nr_digitos_while(n)
        
        def media_digitos_for(n):
            def soma_digitos_for(n):
                s=0
                for i in range(len(str(n))):
                    s+=int(str(n)[i])
                return s
            return soma_digitos_for(n)/nr_digitos_for(n)
        
        def media_digitos_iter(n):
            return sum([int(str(n)[i]) for i in range(len(str(n)))])/len(str(n))
        
        def media_digitos_func(n):
            return reduce(lambda a,b: a+b,list(map(int,str(n))),0)/len(list(str(n)))
        
        def media_digitos_func(n):
            def lista_digitos(n):
                return [int(x) for x in str(n)]
            return reduce(lambda a,b:a+b,lista_digitos(n))/len(lista_digitos(n))
        
        media_digitos(1234),media_digitos(2684)
    
    if True: # comprimento(w)
        
        def comprimento(w):
            if w==[]:
                return 0
            else:
                return 1+comprimento(w[1:])
        
        def comprimento_iter(w):
            def compr_aux(w,x):
                if w==[]:
                    return x
                else:
                    return compr_aux(w[1:],x+1)
            return compr_aux(w,0)
        
        def comprimento_while(w):
            r=0
            while w!=[]:
                w=w[1:]
                r+=1
            return r
        
        def comprimento_for(w):
            r=0
            for i in range(len(w)):
                r+=1
            return r
        
        def comprimento_func(w):
            return reduce(lambda a,b:a+b,[1 for x in w],0)
        
        def comprimento_func(w):
            return reduce(lambda a,b:a+b, list(map((lambda a,b:b-a),range(len(w)-1),range(1,len(w)+10))),1)
        
        comprimento([2,3,5,2,2])
    
    if True: # num_perf(n)
        
        def num_perf(n):
            def soma_div_perf(n,x):
                if x==0:
                    return 0
                elif n%x==0:
                    return x+soma_div_perf(n,x-1)
                else:
                    return soma_div_perf(n,x-1)
            return n==soma_div_perf(n,n-1)
        
        
        def num_perf_iter(n):
            def soma_div_perf(n,x):
                if x==0:
                    return 0
                elif n%x==0:
                    return x+soma_div_perf(n,x-1)
                else:
                    return soma_div_perf(n,x-1)
            def num_perf_aux(n,s):
                return n==s
            return num_perf_aux(n,soma_div_perf(n,n-1))
        
        def num_perf_for(n):
            s=0
            for i in range(1,n):
                if n%i==0:
                    s+=i
            return n==s
        
        def num_perf_while(n):
            s=0
            i=1
            while n!=i:
                if n%i==0:
                    s+=i
                i+=1
            return n==s
        
        def num_perf_iter(n):
            return n==sum([i if n%i==0 else 0 for i in range(1,n)])
        
        def num_perf_func(n):
            return n==reduce(lambda a,b: a+b,[x for x in range(1,n) if x%n==0])
        
        def num_perf_func(n):
            def div_perfx(x):
                return x if n%x==0 else 0 
            return n==reduce(lambda a,b: a+div_perfx(b),range(1,n))
        
        num_perf(6), num_perf(5), num_perf(15), num_perf(496), num_perf(8128)
    
    if True: # num_it(n)
        
        def num_it(n):
            if n==1:
                return 0
            elif n%2==0:
                return 1+num_it(n/2)
            else:
                return 1+num_it((3*n)+1)
        
        def num_it_while(n):
            c=0
            while n!=1:
                if n%2==0:
                    n=(n/2)
                else:
                    n=((3*n)+1)
                c+=1
            return c
        
        num_it(5),num_it(21),num_it(11), num_it(27)
    
    if True: # fatorial(n)
        
        def factorial_rec(n):
            if n==0:
                return 1
            else:
                return n*factorial_rec(n-1)
        def factrec(n):
            def cond(estado):
                return estado["n"]>1
            def passo(estado):
                estado["r"]*=estado["n"]
                estado["n"]+=-1
                return estado
            return enquanto(cond,passo,{"n":n,"r":1})["r"]
        def factorial_iter(n):
            def factorialaux(i,r):
                if i==0:
                    return r
                else:
                    return factorialaux(i-1,r*i)
            return factorialaux(n,1)
        def factorial_iter_v2(n):
            def factorial_iter_aux(n,r):
                if n==0:
                    return r
                else:
                    return factorial_iter_aux(n-1,n*r)    
            return factorial_iter_aux(n,1)
        def factorial_imp_while(n):
            r=1
            while n!=0:
                r=r*n
                n=n-1
            return r
        def factorial_imp_while_v2(n):
            r=1
            while n!=0:
                r*=n
                n-=1
            return r
        def factorial_imp_while_v3(n):
            r=1
            while n>1:
                r*=n
                n+=-1
            return r
        def factorial_imp_for(n):
            r=1
            for i in range(n):
                r*=(i+1)
            return r   
        def factorial_func(n):
            return reduce(lambda x,y:x*y,range(1,n+1),1)
        def Y(h):
            def W(f):
                def r(x):
                    return h(f(f))(x)
                return r
            return W(W)
        def FACT(f):
            def fact(n):
                if n==0:
                    return 1
                else:
                    return n*f(n-1)
            return fact
        
        def flista_rec(w):
            if w==[]:
                return w
            else:
                return [factorial(w[0])]+flista(w[1:])
        def flista_iter(w):
            
            def flistaaux(wfalta,wfeito):
                if wfalta==[]:
                    return wfeito
                else:
                    return flistaaux(wfalta[1:],wfeito+[factorial(wfalta[0])])
                
            return flistaaux(w,[])
        def flista_imp(w):
            wfeito=[]
            while w!=[]:
                wfeito=wfeito+[factorial(w[0])]
                w=w[1:]
            return wfeito
        def flista_imp_v2(w):
            wfeito=[]
            while w!=[]:
                wfeito+=[factorial(w[0])]
                w=w[1:]
            return wfeito
        def flista_imp_2(w):
            wfeito=[]
            while w!=[]:
                wfeito=[factorial(w[-1])]+wfeito
                w=w[:-1]
            return wfeito
        def flista_imp_for(w):
            r=[]
            for x in w:
                r+=[factorial(x)]
            return r
        def flista_func(w):
            return list(map(factorial_func,w))
        
        def factorial_robusto(x):
            if isinstance(x,int) and x>=0:
                return factorial(x)
            else:
                print("erro, factorial de argumento inválido")
        def factorial_robusto2(x):
            assert isinstance(x,int) and x>=0
            return factorial(x)
        def maufactorial(n):
            r=1
            while True:
                if n!=0:
                    r=r*n
                    n=n-1
                else:
                    return r
        def piorfactorial(n):
            r=1
            while 1:
                if n!=0:
                    r=r*n
                    n=n-1
                else:
                    break
            return r
    
    if True: # comb(m,q)
        
        def comb(m,q):
            def factorial(n):
                if n==0:
                    return 1
                else:
                    return n*(factorial(n-1))
            if m<q:
                return 0
            else:
                return int(factorial(m-1)/(factorial(q-1)*factorial(m-1-(q-1)))) + comb(m-1,q)
        
        def comb_iter(m,q):
            return int(factorial(m)/(factorial(q)*factorial(m-q)))
        
        comb(3,2), comb(5,2)
    
    if True: # quadrados(n)
        
        def quadrados(n):
            if n==0:
                return []
            else:
                return quadrados(n-1)+[n**2]
        
        def quadrados_for(n):
            r=[]
            for i in range(1,n):
                r+=[i**2]
            return r
        
        def quadrados_while(n):
            r=[]
            i=1
            while len(r)<n:
                r+=[i**2]
                i+=1
            return r
        
        def quadrados_iter(n):
            return [i**2 for i in range(1,n+1)]
        
        def quadrados_func(n):
            return list(map(lambda x: x**2,range(1,n+1)))
        
        quadrados(6),quadrados(14)
    
    if True: # quadrados_inv(n)
        
        # from math import *
        def quadrados_inv(n):
            if n==0:
                return []
            elif ceil(sqrt(n))**2==n:
                return quadrados_inv(n-1)+[n]
            else:
                return quadrados_inv(n-1)
        
        def quadrados_inv_for(n):
            r=[]
            for i in range(n,0,-1):
                if ceil(sqrt(i))**2==i:
                    r+=[i]
            return r
        
        def quadrados_inv_while(n):
            r=[]
            i=n
            while i>0:
                if ceil(sqrt(i))**2==i:
                    r+=[i]
                i-=1
            return r
        
        def quadrados_inv_iter(n):
            return [i for i in range(n,0,-1) if ceil(sqrt(i))**2==i]
        
        def quadrados_inv_func(n):
            return list(filter(lambda x: ceil(sqrt(x))**2==x,range(n,0,-1)))
        
        quadrados_inv(6), quadrados_inv(15), quadrados_inv(0), quadrados_inv(4), quadrados_inv(9)
    
    if True: # triangulo(n)
        
        def triangulo(n):
            def lista_atex(x):
                return list(range(1,x+1))
            return list(map(lista_atex,range(1,n+1)))
        
        def triangulo_iter(n):
            return [[i for i in range(1,j+1)] for j in range(1,n+1)]
        
        def triangulo_func(n):
            return [list(range(1,j+1)) for j in range(1,n+1)]
        
        triangulo(4)
    
    if True: # prod_lista(w)
        
        def prod_lista(w):
            if w==[]:
                return 1
            else:
                return w[0]*prod_lista(w[1:])
        
        def prod_lista_for(w):
            r=1
            for i in range(len(w)):
                r*=w[i]
            return r
        
        def prod_lista_while(w):
            r=1
            i=0
            while i<len(w):
                r*=w[i]
                i+=1
            return r
        
        ## from numpy import prod
        def prod_lista_iter(w):
            return int(prod(w))
        
        def prod_lista_func(w):
            return reduce(lambda a,b: a*b,w,1)
        
        prod_lista([1,2,3,4,5,6]), prod_lista([20,19,18,17,16,15])
    
    if True: # prodmatriz(m)
        
        def prodmatriz(m):
            def prodlista(w):
                if w==[]:
                    return 1
                else:
                    return w[0]*prodlista(w[1:])
            if m==[[]]:
                return prodlista(m[0])
            else:
                return prodlista(m[0])*prodmatriz(m[1:])
        
        def prodMatriz(m):
            r=1
            for i in range(len(m)):
                for j in range(len(m[i])):
                    r*=m[i][j]
            return r
        
        prodMatriz([[1,2,3],[4,5,6]])
    
    if True: # contem_parQ(w)
        
        def contem_parQ(w):
            if len(w)==0:
                return False
            else:
                if w[0]%2==0:
                    return True
                else:
                    return contem_parQ(w[1:])
        
        def contem_parQ(w):
            if w==[]:
                return False
            else:
                return (w[0]%2==0) or contem_parQ(w[1:])
        
        def contem_parQ_for(w):
            q=False
            for x in w:
                if x%2==0:
                    q=(x%2==0)
            return q
        
        def contem_parQ_while(w):
            q=False
            i=0
            while i<len(w) and q!=True:
                q=(w[i]%2==0)
                i+=1
            return q
        
        def contem_parQ_iter(w):
            return sum([x%2==0 for x in w])>0
        
        def contem_parQ_func(w):
            return any(list(filter((lambda x: x%2==0),w)))
        def contem_parQ_func(w):
            return any(list(map((lambda x: x%2==0),w)))
        
        def contem_parQ_func(w):
            def valorx_par(x):
                return x%2==0
            return reduce(lambda x,y:x or y,list(map(valorx_par,w)),False)
        
        contem_parQ([2,3,1,2,3,4]),contem_parQ([1,3,5,7]),contem_parQ([])
    
    if True: # todos_imparesQ(w)
        
        def todos_imparesQ(w):
            if len(w)==0:
                return True
            else:
                if w[0]%2==0:
                    return False
                else: 
                    return todos_imparesQ(w[1:])
                
        def todos_imparesQ_for(w):
            r=True
            for x in w:
                if r==True:
                    r=not(x%2==0)
            return r
        
        def todos_imparesQ_while(w):
            r=True
            i=0
            while r==True and i<len(w):
                r=not(w[i]%2==0)
                i+=1
            return r
        
        def todos_imparesQ_iter(w):
            return sum([x%2!=0 for x in w])==len(w)
        
        def todos_imparesQ_func(w):
            return all(list(map((lambda x: x%2!=0),w)))
        
        def todos_imparesQ_func(w):
            def valorx_impar(x):
                return x%2!=0
            return reduce(lambda x,y:x and y,list(map(valorx_impar,w)),True)
        
        todos_imparesQ([1,3,5,7]),todos_imparesQ([]),todos_imparesQ([1,2,3,4,5])
    
    if True: # pertenceQ(w,n)
        
        def pertenceQ(w,n):
            if w==[]:
                return False
            else:
                return (w[0]==n) or pertenceQ(w[1:],n)
        
        def pertenceQ(w,n):
            if w==[]:
                return False
            else:
                return (n==(w[0])) or pertenceQ(w[1:],n)
            
        def pertenceQ_for(w,n):
            r=False
            for x in w:
                if not r:
                    r=(x==n)
            return r
        
        def pertenceQ_while(w,n):
            r=False
            i=0
            while not r and i<len(w):
                r=(w[i]==n)
                i+=1
            return r
        
        def pertenceQ_iter(w,n):
            return sum([x==n for x in w])>0
        
        def pertenceQ_func(w,n):
            return any(list(map((lambda x: x==n),w)))
        
        def pertenceQ_func(w,n):
            def valorx_igual_n(x):
                return x==n
            return reduce(lambda x,y:x or y,list(map(valorx_igual_n,w)),False)
        
        pertenceQ([1,2,3],1), pertenceQ([1,2,3],2), pertenceQ([1,2,3],3), pertenceQ([1,2,3],4)
    
    if True: # listaQ(w)
        
        def int_listaQ(w):
            if w==[]:
                return True
            else:
                return isinstance(w[0],int) and int_listaQ(w[1:])
        
        def int_listaQ(w):
            return all(list(map((lambda x: isinstance(x,int)),w)))
        
        def int_listaQ_func(w):
            def valorx_intQ(x):
                return isinstance(x,int)
            return reduce(lambda x,y:x and y,list(map(valorx_intQ,w)),True)
        
        int_listaQ([1,2,-3,4,9]), int_listaQ([1.1,3,-3])
        
        
        def nat_listaQ(w):
            if w==[]:
                return True
            else:
                return (w[0]>0 and isinstance(w[0],int)) and nat_listaQ(w[1:])
        
        def nat_listaQ_func(w):
            return all(list(map((lambda x: x>0 and isinstance(x,int)),w)))
        
        def nat_listaQ_func(w):
            def valorx_natQ(x):
                return isinstance(x,int) and x>0
            return reduce(lambda x,y:x and y,list(map(valorx_natQ,w)),True)
        
        nat_listaQ([1,2,3,-1]), nat_listaQ([1,2,3,4])
        
        
        def int_lista_listaQ_func(w):
            def nat_listaQ(z):
                def valorx_natQ(x):
                    return isinstance(x,int) and x>0
                return reduce(lambda x,y:x and y,list(map(valorx_natQ,z)),True) if isinstance(z,list) else False
            return reduce(lambda x,y:x and y,list(map(nat_listaQ,w)),True)
        
        int_lista_listaQ([[1,2,3],[4,5,6]]), int_lista_listaQ([[1,2,3],["ola",3]]), int_lista_listaQ([1,[1,2,3],[4,5,6]])
        
        def int_matrizQ(w):
            def int_listaQ_func(l):
                def valorx_intQ(x):
                    return isinstance(x,int)
                return (isinstance(l,list) and len(l)==len(w[0])) and reduce(lambda x,y:x and y,list(map(valorx_intQ,l)),True)
            return reduce(lambda x,y:x and y,list(map(int_listaQ_func,w)),True)
        
        int_matrizQ([[1,2],[4,5],[7,8]]), int_matrizQ([[1,2],[4],[7,8]]), int_matrizQ([[1,2],[4],7])
    
    if True: # negpos(w)
        
        def negpos(w):
            if w==[]:
                return 0
            else:
                return (1*(w[0]>0)+(-1)*(w[0]<0))+negpos(w[1:])
        
        def negpos_for(w):
            s=0
            for x in w:
                if x<0:
                    s-=1
                elif x>0:
                    s+=1
            return s
        
        def negpos_while(w):
            s=0
            i=0
            while i<len(w):
                if w[i]<0:
                    s+=1
                elif w[i]>0:
                    s-=1
                i+=1
            return s
        
        def negpos_func(w):
            return reduce((lambda a,b: a+b),list(map((lambda x: 1*(x>0) - 1*(x<0)),w)),0)
        
        def negpos_iter(w):
            return sum([(x<0)*-1 for x in w])+sum([(x>0)*1 for x in w])
        
        negpos([1,-2,-1,4,6,3]), negpos([-1,-2,-3,4]), negpos([1,-1])
    
    if True: # junta(s,t)
        
        def junta(s,t):
            if s==[]:
                return t
            elif t==[]:
                return s
            else:
                return s+junta([],t)
        
        def junta_iter(s,t):
            def junta_aux(s,t,r):
                if s!=[] and t!=[]:
                    return junta_aux(s[:len(w)-1],t[1:],[s[len(w)-1]]+r+[t[0]])
                elif s==[] and t!=[]:
                    return junta_aux(s,t[1:],r+[t[0]])
                elif s!=[] and t==[]:
                    return junta_aux(s[:len(w)-1],t,[s[len(w)-1]]+r)
                else:
                    return r
            return junta_aux(s,t,[])
        
        def junta_for(s,t):
            r=[]
            for i in range(max(len(s),len(t))+1):
                if i<len(s) and i<len(t):
                    r=[s[-i-1]]+r+[t[i]]
                elif i<len(s) and not(i<len(t)):
                    r=[s[-i-1]]+r
                elif not(i<len(s)) and i<len(t):
                    r+=[t[i]]
            return r
        
        def junta_while(s,t):
            r=[]
            i=len(s)-1
            j=0
            while not(i<0) or j<len(t):
                if i<0:
                    r+=[t[j]]
                elif j>=len(t):
                    r=[s[i]]+r
                else:
                    r=[s[i]]+r+[t[j]]
                i-=1
                j+=1
            return r
        
        def junta_iter(s,t):
            return s+t
        
        junta([1,2,3],[4,5,6]),junta([],[4,5,6]),junta([1,2,3],[])
    
    if True: # indices_impar(w)
        
        def indices_impar(w):
            if w==[]:
                return []
            else:
                if len(w)%2==1:
                    return indices_impar(w[:-1])
                else:
                    return indices_impar(w[:-1])+[w[-1]]
        
        def indices_impar(w):
            if w==[]:
                return []
            elif len(w)%2==0:
                return [w[0]]+indices_impar(w[:1])
            else:
                return indices_impar(w[:1])
        
        def indices_impar_for(w):
            r=[]
            for i in range(len(w)):
                if i%2!=0:
                    r+=[w[i]]
            return r
        
        def indices_impar_while(w):
            r=[]
            i=0
            while i<len(w):
                if i%2!=0:
                    r+=[w[i]]
                i+=1
            return r
        
        def indices_impar_iter(w):
            return [w[i] for i in range(len(w)) if i%2!=0]
        
        def indices_impar_func(w):
            return list(filter((lambda x: x!=0),list(map((lambda x,i: x*(i%2==0)),w,list(range(len(w)))))))
        
        def indices_pares_func(w):
            def valor_ind_par(x):
                return w[x]
            return list(map(valor_ind_par,range(0,len(w),2)))
        
        indices_impar([0,1,2,3,4,5,6]), indices_impar([0,1,2,3,4,5]), indices_impar([]), indices_impar([1,2])
    
    if True: # escolhe_pares(w)
        
        def escolhe_pares(w):
            if len(w)==0:
                return []
            else:
                if w[0]%2!=0:
                    return escolhe_pares(w[1:])
                else:
                    return [w[0]]+escolhe_pares(w[1:])
        
        def escolhe_pares(w):
            if w==[]:
                return []
            elif w[0]%2==0:
                return [w[0]]+escolhe_pares(w[1:])
            else:
                return escolhe_pares(w[1:])
            
        def escolhe_pares_for(w):
            r=[]
            for x in w:
                if x%2==0:
                    r+=[x] 
            return r
        
        def escolhe_pares_while(w):
            r=[]
            i=0
            while i<len(w):
                if w[i]%2==0:
                    r+=[w[i]] 
                i+=1
            return r
        
        def escolhe_pares_func(w):
            return list(filter((lambda x: x%2==0),w))
        
        def escolhe_pares_iter(w):
            return [x for x in w if x%2==0]
        
        def escolhe_pares_func(w):
            def valorx_par(x):
                return x if (x%2==0) else 0
            return [x for x in list(map(valorx_par,w)) if x!=0]
        
        escolhe_pares([1,2,3,4,4,2,6,8,9]),escolhe_pares([]),escolhe_pares([1,3,5,7,9])
    
    if True: # retira_negativos(w)
        
        def retira_negativos(w):
            if w==[]:
                return []
            elif not(w[0]<0):
                return [w[0]]+retira_negativos(w[1:])
            else:
                return retira_negativos(w[1:])
        
        def retira_negativos(w):
            if len(w)==0:
                return []
            else:
                if w[0]<0:
                    return retira_negativos(w[1:])
                else:
                    return [w[0]]+retira_negativos(w[1:])
        
        def retira_negativos_for(w):
            r=[]
            for x in w:
                if x>=0:
                    r+=[x]
            return r
        
        def retira_negativos_while(w):
            r=[]
            i=0
            while i<len(w):
                if w[i]>=0:
                    r+=[w[i]]
                i+=1
            return r
        
        def retira_negativos_iter(w):
            return [x for x in w if x>=0]
        
        def retira_negativos_func(w):
            return list(filter((lambda x: not(x<0)),w))
        
        def retira_negativos_func(w):
            def valx_pos(x):
                return x if x>=0 else 0
            return [x for x in list(map(valx_pos,w)) if x!=0]
        
        retira_negativos([1,-2,-3,7,0])
    
    if True: # menores_sublista(n,w)
        
        def menores_sublista(n,w):
            if w==[]:
                return []
            elif w[0]<n:
                return [w[0]]+menores_sublista(n,w[1:])
            else:
                return menores_sublista(n,w[1:])
        
        def menores_sublista(n,w):
            if len(w)==0:
                return []
            else:
                if w[0]>=n:
                    return menores_sublista(n,w[1:])
                else:
                    return [w[0]] + menores_sublista(n,w[1:])
        
        def menores_sublista_for(n,w):
            r=[]
            for x in w:
                if x<n:
                    r+=[x]
            return r
        
        def menores_sublista_while(n,w):
            r=[]
            i=0
            while i<len(w):
                if w[i]<n:
                    r+=[w[i]]
            return r
        
        def menores_sublista_iter(n,w):
            return [x for x in w if x<n]
        
        def menores_sublista_func(n,w):
            return list(filter((lambda x: x<n),w))
    
    if True: # supremo(w)
        
        # from math import inf
        def supremo(w):
            if w==[]:
                return -inf
            elif len(w)==1:
                return w[0]
            else:
                if w[0]>w[1]:
                    return supremo([w[0]]+w[2:])
                else:
                    return supremo(w[1:])
        
        def supremo(w):
            if w==[]:
                return -inf
            elif len(w)==1:
                return w[0]
            elif w[0]>w[1]:
                return supremo(w[0]+w[2:])
            else:
                return supremo(w[1:])
        
        def supremo_for(w):
            r=-inf
            for x in w:
                if x>r:
                    r=x
            return r
        
        def supremo_while(w):
            r=-inf
            i=0
            while i<len(w):
                if w[i]>r:
                    r=w[i]
                i+=1
            return r
        
        def supremo_iter(w):
            return max(w) if w!=[] else -inf
        
        def supremo_func(w):
            return list(filter((lambda x: x==(max(w))),w))[0] if w!=[] else -inf
        
        supremo([1,2,3,-2,5,-7]), supremo([1,3,-7]), supremo([]), supremo([3,2,1])
    
    if True: # posicoesMaximo(w)
        
        def posicoesMaximo(w):
            return lposicoes(w,supremo(w))
        
        def posicoes_maximo_iter(w):
            def pos_max_aux(w,s,i):
                if w==[]:
                    return []
                elif s==w[0]:
                    return [i]+pos_max_aux(w[1:],s,i+1)
                else:
                    return pos_max_aux(w[1:],s,i+1)
            if w==[]:
                return []
            else:
                return pos_max_aux(w,supremo(w),0)
        
        def posicoesMaximo_for(w):
            r=[]
            for i in range(len(w)):
                if w[i]==max(w):
                    r+=[i]
            return r
        
        def posicoesMaximo_while(w):
            r=[]
            i=0
            while i<len(w):
                if w[i]==max(w):
                    r+=[i]
                i+=1
            return r
        
        def posicoesMaximo_iter(w):
            return [i for i in range(len(w)) if w[i]==max(w)]
        
        def posicoes_maximo_func(w):
            return list(filter((lambda x: x!=0),list(map((lambda x,i: i*(x==max(w))),w,list(range(len(w)))))))
        
        posicoesMaximo([1,2,3,2,1,2,3]),posicoesMaximo([])
    
    if True: # conta(w,k)
        
        def conta(w,k):
            if w==[]:
                return 0
            elif w[0]==k:
                return 1+conta(w[1:],k)
            else:
                return conta(w[1:],k)
        
        def conta_for(w,k):
            r=0
            for x in w:
                if x==k:
                    r+=1
            return r
        
        def conta_while(w,k):
            r=0
            i=0
            while i<len(w):
                if w[i]==k:
                    r+=1
                i+=1
            return r
        
        def conta_iter(w,k):
            return sum([x==k for x in w])
        
        def conta_func(w,k):
            return len(list(filter((lambda x: x==k),w)))
        def conta_func2(w,k):
            return reduce((lambda a,b: a+b),list(map((lambda x: x==k),w)),0)
        def conta_func3(w,k):
            return reduce((lambda a,b: a+b),list(filter((lambda x: x!=0),list(map((lambda x: x==k),w)))),0)
        
        def conta_func(w,k):
            def valorx_igual_k(x):
                return x==k
            return reduce(lambda a,b: a+b,list(map(valor_igual_k,w)),0)
        
        conta([1,2,3,2,1,2],2),conta([1,2,3,2,1,2],4),conta([],5)
    
    if True: # lposicoes(w,k)
        
        def lposicoes(w,k):
            if w==[]:
                return []
            elif w[len(w)-1]==k:
                return lposicoes(w[:len(w)-1],k)+[len(w)-1]
            else:
                return lposicoes(w[:len(w)-1],k)
        
        def lposicoes(w,k):
            def lposaux(w,k,i):
                if w==[]:
                    return []
                elif w[0]==k:
                    return [i]+lposaux(w[1:],k,i+1)
                else:
                    return lposaux(w[1:],k,i+1)
            return lposaux(w,k,0)
        
        def lposicoes_for(w,k):
            r=[]
            for i in range(len(w)):
                if w[i]==k:
                    r+=[i]
            return r
        
        def lposicoes_while(w,k):
            r=[]
            i=0
            while i<len(w):
                if w[i]==k:
                    r+=[i]
                i+=1
            return r
        
        def lposicoes_iter(w,k):
            return [i for i in range(len(w)) if w[i]==k]
        
        def lposicoes_func(w,k):
            return list(filter((lambda x: x!=0),list(map((lambda x,i: i*(x==k)),w,list(range(len(w)))))))
        
        lposicoes([1,2,3,4,2,2],2),lposicoes([1,2,3,4,2,2],7),lposicoes([],3)
    
    if True: # pos_max(w)
        
        def pos_max(w):
            if w==[]:
                return -1
            else:
                return lposicoes(w,supremo(w))[0]
        
        def pos_max_iter(w):
            def pmaxaux(w,s,i):
                if w[0]==s:
                    return i
                else:
                    return pmaxaux(w[1:],s,i+1)
            
            if w==[]:
                return -1
            else:
                return pmaxaux(w,supremo(w),0)
        
        def pos_max_for(w):
            r=-1
            for i in range(len(w)):
                if r==-1 and w[i]==max(w):
                    r=i
            return r
        
        def pos_max_while(w):
            r=-1
            i=0
            while i<len(w):
                if r==-1 and w[i]==max(w):
                    r=i
                i+=1
            return r
        
        def pos_max_iter(w):
            return -1 if w==[] else [i for i in range(len(w)) if w[i]==max(w)][0]
        
        pos_max([1,2,3,3,2,1,3])
    
    if True: # car_par(w)
        
        def car_par(w):
            if w==[]:
                return []
            else:
                return [w[0]%2==0]+car_par(w[1:])
        
        def car_par_for(w):
            r=[]
            for x in w:
                r+=[x%2==0]
            return r
        
        def car_par_while(w):
            r=[]
            i=0
            while i<len(w):
                r+=[w[i]%2==0]
                i+=1
            return r
        
        def car_par_iter(w):
            return [w[i]%2==0 for i in range(len(w))]
        
        car_par([2,3,4,3,2,2]),car_par([3,3,3]),car_par([])
    
    if True: # apaga1(w,k)
        
        def apaga1(w,k):
            if w==[]:
                return []
            else:
                return w[1:] if w[0]==k else [w[0]]+apaga1(w[1:],k)
        
        def apaga1_for(w,k):
            r=[]
            q=False
            for i in range(len(w)):
                if not q and w[i]==k:
                    q=True
                    r=w[:i]+w[i+1:]
            return r
        
        def apaga1_while(w,k):
            r=[]
            q=False
            i=0
            while i<len(w):
                if not q and w[i]==k:
                    q=True
                    r=w[:i]+w[i+1:]
                i+=1
            return r
        
        def apaga1_iter(w,k):
            return [w[i] for i in range(len(w)) if i!=lposicoes(w,k)[0]]
        
        apaga1([1,2,3,4,3,2,1],3),apaga1([1,2,3,4,3,2,1],1),apaga1([1,2,3,4,3,2,1],5),apaga1([],3)
    
    if True: # apaga(w,k)
        
        def apaga(w,k):
            if w==[]:
                return []
            else:
                return apaga(w[1:],k) if w[0]==k else [w[0]]+apaga(w[1:],k)
        
        def apaga_for(w,k):
            r=[]
            for i in range(len(w)):
                if w[i]!=k:
                    r+=[w[i]]
            return r
        
        def apaga_while(w,k):
            r=[]
            while i<len(w):
                if w[i]!=k:
                    r+=[w[i]]
                i+=1
            return r
        
        def apaga_iter(w,k):
            return [x for x in w if x!=k]
        
        apaga([1,2,3,4,3,2,1],3), apaga([1,2,3,4,3,2,1],5), apaga([],3)
    
    if True: # seleccao(w,p)
        
        def primoQ(n):
            def temdivisorQ(n,i,j):
                if i>j:
                    return False
                elif n%i==0:
                    return True
                else:
                    return temdivisorQ(n,i+1,j)
            return n>1 and not(temdivisorQ(n,2,n-1))
        
        def existeQ(w1,w2):
            def pertenceQ(w,n):
                if w==[]:
                    return False
                else: 
                    return (w[0]==n) or pertenceQ(w[1:],n)
            if w1==[]:
                return False
            else:
                return pertenceQ(w2,w1[0]) or existeQ(w1[1:],w2)
        
        def seleccao(w,p):
            if w==[]:
                return []
            else:
                return [w[0]]+seleccao(w[1:],p) if p(w[0]) else seleccao(w[1:],p)
        
        def seleccao_for(w,p):
            r=[]
            for x in w:
                if p(x):
                    r+=[x]
            return r
        
        def seleccao_while(w,p):
            r=[]
            i=0
            while i<len(w):
                if p(w[i]):
                    r+=[w[i]]
                i+=1
            return r
        
        def seleccao_iter(w,p):
            return [] if w==[] else [x for x in w if p(x)]
        
        def seleccao_func(w,p):
            return list(filter(p,w))
        
        seleccao([],primoQ),seleccao([1,2,3,4,5,6,7,8,9,10],primoQ)
    
    if True: # mapeia(f,w)
        
        def suc(x):
            return x+1
        
        def mapeia(f,w):
            if w==[]:
                return []
            else:
                return [f(w[0])]+mapeia(f,w[1:])
        
        def mapeia_for(f,w):
            r=[]
            for x in w:
                r+=[f(x)]
            return r
        
        def mapeia_while(f,w):
            r=[]
            i=0
            while i<len(w):
                r+=[f(w[i])]
                i+=1
            return r
        
        def mapeia_iter(f,w):
            return [f(x) for x in w]
        
        def mapeia_func(f,w):
            return list(map(f,w))
        
        mapeia(suc,[0,1,2,3,4,5]), mapeia(suc,[])
    
    if True: # sufixoQ(s,w)
        
        def sufixoQ(s,w):
            if s==[]:
                return True
            elif w==[]:
                return False
            else:
                return s[-1]==w[-1] and sufixoQ(s[:len(s)-1],w[:len(w)-1])
        
        def sufixoQ_for(s,w):
            q = not(len(w)<len(s)) and (s==[] or w!=[])
            for i in range(1,len(s)+1):
                 if q:
                    q=(s[-i]!=w[-i])
            return q
        
        def sufixoQ_while(s,w):
            q = not(len(w)<len(s)) and (s==[] or w!=[])
            i=1
            while q and i<len(s)+1:
                q=(s[-i]!=w[-i])
                i+=1
            return q
        
        def sufixoQ_iter(s,w):
            return not(len(w)<len(s)) and ((s==[] or w!=[]) and s==w[len(w)-len(s):len(w)])
        
        sufixoQ([3,4],[1,2,3,4]),sufixoQ([3,4],[1,2,3,4,5]),sufixoQ([1,2,3],[1,2]),sufixoQ([],[1]),sufixoQ([1,2,3],[1,2,3])
    
    if True: # temprimoQ(w)
        
        def primoQ(n):
            def temdivisorQ(n,i,j):
                if i>j:
                    return False
                elif n%i==0:
                    return True
                else:
                    return temdivisorQ(n,i+1,j)
            return n>1 and not(temdivisorQ(n,2,n-1))
        
        def temPrimoQ(w):
            def temPrimol(l):
                if l==[]:
                    return False
                else:
                    if primoQ(l[0]):
                        return True
                    else:
                        return temPrimol(l[1:])
            if len(w[0])==0:
                return False
            else:
                if temPrimol(w[0]):
                    return True
                else:
                    return temPrimoQ(w[1:])
        
        def temPrimoQ_for(w):
            q=False
            for i in range(len(w)):
                for j in range(len(w[i])):
                    if not(q) and primoQ(w[i][j]):
                        q=True
            return q
        
        def temPrimoQ_while(w):
            q=False
            i=0
            j=0
            while i<len(w):
                while j<len(w[i]):
                    if not(q) and primoQ(w[i][j]):
                        q=True
                    j+=1
                i+=1
            return q
        
        def temPrimoQ_iter(w):
            return sum([primoQ(x) for z in w for x in z])>0
        
        temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]),temPrimoQ([[4,4,4,4],[4,4,4],[],[4]])
    
    if True: # invertelista(w)
        
        def invertelista(w):
            if w==[]:
                return []
            else:
                return invertelista(w[1:])+[w[0]]
        
        def invertelista_for(w):
            r=[]
            for i in range(len(w)-1,-1,-1):
                r+=[w[i]]
            return r
        
        def invertelista_while(w):
            r=[]
            i=len(w)-1
            while i>=0:
                r+=[w[i]]
                i-=1
            return r
        
        def invertelista_iter(w):
            return [w[i] for i in range(len(w)-1,-1,-1)]
        
        def invertelista_func(w):
            def valor_posx(x):
                return w[x]
            return list(map(valor_posx,range(len(w)-1,-1,-1)))
        
        invertelista([1,2,3,4,5]), invertelista([])
    
    if True: # lista_igualQ(w1,w2)
        
        def lista_igualQ(w1,w2):
            if not len(w1)==len(w2):
                return False
            elif w1==[] and w2==[]:
                return True
            else:
                return True and lista_igualQ(w1[1:],w2[1:]) if (w1[0]==w2[0]) else lista_igualQ([],w2)
        
        def lista_igualQ(w1,w2):
            if not len(w1)==len(w2):
                return False
            elif (w1 and w2)==[]:
                return True
            elif w1[0]==w2[0]:
                return lista_igualQ(w1[1:],w2[1:])
            else:
                return lista_igualQ([],w2)
        
        
        def lista_igualQ_for(s,t):
            r=(len(s)==len(t))
            for i in range(len(s)):
                if r:
                    r=(s[i]==t[i])
            return r
        
        def lista_igualQ_while(s,t):
            r=(len(s)==len(t))
            i=0
            while i<len(s):
                if r:
                    r=(s[i]==t[i])
                i+=1
            return r
        
        def lista_igualQ_iter(s,t):
            return len(s)==len(t) and sum([s[i]==t[i] for i in range(len(s))])==len(s)
        
        def lista_igualQ_iter_v2(s,t):
            return len(s)==len(t) and s==t
        
        lista_igualQ([1,2,3],[1,2,3]), lista_igualQ([1,2,3],[1,2,2]), lista_igualQ([],[]), lista_igualQ([1,2,3],[1,2]), lista_igualQ((1,2,3),[1,2])
    
    if True: # sup_listas1(w)
    
        # from math import inf
        def supremo(w):
            if w==[]:
                return -inf
            elif len(w)==1:
                return w[0]
            else:
                return supremo([w[0]]+w[2:]) if w[0]>w[1] else supremo(w[1:])
        
        def sup_listas1(w):
            if len(w)<=1:
                return supremo(w[0])
            else:
                if supremo(w[0][0:])>supremo(w[1][0:]):
                    return sup_listas1([w[0]]+w[2:])
                else:
                    return sup_listas1(w[1:])
        
        def sup_listas1_for(w):
            r=-inf
            for i in range(len(w)):
                for j in range(len(w[i])):
                    if r<w[i][j]:
                        r=w[i][j]
            return r
        
        def sup_listas1_for_v2(w):
            r=[]
            for i in range(len(w)):
                if w[i]==[]:
                    r+=[-inf]
                else:
                    r+=[max(w[i])]
            return max(r)
        
        def sup_listas1_while(w):
            r=-inf
            i=0
            while i<len(w):
                j=0
                while j<len(w[i]):
                    if r<w[i][j]:
                        r=w[i][j]
                    j+=1
                i+=1
            return r
        
        def sup_listas1_while_v2(w):
            r=[]
            i=0
            while i<len(w):
                if w[i]==[]:
                    r+=[-inf]
                else:
                    r+=[max(w[i])]
                i+=1
            return max(r)
        
        def sup_listas1_iter(w):
            return max([-inf if x==[] else max(x) for x in w])
        
        sup_listas1([[1,2,3],[2,3,4],[2]]),sup_listas1([[7,3,2],[],[1,2,3]]), sup_listas1([]),sup_listas1([[],[],[]]),sup_listas1([[5,2,5],[3,8,1],[0]])
    
    if True: # sup_listas2(w)
        
        def sup_listas2(w):
            if len(w)==0:
                return []
            else:
                return [supremo(w[0][0:])] + sup_listas2(w[1:])
        
        def sup_listas2_for(w):
            r=[]
            for i in range(len(w)):
                s=-inf
                for j in range(len(w[i])):
                    if s<w[i][j]:
                        s=w[i][j]
                r+=[s]
            return r
        
        def sup_listas2_for_v2(w):
            r=[]
            for i in range(len(w)):
                if w[i]==[]:
                    r+=[[-inf]]
                else:
                    r+=[[max(w[i])]]
            return r
        
        def sup_listas2_while(w):
            r=[]
            i=0
            while i<len(w):
                s=-inf
                j=0
                while j<len(w[i]):
                    if s<w[i][j]:
                        s=w[i][j]
                    j+=1
                r+=[s]
                i+=1
            return r
        
        def sup_listas2_while_v2(w):
            r=[]
            i=0
            while i<len(w):
                if w[i]==[]:
                    r+=[[-inf]]
                else:
                    r+=[[max(w[i])]]
                i+=1
            return r
        
        def sup_listas2_iter(w):
            return [-inf if x==[] else max(x) for x in w]
        
        sup_listas2([[1,2,3],[4,3,2],[],[7,7,7,7]]), sup_listas2([]), sup_listas2([[],[],[]]), sup_listas2([[5,2,5],[3,8,1],[0]])
    
    if True: # permutacao(s,t)
        
        def permutacao(s,t):
            def tem_valQ(n,t):
                if t==[]:
                    return False
                else:
                    return (n==t[0]) or tem_valQ(n,t[1:])
            def apaga1(w,k):
                if w==[]:
                    return []
                else:
                    return w[1:] if w[0]==k else [w[0]]+apaga1(w[1:],k)
            if not(len(s)==len(t)):
                return False
            elif s==[] and t==[]:
                return True
            else:
                return permutacao(s[1:],apaga1(t,s[0])) if tem_valQ(s[0],t) else permutacao([],t)
        
        def permutacao_while(s,t):
            r=(len(s)==len(t))
            i=0
            while r and i<len(s):
                j=0
                q=True
                while q and j<len(t):
                    q=not(s[i]==t[j])
                    r=q
                    j+=1
                i+=1
            return r
        
        def permutacoes(w):
            r=[[]]
            for x in w:
                rs=[]
                for u in r:
                    for i in range(len(u)+1):
                        novo=u[:]
                        novo.insert(i,x)
                        rs+=[novo]
                r=rs
            return r
        
        def permutacao_q(s,t):
            r=(len(s)==len(t))
            i=0
            while r and i<len(s):
                j=0
                q=False
                while not(q) and j<len(t):
                    q=(s[i]==t[j])
                    if q:
                        s=s[:i]+s[i+1:]
                        t=t[:j]+t[j+1:]
                    j+=1
                i+=1
                r=q
            return r
        
        def permutacao_func(s,t):
            list.sort(s);list.sort(t)
            return len(s)==len(t) and s==t
        
        s=[i for i in range(1,10)]; t=[i for i in range(9,0,-1)]
        permutacao([1,2,3],[1,2,3]),permutacao([1,2,3],[2,3,1]),permutacao([1,1,1,2,3],[1,2,3])
    
    if True: # intercala(s,t)
        
        def intercala(s,t):
            if s==[]:
                return t
            elif t==[]:
                return s
            else:
                return [s[0]]+[t[0]]+intercala(s[1:],t[1:])
        
        def intercala_for(s,t):
            r=[]
            for i in range(max(len(s),len(t))):
                if i>=len(s) and i<len(t):
                    r+=[t[i]]
                elif i>=len(t) and i<len(s):
                    r+=[s[i]]
                elif i<len(s) and i<len(t):
                    r+=[s[i],t[i]]
            return r
        
        def intercala_while(s,t):
            r=[]
            i=0
            j=0
            while len(r)<(len(s)+len(t)):
                if i>=len(s) and j<len(t):
                    r+=[t[j]]
                elif j>=len(t) and i<len(s):
                    r+=[s[i]]
                elif i<len(s) and j<len(t):
                    r+=[s[i],t[j]]
                i+=1
                j+=1
            return r
        
        def intercala_iter(s,t):
            return [s[i//2] if ((i//2<len(s) and i//2<len(t)) and i%2==0) else t[i//2] if ((i//2<len(s) and i//2<len(t)) and i%2!=0) else s[i-len(t)] if i//2>=len(t) else t[i-len(s)] if i//2>=len(s) for i in range(len(s)+len(t))]
        
        def intercala_func(s,t):
            def inter(x,y):
                return x+y
            return list(map(inter,s,t))
        
        intercala([1,2,3],[4,5,6]),intercala([1,3,5,7,9],[2,4])
    
    if True: # indPrimos(w)
        
        def indPrimos(w):
            def lindices(l):
                if l==[]:
                    return []
                else:
                    return lindices(l[:-2])+[len(l)-1] if PrimoQ(l[-1]) else lindices(l[:-2])
            if w==[[]]:
                return []
            else:
                return [lindices(w[0])]+indPrimos(w[1:])
        
        def indPrimos_for(w):
            r=[]
            for z in w:
                s=[]
                for x in z:
                    if PrimoQ(x):
                        s+=[x]
                r+=[s]
            return r
        
        def indPrimos_while(w):
            r=[]
            i=0
            while i<len(w):
                s=[]
                j=0
                while j<len(w[i]):
                    if PrimoQ(w[i][j]):
                        s+=[w[i][j]]
                    j+=1
                r+=[s]
                i+=1
            return r
        
        def indPrimos_iter(w):
            return [[i for i in range(len(x)) if primoQ(x[i])] for x in w]
        
        indPrimos_iter([[1,2,3,4],[1,2,3,4,5],[2,3,5,7,11],[4,6,8,9],[11,12,13,14,15],[],[22,33,44]])
    
    if True: # mult3e5(w)
        
        def mult3e5(w):
            def m3(w):
                if w==[]:
                    return []
                else:
                    return [w[0]]+m3(w[1:]) if w[0]%3==0 else m3(w[1:])
            def m5(w):
                if w==[]:
                    return []
                else:
                    return [w[0]]+m5(w[1:]) if w[0]%5==0 else m5(w[1:])
            return [m5(w),m3(w)]
        
        def mult3e5_for(w):
            r=[[],[]]
            for x in w:
                if x%3==0:
                    r[0]+=[x]
                elif x%5==0:
                    r[1]+=[x]
            return r
        
        def mult3e5_while(w):
            r=[[],[]]
            i=0
            while i<len(w):
                if w[i]%3==0:
                    r[0]+=[w[i]]
                elif w[i]%5==0:
                    r[1]+=[w[i]]
            return r
        
        def mult3e5_iter(w):
            return [[x for x in w if x%5==0],[x for x in w if x%3==0]]
        
        mult3e5([1,2,3,4,5,9,15]),mult3e5([1,2,3,4,6,7,8,9])
    
    if True: # max_soma_linha(w)
        
        def max_soma_linha(w):
            def lista_soma_linhas(w):
                def soma_linha(l):
                    if l==[]:
                        return 0
                    else:
                        return l[0]+soma_linha(l[1:])
                if w==[]:
                    return []
                else:
                    return [soma_linha(w[0])]+lista_soma_linhas(w[1:])
            if not(w==[[]]) and lista_soma_linha(w)[0]<supremo(lista_soma_linha(w)):
                return 1+lista_soma_linha(w)[1:]
            else:
                return 0
        
        def max_soma_linha_for(w):
            r=[]
            for i in range(len(w)):
                s=0
                for j in range(len(w[i])):
                    s+=w[i][j]
                r+=[s]
            sol=0
            q=False
            for i in range(len(r)):
                if not(q) and r[i]==max(r):
                    sol=i
                    q=True
            return sol
        
        def max_soma_linha_while(w):
            r=[]
            i=0
            while i<len(w):
                s=0
                j=0
                while j<len(w[i]):
                    s+=w[i][j]
                    j+=1
                r+=[s]
                i+=1
            q=False
            sol=0
            k=0
            while not(q) and k<len(r):
                if not(q) and r[k]==max(r):
                    sol=k
                    q=True
                k+=1
            return sol
        
        def max_soma_linha_iter(w):
            return [i for i in range(len(w)) if sum(w[i])==max([sum(w[i]) for i in range(len(w))])][0]
        
        max_soma_linha([[1,2,3],[11,11,11],[6,7,8],[10,11,12]])
    
    if True: # potencia(k)
        
        def potencia(k):
            def prim_alg(n):
                if n<10:
                    return n
                else:
                    return prim_alg(int(n//10))
            def prim_alg_igual_k(n,k):
                if prim_alg(2**n)==k:
                    return n
                else:
                    return prim_alg_igual_k(n+1,k)
            if k==0:
                print("Erro! Não é possível obter resultado nulo para potência")
            else:
                return prim_alg_igual_k(0,k)
        
        def potencia_while(k):
            n=0
            while prim_alg(2**n)!=k:
                n+=1
            return n
        
        potencia(2), potencia(3)
    
    if True: # repete(w)
        
        def repete(w):
            def repete_aux(v,n):
                if n==0:
                    return []
                else:
                    return [v]+repete_aux(v,n-1)
            if w==[]:
                return []
            else:
                return repete(w[:len(w)-1])+repete_aux(w[len(w)-1],len(w))
        
        def repete_for(w):
            r=[]
            for i in range(len(w)):
                for k in range(i+1):
                    r+=[w[i]]
            return r
        
        def repete_while(w):
            r=[]
            i=0
            while i<len(w):
                k=0
                while k<(i+1):
                    r+=[w[i]]
                    k+=1
                i+=1
            return r
        
        def repete_iter(w):
            return [w[i] for k in range(i+1) for i in range(len(w))]
        
        repete([1,2,3]), repete([3,4,5,6]), repete([1,4,6,7]), repete([i for i in range(1,6)]), repete([[1,2,3],[3,4,5,6],[1,4,6,7]])
    
    if True: # medcolpares(w)
        
        def medcolpares(w):
            r=0
            l=0
            for i in range(len(w)):
                s=0
                n=0
                for j in range(0,len(w[i]),2):
                    s+=w[i][j]
                    n+=1
                r+=(s/n)
                l+=1
            return r/l
        
        def medcolpares_for(w):
            r=0
            n=0
            for i in range(len(w)):
                for j in range(len(w[i]),2):
                    r+=w[i][j]
                    n+=1
            return r/n
        
        def medcolpares_while(w):
            r=0
            n=0
            i=0
            while i<len(w):
                j=0
                while j<len(w[i]):
                    r+=w[i][j]
                    n+=1
                    j+=2
                i+=1
            return r/n
        
        # from numpy import average
        def medcolpares_iter(w):
            return average([w[i][j] for i in range(len(w)) for j in range(0,len(w),2)])
        
        medcolpares([[1,2,3,4,5],[5,4,3,2,1],[0,2,4,6,5]]), medcolpares([[1,2,3,4],[4,3,2,1]]), medcolpares_iter([[i+j for i in range(5)] for j in range(5)])
    
    if True: # transposta(w)
        
        def transposta(m):
            def coluna_para_linha(m):
                if m==[[]]:
                    return []
                else:
                    return [m[0][0]]+coluna_para_linha(m[1:])
            def retira_coluna(m):
                if m==[]:
                    return []
                else:
                    return [m[0][1:]]+retira_coluna(m[1:])
            if m==[[]]:
                return []
            else:
                return [coluna_para_linha(m)]+transposta(retira_coluna(m))
        
        def transposta_for(w):
            r=[]
            for j in range(len(w[0])):
                l=[]
                for i in range(len(w)):
                    l+=[w[i][j]]
                r+=[l]
            return r
        
        def transposta_while(w):
            r=[]
            j=0
            while j<len(w[0]):
                l=[]
                i=0
                while i<len(w):
                    l+=[w[i][j]]
                    i+=1
                r+=[l]
                j+=1
            return r
        
        def transposta_iter(w):
            return [[w[i][j] for i in range(len(w))] for j in range(len(w[0]))]
        
        transposta([[1,2,3],[4,5,6]])
    
    if True: # produtoMatrizes(a,b)
        
        def produtoMatrizes(a,b):
            if len(a)!=len(b[0]):
                print("Erro: Matrizes não permitidas.")
            else:
                r=[]
                for i in range(len(a)):
                    l=[]
                    for c in range(len(b[0])):
                        s=0
                        for x in range(len(a[i])):
                            s+=a[i][x]*b[x][c]
                        l+=[s]
                    r+=[l]
                return r
        
        def produtoMatrizes(a,b):
            if len(a)!=len(b[0]):
                print("Erro: Matrizes não permitidas.")
            else:
                r=[]
                for i in range(len(a)):
                    l=[]
                    for j in range(len(b[0])):
                        s=0
                        for x in range(len(a[i])):
                            s+=a[i][x]*b[x][j]
                        l+=[s]
                    r+=[l]
                return r
        
        produtoMatrizes([[1,2],[3,4],[5,6]],[[1,2,3],[4,5,6]])

# from IPython.display import HTML ## video exportado do sistema Mathematica em formato swf e convertido depois para mp4
# HTML("""
# <video width="400" height="400" controls>
#  <source src="insertionsort.mp4" type="video/mp4">
# </video>
# """)
# HTML("""
# <video width="400" height="400" controls>
#   <source src="selectionsort.mp4" type="video/mp4">
# </video>
# """)
# HTML("""
# <video width="400" height="400" controls>
#   <source src="quicksort.mp4" type="video/mp4">
# </video>
# """)
# HTML("""
# <video width="400" height="400" controls>
#   <source src="mergesort.mp4" type="video/mp4">
# </video>
# """)
