import math
import numpy as np
from numpy import log, std, arange, ndarray, array, sum, mean
from math import pi, sin, cos, ceil, sqrt
from scipy.stats import norm, expon, lognorm

from pandas import read_csv, Series, DataFrame, concat, Index, Period
from pandas import to_numeric, to_datetime
from pandas.api.types import is_integer_dtype, is_any_real_numeric_dtype
import numbers
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

#import matplotlib.pyplot as plt
from matplotlib.pyplot import gca, figure, show, close #, savefig, plot
from matplotlib.pyplot import gcf
from matplotlib.pyplot import subplots #, xticks
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from matplotlib.container import BarContainer
from matplotlib.collections import PathCollection
from matplotlib.colorbar import Colorbar
import matplotlib.dates as mdates #mdates.num2date(17836) # mdates.num2date(17836).strftime("%d/%m/%Y") #mdates.date2num(datetime(2018, 8, 1))
from seaborn import heatmap
from matplotlib.font_manager import FontProperties

from config import LINE_COLOR, FILL_COLOR
from dslabs_functions import ACTIVE_COLORS, FILL_COLOR # from dslabs_functions import FONT_TEXT, HEIGHT

#import pandas as pd
#pd.set_option('display.max_columns', None) # Display / Show all columns
#pd.set_option('display.width', 1000) # Set a high enough width to prevent line breaks 
#pd.reset_option('display.max_columns')

TEXT_MARGIN = 0.05
FONT_SIZE = 6
FONT_TEXT = FontProperties(size=FONT_SIZE)
HEIGHT: int = 4
# alpha = 0.3







# PLOTS: LINE CHARTS (Time Series), BAR CHARTS (Granularity), SCATTER PLOTS (Sparsity), BOXPLOTS (Outliers), HISTOGRAMS, CORRELATION

# IDEIA (Ignorar): JUNTAR ESTAS DUAS FUNÇÕES NUMA SÓ "set_chart_ticks_and_labels"
def set_chart_labels(ax: Axes, title: str = "", xlabel: str = "", ylabel: str = "") -> Axes: # The set_chart_labels function, abstracts the statment of the several labels to enrich our chart, namely: its title and labels for its x-axis and y-axis.
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return ax
def set_chart_xticks(xvalues: list[str | int | float | datetime], yvalues: list[str | int | float | datetime], ax: Axes, percentage: bool = False, xleftQ: bool = True, yleftQ: bool = True) -> Axes:
    # The set_chart_xticks function, which formats the x-axis depending on its data type. So, it receives the values to print in the x-axis (xvalues), using the best matplotlib tools to do it according to its data type. Additionaly, it receives a boolean specifying if the y-axis is a percentual number or not (percentage).
    
    def give_limits_and_ticks(values, ticks, leftQ):
        # xvalues = data_cancer.sort_index().head(n=50).index.to_list(); yvalues = data_cancer['age'].sort_index().head(n=50).to_list()
        # xticks = ax.get_xticks(); yticks = ax.get_yticks()
        a = min([x for x in values if not math.isnan(x)]); b = max([x for x in values if not math.isnan(x)])
        l1 = 0; l2 = 0; k = 0.05
        if (a < ticks[0]) or (b > ticks[-1]): # Antes de começar, verificar se o min e máx estão compreendidos dentro dos ticks, caso contrário acrescentar ticks até ambos estarem contidos nos ticks
            passo = ticks[1] - ticks[0]
            first = ticks[0]; new_left_ticks = [] # Lado esquerdo
            while first > a:
                new_first = first - passo
                new_left_ticks = [new_first] + new_left_ticks
                first = new_first
            if new_left_ticks != []: ticks = np.concatenate([new_left_ticks, ticks])
            last = ticks[-1]; new_right_ticks = [] # Lado direito
            while last < b:
                new_last = last + passo
                new_right_ticks += [new_last]
                last = new_last
            if new_right_ticks != []: ticks = np.concatenate([ticks, new_right_ticks])
        for t in ticks:
            if t <= a:
                l1 = t
            else:
                break
        for t in ticks:
            if t >= b:
                l2 = t
                break
        intervalo = l2 - l1
        lr1 = l1 - intervalo * k if leftQ else l1
        lr2 = l2 + intervalo * k
        new_ticks = [t for t in ticks if (t >= l1) and (t <= l2)]
        #print((lr1, lr2), new_ticks)
        return (lr1, lr2), new_ticks
    
    if len(xvalues) > 0:
        
        
        
        if isinstance(xvalues[0], datetime):
            # locator = AutoDateLocator() # ax.xaxis.set_major_locator(locator) # ax.xaxis.set_major_formatter(AutoDateFormatter(locator, defaultfmt="%Y-%m-%d"))
            def give_limits_and_ticks_date(xvalues, xticks, leftQ):
                #from dateutil.relativedelta import relativedelta
                ticks = [datetime(mdates.num2date(t).year, mdates.num2date(t).month, mdates.num2date(t).day, mdates.num2date(t).hour, mdates.num2date(t).minute) for t in xticks] #[datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second) for dt in map(mdates.num2date, xticks)] #import matplotlib.dates as mdates
                ry = []; rm = []; rd = []; rh = []; rmin = [] #print(ticks, ticks[:-1])
                for i, x in enumerate(ticks[:-1]):
                    d1 = x; d2 = ticks[i+1]
                    ry.append(relativedelta(d2, d1).years); rm.append(relativedelta(d2, d1).months); rd.append(abs(d2.day - d1.day))
                    # total_seconds = (d2 - d1).total_seconds(); hours = int(total_seconds / 3600); minutes = int(((total_seconds / 3600) - hours) / 60) # seconds...
                    # rh.append(hours); rmin.append(minutes) # seconds...
                sy = list(set(ry))[0] if len(set(ry)) == 1 else list(set(ry))
                sm = list(set(rm))[0] if len(set(rm)) == 1 else list(set(rm))
                sd = list(set(rd))[0] if len(set(rd)) == 1 else min(list(set(rd)))
                # sh = list(set(rh))[0] if len(set(rh)) == 1 else min(list(set(rh)))
                # smin = list(set(rmin))[0] if len(set(rmin)) == 1 else min(list(set(rh)))
                #print(sy, sm, sd) #, sh, smin
                first = datetime(xvalues[0].year, xvalues[0].month, xvalues[0].day, xvalues[0].hour, xvalues[0].minute) #print(first, ticks[0])
                last = datetime(xvalues[-1].year, xvalues[-1].month, xvalues[-1].day, xvalues[-1].hour, xvalues[-1].minute) #print(last, ticks[-1])
                if first < ticks[0]:
                    if sy != 0: ft = ticks[0] - relativedelta(years = sy)
                    elif sm != 0: ft = ticks[0] - relativedelta(months = sm)
                    elif sd != 0: ft = ticks[0] - relativedelta(days = sd)
                    # elif sh != 0: ft = ticks[0] - timedelta(hours = sh)
                    # elif smin != 0: ft = ticks[0] - timedelta(minutes = smin)
                    if first >= ft:
                        ticks = [ft] + ticks
                elif first >= ticks[0]:
                    ft = ticks[0]
                if last > ticks[-1]:
                    if sy != 0: lt = ticks[-1] + relativedelta(years = sy)
                    elif sm != 0: lt = ticks[-1] + relativedelta(months = sm)
                    elif sd != 0: lt = ticks[-1] + relativedelta(days = sd)
                    # elif sh != 0: lt = ticks[-1] + timedelta(hours = sh)
                    # elif smin != 0: lt = ticks[-1] + timedelta(minutes = smin)
                    if last <= lt:
                        ticks = ticks + [lt]
                elif last <= ticks[-1]:
                    lt = ticks[-1]
                k = 0.025
                intervalo = mdates.date2num(lt) - mdates.date2num(ft)
                lr1 = mdates.date2num(ft) - intervalo * k if leftQ else mdates.date2num(ft)
                lr2 = mdates.date2num(lt) + intervalo * k
                new_ticks = [t for t in ticks if (t >= ft) and (t <= lt)]
                #print((lr1, lr2), new_ticks)
                return (lr1, lr2), new_ticks
            
            fig1, ax1 = subplots()
            ax1.plot(xvalues, yvalues)
            xticks = ax1.get_xticks(); yticks = ax1.get_yticks()
            close(fig1)
            
            xlim, xticks = give_limits_and_ticks_date(xvalues, xticks, xleftQ)
            ylim, yticks = give_limits_and_ticks(yvalues, yticks, yleftQ)
            
            ax.set_xlim(xlim); ax.set_ylim(ylim)
            ax.set_xticks(xticks); ax.set_yticks(yticks)
            ax.set_xticklabels([t.strftime("%Y/%m/%d") for t in xticks])
        
        if not(any(not isinstance(x, (int, float)) for x in xvalues)) and not(any(not isinstance(y, (int, float)) for y in yvalues)):
            fig1, ax1 = subplots()
            ax1.plot(xvalues, yvalues)
            xticks = ax1.get_xticks(); yticks = ax1.get_yticks()
            close(fig1)
            xlim, xticks = give_limits_and_ticks(xvalues, xticks, xleftQ)
            ylim, yticks = give_limits_and_ticks(yvalues, yticks, yleftQ)
            ax.set_xlim(xlim); ax.set_ylim(ylim) # ax.set_xlim(left=xvalues[0], right=xvalues[-1])
            ax.set_xticks(xticks); ax.set_yticks(yticks) # ax.set_xticks(xvalues, labels=xvalues)
        elif any(not isinstance(x, (int, float)) for x in xvalues) and not(any(not isinstance(y, (int, float)) for y in yvalues)):
            fig1, ax1 = subplots()
            ax1.plot(xvalues, yvalues)
            xticks = ax1.get_xticks(); yticks = ax1.get_yticks()
            close(fig1)
            ylim, yticks = give_limits_and_ticks(yvalues, yticks, yleftQ)
            ax.set_ylim(ylim); ax.set_yticks(yticks)
        elif any(not isinstance(y, (int, float)) for y in yvalues) and not(any(not isinstance(x, (int, float)) for x in xvalues)):
            fig1, ax1 = subplots()
            ax1.plot(xvalues, yvalues)
            xticks = ax1.get_xticks(); yticks = ax1.get_yticks()
            close(fig1)
            xlim, xticks = give_limits_and_ticks(xvalues, xticks, xleftQ)
            ax.set_xlim(xlim); ax.set_xticks(xticks)
        if percentage: #ax.set_ylim(0.0, 1.0)
            fig1, ax1 = subplots(); ax1.plot(xvalues, np.linspace(0, 1, len(xvalues)))
            xticks = ax1.get_xticks(); yticks = ax1.get_yticks(); close(fig1)
            ylim, yticks = give_limits_and_ticks(np.linspace(0, 1, len(xvalues)), yticks, leftQ=False) #yleftQ
            ax.set_ylim(ylim); ax.set_yticks(yticks)
        rotation: int = 0 #45
        ax.tick_params(axis="x", labelrotation=rotation, labelsize="xx-small")
    return ax
