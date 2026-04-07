# https://www.python.org/
# %pwd, %ls, cls, %reset, dir()
# %pylab inline, ?pylab
import keyword # print(keyword.kwlist)
import sys # sys.path.append('./modules'); print(sys.path) # sys.setrecursionlimit(5000); sys.setrecursionlimit(2100)
from time import sleep

import turtle
import pandas as pd
import numpy as np
from sympy import cos, pi # from sympy import *
from mpmath import mp
from math import factorial, inf, ceil # from math import factorial as fact
from random import random, shuffle, randrange, randint # from random import *
from functools import reduce, partial # ?reduce, ?map, ?filter
from itertools import * # ?count # ?combinations

from sympy.plotting import * # ?plot ?plot3d
from matplotlib.pyplot import plot as dataplot # ?dataplot
import matplotlib.pyplot as plt # ?plt
from IPython.core.display import display, HTML
from IPython.display import Image, HTML

if True: # NB 1 - Programação Básica # Matemática Básica
    
    if True: # Cálculo Numérico: Real e Complexo
        # Cálculo Numérico: Recorde as operações aritméticas básicas do Python: + (adição), - (subtracção), * (multiplicação), / (divisão), ** (exponenciação), // (divisão inteira), % (resto da divisão inteira).
        1+1-3, (2*3)%5, 7/3, 7//3, 10**3, 1/3+1/2, 
        pi, pi/2, cos(2*pi), sin(pi/6), sin(2*pi/3)-sqrt(3)/2 # ?pi
        log(e**5), log2(1024)-log10(1000), fact(6)
        abs(-1)*max(1,2,3)+min(1,2,3)+round(2.6), sum((3,2,1)), pow(3,2)
        # Cálculo Complexo: A unidade imaginária em Python é representada pelo símbolo j, disponibilizado pela extensão pylab.
        complex(1,1), real(complex(1,-1)), imag(complex(1,-1)),(0+1j)**2+1j 
        I**2, (1+2*I)*(1-I), im(1+2*I+3), re(1+2*I+3), conjugate(a+b*I) # ?I
        conjugate(1+1j), abs(1+1j)
        
        mp.pi, 2*mp.pi; mp.dps=100; mp.dps=500; mp.dps=200; mp.findroot(lambda x:x*cos(x)-log(x),1); print(mp.fraction(3,7)); print(mp.pi)
        x=8; int.bit_length(x), x.bit_length(), int.bit_length(7), (7).bit_length() # ?bit_length; help(int.bit_length); bin(7), bin(8), bin(0)
        
    if True: # Cálculo Simbólico. # Cálculo Integral e Diferencial # from sympy import *
        e+E, sin(pi/6), sin(2*pi/3)-sqrt(3)/2, Rational(1,2)+Rational(1,3), (pi/2).evalf(), (Rational(1,2)+Rational(1,3)).evalf()
        x,y,z=symbols("x"),symbols("y"),symbols("z");
        x+x, x*y+y*x, factor(x**2-y**2), (x-y)*(x+y), expand((x-y)*(x+y))
        expand((1+x)**5), factor(x**5 + 5*x**4 + 10*x**3 + 10*x**2 + 5*x + 1)
        x*x**2-x**3, together(1/x+1/y), (x+y).subs(y,x), (x**2-y).subs([(x,5),(y,3)])
        srepr(x+y*z), srepr((x+y)*z) # ?sympify
        f,g=Function("f"),Function("g"); 
        n=Symbol("n"); a,b=Symbol("a"),Symbol("b"); c=Symbol("c");
        # Diferenciação e Integração de funções: Primitivas e Derivadas.
        diff(x**2+x+5,x), diff(1/x**2,x), diff(sin(x),x), diff(f(x)**2,x), diff(f(x)+g(x),x), diff(f(x)*g(x),x), diff(f(g(x)),x), integrate(x,x), integrate(1/(1+x**2),x), integrate(x*sin(x),x), integrate(x,(x,0,1)), integrate(sin(x),(x,0,pi)), integrate(E**-x,(x,0,oo))
        # Somatório e séries. # ?summation, ?series
        summation(x,(x,0,5)), summation(x,(x,0,n)), summation(1/2**n,(n,1,oo)), summation(1/factorial(x),(x,0,oo)), summation(x,(x,0,oo)), series(cos(x),x, 0, 10), series(E**x,x,0,10)
        # Limites. # ?limit
        limit(sin(x)/x,x,0), limit(atan(x),x,oo), limit(1/x,x,0,dir="+"), limit(1/x,x,0,dir="-")
        # Equaçãoes. # ?solve
        solve(x**2+1,x), solve(2*x+5-7,x), solve(a*x**2+b*x+c,x), solve(a*x**2+b*x+c,c), solve(x**2+1,x), solve((2*a-b,a+b-3),a,b), solve(cos(x),x), solve(2*x<1,x), solve([x<3,x**2>1],x), solve(1-log(x),x), solve(x*cos(x)-log(x),x)
       
    if True: # Arrays e Matrizes
        array([1,2,3,4]), arange(1,5), arange(1,10,2)
        shape(array([1,2,3,4])), shape(array([[1,2,3],[3,4,5]]))
        ndim(array([[[1,1],[1,1]],[[2,2],[2,2]],[[3,3],[3,3]]])), shape(array([[[1,1],[1,1]],[[2,2],[2,2]],[[3,3],[3,3]]]))
        reshape(arange(100),(10,10)), fromfunction(lambda i,j: i+j, (3,3)), zeros((3,3)), ones((3,4)),  eye(3), rand(3,4)
        print(rand(3,4)), print(arange(1,10000))
        array([1,2,3])+array([1,2,3]), 2*array([1,2,3]),  array([1,2,3])*array([1,2,3])
        eye(3)+eye(3), ones((3,3))*ones((3)), 
        dot(array([1,2,3]),array([4,5,6])), dot(ones((3,3)),ones((3,3))), dot(ones((3,3)),eye(3))
        transpose(array([[1,2],[3,4],[5,6]]))
        trace(array([[2,0],[1,3]]))
        det(array([[1,0],[1,0]])), det(array([[2,3,2],[4,2,3],[9,6,7]]))
        inv(array([[2,3,2],[4,2,3],[9,6,7]]))
        dot(array([[2,3,2],[4,2,3],[9,6,7]]),array([[-4,-9,5],[-1,-4,2],[6,15,-8]]))
        solve(array([[1,1],[1,-1]]),array([[2],[0]]))
        eig(array([[2,0],[1,3]]))
    
    if True: # Matrizes Revistadas
        Matrix([[1,x],[2,y]])+Matrix([[x,x],[y,x]]), Matrix([[1,x],[2,y]])*Matrix([[x,x],[y,x]])
        shape(Matrix([[1,x],[2,y]])), Matrix([[1,x],[2,y]]).row(1), Matrix([[1,x],[2,y]]).row(0), Matrix([[1,x],[2,y]]).col(0)
        Matrix([[1,x],[2,y]])**(-1), det(Matrix([[1,x],[2,y]])), Matrix([[1,x],[2,y]]).eigenvals(), Matrix([[1,x],[2,y]]).eigenvects()
        Matrix(2,2,[1,2,3,4]), Matrix(3,2,range(6)), Matrix(3,2,lambda i,j:i+j)
    
    if True: # Gráficos
        # from sympy.plotting import * # ?plot3d
        # from matplotlib.pyplot import plot as dataplot # ?dataplot
        plot(1+x**2,(x,-5,5)), plot(sin(x),(x,0,2*pi)), plot(sin(x**2),(x,0,10)), plot(x*cos(x)-log(x),(x,10**(-3),2)), plot((sin(x),(x,-pi,pi)),(x,(x,-2,2)))
        plot(arange(0,4*pi,0.1),sin(arange(0,4*pi,0.1)))
        plot3d(x+y,(x,-1,1),(y,-1,1)), plot3d(y**2*sin(x),(x,0,2*pi),(y,0,20)), plot3d(sin(x*cos(y)),(x,0,2*pi),(y,10,20))
        
        pie([45,30,10,10,4,1]), bar(range(10),[10,-7,20,3,15,-8,5,11,0,14]), hist([5,5,1,1,1,5,2,2,3,5])
        dataplot([1,2,3,4,5], "go-", label="line 1", linewidth=2), dataplot([1,2,3,4,5]), dataplot([1,-2,3,-4,5],"ro-"), dataplot([1,5,3,4,2,6],"g*--")
        dataplot([2,9,0,4], "rs",  label="line 2")
        # dataplot(range(6,0,-1),"bo-", label="line 1", linewidth=1), dataplot([1,2,3,4,5], "go-", label="line 1", linewidth=1)
        # dataplot([2,9,0,4], "r*-",  label="line 2"), dataplot(range(6),"rs--", label="line 2", linewidth=1)
        # dataplot(arange(0,10,.1),list(map((lambda x: log(x)),arange(0,10,.1))), "bs-")
        axis([0,8,0,8]); axis([-2,8,-2,10]); legend()

