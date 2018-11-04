import pandas as pd
from bokeh.layouts import row, column, widgetbox, gridplot
from bokeh.models import Select, ColumnDataSource, HoverTool
from bokeh.palettes import Blues8
from bokeh.plotting import curdoc, figure

df = pd.read_csv('factbook.csv')

SIZES = list(range(6, 22, 3)) # [6, 9, 12, 15, 18, 21]; Possible sizes 
COLORS = Blues8 # Possible colors 
N_SIZES = len(SIZES) # 6
N_COLORS = len(COLORS) # 5


columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
continuous = [x for x in columns if x not in discrete]

def update(attr, old, new):
    new_fig = create_figure()
#    col_left = column(new_fig[2], new_fig[0])
#    col_right = column(new_fig[3], new_fig[1])
#    main_row = row(col_left, col_right)
    grid = gridplot([[new_fig[2], new_fig[3]], [new_fig[0], new_fig[1]]])
    layout.children[0] = grid
    

x0 = Select(title='X0-Axis', value='GDP', options=columns)
x0.on_change('value', update)

x1 = Select(title='X1-Axis', value='GDP per capita', options=columns)
x1.on_change('value', update)

y0 = Select(title='Y0-Axis', value='Birth rate', options=columns)
y0.on_change('value', update)

y1 = Select(title='Y1-Axis', value='Life expectancy at birth', options=columns)
y1.on_change('value', update)

size = Select(title='Size', value='None', options=['None'] + continuous)
size.on_change('value', update)

color = Select(title='Color', value='None', options=['None'] + continuous)
color.on_change('value', update)


#xs0 = df[x0.value].values
#xs1 = df[x1.value].values
#ys0 = df[y0.value].values
#ys1 = df[y1.value].values
#
#source = ColumnDataSource(data=dict(xs0=xs0, xs1=xs1, ys0=ys0, ys1=ys1))

def create_figure():
    
    xs0 = df[x0.value].values
    xs1 = df[x1.value].values
    ys0 = df[y0.value].values
    ys1 = df[y1.value].values
    
#    source = ColumnDataSource(data=dict(xs0=xs0, xs1=xs1, ys0=ys0, ys1=ys1))
    source = ColumnDataSource(data=df)
    
    kw00 = kw10 = kw01 = kw11 = dict()
    
    if x0.value in discrete:
        kw00['x_range'] = sorted(set(xs0))
        kw01['x_range'] = sorted(set(xs0))
    
    if x1.value in discrete:
        kw10['x_range'] = sorted(set(xs1))
        kw11['x_range'] = sorted(set(xs1))
        
    if y0.value in discrete:
        kw00['y_range'] = sorted(set(ys0))
        kw10['y_range'] = sorted(set(ys0))
    
    if y1.value in discrete:
        kw01['y_range'] = sorted(set(ys1))
        kw11['y_range'] = sorted(set(ys1))
    
#    kw00['title'] = "%s vs %s" % (x0_title, y0_title)
#    kw10['title'] = "%s vs %s" % (x1_title, y0_title)
#    kw01['title'] = "%s vs %s" % (x0_title, y1_title)
#    kw11['title'] = "%s vs %s" % (x1_title, y1_title)    

    
    p00 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw00)
    p10 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw10)
    p01 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw01)
    p11 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw11)
    

    p00.xaxis.axis_label = x0.value
    p10.xaxis.axis_label = x1.value
    p00.yaxis.axis_label = y0.value
    p01.yaxis.axis_label = y1.value
    if x0.value in discrete:
        p00.xaxis.major_label_orientation = pd.np.pi / 4

    sz = 9 # default size
    if size.value != 'None':
        if len(set(df[size.value])) > N_SIZES:
            groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
        else:
            groups = pd.Categorical(df[size.value])
        sz = [SIZES[xx] for xx in groups.codes]


    c = "#31AADE" # default color
    if color.value != 'None':
        if len(set(df[color.value])) > N_SIZES:
            groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
        else:
            groups = pd.Categorical(df[color.value])
        c = [COLORS[xx] for xx in groups.codes]

    p00.circle(x=str(x0.value), y=str(y0.value), source=source, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, selection_color="#B03A2E")
    p10.circle(x=str(x1.value), y=str(y0.value), source=source, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, selection_color="#B03A2E")
    p01.circle(x=str(x0.value), y=str(y1.value), source=source, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, selection_color="#B03A2E")
    p11.circle(x=str(x1.value), y=str(y1.value), source=source, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5, selection_color="#B03A2E")
    
#    p00.circle(x=xs0, y=ys0, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)
#    p10.circle(x=xs1, y=ys0, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)
#    p01.circle(x=xs0, y=ys1, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)
#    p11.circle(x=xs1, y=ys1, color=c, size=sz, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)
    
    for plot in [p00, p10, p01, p11]:        
        hover = HoverTool()

        hover.tooltips = [
                ('Country', '@Country'),
                ('Area', '@Area'),
                ('Birth Rate', '@{Birth rate}'),
                ('Current Account Balance', '@{Current account balance}'), 
                ('Death Rate', '@{Death rate}'),
                ('Electricity Consumption', '@{Electricity consumption}'),
                ('Electricity Production', '@{Electricity production}'),
                ('Exports', '@Exports'),
                ('GDP', '@GDP'),
                ('GDP Per Capita', '@{GDP per capita}'),
                 ('GDP Real Growth Rate', '@{GDP real growth rate}'),
                 ('Highways', '@Highways'),
                 ('Imports','@Imports'),
                 ('Industrial production growth rate', '@{Industrial production growth rate}'),
                 ('Infant mortality rate', '@{Infant mortality rate}'),
                 ('Inflation rate', '@{Inflation rate }'),
                 ('Internet users','@{Internet users}'),
                 ('Investment', '@Investment'),
                 ('Labor force', '@{Labor force}'),
                 ('Life expectancy at birth','@{Life expectancy at birth}'),
                 ('Military expenditures', '@{Military expenditures}'),
                 ('Natural gas consumption', '@{Natural gas consumption}'),
                 ('Oil consumption', '@{Oil consumption}'),
                 ('Population', '@Population'),
                 ('Public debt', '@{Public debt}'),
                 ('Railways','@Railways'),
                 ('Reserves of foreign exchange & gold', '@{Reserves of foreign exchange & gold}'),
                 ('Total fertility rate', '@{Total fertility rate}'),
                 ('Unemployment rate', '@{Unemployment rate}')
                 ]
        plot.add_tools(hover)
    
    return p00, p10, p01, p11



#controls = widgetbox([x0, x1, y0, y1, color, size], width=80)

widgets = widgetbox([x0, x1, y0, y1, color, size], width=80)
#col_left = column(create_figure()[2], create_figure()[0])
#col_right = column(create_figure()[3], create_figure()[1])
#main_row = row(col_left, col_right)
new_fig = create_figure()
grid = gridplot([[new_fig[2], new_fig[3]], [new_fig[0], new_fig[1]]])
layout = row(grid, widgets)

# layout = column(controls, create_figure()) ##### 2*2

curdoc().add_root(layout)
curdoc().title = "Crossfilter"

#a = dict(k1=1, k2=2)
#print(a['k1'])

#print(x0.value.title())