def define_grid(nr_vars: int, nr_cols: int | str = "") -> tuple[int, int]: #nr_cols: int = NR_COLUMNS
    if nr_cols == "":
        if nr_vars <= 3: nr_rows, nr_cols = 1, nr_vars
        else: nr_cols = int(math.sqrt(nr_vars)); nr_rows = nr_cols + 1 if math.sqrt(nr_vars) > int(math.sqrt(nr_vars)) else nr_cols 
        #print(n_vars, n_cols, n_rows, n_cols*n_rows)
    else:
        nr_rows: int = 1 # NR_COLUMNS: int = 3
        if nr_vars % nr_cols == 0: nr_rows = nr_vars // nr_cols
        else: nr_rows = nr_vars // nr_cols + 1
    return nr_rows, nr_cols


def plot_pie_chart(xvalues: list | dict | Index, yvalues: list | dict | Series, ax: Axes = None, title: str = "", percentage: bool = True, show_plot: bool = True) -> Axes:
    if show_plot: figure(figsize=(HEIGHT, HEIGHT))
    if ax is None: ax = gca()
    ax = set_chart_labels(ax=ax, title=title) #ax.axis('equal') # Deixa o gráfico com um formato mais 'redondo'
    
    # Dataframes / Series
    if isinstance(xvalues, Index) and isinstance(yvalues, Series):
        xvalues = xvalues.to_list(); yvalues = yvalues.to_list()
        if any(isinstance(x, int | float) for x in xvalues): xvalues = list(map(str, xvalues))
    # Dicionários
    elif isinstance(xvalues, dict) and isinstance(yvalues, dict):
        xvalues = list(xvalues.keys()); yvalues = list(yvalues.values())
        if any(isinstance(x, int | float) for x in xvalues): xvalues = list(map(str, xvalues))
    
    yvalues, xvalues = zip(*sorted(zip(yvalues, xvalues), reverse=True)) # Ordenar os dados por ordem decrescente # xvalues = ["a", "b", "c", "d",] # yvalues = [1, 2, 3, 4]
    wedges, texts, autotexts = ax.pie(yvalues, labels=xvalues, radius=1, autopct='%1.1f%%', pctdistance=0.8, textprops={'fontproperties': FONT_TEXT}, startangle=90, explode= [0.005] * len(xvalues), counterclock=False)
    for wedge, valor in zip(wedges, yvalues):
        ang = (wedge.theta2 + wedge.theta1) / 2
        x = 0.5 * np.cos(np.deg2rad(ang))
        y = 0.5 * np.sin(np.deg2rad(ang))
        ax.text(x, y, valor, fontproperties=FONT_TEXT, ha='center', va='center') # # ha = 'left', 'center', 'right' # va = 'bottom', 'center', 'top', 'baseline', 'center_baseline'
    ax.legend(xvalues, fontsize="xx-small")
    
    if not(percentage): #format = "%.2f" if percentage else "%.0f"
        for autotext in autotexts: autotext.set_visible(False)
    
    if show_plot: show() #savefig("Gráficos/{file_tag}_pie_season_frequency.png") 
    return ax
def plot_line_chart(xvalues: list | dict | Index, yvalues: list | dict | Series, ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", name: str = "", percentage: bool = False, show_stdev: bool = False, xleftQ: bool = True, yleftQ: bool = False, show_plot: bool = True) -> Axes:
    if show_plot: figure(figsize=(HEIGHT * 5, HEIGHT))
    if ax is None: ax = gca()
    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel)
    
    # Dataframes / Series
    if isinstance(xvalues, Index) and isinstance(yvalues, Series):
        xvalues = xvalues.to_list()
        yvalues = yvalues.to_list()
    # Dicionários
    elif isinstance(xvalues, dict | list) and isinstance(yvalues, dict):
        xvalues = list(xvalues.keys())
        if not(isinstance(xvalues, list)): yvalues = list(yvalues.values())
    
    ax.plot(xvalues, yvalues, label=name) #c=LINE_COLOR, 
    if show_stdev:
        stdev: float = round(std(yvalues), 3)
        y_bottom: list[float] = [(y - stdev) for y in yvalues]
        y_top: list[float] = [(y + stdev) for y in yvalues]
        ax.fill_between(xvalues, y_bottom, y_top, color=FILL_COLOR, alpha=0.2)
    
    yvals = np.linspace(min([x for x in yvalues if not math.isnan(x)]), max([x for x in yvalues if not math.isnan(x)]), len(xvalues))
    ax = set_chart_xticks(xvalues, yvals, ax, percentage=percentage, xleftQ=xleftQ, yleftQ=yleftQ)
    
    if show_plot: show() #savefig("Gráficos/pH_variation.png")
    return ax
def plot_bar_chart(xvalues: list | dict | Index, yvalues: list | dict | Series, error: list = [], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", percentage: bool = False, horizontal: bool = False, yleftQ: bool = False, show_plot: bool = True) -> Axes:
    if show_plot: figure(figsize=(HEIGHT * 2, HEIGHT))
    if ax is None: ax = gca()
    format = "%.2f" if percentage else "%.0f"
    
    # Dataframes / Series
    if isinstance(xvalues, Index) and isinstance(yvalues, Series):
        xvalues = xvalues.to_list(); yvalues = yvalues.to_list()
        if any(isinstance(x, int | float) for x in xvalues): xvalues = list(map(str, xvalues))
    # Dicionários
    elif isinstance(xvalues, dict) and isinstance(yvalues, dict):
        xvalues = list(xvalues.keys()); yvalues = list(yvalues.values())
        if any(isinstance(x, int | float) for x in xvalues): xvalues = list(map(str, xvalues))
    
    yvals = np.linspace(min([x for x in yvalues if not math.isnan(x)]) if min([x for x in yvalues if not math.isnan(x)])<=0 else 0, max([x for x in yvalues if not math.isnan(x)]), len(xvalues))
    
    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel) if not(horizontal) else set_chart_labels(ax=ax, title=title, xlabel=ylabel, ylabel=xlabel)
    if not horizontal:
        ax = set_chart_xticks(xvalues, yvals, ax=ax, percentage=percentage, yleftQ=yleftQ)
        values: BarContainer = ax.bar(xvalues, yvalues, label=yvalues, edgecolor=LINE_COLOR, color=FILL_COLOR, tick_label=xvalues)
        ax.bar_label(values, fmt=format, fontproperties=FONT_TEXT)
    
    elif horizontal: # horizontal bar chart
        if error == []: error = [0] * len(xvalues)
        y_pos: list = list(arange(len(xvalues)))
        values = ax.barh(y_pos, yvalues, xerr=error, align="center", error_kw={"lw": 0.5, "ecolor": "r"})
        ax.set_yticks(y_pos, labels=xvalues); ax.invert_yaxis()  # labels read top-to-bottom
        ax.bar_label(values, fmt=format, fontproperties=FONT_TEXT)
        ax.grid(False, axis='y')  # remover grids horizontais
        ax = set_chart_xticks(xvalues=yvals, yvalues=xvalues, ax=ax, percentage=percentage, xleftQ=False)
    if show_plot: show() #savefig("Gráficos/histogram_season_frequency.png") #savefig("Gráficos/Horizontal_bar_chart_season_frequency.png")
    return ax




