from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
from wh import workhours
from datetime import datetime
from flask import send_file
from icsmodule import ics

#import pandas as pd

#df = pd.DataFrame()

app = Dash(__name__)


#Server route to allow file downloads
@app.server.route('/download_file/')
def download_file():
    return send_file('MyCalendar/time.ics', as_attachment=True)


app.layout = html.Div(
    [
        html.H1(children='Working Hour Scheduler',
                style={
                    'color': 'black',
                    'textAlign': 'center',
                    'background-color': 'transparent'
                }),
        html.Div(children=[
            dcc.Input(id="dateinput", type="date"),
            dcc.Input(id="timeinput", type="time", step=0),
            dcc.Input(id="timeinput2", type="time", step=0),
            html.Button('Add to schedule', id='add_to_schedule', n_clicks=0)
        ],
                 style={
                     'display': 'flex',
                     'justify-content': 'center'
                 }),
        html.Br(),
        dash_table.DataTable(
            id='adding-rows-table',
            columns=[{
                'name': 'Date',
                'id': 'date',
                'deletable': False,
                'renamable': False
            }, {
                'name': 'Start time',
                'id': 'start_time',
                'type': 'text',
                'deletable': False,
                'renamable': False
            }, {
                'name': 'End time',
                'id': 'end_time',
                'deletable': False,
                'renamable': False
            }, {
                'name': 'Work hours',
                'id': 'work_hours',
                'deletable': False,
                'renamable': False
            }, {
                'name': 'Paid hours',
                'id': 'paid_hours',
                'deletable': False,
                'renamable': False
            }],
            data=[],  #starts with empty data
            editable=True,
            row_deletable=True,
            style_cell={
                'fontSize': 15,
                'font-family': 'sans-serif',
                'textAlign': 'center'  #to center align the text in the cell
            },
            style_table={
                'padding-left': '0%',
                'padding-right': '0%',
                #'marginLeft': '5%',
                'margin': 'auto',  #to keep table center aligned
                'width': '70%'
            },
            style_header={
                #'backgroundColor': 'white',
                'backgroundColor': 'rgb(0,0,0)',
                #'fontWeight': 'bold',
                'color': 'white'
            }),

        #html.Button('Add Row', id='editing-rows-button', n_clicks=0),
        html.Div(id='dlbutton', style={'text-align': 'center'}),
    ],
    style={'font-family': 'sans-serif'})


@app.callback(
    Output('adding-rows-table', 'data'),
    #Input('editing-rows-button', 'n_clicks'),  #add row button
    State('adding-rows-table', 'data'),  #
    State('adding-rows-table', 'columns'),
    State("dateinput", "value"),
    State("timeinput", "value"),
    State("timeinput2", "value"),
    Input('add_to_schedule', 'n_clicks'),  #input button
)
def add_row(rows, columns, dvalue, tvalue1, tvalue2, n_clicks):
    if n_clicks > 0:
        #inputs are split and stored in list
        #date = dvalue.split('-')  #date
        st = tvalue1.split(':')  #start time
        et = tvalue2.split(':')  #end time
        print(tvalue1, tvalue2)
        print(st, et)

        t1 = datetime(year=2022,
                      month=8,
                      day=1,
                      hour=int(st[0]),
                      minute=int(st[1]))
        t2 = datetime(year=2022,
                      month=8,
                      day=1,
                      hour=int(et[0]),
                      minute=int(et[1]))
        t3 = t2 - t1
        wh = t3.seconds / 3600  #seconds attribute of datetime function is taken & converted to hours

        #the fn is called and the return values are copied in respective variables
        msg, ph = workhours(wh)
        rows.append({
            'date': dvalue,
            'start_time': tvalue1,
            'end_time': tvalue2,
            'work_hours': wh,
            'paid_hours': ph
        })

    ics(rows)  #send list to fn

    return rows


#when at least one workdate is added, the download link will appear
@app.callback(Output("dlbutton", "children"), State("dateinput", "value"),
              State("timeinput", "value"), State("timeinput2", "value"),
              Input('add_to_schedule', 'n_clicks'))
def dl_button(dvalue, tvalue1, tvalue2, n_clicks):
    if n_clicks > 0 and dvalue is not None:
        DL = (html.P([html.A("Download ICS file", href="/download_file/")])
              )  #Link for downloading file
    return DL


if __name__ == '__main__':
    app.run_server(debug=True, port=os.getenv("PORT", default=5000))
#app.run_server(host='0.0.0.0', port=8081, debug=False)

#debug=False just to allow time input in Dash HTML app