if True: # NB 2 - Tipos dados: Input e Output.
    
    if True: # Números: Inteiros e Flutuantes.
        6+7,6/7,6*7,exp(1),log(e),sqrt(2),pow(pi,2)
        type(1),type(1.0),id(1),id(1.0),type(e),type(pi),id(e),id(pi)
        int("523")+1,int(2.9),float(2)
        a=5;a+a**2;b=a;a=a+1;a,b
        x=5;x=7;x=8;x=x+1;x
    
    if True: # Strings: Texto e Formatação.
        list_str=[chr(x) for x in list(range(30,70))],chr(123)
        type("bom"),"boma"/2,"bom"+" "+"dia",str(123)+str(124),str(1==1)
        "bom dia"[0],"bom dia"[1],"bom dia"[-1],"bom dia"[2:5],"bom dia"[4:]
        "depois de "+str(123)+" vem "+str(124),"conseguir fazer {} dos {} exercícios do teste".format(3,5)
    
    if True: # Expressões Booleanas & IF's: True ou False.
        (1==1),type(1==1),id(1==1),(1!=1),type(1!=1),id(1!=1),2 is 1+1,(2==2.0),2 is 2.0
        isinstance(2.0,int),isinstance(2.0,float),isinstance(pi,Number),isinstance(e,Number)
        bool(False),bool(0),bool(""),bool(True),bool(1),bool("False"),bool("abc")
        1!=3 and (3<1 or (not 0==1)), 2 if 1==1 else 3, 2 if 1==2 else 3 if 1==1 else 4, 2 if 1==2 else 3 if 1==3 else 4
        [[x,x*2 if x<3 else (x+1)**(x+1) if x<5 else x+1 if x<10 else 0,x*2 if x<3 else (x+1)**(x+1) if x<5 else x+1 if x<50 else x] for x in [2,4,8,100]]
        def fun_IFs(w):
            r=[]
            for x in w:
                if x<3: x=x*2
                elif x<5: x+=1;x**=2
                elif x<50: x+=1
                else: x=0
                r+=[x]
            return r
        fun_IFs([2,4,8,100])
        
    if True: # Input/Output & Print
        [input("valor? "),int(input("valor? ")),int(input("valor? "))+1,input("valor? ")+str(1)] 
        print(input("valor? "),int(input("valor? "))+1,input("valor? ")+str(1))
        v=input("valor? "); print("valor =",v,", quadrado =",int(v)**2,"\nvalor =",v,"\nquadrado =",int(v)**2,"\n"+v+"\n"+str(int(v)**2))
        for i in range(1,10,3): print(i)
        for x in [3,5,7,9]: print(x)
        
        # import pandas as pd # import numpy as np
        # import matplotlib.pyplot as plt # ?plt # from matplotlib.pyplot import plot as dataplot # ?dataplot
        caminho = r"C:\Users\User\Desktop\exmp.xlsx"; dados_excel = pd.read_excel(caminho);  # print(dados_excel)
        lista_dados = list(map(list,dados_excel.T.to_numpy())); # print(lista_dados); type(lista_dados) # lista_dados = dados_excel.values.tolist(); # dados = dados**2 # print(dados)
        xi=list(range(10)); yi=list(map((lambda x: x**2),range(10))); data_frame = pd.DataFrame(xi,yi); data_frame.to_excel(caminho) # print(data_frame)
        def cria_gráficos(m):
            for y in m:
                fig, ax = plt.subplots()
                ax.plot(y) # dataplot(lista_dados[i]);
                plt.show()
                plt.close()
        cria_gráficos(lista_dados)
        
    if True: # Text: %pwd; %ls
        
        # Criar ficheiro e escrever.
        ficheiro=open("novo_log.txt","x"); ficheiro.write("ola!\ntudo bem?\nque fazes?\nadeus"); ficheiro.close() # f=open("novo.txt","x"); type(f); f.write("bom dia\nboa tarde\nboa noite"); f.close()
        # Abrir e escrever a partir do final.
        ficheiro=open("novo_log.txt","a"); ficheiro.write("\nBYEE"), ficheiro.close() 
        f=open("new.txt","a"); f.write("\nfim"); f.close() # f=open("new.txt","r"); f.read(); f.close()
        # Abrir e rescrever. O conteudo anterior é eliminado.
        ficheiro=open("novo_log.txt","w")
        # Abrir e Ler tudo
        ficheiro=open("novo_log.txt","r"); ficheiro.read(), ficheiro.close() # f=open("novo.txt","r"); f.read(); f.read(); f.close()
        # Abrir e Ler linha a linha
        ficheiro=open("novo_log.txt","r"); ficheiro.readline(), ficheiro.readline(), ficheiro.readline(), ficheiro.readline(), ficheiro.close() 
        # f=open("novo.txt","r"); f.readline(); f.readline(); f.readline(); f.readline(); f.close() # f=open("new.txt","r"); print(f.readline()+f.readline()+f.readline()+f.readline()); f.close()
        
        fic=open("new_log.txt","x");
        def guarda_dados_ficheiro_texto_novo(f):
            for i in range(10):
                fic.write(str(i)+"\n")
            fic.close()
        
        fic=open("new_log.txt","a");
        def guarda_dados_ficheiro_texto_existente(f):
            for i in range(1,10,2):
                f.write(str(i)+" ")
            f.close()
        