def plot_multi_line_chart(xvalues: list | dict | Index, yvalues: dict[str, Series | dict] | list[Series], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", percentage: bool = False, show_stdev: bool = False, xleftQ: bool = True, yleftQ: bool = False, show_plot: bool = True) -> Axes:
    # Melhorar este gráfico para receber entradas dos yvalues semelhantes às do plot_multi_bar_chart (dict...)
    if show_plot: figure(figsize=(HEIGHT * 5, HEIGHT))
    
    if ax is None: ax = gca()
    
    # Dataframes / Series
    if isinstance(xvalues, Index) and isinstance(yvalues, list):
        xvalues = xvalues.to_list()
        ys = {}
        for e in yvalues:
            if isinstance(e, Series): ys[e.name] = e
        yvalues = ys
    
    # Dicionários
    elif isinstance(xvalues, list | dict) and isinstance(yvalues, dict):
        if isinstance(xvalues, dict):
            xvalues = list(xvalues.values())
        if isinstance(yvalues, dict):
            ys = {}
            for e in yvalues:
                if isinstance(yvalues[e], dict): ys[e] = list(yvalues[e].values())
            yvalues = ys
    
    #nmax = max([len(yvalues[ys]) for ys in yvalues]); #ymax = max([x for e in yvalues for x in yvalues[e]]); #ymin = min([x for e in yvalues for x in yvalues[e]]) #print(nmax, ymin, ymax, yvals)
    yvals = np.linspace(min([x for e in yvalues for x in yvalues[e] if not math.isnan(x)]), max([x for e in yvalues for x in yvalues[e] if not math.isnan(x)]), len(xvalues))
    
    
    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel)
    ax = set_chart_xticks(xvalues, yvals, ax=ax, percentage=percentage, xleftQ=xleftQ, yleftQ=yleftQ)
    
    legend: list = []
    for name, y in yvalues.items(): 
        ax.plot(y.index, y, marker='.'); legend.append(name) #ax.plot(xvalues, y, marker='.')
        if show_stdev:
            stdev: float = round(std(y), 3); y_bottom: list[float] = [(yi - stdev) for yi in y]; y_top: list[float] = [(yi + stdev) for yi in y]
            ax.fill_between(xvalues, y_bottom, y_top, alpha=0.2) #color=FILL_COLOR
    ax.legend(legend, fontsize="xx-small")
    
    if show_plot: show() #savefig("Gráficos/multiline_chart_Phosphate_Orthophosphate.png")
    
    return ax
def plot_multi_bar_chart(xvalues: list | Index, yvalues: dict[str, dict] | list[Series], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", stacked: bool = False, percentage: bool = False, yleftQ: bool = False, show_plot: bool = True) -> Axes | list[Axes]:
    if show_plot: figure(figsize=(HEIGHT * 2, HEIGHT))
    
    if ax is None: ax = gca()
    
    # Dataframes / Series
    if isinstance(xvalues, Index | list) and isinstance(yvalues, list): 
        if isinstance(xvalues, Index): xvalues = xvalues.to_list()
        ys = {} #ys: dict[str, Series] = {"river_depth": data["river_depth"].value_counts().sort_index(), "fluid_velocity": data["fluid_velocity"].value_counts().sort_index()}
        for e in yvalues:
            if isinstance(e, Series): ys[e.name] = e
        yvalues = ys
    
    # Dicionários
    elif isinstance(xvalues, list | dict) and isinstance(yvalues, dict):
        if isinstance(xvalues, dict):
            xvalues = list(xvalues.values())
        if isinstance(yvalues, dict):
            ys = {}
            for e in yvalues:
                if isinstance(yvalues[e], dict): ys[e] = list(yvalues[e].values())
            yvalues = ys
    
    #ymin = min([x for e in yvalues for x in yvalues[e]]); ymax = max([x for e in yvalues for x in yvalues[e]]); nmax = max([len(yvalues[ys]) for ys in yvalues]) #print(nmax, ymin, ymax, yvals)
    #yvals = np.linspace(min([x for e in yvalues for x in yvalues[e]]) if min([x for e in yvalues for x in yvalues[e]]) <= 0 else 0, max([x for e in yvalues for x in yvalues[e]]), max([len(yvalues[ys]) for ys in yvalues]))
    
    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel)
    #ax = set_chart_xticks([str(y) for y in yvals], yvals, ax=ax, percentage=percentage, yleftQ=yleftQ) #if percentage: ax.set_ylim(0.0, 1.0)
    
    bar_labels: list = list(yvalues.keys()) # CATEGORIAS -> EIXO YY
    
    if stacked == True:
        xvalues: list[str] # NOMES/ELEMENTOS -> EIXO XX
        # x = np.arange(len(xvalues))
        yvals = np.linspace(min([sum([vals[i] for vals in yvalues.values()]) for i in range(max([len(vals) for vals in yvalues.values()]))]) if min([sum([vals[i] for vals in yvalues.values()]) for i in range(max([len(vals) for vals in yvalues.values()]))]) <= 0 else 0, max([sum([vals[i] for vals in yvalues.values()]) for i in range(max([len(vals) for vals in yvalues.values()]))]), max([len(vals) for vals in yvalues.values()]))
        ax = set_chart_xticks([str(x) for x in xvalues], yvals, ax=ax, percentage=percentage, yleftQ=yleftQ) #if percentage: ax.set_ylim(0.0, 1.0)
        
        yvalues: dict[str, list] # d = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]} # df = pd.DataFrame(d, index=labels)
        
        r = np.zeros(len(xvalues))
        for cat in yvalues:
            heights = np.array(yvalues[cat])
            b = ax.bar(xvalues, heights, bottom=np.array(r), label=cat)
            ax.bar_label(b, labels=[f"{h:.0f}" if h > 0 else "" for h in heights], label_type="center", fontproperties=FONT_TEXT)
            # ax.bar_label(b, label_type="center", fmt=format, fontproperties=FONT_TEXT) # format = "%.2f" if percentage else "%.0f"
            r += heights #r += np.array(cat_vals)
    
    else:
        yvals = np.linspace(min([x for e in yvalues for x in yvalues[e]]) if min([x for e in yvalues for x in yvalues[e]]) <= 0 else 0, max([x for e in yvalues for x in yvalues[e]]), max([len(yvalues[ys]) for ys in yvalues]))
        ax = set_chart_xticks([str(y) for y in yvals], yvals, ax=ax, percentage=percentage, yleftQ=yleftQ) #if percentage: ax.set_ylim(0.0, 1.0)
        n = len(bar_labels)
        bar_width: float = 0.8 / len(bar_labels)
        index: ndarray = arange(len(xvalues)) # This is the location for each bar
        ax.set_xticks(index, labels=xvalues) #ax.set_xticks( index + (bar_width * len(bar_labels)) / 2, labels=xvalues)
        for i in range(len(bar_labels)):
            offset = (i - (n - 1)/2) * bar_width
            values: BarContainer = ax.bar(index + offset, yvalues[bar_labels[i]], width=bar_width, label=bar_labels[i]) #values: BarContainer = ax.bar(index + i * bar_width, yvalues[bar_labels[i]], width=bar_width, label=bar_labels[i])
            format = "%.2f" if percentage else "%.0f"
            ax.bar_label(values, fmt=format, fontproperties=FONT_TEXT)
    
    ax.legend(fontsize="xx-small")
    if show_plot: show() #savefig("Gráficos/multibar_chart_river_depth_fluid_velocity.png")
    return ax


