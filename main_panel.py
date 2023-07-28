import os

import panel as pn
import yaml

from helpers import *

pn.extension(sizing_mode="stretch_width")

with open('parameters/TY2022.yaml', 'r', encoding='utf-8') as f:
    sq_params = yaml.safe_load(f)

with open('parameters/TY2022_reform.yaml', 'r', encoding='utf-8') as f:
    reform_params = yaml.safe_load(f)
    
title = pn.Column(
    pn.Row(
        pn.pane.Markdown('# Income Explorer Prototype', width=600),
        pn.pane.Markdown('*Best viewed full screen*', align = ('end', 'end'))),
    # add a horizontal line
    pn.layout.Divider()).servable(target='title')


# all the controls are in a widget box ------------------------------------------------

example_param_file_select = pn.widgets.FileSelector(directory='parameters', name='Example parameters')
example_param_file_download = pn.widgets.FileDownload(
    file = 'parameters/TY2022.yaml', filename = 'TY2022.yaml', button_type = 'primary')

def update_example_file_download(event):
    example_param_file_download.file = example_param_file_select.value[0]
    example_param_file_download.filename = os.path.basename(example_param_file_select.value[0])

example_param_file_select.param.watch(update_example_file_download, 'value')

sq_param_input = pn.widgets.FileInput(name = 'SQ')
reform_param_input = pn.widgets.FileInput(name = 'Reform')

hrly_wage_input = pn.widgets.FloatInput(name = 'Hourly Wage', value = 20)
max_hours_input = pn.widgets.IntInput(name = 'Max Hours', value = 50)

accom_cost_input = pn.widgets.FloatInput(name = 'Weekly Accom.\n Cost', value = 450)
as_area_input = pn.widgets.Select(name = 'AS Area', options = [1, 2, 3, 4], value = 1)
accom_type_input = pn.widgets.Select(
    name = 'Accom.', options = ['Rent', 'Mortgage'], value = 'Rent')


go_button = pn.widgets.Button(
    name='Calculate !', button_type='success', width=200, align=('center', 'center'))

pn.WidgetBox(
    pn.pane.Markdown('### Policy parameters'),
    pn.Row(pn.pane.Markdown('Status Quo:', width = 60),sq_param_input), 
    pn.Row(pn.pane.Markdown("Reform:", width = 60), reform_param_input),
    pn.pane.Markdown('For help creating your own parameter file, see the "Example Parameters" tab'),
    pn.pane.Markdown('### Family specification'),
    pn.Row(hrly_wage_input, max_hours_input),
    pn.Row(accom_cost_input, as_area_input), accom_type_input,
    go_button, width = 300).servable(target='widget_box')

# ------------------------------------------------------------------------------------

# Params tab

params_tab = pn.WidgetBox(
    pn.pane.Markdown(
        'To help create your own parameter file, choose one of the examples below to download, and edit '
        'it in a text editor. Only the first file selected will be downloaded.'),
        example_param_file_select, example_param_file_download, 
        name = 'Example Parameters', width = 600, height = 500
)


# Initial plots and table
figs, table_data = fig_table_data(
    sq_params, reform_params, hrly_wage_input.value, max_hours_input.value, 
    accom_cost_input.value, as_area_input.value, accom_type_input.value)

# The I couldn't get a Plotly pane to update properly when the data changed.
# using html works, but it is probably slower
rate_panes = {var: pn.pane.HTML(figs[var].to_html(), width=1000) for var in RATE_VARS}

emtr_tab = pn.Column(
    pn.pane.Markdown('## Net Income \n\n Not done yet'),
    pn.pane.Markdown('## Effective Marginal Tax Rate'), rate_panes['emtr'],
    pn.pane.Markdown('## Replacement Rate'), rate_panes['replacement_rate'],
    pn.pane.Markdown('## Participation Tax Rate'), rate_panes['participation_tax_rate'],
    width = 1000, height=2000, name = 'EMTR')

composition_tab = pn.Column(
    pn.pane.Markdown('## Status Quo \n\n Not done yet'),
    pn.pane.Markdown('## Reform \n\n Not done yet'),
    width = 1000, height=2000, name = 'Income Composition')

# Instructions tab
with open('instructions.md', 'r') as f:
    instructions = pn.pane.Markdown(
        f.read(), name = "Instructions", width=600)

# Definitions tab
with open('definitions.md', 'r') as f:
    definitions = pn.pane.Markdown(
        f.read(), name = "Definitions", width=800, height=600)

pn.Tabs(
    params_tab, emtr_tab, composition_tab, instructions, definitions, 
    width = 1500, height=2000, active=1).servable(target='tabs')

#-------------------------------------------------------------------------------------

def update(event):
    """Update the plot and table when the Go button is clicked"""
    if sq_param_input.value:
        # decode the bytes to a string, and then decode the yaml
        sq_params = yaml.safe_load(sq_param_input.value.decode('utf-8'))
    if reform_param_input.value:
        reform_params = yaml.safe_load(reform_param_input.value.decode('utf-8'))

    figs, table_data = fig_table_data(
        sq_params, reform_params, hrly_wage_input.value, max_hours_input.value, 
        accom_cost_input.value, as_area_input.value, accom_type_input.value)
    for key in figs:
        rate_panes[key].object=figs[key].to_html()


go_button.on_click(update)