if True: # NB 3 - Listas e outros tipos de iteráveis
    
    if True: # Funções Auxiliares
        def soma_tuplo(x,*ys):
            for y in ys:
                x=x+y
            return x
        
        def pauta_notas(dic):
            r=[]
            for nome in dic.keys():
                if dic[nome]<10: r+=[[nome,"RE"]]; print(nome+" RE")
                else: r+=[[nome,dic[nome]]]; print(nome+" "+str(dic[nome]))
            return r
        def mostra_dic(dic):
            r=[]
            for (i,[x,y]) in dic.items():
                r+=[[i,x>y,[x,y]]]; print(x>y)
            return r
        
        def g1(x,*ys,**zs):
            for y in ys:
                x=x+y
            return zs["a"]+x
        def g2(x,*ys,**zs):
            for y in ys:
                x+=y; print(x,y)
            for z in zs:
                x+=zs[z]; print(x,zs[z])
            return x
    
    if True: # Listas - ?list; list.; dir(list); id(list); type(list())
        [list(range(10)),list(range(0,5)),list(range(3,10)),list(range(0,10,2)),list(range(10,0,-1))]
        [[[x,y] for x in range(2) for y in range(3)],[[x,y] for x in range(1,4) for y in range(1,4) if x!=y],[[(x,y) for x in range(2)] for y in range(3)]]
        [[x**2 for x in range(10)],[x**2 for x in [1,3,5,8]]]
        
        a=[]; b=[1,2,3]; c=[4,5]; d=5; d+=1; w=[1,2,[3,2,1],'ola'];
        x=[1,2,3]; x[1]=[7,7,7]; x
        
        [[b+c,b+b,b*2,b*3],[a,len(a),id(a),b,len(b),id(b),c,len(c),id(c),d,id(d)]]
        [[b[0],b[1],b[2],b[3]],b[len(b)-1]],[b[-1],b[-2],b[-3],[w[0],w[1],w[2],w[2][1],w[3]]]
        [b[0:2],b[1:3],b[1:2],b[1:1],b[0:len(b)],b[:2],b[1:],b[:],list.append(b,10)]
        
        a.append(5);list.append(a,[7,7,7]);list.append(a,7);list.append(a,12);list.append(a,'ola'); a
        a.pop();list.pop(a,0);list.pop(a,-2);list.insert(a,1,5);list.insert(a,0,5);list.insert(a,len(a),20);list.insert(a,-1,30);list.remove(a,5); a
        list.index(a,12);list.index(a,[7, 7, 7]);list.count(a,12);list.count(a,7);list.append(a,20);list.count(a,20); 
        list.reverse(a);list.pop(a);list.sort(a);list.sort(a,reverse=True); a
        list.clear(a); a
        
        s=['a','i','o','u','e']; t=[[4],[2],[3],[1]]; v=[[1,2],[4],[2,6],[2,6,7],[4,5]]; r=[1,[1],'1']; k=list(range(20)); z=[[1,2,3],[4,5,6],[7,8,9]];
        list.sort(s); list.sort(s,reverse=True); list.sort(t); list.sort(v); list.sort(r); shuffle(k); [list.reverse(w) for w in z]; s,t,v,r,k,z
        
        h=[1,3,2]; h1=h; list.sort(h); id(h)==id(h1); del h,h1
        h=[1,3,2]; h1=h[:]; id(h)==id(h1); list.sort(h); h,h1
        x1=[1,2,3]; x1[1]=5; x2=[1,x1,0]; x3=b[:]; x2,x3
        
        list(range(10)), list(map(int,str(123456789)))
        [i for i in range(10)], [[i for i in range(10)] for j in range(10)], 
        [i for i in range(len(10)) if i%2==0], [i if i%2==0 else 0 for i in range(10)]
        [[i+j for i in range(10)] for j in range(10)], [[i+j for j in range(5)] for i in range(6)], [[i+j] for i in range(10) for j in range(10)]
        [[(i,j) for j in range(5)] for i in range(6)], [[[i,j] for j in range(5)] for i in range(6)]
        
        g=(lambda x,y:x*y); type(g),g(7,9),(lambda x,y:x*y)(7,9)
        [(lambda x:x**2)(5),list(map((lambda x:x**2),range(10))),type(lambda x:x**2)]
        [(lambda x:e**x)(0),(lambda x:log(x))(log(e)),(lambda x:e**x)(1),(lambda x:log(x))(e),(lambda x:cos(x))(round(pi/2,10)),(lambda x:sin(x))(round(pi,10))]
    
    if True: # Tuplos e Dicionários
        # Tuplos - ?tuple; tuple.; dir(tuple); id(tuple); type(tuple())
        x=2;y=9; x,y=x+y,x*y; x,y=y,x; x,y
        aux=x; x=y; y=aux; x,y
        u=(1,2,3);u1=tuple(range(1,5)); u2=tuple(2*i for i in range(5)); u+u1+u2; len(u)
        t=(1,2,3); [soma_tuplo(5,6,7,10),[soma_tuplo(5,*t),soma_tuplo(5,(1,2,3))]]
        
        # Dicionários e Sets - ?dict; dict.; dir(dict); id(dict); type(dict()) | set?; set.; dir(set); id(set); type(set())
        notas={'joao':10,'maria':14,'jack':9,'ana':18}; notas['joao']
        notas.pop('joao'); notas['john']=10; [notas,notas.keys(),notas.values(),notas.items()],pauta_notas(notas)
        dados={x:[(lambda x: 2**x)(x),(lambda x: x**2)(x)] for x in range(6)}; [dados,dados.keys(),dados.values(),dados.items()],mostra_dic(dados)
        
        {x for x in "as armas e os baroes assinalados" if x not in " "}
        a={0,1,2,0}; b=set(); c=set([3,4]); a.add(3);c.add(0); a.intersection(c); a,b,c
        t=(1,1); d={"b":100,"c":10,"a":1}; [[g1(1,1,a=8,b=23),g1(1,*t,**d)],[g2(1,1,a=8,b=23),g2(1,*t,**d)]]
        
        # ?dict; dir(dict)
        pauta={}; pauta[333]=20; pauta[334]=10; pauta, 335 in pauta
        pauta; copia=pauta; copia.clear(); print(copia,pauta); pauta[333]=20; copia[333]
        copia=pauta.copy(); pauta,copia; pauta.clear(); pauta,copia
        
        # ?iter; dir(iter); dir(witer)
        w=[1,2,3]; witer=iter(w); w.append(4); next(witer); next(witer); next(witer); next(witer); w
        mult5=count(0,5); next(mult5); next(mult5) # from itertools import *
        rng=range(6); rrng=iter(rng); next(rrng); next(rrng)
        # No entanto, em Python, o mecanismo associado à composição iterativa usando for é bem mais poderoso.
        # Para além de range, é possível construir ciclos for a partir de qualquer objecto iterável (e.g., listas, strings, tuplos, ficheiros, dicionários).
        # são ainda expressáveis, equivalentemente, usando while, mas com uma estrutura um pouco mais complexa, nomeadamente
        # primitiva enumerate que constrói iteradores formados por pares posição e valor.
        # Tendo assim acesso directo ao valor x na posição i não é necessário lê-lo usando w[i].
        l=[w[i] for i in range(len(w)) if i%2!=0]; w=[list(range(1,4)) for i in range(3)]; m=[w for i in range(3)]
        f=(lambda x:x+1); g=(lambda a,b:a+b); # reduce(g,range(5)) # [nest(lambda x:x**2,1,10), fixedpoint((lambda x:x**2+1),3), myany([1,0,1,0])]
        rng=range(6); ri=iter(rng); next(ri); next(ri) # w=list(range(6)); wi=iter(w); next(wi); next(wi); next(wi)
        def funcao_print_for(iteravel):
            for i in iteravel:
                print(i)
        def funcao_print_enumerate(iteravel):
            for i,x in enumerate(iteravel):
                print(i,x)
        def funcao_print_iteradora(iteravel):
            stop=False
            seq=iter(iteravel)
            while not stop:
                i=next(seq,None)
                if i==None:
                    stop=True
                else:
                    print(i)
        
        def naturals(i):
            x=i
            while True:
                yield x
                x+=1
        nats=naturals(0); next(nats); next(nats)
        
        def zip(a,b):
            while True:
                yield next(a)
                a,b=b,a
        seq=zip(naturals(0),naturals(10)); next(seq), next(seq), next(seq), next(seq)