def plot_bar_charts(data: dict[str, dict | Series] | DataFrame, vars: list[str]):
    # plot_bar_charts é o nome correto da função; para ser "plot_multi_bar_chart" é necessário fornecer combinações de variáveis por cada multi_bar_chart (Ver exemplo da função "plot_outliers_count")
    # Esta função dantes estava para os histogramas de variáveis não numéricas (Por causa do 'counts')
    # Agora se for para fazer a frequência, o counts tem de ser realizado antes de se chamar a função para ser recebido como entrada
    fig: Figure
    axs: ndarray
    rows, cols = define_grid(len(vars))
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False)
    i, j = 0, 0
    for n in range(rows*cols):
        if n < len(vars):
            if isinstance(data[vars[n]], Series): plot_bar_chart(data[vars[n]].index, data[vars[n]], ax=axs[i, j], title=f"Frequency for {vars[n]}", xlabel=vars[n], ylabel="frequency", show_plot=False)
            else: plot_bar_chart(list(data[vars[n]].keys()), list(data[vars[n]].values()), ax=axs[i, j], title=f"Frequency for {vars[n]}", xlabel=vars[n], ylabel="frequency", show_plot=False)
        else: axs[i, j].scatter([],[]); axs[i, j].set_xticks([]); axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False); 
        i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
    show() #savefig("Gráficos/multi_bar_charts.png")
def plot_line_charts(data: dict[str, dict | Series] | DataFrame, vars: list[str] = [], nr_cols: int = 1, show_stdev: bool = False): #, xleftQ: bool = True
    # plot_line_charts é o nome correto da função; para ser "plot_multi_line_charts" é necessário fornecer combinações de variáveis por cada multi_line_chart
    l_vars = get_variable_types(data)["numeric"] if vars == [] else vars; vars = l_vars
    fig: Figure
    axs: ndarray
    rows, cols = define_grid(len(vars), 1)
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 5, rows * HEIGHT), squeeze=False)
    i, j = 0, 0
    for n in range(rows*cols):
        if n < len(vars):
            if isinstance(data[vars[n]], Series): plot_line_chart(data[vars[n]].index, data[vars[n]], ax=axs[i, j], title=f"{vars[n]}", xlabel=data[vars[n]].index.name, ylabel=f"{data[vars[n]].name} values", show_stdev=show_stdev, show_plot=False)
            elif isinstance(data[vars[n]], dict): plot_line_chart(list(data[vars[n]].keys()), list(data[vars[n]].values()), ax=axs[i, j], title=f"{vars[n]}", xlabel=data[vars[n]].index.name, ylabel=f"{data[vars[n]].name} values", show_stdev=show_stdev, show_plot=False)
        else: axs[i, j].scatter([],[]); axs[i, j].set_xticks([]); axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False)
        i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
    show() #savefig("Gráficos/multi_line_charts.png")

def plot_scatter_chart(var1: list | Series | dict[str, dict], var2: list | Series | dict[str, dict], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", xleftQ: bool = False, yleftQ: bool = False, show_plot: bool = True) -> Axes:
    # IGNORAR : Meter o "plot_scatter_chart" a receber o mesmo input que o multi_scatter_chart (data, var1, var2) -> Para isso é necessário criar uma nova função ou alterar as entradas do gráfico
    if show_plot: figure() #figure(figsize=(HEIGHT, HEIGHT))
    if ax is None: ax = gca()
    # Dataframes / Series
    if isinstance(var1, Series) and isinstance(var2, Series):
        var1_name = var1.name; xlabel = var1_name if xlabel == "" else xlabel
        var2_name = var2.name; ylabel = var2_name if ylabel == "" else ylabel
        var1 = var1.to_list(); var2 = var2.to_list() 
    # Dicionários
    elif isinstance(var1, dict) and isinstance(var2, dict):
        var1_name = list(var1.keys())[0]; xlabel = var1_name if xlabel == "" else xlabel
        var2_name = list(var2.keys())[0]; ylabel = var2_name if ylabel == "" else ylabel
        var1 = list(var1[var1_name].values()); var2 = list(var2[var2_name].values())
    if title == "": title += var1_name + " x " + var2_name
    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel) #(corr={round(data[[var1,var2]].corr().abs()[var1][var2],3)})
    ax = set_chart_xticks(var1, var2, ax=ax, xleftQ=xleftQ, yleftQ=yleftQ)
    ax.scatter(var1, var2)
    if show_plot: show() #savefig(f"Gráficos/Scatterplot_{xlabel}_{ylabel}.png")
    return ax
def plot_multi_scatter_chart(data: DataFrame | dict[str, dict], var1: str, var2: str, var3: str = "", ax: Axes = None, xleftQ: bool = False, yleftQ: bool = False, show_plot: bool = True) -> Axes:
    if show_plot: figure()
    if ax is None: ax = gca()
    # Dicionários
    if isinstance(data, dict):
        ds = {} #ds = {key: {i: data[key][i] for i in data[key]} for key in data if key in [var1, var2, var3]}
        for var in [var1, var2, var3]:
            ds[var] = {}
            for i in data[var]:
                ds[var][i] = data[var][i]
        data: DataFrame = DataFrame(ds, columns = [var1, var2, var3])
    title: str = f"{var1} x {var2}" #(corr={round(data[[var1,var2]].corr().abs()[var1][var2],3)})
    if var3 != "":
        title += f" per {var3}"
        if is_any_real_numeric_dtype(data[var3]) and not is_integer_dtype(data[var3]):
            chart: PathCollection = ax.scatter(data[var1], data[var2], c=data[var3].to_list())
            cbar: Colorbar = gcf().colorbar(chart)
            cbar.outline.set_visible(False)  # type: ignore
            cbar.set_label(var3, loc="top")
        else:
            values: list = data[var3].unique().tolist()
            values.sort()
            for i in range(len(values)):
                subset: DataFrame = data[data[var3] == values[i]]
                ax.scatter(subset[var1], subset[var2], color=ACTIVE_COLORS[i], label=values[i]) #, s=1) # s=1 for very small point size
                # Linear Regression trendline
                # df = data[[var2,var1]].dropna(); df.sort_values(by=var2, ascending=True, inplace=True)
                # X = df[var2].values.reshape(-1,1); y = df[var1].values
                # model = LinearRegression(); model.fit(X,y); y_pred = model.predict(X) #from sklearn.linear_model import LinearRegression
                # ax.plot([X[0],X[-1]], [y_pred[0],y_pred[-1]], color='grey', linewidth=1) #, label = "Regression line"
            ax.legend(fontsize="xx-small")
    else: ax.scatter(data[var1], data[var2], color=FILL_COLOR)
    ax = set_chart_labels(ax=ax, title=title, xlabel=var1, ylabel=var2)
    ax = set_chart_xticks(data[var1].to_list(), data[var2].to_list(), ax=ax, xleftQ=xleftQ, yleftQ=yleftQ)
    if show_plot: show() #savefig("Gráficos/multi_scatters_chart_Phosphate_Orthophosphate_pH.png"); savefig("Gráficos/multi_scatters_chart_Phosphate_Orthophosphate_season.png")
    return ax
def plot_scatter_charts(data: DataFrame, vars: list[str] = [], show_all: bool = False): 
    # sparsity_study
    # Esta função não precisa de receber a lista de variáveis como entrada (o que é vantajoso)
    variables_types: dict[str, list] = get_variable_types(data)
    numeric: list[str] = variables_types["numeric"] #+ get_variable_types(data)["binary"] # Binárias/Simbólicas só se estiverem encoded
    l_vars: list[str] = [var for var in vars if var in numeric] if [var for var in vars if var in numeric] != [] else numeric
    vars = l_vars
    if vars != []:
        fig: Figure
        axs: ndarray
        if show_all:
            fig, axs = subplots(len(vars), len(vars), figsize=(len(vars) * HEIGHT, len(vars) * HEIGHT), squeeze=False) #dpi=300
            for i in range(len(vars)):
                for j in range(len(vars)):
                    plot_scatter_chart(data[vars[i]], data[vars[j]], title=f"{vars[i]} x {vars[j]}", xlabel=vars[i], ylabel=vars[j], ax=axs[i, j], show_plot=False)
        else:
            n: int = len(vars) - 1
            fig, axs = subplots(n, n, figsize=(n * HEIGHT, n * HEIGHT), squeeze=False) #dpi=300
            for i in range(n):
                for j in range(1, n+1):
                    if j > i:
                        plot_scatter_chart(data[vars[i]], data[vars[j]], title=f"{vars[i]} x {vars[j]}", xlabel=vars[i], ylabel=vars[j], ax=axs[i, j-1], show_plot=False)
                    else: axs[i, j-1].scatter(x=[],y=[]); axs[i, j-1].set_xticks([]); axs[i, j-1].set_yticks([]); axs[i, j-1].spines['left'].set_visible(False); axs[i, j-1].spines['bottom'].set_visible(False)
        show() #savefig("Gráficos/multi_scatterplot_charts.png") #savefig(f"images/{file_tag}_sparsity_study.png")
    else: print("Sparsity class: there are no variables.")
