import pandas as pd
from bokeh.layouts import row, column, widgetbox
from bokeh.models import Select, Slider, ColumnDataSource
from bokeh.palettes import Blues8
from bokeh.plotting import curdoc, figure


df = pd.read_csv('factbook.csv')


columns = sorted(df.columns)
discrete = [x for x in columns if df[x].dtype == object]
continuous = [x for x in columns if x not in discrete]


# widgets
x = Select(title='X-Axis', value='GDP per capita', options=continuous)
y = Select(title='Y-Axis', value='Life expectancy at birth', options=continuous)
color = Select(title='Color', value='None', options=['None'] + continuous)
size = Select(title='Size', value='None', options=['None'] + continuous)
slider = Slider(title='Radius Scale', value=3, start=1, end=5, step=0.5)


source = ColumnDataSource(data=dict(x=[], y=[], color=[], size=[]))

kw = dict()

p = figure(plot_height=400, plot_width=600, tools='box_select, pan, box_zoom, reset', **kw)
p.circle(x='x', y='y', source=source, color='color', size='size', line_color="white", alpha=0.6)


SIZES = list(range(6, 22, 3)) # [6, 9, 12, 15, 18, 21]; possible sizes 
COLORS = Blues8  # possible colors 
N_SIZES = len(SIZES) 
N_COLORS = len(COLORS) 


def update():
    x_title = x.value.title() # current x title
    y_title = y.value.title() # current y title
    p.xaxis.axis_label = x_title
    p.yaxis.axis_label = y_title

    p.title.text = "%s vs. %s" % (x.value.title(), y.value.title())
    
    if color.value != 'None':
        groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
        c = [COLORS[xx] for xx in groups.codes]
    else:
        c = ["#31AADE"] * 149
    
    scale = slider.value
    if size.value != 'None':
        groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
        sz = [SIZES[xx] for xx in groups.codes] 
        sz = [scale *x for x in sz]
    else:
        sz = [12] * 149

    df2 = pd.DataFrame({'color':c, 'size':sz})
    
    source.data = dict(
            x=df[x.value],
            y=df[y.value],
            color=df2['color'],
            size=df2['size'],
            )
    
control_list = [x, y, color, size, slider]
for control in control_list:
    control.on_change('value', lambda attr, old,new: update())


controls = widgetbox([x, y, color, size], width=80)
controls_ = column(controls, slider)
layout = row(p, controls_)


update()


curdoc().add_root(layout)
curdoc().title = "Widgets"