if True: # Projeto EP
    
    if True: # class individuo()
        
        # Indivíduo é caraterizado por: Identificador e Estado.
        # Tipos de Estados:
        # S - Suscetível (O indivíduo está operacional para todos os eventos do simulador e não pode alterar o estado dos indivíduos).
        # E - Exposto (Não pode alterar o estado dos indivíduos).
        # I - Infetado (Pode alterar o estado dos indivíduos).
        # R - Recuperado (Não pode alterar o seu estado nem o dos indivíduos).
        
        # Ind_test=individuo(123,"S")
        # Ind_test.Dados_individuo()
        
        class individuo():
            def __init__(self,ID):
                self._IDi = ID
                self._Estd = 'S'
            
            def ID_i(self):
                return self._IDi
            def Estado_i(self):
                return self._Estd
            def Muda_estado(self,nEstd):
                self._Estd = nEstd
            
            def Dados_individuo(self):
                print("Indivíduo::",self._IDi,":",self._Estd)
    
    if True: # class evento()
        
        # evento_test0=(123,0,'Rep')
        # evento_test1=(123,1,'Mrt')
        # evento_test2=(1234,2,'Des')
        # evento_test3=(1234,3,'Rep')
        # evento_test4=(123,4,'Mrt')
        # evento_test0.Dados_evento()
        
        class evento():
            def __init__(self,ID_ind,Tempo_ev,Tipo_ev):
                self._IDindividuo = ID_ind
                self._Tempo = Tempo_ev
                self._Tipo = Tipo_ev
            
            def ID_individuo(self):
                return self._IDindividuo
            def Tempo_evento(self):
                return self._Tempo
            def Tipo_evento(self):
                return self._Tipo
            
            def Dados_evento(self):
                print("Evento::",self._Tipo,":",self._Tempo,":",self._IDindividuo)
    
    if True: # class cap
        
        from evento import *
        
        # cap_test=[evento_test0,evento_test1,evento_test2,evento_test3,evento_test4]
        # cap_test.Elementos_cap()
        
        class cap():
            def __init__(self):
                self._cap=[]
                
            def Proximo_evento(self):
                assert len(self._cap)>0
                return self.cap[0]
            
            def Exclui_evento(self):
                assert len(self._cap)>0
                self._cap.pop(0)
            
            def Insere_evento(self,ev):
                i=0
                j=len(self._cap)-1
                    while (i<=j):
                        m=(i+j)//2
                        if ev.Tempo_evento()<self._cap[m].Tempo_evento():
                            j=m-1
                        else:
                            i=m+1
                    self._cap.insert(j+1,ev)
            
            def Remove_eventosIDi(self,idI):
                for e in self._cap:
                    if e.ID_individuo() == idI:
                        self._cap.remove(e)
            
            def Tamanho_cap(self):
                return len(self._cap)
            
            def Elementos_cap(self):
                for e in self._cap:
                    print (e.Dados_evento())
    
    if True: # class grelha()
        
        from individuo import *
        # Grelha formada por NxN posições.
        # A grelha possuí coordenadas continuas em que o individuo se desloca para fora
        # de um dos limites a sua nova posição será no limite oposto do grelha.
        
        class grelha():
            def __init__(self, N, obstaculos):
                self._dimgrelha = N
                
                self._sus={}
                self._exp={}
                self._inf={}
                self._rec={}
                
                self._listObst={}
                for x in obstaculos:
                    self._listObst[x]='X'
                    
                    
            def Dim_grelha(self):
                return self._dimgrelha
            
            
            def nr_individuos(self):
                DIndividuos={}
                DIndividuos.update(self._sus)
                DIndividuos.update(self._exp)
                DIndividuos.update(self._inf)
                DIndividuos.update(self._rec)
                return len(self._DIndividuos.keys())
            
            
            def Posicao_livreQ(self,x,y):
                return not ((x,y) in self._sus) and\
                       not ((x,y) in self._exp) and\
                       not ((x,y) in self._inf) and\
                       not ((x,y) in self._rec) and\
                       not ((x,y) in self._listObst)
            
            
            def insere_individuo(self,i,x,y):
                if self.Posicao_livreQ(x,y):
                    if abs(x)<=self.Dim_grelha() and abs(y)<=self.Dim_grelha():
                        if i.Estado_i() == 'S':
                            self._sus[(x,y)]=i
                        elif i.Estado_i() == 'E':
                            self._exp[(x,y)]=i
                        elif i.Estado_i() == 'I':
                            self._inf[(x,y)]=i
                        elif i.Estado_i() == 'R':
                            self._rec[(x,y)]=i
                        else:
                            print("Grelha::insere_individuo: indivíduo com estado inválido.")
                    else:
                        print("Grelha::insere_individuo: posição inadequada.")
                else:
                    print("Grelha::insere_individuo: posição dada não está livre.")
            
            
            def individuo_posicao(self,x,y):
                if (x,y) in self._sus:
                    return self._sus[(x,y)]
                elif (x,y) in self._exp:
                    return self._exp[(x,y)]
                elif (x,y) in self._inf:
                    return self._inf[(x,y)]
                elif (x,y) in self._rec:
                    return self._rec[(x,y)]
                else:
                    print("Grelha::individuo_posicao: a posição dada não tem um individuo, i.e., ou está livre ou tem um obstáculo...")
                    return -1
                
                    
            def estadoQ_posicao(self,x,y):
                if (x,y) in self._sus:
                    return 'S'
                elif (x,y) in self._exp:
                    return 'E'
                elif (x,y) in self._inf:
                    return 'I'
                elif (x,y) in self._rec:
                    return 'R'
                elif (x,y) in self._listObst:
                    return 'X'
                else:
                    print("Grelha::estado_posicao: posição não ocupada.")
                    return -1
                
                
            def remove_individuo(self,x,y):
                if self.Posicao_livreQ(x,y):
                    print("Grelha::remove_individuo: a posição dada está livre.")
                elif (x,y) in self._listObst:
                    print("Grelha::remove_individuo: a posição dada está ocupada por um obstáculo.")
                else:
                    if self.estadoQ_posicao(x,y) == 'S':
                        return self._sus.pop((x,y))
                    elif self.estadoQ_posicao(x,y) == 'E':
                        return self._exp.pop((x,y))            
                    elif self.estadoQ_posicao(x,y) == 'I':
                        return self._inf.pop((x,y))     
                    elif self.estadoQ_posicao(x,y) == 'R':
                        return self._rec.pop((x,y))
            
            
            def posicao_IDindividuo(self,identificador):
                DIndividuos={}
                DIndividuos.update(self._sus)
                DIndividuos.update(self._exp)
                DIndividuos.update(self._inf)
                DIndividuos.update(self._rec)
                
                lista_posicoes=list(DIndividuos.keys())
                stopQ=False
                i=0
                while i<len(lista_posicoes) and not stopQ:
                    stopQ = (DIndividuos.get(lista_posicoes[i]).ID_i() == identificador)
                    i += 1
                return (((0,0) if not stopQ else lista_posicoes[i-1]),stopQ)
            
            
            def trunca_viz1(self,x):
                if x==self.Dim_grelha()+1:
                    return -self.Dim_grelha()
                elif x==-self.Dim_grelha()-1:
                    return self.Dim_grelha()
                else:
                    return x
                
                
            def trunca_viz2(x):
                if x == self.Dim_grelha()+1:
                    return -self.Dim_grelha()
                elif x == self.Dim_grelha()-1:
                    return self.Dim_grelha()
                elif x == self.Dim_grelha()+2:
                    return -self.Dim_grelha()+1
                elif x == -self.Dim_grelha()-2:
                    return self.Dim_grelha()-1
                else:
                    return x
                
                
            def posicoes_viz1(self,x,y):
                dist_viz1 = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
                
                pos_viz1 = [(self.trunca_viz1(x+a),self.trunca_viz1(y+b)) for (a,b) in dist_viz1]
                return pos_viz1
            
            
            def posicoes_viz2(self,x,y):
                dist_viz2 = [(2,a) for a in range(-2,3)]+[(-2,a) for a in range(-2,3)]+\
                [(b,2) for b in range(-1,2)]+[(b,-2) for b in range(-1,2)]
                
                pos_viz2 = [(self.trunca_viz2(x+a),self.trunca_viz2(y+b)) for (a,b) in dist_viz2]
                return pos_viz2
            
            
            def posicoeslivres_viz1(self,x,y):
                dist_viz1 = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
                
                poslivres_viz1 = [(self.trunca_viz1(x+a),self.trunca_viz1(y+b)) for (a,b) in dist_viz1\
                                  if self.Posicao_livreQ(self.trunca_viz1(x+a),self.trunca_viz1(y+b))]
                return poslivres_viz1
            
            
            def nr_plivres_viz1(self,x,y):
                dist_viz1 = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
                
                poslivres_viz1 = [(self.trunca_viz1(x+a),self.trunca_viz1(y+b)) for (a,b) in dist_viz1\
                                  if self.Posicao_livreQ(self.trunca_viz1(x+a),self.trunca_viz1(y+b))]
                return len(poslivres_viz1)
            
            
            def posicoeslivres_viz2(x,y):
                dist_viz2 = [(2,a) for a in range(-2,3)]+[(-2,a) for a in range(-2,3)]+\
                [(b,2) for b in range(-1,2)]+[(b,-2) for b in range(-1,2)]
                
                poslivres_viz2 = [(self.trunca_viz2(x+a),self.trunca_viz2(y+b)) for (a,b) in dist_viz2\
                                  if Posicao_livreQ(self.trunca_viz2(x+a),self.trunca_viz2(y+b))]
                return poslivres_viz2
            
            
            def nr_plivres_viz2(self,x,y):
                dist_viz2 = [(2,a) for a in range(-2,3)]+[(-2,a) for a in range(-2,3)]+\
                [(b,2) for b in range(-1,2)]+[(b,-2) for b in range(-1,2)]
                
                poslivres_viz2 = [(self.trunca_viz2(x+a),self.trunca_viz2(y+b)) for (a,b) in dist_viz2\
                                  if Posicao_livreQ(self.trunca_viz2(x+a),self.trunca_viz2(y+b))]
                return len(poslivres_viz2)
            
            
            def posicoes_individuos_viz1(self,x,y):
                return [p for p in self.posicoes_viz1(x,y)\
                        if not self.Posicao_livreQ([p[0],p[1]]) and\
                        p not in self._listObst.keys()]
            
            
            def posicoes_individuos_viz2(self,x,y):
                return [p for p in self.posicoes_viz2(x,y)\
                        if not self.Posicao_livreQ(p[0],p[1]) and\
                        p not in self._listObst.keys()]
            
            
            def nr_individuos_viz1(self,x,y):
                return len([p for p in self.posicoes_viz1(x,y)\
                            if not self.Posicao_livreQ(p[0],p[1]) and\
                            p not in self._listObst.keys()])
            
            
            def nr_indidviduos_viz2(self,x,y):
                return len([p for p in self.posicoes_viz2(x,y)\
                            if not self.Posicao_livreQ(p[0],p[1]) and\
                            p not in self.listObst.keys()])
            
            
            def Posicao_infetadoQ(self,x,y):
                return (x,y) in self._inf
            
            
            def nr_infetados_viz1(self,x,y):
                dist_viz1 = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
                
                posInfetados_viz1 = [(self.trunca_viz1(x+a),self.trunca_viz1(y+b)) for (a,b) in dist_viz1\
                                     if self.Posicao_infetadoQ(self.trunca_viz1(x+a),self.trunca_viz1(y+b))]
                return len(posInfetados_viz1)
            
            
            def Pos_infetados_viz2(self,x,y):
                dist_viz2 = [(2,a) for a in range(-2,3)]+[(-2,a) for a in range(-2,3)]+\
                [(b,2) for b in range(-1,2)]+[(b,-2) for b in range(-1,2)]
                
                posInfetados_viz1 = [(self.trunca_viz1(x+a),self.trunca_viz1(y+b)) for (a,b) in dist_viz2\
                                     if self.Posicao_infetadoQ(self.trunca_viz1(x+a),self.trunca_viz1(y+b))]
                return posInfetados_viz2
                
            
            def nr_infetados_viz2(self,x,y):
                dist_viz2 = [(2,a) for a in range(-2,3)]+[(-2,a) for a in range(-2,3)]+\
                [(b,2) for b in range(-1,2)]+[(b,-2) for b in range(-1,2)]
                
                posInfetados_viz2 = [(self.trunca_viz2(x+a),self.trunca_viz2(y+b)) for (a,b) in dist_viz2\
                                     if self.Posicao_infetadoQ(trunca_viz2(x+a),trunca_viz2(y+b))]
                return len(posInfetados_viz2)
            
            
            def caminhoQ(self,x1,y1,x2,y2):
                return len([p for p in self.posicoes_viz1(x1,y1)\
                            if p in self.posicoes_viz1(x2,y2) and\
                            p not in self._listObst.keys()]) > 0
            
            
            def nr_infetadosV2_contacto(self,x,y):
                return len([p for p in self.Pos_infetados_viz2(x,y) if self.caminhoQ(x,y,p[0],p[1])])
            
            
            def Lposicoes_estado(self,s):
                if s=='S':
                    return list(self._sus.keys())
                elif s=='E':
                    return list(self._rec.keys())
                elif s=='I':
                    return list(self._inf.keys())
                elif s=='R':
                    return list(self._rec.keys())
                else:
                    print("Grelha::Lposicoes_estado: O estado dado não pertence ao SEIR.")
                    return -1
                
                
            def nr_posicoes_estado(self,s):
                if s=='S':
                    return len(list(self._sus.keys()))
                elif s=='E':
                    return len(list(self._exp.keys()))
                elif s=='I':
                    return len(list(self._inf.keys()))
                elif s=='R':
                    return len(list(self._rec.keys()))
                else:
                    print("Grelha::nr_posicoes_estado: O estado dado não  pertence ao SEIR.")
    
    if True: # simulador
        
        from math import exp, log
        
        from cap import *
        from grelha import *
        
        from random import *
        import matplotlib.pyplot as plt
        
        def sim(Th,p,obstaculos):
            Posmaxjogo = ((2*N)+1)**2 - len(obstaculos)
            
            def exprandom(m):
                x = random()
                return -m*(log(x))
            
            
            def Inicializa(p,obstaculos):
                Dim = int(input("Dimensão N:"))
                N = Dim
                # obstaculos = input("Lista de posições dos obstáculos definida na grelha (se o tamanho da lista não corresponder ao nº mínimo de obstáculos desejado na grelha, as restantes posições são introduzidas de forma aleatória):")
                n_obst = int(input("Nº de obstáculos a introduzir:"))
                obstaculos =  [(-N,-N),(N,-N),(0,0),(-N,N),(N,N)]
                while len(obstaculos)<n_obst:
                    (x1,y1)=(randint(-N,N),randint(-N,N))
                    if (x1,y1) not in obstaculos:
                        obstaculos += [(x1,y1)]
                        
                c = []
                gr = grelha(Dim,obstaculos)
                
                Ps = int(input("População Suscetível inicial:"))
                Pi = int(input("População Infetada inicial:"))
                p = int(input("Percentagem da populaçao total inicial agrupada:"))    
                Pjogo = Ps + Pi
                nrP_agr = p * Pjogo
                nrP_alt = Pjogo - nrP_agr
                
                lista_posicoes = []
                listp_agr = []
                listp_alt = []
                while len(lista_posicoes) < Pjogo:
                    (x1,y1) = (randint(-N,N),randint(-N,N))
                    if gr.Posicao_livreQ(x1,y1):
                        if gr.nr_individuos_viz1(x1,y1)>0 and (nrP_agr - len(listp_agr))>len([p for p in listp_alt if p in gr.posicoes_individuos_viz1(x1,y1)]):
                            lista_posicoes += [(x1,y1)]
                            listp_agr += [p for p in listp_alt if p in gr.posicoes_individuos_viz1(x1,y1) and\
                                          p not in listp_agr] + [(x1,y1)]
                            listp_alt = [p for p in listp_alt if p not in listp_agr]
                            
                        elif gr.nr_individuos_viz1(x1,y1)==0 and len(listp_alt)<nrP_alt:
                            lista_posicoes += [(x1,y1)]
                            listp_alt += [(x1,y1)]
                            
                        ind = individuo(len(lista_posicoes))
                        gr.insere_individuo(ind,lista_posicoes[ind.ID_i()-1])
                
                nrPi_agr = p*Pi
                nrPs_agr = p*Ps
                xI_agr=0
                xS_agr=0
                
                nrPi_alt = Pi*(1-p)
                nrPs_alt = Ps*(1-p)
                xI_alt=0
                xS_alt=0
                
                for i in range(len(lista_posicoes)):
                    ind = individuo(i+1)
                    c.Insere_evento(Evento(ind.ID_I(),0.0,'Des'))
                    c.Insere_evento(Evento(ind.ID_I(),0.0,'Rep'))
                    c.Insere_evento(Evento(ind.ID_I(),0.0,'Atl'))
                    c.Insere_evento(Evento(ind.ID_I(),0.0,'Mrt'))
                    
                    x = randint(1)
                    if lista_posicoes[i] in listp_agr:
                        if x==1:
                            if xI_agr < nrPi_agr:
                                xI_agr += 1
                                gr.remove_individuo(lista_posicoes[i])
                                ind.Muda_estado('I')
                                gr.insere_individuo(ind,lista_posicoes[i])
                            elif xS_agr < nrPs_agr:
                                xS_agr += 1
                        else:
                            if xS_agr < nrPs_agr:
                                xS_agr += 1
                            elif xI_agr < nrPi_agr:
                                xI_agr += 1
                                gr.remove_individuo(lista_posicoes[i])
                                ind.Muda_estado('I')
                                gr.insere_individuo(ind,lista_posicoes[i])
                    else:
                        if x==1:
                            if xI_alt < nrPi_alt:
                                xI_alt += 1
                                gr.remove_individuo(lista_posicoes[i])
                                ind.Muda_estado('I')
                                gr.insere_individuo(ind,lista_posicoes[i])
                            elif xS_alt < nrPs_alt:
                                xS_alt += 1
                        else:
                            if xS_alt < nrPs_alt:
                                xS_alt += 1
                            elif xI_alt < nrPi_alt:
                                xI_alt += 1
                                gr.remove_individuo(lista_posicoes[i])
                                ind.Muda_estado('I')
                                gr.insere_individuo(ind,lista_posicoes[i])
                                
        
            return c,gr,obstaculos
        
            c,gr,obstaculos = Inicializa(p,obstaculos)
                                            
            Ti = 0
            Th = int(input('Tempo limite de simulação:'))
            
            f = fopen("Resultados.txt","w")
            f.write(str(gr.Dim_grelha()) + "\n")
            f.write(str(obstaculos) + "\n")
            f.write(str([gr.Lposicoes_estado('S'),gr.Lposicoes_estado('E'),gr.Lposicoes_estado('I'),gr.Lposicoes_estado('R')])+ "\n")
            
            ct = Ti
            lista_nrInfetados = [(ct,gr.nr_posicoes_estado('I'))]
            lista_mortes = [[]]
            while ct < Th and c.Tamanho_cap()>0:
                cE = c.Proximo_evento()
                ct = cE.Tempo_evento()
                cI = cE.ID_individuo()
                (xi,yi) = gr.posicao_IDindividuo(cI)[0]
                ind = gr.individuo_posicao(gr.posicao_IDindividuo(cI)[0])
                
                c.Exclui_evento()
                
                if cE.Tipo_evento() == 'Des':
                    if gr.nr_plivres_viz1(xi,yi)>0:
                        if gr.nr_infetados_viz1(xi,yi)>2:
                            c.Insere_evento(cE(cI,ct+obsrand.exprandom(1),'Des'))
                            gr.remove_individuo(xi,yi)
                            gr.insere_individuo(ind,gr.posicoeslivres_viz1(xi,yi)[randrange(gr.nr_plivres_viz1(xi,yi))])
                        else:
                            def prob_desloc(Pd,Td):
                                Td = 1
                                Pd = 0.6
                                x = random(1)
                                if x>Pd:
                                    c.Insere_evento(cE(cI,ct+obsrand.exprandom(Td),'Des'))
                                    gr.remove_individuo(xi,yi)
                                    gr.insere_individuo(ind,gr.posicoeslivres_viz1(xi,yi)[randrange(gr.nr_plivres_viz1(xi,yi))])
                                else:
                                    c.Insere_evento(cE(cI,ct+obsrand.exprandom(Td),'Des'))
                    else:
                        c.Insere_evento(cE(cI,ct+obsrand.exprandom(1),'Des'))
                        
                elif cE.Tipo_evento() == 'Rep':
                    if gr.nr_plivres_viz1(xi,yi)>1 and gr.nr_individuos_viz1(xi,yi)>0:
                        def prob_reprod(Pr,Tr):
                            Tr = 10
                            Pr = 0.3
                            x = random(1)
                            if x>Pr:
                                c.Insere_evento(cE(cI,ct+obsrand.exprandom(Tr),'Rep'))
                                
                                n_ind = individuo(gr.nr_individuos()+1+len(lista_mortes))
                                c.Insere_evento(evento(n_ind.ID_i(),ct,'Des'))
                                c.Insere_evento(evento(n_ind.ID_i(),ct,'Rep'))
                                c.Insere_evento(evento(n_ind.ID_i(),ct,'Atl'))
                                c.Insere_evento(evento(n_ind.ID_i(),ct,'Mrt'))
                                gr.insere_individuo(n_ind,gr.posicoes_livres_viz1(xi,yi)[randrange(gr.nr_plivres_viz1(xi,yi))])
                            else:
                                c.Insere_evento(cE(cI,ct+obsrand.exprandom(Tr),'Rep'))
                    else:
                        c.Insere_evento(cE(cI,ct+obsrand.exprandom(10),'Rep'))
                        
                elif cE.Tipo_evento() == 'Mrt':
                    if ind.Estado_i() == 'I':
                        def prob_morte_I(Pm,Tm):
                            Tm = 20
                            Pm = 0.5
                            x = random(1)*1.10
                            if x>Pm:
                                gr.remove_individuo(xi,yi)
                                c.Remove_eventosIDi(cI)
                                lista_mortes += [[(xi,yi),cI,ct,'I']]
                            else:
                                c.Insere_evento(cE(cI,ct+obsrand.exprandom(Tm),'Mrt'))
                    
                    if ind.Estado_i() == ('S' or 'E' or 'R'):
                        def prob_morte(Pm,Tm):
                            Tm = 20
                            Pm = 0.5
                            x=random(1)
                            if x>Pm:
                                gr.remove_individuo(xi,yi)
                                c.Remove_eventosIDi(cI)
                                lista_mortes += [[(xi,yi),cI,ct,ind.Estado_i()]]
                            else:
                                c.Insere_evento(cE(cI,ct+obsrand.exprandom(Tm),'Mrt'))
                    else:
                        c.Insere_evento(cE(cI,ct+obsrand.exprandom(20),'Mrt'))
                        
                elif cE.Tipo_evento() == 'Atl':
                    
                    if ind.Estado_i() == 'S':
                        x = 2*(gr.nr_infetados_viz1(xi,yi)) + gr.nr_infetadosV2_contacto(xi,yi)
                        if x>0:
                            def prob_atualizE(x,Ta_E,Ta_S):
                                Ta_E = 1
                                Ta_S = 1
                                y = randint(1)
                                prob_atualiz = ((1/(2*log(1.8))) - (1/(2*log(((x*(x-1))/5)+1.8))))
                                if y > prob_atualiz:
                                    c.Insere_evento(cE(cI,ct+obsrand.exprandom(Ta_E),'Atl'))
                                    gr.remove_individuo(xi,yi)
                                    ind.Muda_estado('E')
                                    gr.insere_individuo(ind,(xi,yi))
                                else:
                                    c.Insere_evento(cE(cI,ct+obsrand.exprandom(Ta_S),'Atl'))              
                        else:
                            #tempo medio de atualização correspondente ao estado suscetível.
                            c.Insere_evento(cE(cI,ct+obsrand.exprandom(1),'Atl'))
                            
                    elif ind.Estado_i() == 'E':
                        Ta_I = 10
                        c.Insere_evento(cE(cI,ct+obsrand.exprandom(Ta_I),'Atl'))
                        gr.remove_individuo(xi,yi)
                        ind.Muda_estado('I')
                        gr.insere_individuo(ind,(xi,yi))
                        
                    elif ind.Estado_i() == 'I':
                        gr.remove_individuo(xi,yi)
                        ind.Muda_estado('R')
                        gr.insere_individuo(ind,(xi,yi))
            
                lista_nrInfetados += [(ct,gr.nr_posicoes_estado('I'))]
                f.write(str([gr.Lposicoes_estado('S'),gr.Lposicoes_estado('E'),gr.Lposicoes_estado('I'),gr.Lposicoes_estado('R')])+ "\n")
                f.close()
                
            return lista_nrInfetados
        
        lista_Inf = sim(Th,p,obstaculos)
        # Visualização do gráfico de simulação pretendido:
        
        xS = [p[0] for p in lista_Inf]
        yS = [p[1] for p in lista_Inf]
        plt.plot(yS,xS)
        plt.show()
    
    if True: # animação
        
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        
        from simulador import *
        
        
        # Lista de obstaculos: linha vertical em (1,y)
        lisobs1=[(1,x) for x in range(-Dim,Dim+1)]
        # Lista de obstaculos 2: duas linhas verticais
        lisobs2=[(-5,x) for x in range(-Dim,Dim+1)]+[(5,x) for x in range(-Dim,Dim+1)]
        # quadrado
        lisobs3=[(x,15) for x in range(-2,18)]+[(x,5) for x in range(-2,18)]+\
                [(-2,y) for y in range(6,15)]+[(17,y) for y in range(6,15)]
        
        lista = sim(50,0.6,lisobs2)
        print("len(lista)=",len(lista))
        
        
        
        #ANIMACAO
        
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        import ast
        
        f=open('resultados.txt','r')
        lista=[]
        for line in f:
            lista.append(ast.literal_eval(line))
            
        f.close()
        Dim=lista[0]
        obstaculos=lista[1]
        nobst=len(obstaculos)
        lista=lista[2:]
        max_point=max([len(w[0])+len(w[1])+len(w[2])+len(w[3]) for w in lista])+nobst+1
        
        
        print("len(lista)=",len(lista))
        
        
        #Dim=25
        
        fig=plt.figure()
        ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-Dim-5,Dim+5), ylim=(-Dim-5,Dim+5))
        
        #desenha as grelhas (defasadas das coordenadas certas para os pontos ficarem centrados) - check limites
        for i in range(-Dim,Dim):
            lines, = ax.plot([-Dim-0.5,Dim+0.5],[i+0.5,i+0.5],'-',color='0.75')
        for i in range(-Dim,Dim):
            lines, = ax.plot([i+0.5,i+0.5],[-Dim-0.5,Dim+0.5],'-',color='0.75')
            
        
        # valor inicial dos pontos
        ponto=[[] for i in range(max_point)]
        for i in range(max_point):
            ponto[i], = ax.plot([],[], marker='o',markersize=2)
        
        for j in range(nobst):
            ponto[j].set_data(obstaculos[j][0],obstaculos[j][1])
            ponto[j].set_color("black")
            
        #k=4
        #for j in range(len(lista[k])):
        #    px1 = lista[k][j][0]
        #    py1 = lista[k][j][1]
        #    ponto[j].set_data(px1,py1)
            
        def animate(i):
            print("i=",i)
            frame=lista[i]
        # setup dos susceptiveis
        
            k=nobst
            for j in range(k,k+len(frame[0])):
                ponto[j].set_data(frame[0][j-k][0],frame[0][j-k][1])
                ponto[j].set_color("green")
            k=k+len(frame[0])
            for j in range(k,k+len(frame[1])):
                ponto[j].set_data(frame[1][j-k][0],frame[1][j-k][1])
                ponto[j].set_color("orange")
            k=k+len(frame[1])
            for j in range(k,k+len(frame[2])):
                ponto[j].set_data(frame[2][j-k][0],frame[2][j-k][1])
                ponto[j].set_color("red")
            k=k+len(frame[2])
            for j in range(k,k+len(frame[3])):
                ponto[j].set_data(frame[3][j-k][0],frame[3][j-k][1])
                ponto[j].set_color("blue")
            k=k+len(frame[3])
            for j in range(k,max_point):
                ponto[j].set_color("white")
            return ponto
        
        ani = animation.FuncAnimation(fig, animate, frames=len(lista), interval=1, repeat=False, blit=True)
        
        # Se retirar o comentário da linha de código abaixo, é gerado um ficheiro contento do filme da animação
        ani.save('animacao.mp4', fps=25)