def plot_multi_scatter_charts(data: DataFrame, vars: list[str] = [], target: str = "", show_all: bool = False):
    # sparsity_per_class_study
    # Esta função não precisa de receber a lista de variáveis como entrada (o que é vantajoso)
    variables_types: dict[str, list] = get_variable_types(data)
    numeric: list[str] = variables_types["numeric"] #+ get_variable_types(data)["binary"] # Binárias/Simbólicas só se estiverem encoded
    l_vars: list[str] = [var for var in vars if var in numeric] if [var for var in vars if var in numeric] != [] else numeric
    vars = l_vars
    fig: Figure
    axs: ndarray
    if vars != []:
        if target == "": plot_scatter_charts(data, vars, show_all=show_all)
        else:
            if show_all:
                fig, axs = subplots(len(vars), len(vars), figsize=(len(vars) * HEIGHT, len(vars) * HEIGHT), squeeze=False) #dpi=300
                for i in range(len(vars)):
                    for j in range(len(vars)):
                        plot_multi_scatter_chart(data, vars[i], vars[j], target, ax=axs[i, j], show_plot=False)
            else:
                n: int = len(vars) - 1
                fig, axs = subplots(n, n, figsize=(n * HEIGHT, n * HEIGHT), squeeze=False) #dpi=300
                for i in range(n):
                    for j in range(1, n+1):
                        if j > i:
                            plot_multi_scatter_chart(data, vars[i], vars[j], target, ax=axs[i, j-1], show_plot=False)
                        else: axs[i, j-1].scatter(x=[],y=[]); axs[i, j-1].set_xticks([]); axs[i, j-1].set_yticks([]); axs[i, j-1].spines['left'].set_visible(False); axs[i, j-1].spines['bottom'].set_visible(False)
            #fig.tight_layout(pad=0.1) # Tight layout for better spacing #savefig("scatter_matrix.png", dpi=300, bbox_inches="tight")
            show() #savefig("Gráficos/multi_scatterplot_charts.png") #savefig(f"images/{file_tag}_sparsity_per_class_study.png") #target = "stroke"
    else: print("Sparsity per class: there are no variables.")


# Granularity
def plot_granularity_charts_by_property(data: DataFrame, property: str, vars: list[str]) -> ndarray:
    # Este gráfico não tem nada de mais do que qualquer plot_bar_chart além de relembrar que colocar vários gráficos de barras lado a lado de diferentes variáveis mas que estão associadas a uma mesma caraterística, ou propriedade, é sinónimo de estudo de granularidade de uma certa "propriedade" associada a essas variáveis.
    # property = "location"
    cols: int = len(vars)
    fig: Figure
    axs: ndarray
    fig, axs = subplots(1, cols, figsize=(cols * HEIGHT * 2, HEIGHT), squeeze=False)
    fig.suptitle(f"Granularity study for {property}")
    for i in range(cols):
        counts: Series[int] = data[vars[i]].value_counts()
        plot_bar_chart([str(i) for i in counts.index.to_list()], counts, ax=axs[0, i], title=vars[i], ylabel="N.º of records", percentage=False, show_plot=False)
        set_chart_xticks([str(i) for i in counts.index.to_list()], np.linspace(0, counts.max(), len([str(i) for i in counts.index.to_list()])), ax=axs[0, i], yleftQ=False)
    show() #savefig(f"images/{file_tag}_granularity_{prop}.png")
    return axs
def plot_granularity_charts_by_date(data: DataFrame):
    # Este gráfico é útil pois separa datas em diferentes periodos de agregação; contudo não os distingue, por exemplo por ano, etc.
    # Era interessante fazer esse tipo de agregação, contudo é muito mais complexo de se analisar (necessário criar muitas var dummys)
    def derive_date_variables(data: DataFrame, date_vars: list[str]) -> DataFrame:
        df: DataFrame = data.copy(deep=True)
        for date in date_vars:
            df[date + "_year"] = df[date].dt.year
            df[date + "_quarter"] = df[date].dt.quarter
            df[date + "_month"] = df[date].dt.month
            df[date + "_day"] = df[date].dt.day
        return df
    def analyse_date_granularity(data: DataFrame, var: str, levels: list[str]) -> ndarray:
        rows: int = len(levels)
        cols: int = 1
        fig: Figure
        axs: ndarray
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 2, rows * HEIGHT), squeeze=False)
        #fig.suptitle(f"Granularity study for {var}")
        for i in range(rows):
            counts: Series[int] = data[var + "_" + levels[i]].value_counts().sort_index()
            plot_bar_chart([str(i) for i in counts.index.to_list()], counts, ax=axs[i, 0], title=levels[i], xlabel=levels[i], ylabel="N.º of records", percentage=False, show_plot=False)
            set_chart_xticks([str(i) for i in counts.index.to_list()], np.linspace(0, counts.max(), len([str(i) for i in counts.index.to_list()])), ax=axs[i, 0], yleftQ=False)
        show() #savefig(f"images/{file_tag}_granularity_{v_date}.png")
        return axs
    
    variables_types: dict[str, list] = get_variable_types(data)
    data_ext: DataFrame = derive_date_variables(data, variables_types["date"])
    for v_date in variables_types["date"]:
        analyse_date_granularity(data_ext, v_date, ["year", "quarter", "month", "day"])
        
        years = sorted(data_ext["date_year"].unique())
        quarters = sorted(data_ext["date_quarter"].unique()) #list(range(1, 4+1))
        months = sorted(data_ext["date_month"].unique()) #list(range(1, 12+1))
        days = sorted(data_ext["date_day"].unique()) #list(range(1, 12+1))
        
        d = {"date_year": years, "date_quarter": quarters, "date_month": months} #"date_day": days
        combs = [("date_year", "date_quarter"), ("date_year", "date_month")] #("date_month", "date_day")
        
        rows = len(combs)
        cols = 2
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 2, rows * HEIGHT), squeeze=False)
        #fig.suptitle(f"Granularity study for {var}")
        for n, u in enumerate(combs):
            i, j = u[0], u[1]
            counts = (data_ext.groupby([i, j]).size().reset_index(name="n_records"))
            full_df = (pd.DataFrame(index=pd.MultiIndex.from_product([d[i], d[j]], names=[i, j])).reset_index()) #full_index = pd.MultiIndex.from_product([d[i], d[j]], names=[i, j])
            counts_full = (full_df.merge(counts, on=[i, j], how="left").fillna({"n_records": 0}))
            plot_multi_bar_chart(d[j], [Series(counts_full[counts_full[i] == k]["n_records"], name=k) for k in d[i]], ax=axs[n, 0], title=f"{i} by {j}", xlabel=j, ylabel="N.º of Records", show_plot=False)
            plot_multi_bar_chart(d[i], [Series(counts_full[counts_full[j] == k]["n_records"], name=k) for k in d[j]], ax=axs[n, 1], title=f"{j} by {i}", xlabel=i, ylabel="N.º of Records", show_plot=False)
        show()


# BOXPLOTS # Meter opção de apresentar o show_summary nos single boxplots
def plot_boxplots(data: DataFrame, show_all: bool = True):
    # BOXPLOTS
    def plot_global_boxplot(data: DataFrame, numeric: list[str], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = ""):
        figure(figsize=(HEIGHT * 2, HEIGHT))
        if ax == None: ax = gca()
        xvalues = [var for var in numeric]; yvalues = {var: data[var].dropna().values for var in numeric}; yvals = np.linspace(min([x for e in yvalues for x in yvalues[e]]), max([x for e in yvalues for x in yvalues[e]]), len(xvalues))
        ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel); ax = set_chart_xticks(xvalues, yvals, ax=ax)
        ax.boxplot([yvalues[var] for var in yvalues.keys()], labels=xvalues) #data[numeric].boxplot(rot=0)#, grid=True, medianprops=dict(color="orange", linewidth=2)) #patch_artist=True, boxprops=dict(facecolor="skyblue", color="darkblue"), medianprops=dict(color="orange", linewidth=2), whiskerprops=dict(color="darkblue", linewidth=1.5), capprops=dict(color="darkblue", linewidth=1.5), flierprops=dict(markerfacecolor="red", markeredgecolor="darkred", markersize=5)
        show() #savefig(f"images/{file_tag}_global_boxplot.png")
    def plot_single_boxplots(data: DataFrame, numeric: list[str]):
        rows: int
        cols: int
        rows, cols = define_grid(len(numeric))
        fig: Figure
        axs: ndarray
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False) #dpi=300
        i, j = 0, 0
        #fig.suptitle("Single Boxplots per variable")
        for n in range(rows*cols):
            if n < len(numeric):
                axs[i, j].set_title("Boxplot for %s" % numeric[n])
                axs[i, j].boxplot(data[numeric[n]].dropna().values) #, medianprops=dict(color="orange", linewidth=2) )
                set_chart_xticks(xvalues=[numeric[n] for x in list(data[numeric[n]].dropna().values)], yvalues=list(data[numeric[n]].dropna().values), ax=axs[i, j])
                axs[i, j].set_xticks([])
                
            else: axs[i, j].boxplot([]); axs[i, j].set_xticks([]);  axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False)
            i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
        show() #savefig(f"images/{file_tag}_single_boxplots.png")
    variable_types: dict[str, list] = get_variable_types(data)
    numeric: list[str] = variable_types["numeric"]
    if numeric != []:
        plot_global_boxplot(data, numeric, title="Boxplot of Variables", xlabel="Variables", ylabel="Values")
        if show_all: plot_single_boxplots(data, numeric)
    else: print("There are no numeric variables.")
