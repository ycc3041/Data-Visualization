import pandas as pd
from bokeh.layouts import row, widgetbox, gridplot
from bokeh.models import Select, ColumnDataSource
from bokeh.palettes import Blues8 
from bokeh.plotting import curdoc, figure

df = pd.read_csv('factbook.csv')


columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
continuous = [x for x in columns if x not in discrete]


# widgets
x0 = Select(title='X0-Axis', value='GDP per capita', options=continuous)
x1 = Select(title='X1-Axis', value='Birth rate', options=continuous)
y0 = Select(title='Y0-Axis', value='Investment', options=continuous)
y1 = Select(title='Y1-Axis', value='Public debt', options=continuous)
size = Select(title='Size', value='None', options=['None'] + continuous)
color = Select(title='Color', value='None', options=['None'] + continuous)


source = ColumnDataSource(data=dict(x0=[], x1=[], y0=[], y1=[], color=[], size=[]))


kw00 = kw01 = kw10 = kw11 = dict()


p00 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw00)
p10 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw10)
p01 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw01)
p11 = figure(plot_height=300, plot_width=400, tools='box_select,pan,box_zoom,reset', **kw11)


p00.circle(x='x0', y='y0', source=source, color='color', size='size', line_color='white', alpha=0.6, selection_color='#E74C3C', selection_fill_alpha=0.8, selection_line_color='white')
p10.circle(x='x1', y='y0', source=source, color='color', size='size', line_color='white', alpha=0.6, selection_color='#E74C3C', selection_fill_alpha=0.8, selection_line_color='white')
p01.circle(x='x0', y='y1', source=source, color='color', size='size', line_color='white', alpha=0.6, selection_color='#E74C3C', selection_fill_alpha=0.8, selection_line_color='white')
p11.circle(x='x1', y='y1', source=source, color='color', size='size', line_color='white', alpha=0.6, selection_color='#E74C3C', selection_fill_alpha=0.8, selection_line_color='white')


SIZES = list(range(8, 40, 3)) # possible sizes 
COLORS = Blues8  # possible colors 
N_SIZES = len(SIZES) 
N_COLORS = len(COLORS) 


def update():
    x0_title = x0.value.title()
    x1_title = x1.value.title()
    y0_title = y0.value.title()
    y1_title = y1.value.title()
    
    p00.xaxis.axis_label = x0_title
    p10.xaxis.axis_label = x1_title
    p00.yaxis.axis_label = y0_title
    p01.yaxis.axis_label = y1_title

    if color.value != 'None':
        groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
        c = [COLORS[xx] for xx in groups.codes]
    else:
        c = ["#31AADE"] * 149
    
    if size.value != 'None':
        groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
        sz = [SIZES[xx] for xx in groups.codes] 
    else:
        sz = [15] * 149

    df2 = pd.DataFrame({'color':c, 'size':sz})
    
    source.data = dict(
        x0=df[x0.value],
        x1=df[x1.value],
        y0=df[y0.value],
        y1=df[y1.value],
        color=df2['color'],
        size=df2['size'],
        )
    

control_list = [x0, x1, y0, y1, size, color]
for control in control_list:
    control.on_change('value', lambda attr, old,new: update())


widgets = widgetbox([x0, x1, y0, y1, color, size], width=80)
grid = gridplot([[p01, p11],[p00, p10]])
layout = row(grid, widgets)


update()


curdoc().add_root(layout)
curdoc().title = "Brushing"