def plot_date_granularity_boxplots(data: DataFrame, grans: list[str] = [], show_summary: bool = True): #, target: str
    # Data Distribution # Like for tabular data, one of the perspectives of analysis to consider is the distribution of data, in particular the centrality, trends and distribution of the variable. But be aware that the different aggregations may show different distributions.# Before proceeding let's create the weekly aggregation. For doing it, we just need to invoke the time_series_aggregation_by function defined before, but now using the sum instead of the mean as the aggregation function, in order to not introduce any error. Remember that this is possible only when the variable keeps its semantic untouched, as is the case for consumptions.# Compare the results obtained with sum and mean: note the difference of scale for the consumptions and the smoother transitions between periods.# Meter funções em conjunto com os boxplots e Histograms -> Recebem todas as variáveis e não apenas uma # 5-Number Summary # The simplest way to analyze our variable's distribution is through the 5-number summary, and visualize it through boxplots.
    grans: list[str] = ["H", "D", "W", "M", "Q", "Y"] #"S", "M", 
    grans_names: dict[str] = {g: ["Hour", "Day", "Week", "Month", "Quarter", "Year"][i] for i,g in enumerate(grans)} #"Second","Minute",
    vars: list[str] = list(data.columns)
    rows: int = len(grans)
    cols: int = len(vars) * 2 if show_summary else len(vars)
    l_cols: list[int] = list(range(0, cols, 2)) if show_summary else  list(range(cols))
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False)
    for k, j in enumerate(l_cols):
        for i, g in enumerate(grans):
            ss_gran: Series = series_aggregation_by_date(data[vars[k]], gran_level=g, agg_func=sum)
            set_chart_labels(axs[i, j], title=f"{vars[k]} : {grans_names[g]}"); 
            axs[i, j].boxplot(ss_gran); 
            set_chart_xticks(xvalues=[vars[k] for x in list(ss_gran.values)], yvalues=list(ss_gran.dropna().values), ax=axs[i, j])
            axs[i, j].set_xticks([])
            if show_summary: axs[i, j+1].grid(False); axs[i, j+1].set_axis_off(); axs[i, j+1].text(0.3, 0.5, str(ss_gran.describe()), fontsize="medium", ha="center", va="center") #, transform=axs[i, j+1].transAxes # axs[i, j+1].text(0, 0, str(ss_gran.describe()), fontsize="medium")
    show() #savefig(f"images/{file_tag}_boxplots_date_granularity.png")
def plot_multi_boxplots(datas: list[DataFrame] | dict[str, DataFrame]):
    # Função faz aparecerem boxplots globais por linha no mesmo gráfico
    # Now we can see the result of the transformed data with a single boxplot.
    def plot_global_boxplot(data: DataFrame, numeric: list[str], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", show_plot = True):
        #numeric: list = get_variable_types(data)["numeric"] # Caso nem todas as variáveis estejam como númericas
        if show_plot: figure(figsize=(HEIGHT * 2, HEIGHT))
        if ax == None: ax = gca()
        xvalues = [var for var in numeric]; yvalues = {var: data[var].dropna().values for var in numeric}; yvals = np.linspace(min([x for e in yvalues for x in yvalues[e]]), max([x for e in yvalues for x in yvalues[e]]), len(xvalues))
        ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel, ylabel=ylabel); ax = set_chart_xticks(xvalues, yvals, ax=ax) #ax.set_title(f"Boxplot of {data.name}")
        ax.boxplot([yvalues[var] for var in yvalues.keys()], labels=xvalues) #data[numeric].boxplot(ax=ax, rot=0) #, grid=True, medianprops=dict(color="orange", linewidth=2)) #patch_artist=True, boxprops=dict(facecolor="skyblue", color="darkblue"), medianprops=dict(color="orange", linewidth=2), whiskerprops=dict(color="darkblue", linewidth=1.5), capprops=dict(color="darkblue", linewidth=1.5), flierprops=dict(markerfacecolor="red", markeredgecolor="darkred", markersize=5)
        if show_plot: show() #savefig(f"images/{file_tag}_global_boxplot.png")
    if isinstance(datas, list): 
        d = {}
        for df in datas: d[df.name] = df
        datas = d
    rows, cols = len(datas), 1
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 5, rows * HEIGHT), squeeze=False) # fig: Figure # axs: ndarray
    for i, name in enumerate(datas):
        numeric: list = get_variable_types(datas[name])["numeric"] # Caso nem todas as variáveis estejam como númericas
        plot_global_boxplot(datas[name], numeric, ax = axs[i, 0], title = f"Boxplot of {name}", show_plot = False)
    show() #savefig(f"images/{file_tag}_multi_boxplots.png") #savefig(f"images/{file_tag}_boxplot_Outliers_scaling.png")

def plot_outliers_count(data: DataFrame):
    def determine_outlier_thresholds_for_var(summary5: Series, threshold: int | float, std_based: bool = True) -> tuple[float, float]:
        #threshold = NR_STDEV or IQR_FACTOR #NR_STDEV: int = 2; IQR_FACTOR: float = 1.5
        top: float = 0
        bottom: float = 0
        if std_based:
            std: float = threshold * summary5["std"]
            top = summary5["mean"] + std
            bottom = summary5["mean"] - std
        else:
            iqr: float = threshold * (summary5["75%"] - summary5["25%"])
            top = summary5["75%"] + iqr
            bottom = summary5["25%"] - iqr
        return top, bottom
    def count_outliers(data: DataFrame, numeric: list[str], nrstdev: int, iqrfactor: float) -> dict:
        # nrstdev: int = NR_STDEV; iqrfactor: float = IQR_FACTOR # NR_STDEV: int = 2; IQR_FACTOR: float = 1.5
        outliers_iqr: list = []
        outliers_stdev: list = []
        summary5: DataFrame = data[numeric].describe()
        for var in numeric:
            top: float
            bottom: float
            top, bottom = determine_outlier_thresholds_for_var(summary5[var], threshold=nrstdev, std_based=True)
            outliers_stdev += [ data[data[var] > top].count()[var] + data[data[var] < bottom].count()[var] ]
            
            top, bottom = determine_outlier_thresholds_for_var( summary5[var], threshold=iqrfactor, std_based=False)
            outliers_iqr += [ data[data[var] > top].count()[var] + data[data[var] < bottom].count()[var] ]
        return {"iqr": outliers_iqr, "stdev": outliers_stdev}
    
    variable_types: dict[str, list] = get_variable_types(data)
    numeric: list[str] = variable_types["numeric"]
    
    if numeric != []:
        figure(figsize=(12, HEIGHT))
        # Standard Outliers
        std_outliers: dict[str, int] = count_outliers(data, numeric, nrstdev=2, iqrfactor=1.5) #NR_STDEV: int = 2; IQR_FACTOR: float = 1.5
        #plot_multi_bar_chart(numeric, [Series(std_outliers['iqr'], index=numeric, name='iqr=2'), Series(std_outliers['stdev'], index=numeric, name='stdev=1.5')], title="N.º of Standard outliers per variable (nrstdev=2, iqrfactor=1.5)", xlabel="Variables", ylabel="Nr outliers", percentage=False)
        #savefig(f"images/{file_tag}_outliers_standard.png")
        
        # Non-Standard Outliers -> Por a função a receber os parametros nrstdev=a, iqrfactor=b como parametros de entrada
        nstd_outliers: dict[str, int] = count_outliers(data, numeric, nrstdev=4, iqrfactor=4.5) #nrstdev=3, iqrfactor=3.5
        
        d = {"Standard outliers": [Series(std_outliers['iqr'], index=numeric, name='iqr=2'), Series(std_outliers['stdev'], index=numeric, name='stdev=1.5')], "Non-Standard outliers": [Series(nstd_outliers['iqr'], index=numeric, name='iqr=4'), Series(nstd_outliers['stdev'], index=numeric, name='stdev=4.5')]}
        
        rows, cols = len(d), 1
        fig, axs = subplots(rows, cols, figsize=(cols * 12, rows * HEIGHT), squeeze=False) #dpi=300
        #fig.suptitle("Nr of standard and non-standard outliers per variable")
        i, j = 0, 0
        for i, k in enumerate(d.keys()):
            plot_multi_bar_chart(numeric, d[k], ax=axs[i,j], title=f"Nr of {k} per variable ({d[k][0].name}, {d[k][1].name})", ylabel="N.º of outliers", percentage=False, show_plot=False)
        show() #savefig(f"images/{file_tag}_outliers_standard_and_non_standard.png")
    else: print("There are no numeric variables.")

# HISTOGRAMS
def plot_histograms(data: DataFrame):
    # HISTOGRAMS
    variable_types: dict[str, list] = get_variable_types(data)
    symbolic: list[str] = variable_types["symbolic"] + variable_types["binary"] # Non numeric variables
    numeric: list[str] = variable_types["numeric"]
    
    if symbolic != []: # Histograms for Symbolic 
        plot_bar_charts({v: data[v].value_counts() for v in symbolic}, symbolic) #title="Histogram for %s" % symbolic[n], xlabel=symbolic[n], ylabel="N.º of records" #savefig(f"images/{file_tag}_histograms_symbolic.png")
    else: print("There are no symbolic variables.")
    
    if numeric != []: # Histograms for Numeric
        # Histograms
        def plot_histograms_numeric(data: DataFrame, numeric: list[str]):
            rows, cols = define_grid(len(numeric))
            fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False) #dpi=300
            i, j = 0, 0
            for n in range(rows*cols):
                if n < len(numeric):
                    set_chart_labels(axs[i, j], title=f"Histogram for {numeric[n]}", xlabel=numeric[n], ylabel="N.º of records")
                    yvalues, xvalues, _ = axs[i, j].hist(data[numeric[n]].dropna().values, bins="auto") #, align="mid", rwidth=0.8)
                    set_chart_xticks(np.linspace(xvalues[0], xvalues[-1], len(yvalues)), np.linspace(0, max(yvalues), len(yvalues)), ax=axs[i, j], yleftQ=False)
                else: axs[i, j].hist([]); axs[i, j].set_xticks([]); axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False)
                i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
            show() #savefig(f"images/{file_tag}_histograms_numeric.png")
        
        # Histograms with distribuitions
        def plot_histograms_numeric_with_distributions(data: DataFrame, numeric: list[str]):
            def histogram_with_distributions(series: Series, var: str, ax: Axes):
                # Tentar tirar esta função daqui
                def plot_multi_line_chart_dist(xvalues: list | DataFrame, yvalues: list[DataFrame], ax: Axes = None, title: str = "", xlabel: str = "", ylabel: str = "", percentage: bool = False, show_plot: bool = True) -> Axes: # type: ignore
                    if show_plot: figure(figsize=(12, 4))
                    if ax is None: ax = gca()
                    
                    if not(isinstance(xvalues, list)): xvalues = xvalues.to_list()
                    ys = {}
                    for e in yvalues:
                        if not(isinstance(e, list)): ys[e.name] = e
                    yvalues = ys
                    
                    ax = set_chart_labels(ax=ax, title=title, xlabel=xlabel) #, ylabel=ylabel); ax = set_chart_xticks(xvalues, ax=ax, percentage=percentage)
                    
                    legend: list = []
                    for name, y in yvalues.items(): ax.plot(xvalues, y); legend.append(name)
                    ax.legend(legend, fontsize="xx-small")
                    
                    if show_plot: show()
                    return ax
                def compute_known_distributions(xvalues: list) -> dict:
                    distributions = dict()
                    mean, sigma = norm.fit(xvalues); distributions["Normal(%.1f,%.2f)" % (mean, sigma)] = norm.pdf(xvalues, mean, sigma) # Gaussian
                    loc, scale = expon.fit(xvalues); distributions["Exp(%.2f)" % (1 / scale)] = expon.pdf(xvalues, loc, scale) # Exponential
                    sigma, loc, scale = lognorm.fit(xvalues); distributions["LogNor(%.1f,%.2f)" % (log(scale), sigma)] = lognorm.pdf(xvalues, sigma, loc, scale) # LogNorm
                    return distributions
                
                if ax == None: ax = gca()
                values: list = series.sort_values().to_list()
                yvalues, xvalues, _ = ax.hist(values, bins="auto", density=True) #, n_bins=20, align="mid", rwidth=0.8)
                distributions: dict = compute_known_distributions(values)
                plot_multi_line_chart_dist(values, [Series(distributions[x], name=x) for x in distributions], ax=ax, title="Best fit for %s" % var, xlabel=numeric[n], show_plot=False) # Best distribution fit
                ax = set_chart_xticks(np.linspace(xvalues[0], xvalues[-1], len(yvalues)), np.linspace(0, max(yvalues), len(yvalues)), ax=ax, yleftQ=False) # Colocar xticks e yticks do histograma no Axe do multi_line_chart
        
            rows, cols = define_grid(len(numeric))
            fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False) #dpi=300
            i, j = 0, 0
            for n in range(rows*cols):
                if n < len(numeric):
                    histogram_with_distributions(data[numeric[n]].dropna(), numeric[n], axs[i, j])
                else: axs[i, j].hist([]); axs[i, j].set_xticks([]); axs[i, j].set_yticks([]); axs[i, j].spines['left'].set_visible(False); axs[i, j].spines['bottom'].set_visible(False)
                i, j = (i + 1, 0) if (n + 1) % cols == 0 else (i, j + 1)
            show() #savefig(f"images/{file_tag}_histograms_numeric_with_distribution.png")
        
        plot_histograms_numeric(data, numeric)
        plot_histograms_numeric_with_distributions(data, numeric)
        
    else: print("There are no numeric variables.")
def plot_date_granularity_histograms(data: DataFrame, grans: list[str] = [], grans_names: dict[str] = [], show_summary: bool = True): #, target: str
    # Data Distribution # Like for tabular data, one of the perspectives of analysis to consider is the distribution of data, in particular the centrality, trends and distribution of the variable. But be aware that the different aggregations may show different distributions.# Before proceeding let's create the weekly aggregation. For doing it, we just need to invoke the time_series_aggregation_by function defined before, but now using the sum instead of the mean as the aggregation function, in order to not introduce any error. Remember that this is possible only when the variable keeps its semantic untouched, as is the case for consumptions.# Compare the results obtained with sum and mean: note the difference of scale for the consumptions and the smoother transitions between periods.# Meter funções em conjunto com os boxplots e Histograms -> Recebem todas as variáveis e não apenas uma # Variables Distribution # But from these charts is not possible to completely understand the variable distribution at the different granularities. In order to do so, we use histograms, as for multivariate data.# Now, let's look at the distribution for the aggregations considered before: hours, days, weeks, months and quarters.
    grans: list[str] = ["H", "D", "W", "M", "Q", "Y"] #"S", "M", 
    grans_names: dict[str] = {g: ["Hour", "Day", "Week", "Month", "Quarter", "Year"][i] for i,g in enumerate(grans)} #"Second","Minute",
    vars: list[str] = list(data.columns)
    rows: int = len(grans)
    cols: int = len(vars) * 2 if show_summary else len(vars)
    l_cols: list[int] = list(range(0, cols, 2)) if show_summary else  list(range(cols))
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT, rows * HEIGHT), squeeze=False)
    #fig.suptitle(f"{file_tag} {target}")
    for k, j in enumerate(l_cols):
        for i, g in enumerate(grans):
            ss_gran: Series = series_aggregation_by_date(data[vars[k]], gran_level=g, agg_func=sum)
            set_chart_labels(axs[i, j], title=f"Histogram for {vars[k]} : {grans_names[g]}", xlabel=vars[k], ylabel="N.º of records") #title=f"Histogram for {grans_names[grans[n]]}ly granularity"
            yvalues, xvalues, _ = axs[i, j].hist(ss_gran.values) #yvalues, xvalues, _ = axs[i, j].hist(ss_gran.dropna().values, bins="auto") #, align="mid", rwidth=0.8)
            set_chart_xticks(np.linspace(xvalues[0], xvalues[-1], len(yvalues)), np.linspace(0, max(yvalues), len(yvalues)), ax=axs[i, j], yleftQ=False)
            if show_summary: axs[i, j+1].grid(False); axs[i, j+1].set_axis_off(); axs[i, j+1].text(0.3, 0.5, str(ss_gran.describe()), fontsize="medium", ha="center", va="center") #, transform=axs[i, j+1].transAxes # axs[i, j+1].text(0, 0, str(ss_gran.describe()), fontsize="medium")
    show() #savefig(f"images/{file_tag}_histograms_date_granularity.png")


# CORRELATION
def plot_correlation(data: DataFrame, vars: list[str] = []):
    # CORRELATION
    variables_types: dict[str, list] = get_variable_types(data)
    numeric: list[str] = variables_types["numeric"] # Dá para colocar binárias também (depois de encoded)
    l_vars: list[str] = [var for var in vars if var in numeric] if [var for var in vars if var in numeric] != [] else numeric
    corr_mtx: DataFrame = data[l_vars].corr().abs()
    figure(figsize=(HEIGHT * 2, HEIGHT * 2)) #figure(figsize=(len(numeric) * 0.2, len(numeric) * 0.2), dpi=300) #HEIGHT = 0.5 #0.8  #Height of each cell in the heatmap. Adjust height per variable to keep the heatmap manageable 
    heatmap(abs(corr_mtx), xticklabels=l_vars, yticklabels=l_vars, annot=True, fmt=".2f", cmap="Blues", vmin=0, vmax=1, annot_kws={"size": 8})
    show() #savefig(f"images/{file_tag}_correlation_analysis.png")





def plot_multi_line_charts(data: DataFrame, vars: list[str] = [], show_per_rows: bool = False):
    # Fazer igual para o plot_bar_charts (se der, porque provavelmente atinar com as entradas do gráfico não é fácil)
    l_vars = get_variable_types(data)["numeric"] if [var for var in vars] == [] else vars
    vars = l_vars
    if show_per_rows:
        # "plot_multi_line_charts_per_rows" : Gráficos por linha para cada combinação de duas variáveis
        for var1 in vars:
            n: int = len(vars) - 1 #if len(vars) > 1 else len(vars)
            fig, axs = subplots(n, 1, figsize=(1 * HEIGHT * 3, n * HEIGHT), squeeze=False) #dpi=300
            l_vars = [var for var in vars if var != var1]
            for i, var2 in enumerate(l_vars):
                plot_multi_line_chart(data.index, [data[var1], data[var2]], ax=axs[i,0], title=f"{var1} x {var2}", xlabel=data.index.name, ylabel="Values", xleftQ=True, show_plot=False)
        show() #savefig("Gráficos/multi_scatterplot_charts.png") #savefig(f"images/{file_tag}_sparsity_study.png")
    else:
        # Todos os gráficos na forma matricial (sem repetir variáveis) -> Semelhante ao "plot_scatter_charts"
        n: int = len(vars) - 1
        fig, axs = subplots(n, n, figsize=(n * HEIGHT * 3, n * HEIGHT), squeeze=False) #dpi=300
        for i in range(1, n+1):
            for j in range(n):
                if j < i:
                    plot_multi_line_chart(data.index, [data[vars[i]], data[vars[j]]], ax=axs[i-1, j], title=f"{vars[i]} x {vars[j]}", xlabel=data.index.name, ylabel="Values", xleftQ=True, show_plot=False)
                else: axs[i-1, j].scatter(x=[], y=[]); axs[i-1, j].set_xticks([]); axs[i-1, j].set_yticks([]); axs[i-1, j].spines['left'].set_visible(False); axs[i-1, j].spines['bottom'].set_visible(False)
        show() #savefig("Gráficos/multi_scatterplot_charts.png") #savefig(f"images/{file_tag}_sparsity_study.png")

# LIXO # Não tem interesse esta função a não ser que fosse semelhante ao plot_multi_line_charts
# def plot_multi_bar_charts_per_rows(datasets: list[Series] | list[dict[str, int | float]]): #rows: int, columns: int
#     fig, axs = subplots(len(datasets), 1, figsize=(HEIGHT * 2, len(datasets) * HEIGHT))
#     for i, df in enumerate(datasets):
#         if not isinstance(df, dict):
#             plot_bar_chart(df.index, df, ax=axs[i], title=f"{df.name}", xlabel=df.index.name, ylabel=df.name, yleftQ=False, show_plot=False)
#         # elif isinstance(df, dict):
#         #     plot_bar_chart(list(df.keys()), list(df.values()), ax=axs[i], yleftQ=False, show_plot=False)
#     show() #savefig("Gráficos/multi_bar_charts.png")





# PLOTS
    
plot_pie_chart(data_algae["season"].value_counts().index, data_algae["season"].value_counts().values, percentage=True, title="Frequency")
plot_bar_chart(data[target].value_counts().index, data[target].value_counts(), title=f"Target distribution (target={target})") #savefig(f"images/{file_tag}_class_distribution.png") #target = "stroke"; target = "CLASS"
plot_bar_chart(data_algae["season"].value_counts().index, data_algae["season"].value_counts(), title="season distribution", xlabel="season", ylabel="frequency") #plot_horizontal_bar_chart(data_algae["season"].value_counts().index, data_algae["season"].value_counts(), title="season distribution", xlabel="frequency", ylabel="season")
#plot_bar_chart(["N.º Records", "N.º Variables"], list(data_cancer.shape), title="Nr of records vs nr variables") #values: dict[str, int] = {"N.º Records": data_cancer.shape[0], "N.º Variables": data.data_cancer[1]}
#plot_bar_chart(list(n_vt.keys()), list(n_vt.values()), title="N.º of variables per type", xlabel="variables types", ylabel="Nº. of variables")
#plot_bar_chart(list(mv.keys()), list(mv.values()), title="N.º of missing values per variable", xlabel="variables", ylabel="Nº. of missing values")
#plot_multi_bar_chart( list(mv.keys()), [Series(list(nmv.values()), name="Non Missing"), Series(list(mv.values()), name="Missing")], title="Frequency for some variables", ylabel="frequency")


# Histograms de symbolic/binary
plot_bar_charts({v: data_algae[v].value_counts() for v in ["fluid_velocity", "river_depth", "season"]}, ["fluid_velocity", "river_depth", "season"])
plot_bar_charts({v: data_cancer[v].value_counts() for v in ['hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status', 'stroke']}, ['hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status', 'stroke'])
plot_multi_bar_chart(Series(data_algae["river_depth"].value_counts().sort_index(), name="river_depth").index, [Series(data_algae["river_depth"].value_counts().sort_index(), name="river_depth"), Series(data_algae["fluid_velocity"].value_counts().sort_index(), name="fluid_velocity")], title="Frequency for some variables", ylabel="frequency")
plot_multi_bar_chart(Series(data_algae["river_depth"].value_counts().sort_index(), name="river_depth").index, [Series(data_algae["river_depth"].value_counts().sort_index(), name="river_depth"), Series(data_algae["fluid_velocity"].value_counts().sort_index(), name="fluid_velocity")], title="Frequency for some variables", ylabel="frequency", stacked=True)

plot_granularity_charts_by_date(data_algae)
plot_granularity_charts_by_property(data_gdindex, "location", ["Hemisphere", "Continent", "Country"]) #property = "location"


plot_line_chart(data_algae.index, data_algae["pH"], title="pH variation", xlabel=data_algae.index.name, ylabel="pH")
# plot_multi_line_chart(data_algae.index, [data_algae["Phosphate"], data_algae["Orthophosphate"]], title="Phosphate and Orthophosphate values", xlabel="date", ylabel="values")
plot_multi_line_chart(data_algae.index, [data_algae[var] for var in get_variable_types(data_algae)["numeric"]], title="Phosphate and Orthophosphate values", xlabel="date", ylabel="values")

plot_line_charts(data_algae, get_variable_types(data_algae)["numeric"], nr_cols = 1, show_stdev=True)
plot_line_charts({var: data_algae[var] for var in get_variable_types(data_algae)["numeric"]}, get_variable_types(data_algae)["numeric"], nr_cols = 1, show_stdev=True)
plot_line_charts(data_cancer, ["age", "bmi", "avg_glucose_level"], nr_cols=1, show_stdev=True)
plot_line_charts({var: data_cancer[var] for var in get_variable_types(data_cancer)["numeric"]}, get_variable_types(data_cancer)["numeric"], nr_cols=1, show_stdev=True)

plot_scatter_chart(data_algae["Phosphate"], data_algae["Orthophosphate"], title="", xlabel="", ylabel="")
plot_multi_scatter_chart(data_algae, "Phosphate", "Orthophosphate", "season")
plot_multi_scatter_chart(data_algae, "Phosphate", "Orthophosphate", "pH")

plot_scatter_charts(data_algae, ["pH", "Oxygen", "Chloride", "Nitrates", "Ammonium", "Orthophosphate", "Phosphate", "Chlorophyll"], show_all=False)
plot_multi_scatter_charts(data_algae, ["pH", "Oxygen", "Chloride", "Nitrates", "Ammonium", "Orthophosphate", "Phosphate", "Chlorophyll"], 'river_depth', show_all=False)
plot_multi_scatter_charts(data_algae, [], 'river_depth')

plot_multi_scatter_charts(data_cancer, [], 'stroke')

plot_multi_boxplots([data_algae, data_cancer, data_gdindex])
plot_multi_boxplots({"original": data_cancer, "zscore": df_zscore, "minmax": df_minmax})

#profilling([data_cancer, data_algae])



