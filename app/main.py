import plotly.express as px
from dash import Dash, html, dcc, dash_table
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table as dt
import sys
sys.path.append("..")
from ClassData.DataClassAPI import GetDataFile
import pandas as pd
from data.twitter import  get_tweets
from time import sleep
import json




arrets_ligne  = GetDataFile(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\data\api\emplacement-des-gares-idf.csv").csv_file(sep=";")
arrets_ligne["lat"] = pd.to_numeric( arrets_ligne["Geo Point"].str.split(',', expand=True)[0], downcast="float")
arrets_ligne["lon"] = pd.to_numeric( arrets_ligne["Geo Point"].str.split(',', expand=True)[1], downcast="float")

table = get_tweets("RER_A")
df_tweets = pd.DataFrame(get_tweets("RER_A")).set_index('Date')

app = Dash(__name__)
########################################################################################################################
# UPDATE
########################################################################################################################
df_hist = px.data.tips()
fig_hist = px.histogram(df_hist, x="day", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))
app_colors = {
    'background': '#343332',
    'text': '#FFFFFF'
}


# fig_hist.update_layout(
#     plot_bgcolor=app_colors['background'],
#     paper_bgcolor=app_colors['background'],
#     font_color=app_colors['text'],
#     margin={"r":0,"t":0,"l":0}
# )
# fig_hist.update_layout(
#     plot_bgcolor=app_colors['background'],
#     paper_bgcolor=app_colors['background'],
#     font_color=app_colors['text'],
#     margin={"r":0,"t":0,"l":0}
# )




########################################################################################################################
# APP
########################################################################################################################

app.title = "Stations de recharge Paris"

app.layout = html.Div(style={'background-color': app_colors['background'],
                             'paper_bgcolor' :app_colors['background'],
                             },
                      className= "content",
                      children=[
                          html.Div(
                              className='all_compenents',
                              children=[

                                  #Left components : H1 dropdown
                                  html.Div(
                                      className="div_left_components",
                                      children=[
                                          #Elements in left component
                                          html.Div(
                                              className='elt_in_left_components',
                                              children=[
                                                  html.H1(
                                                      "Trafic en temps réel du réseau ferroviaire en IDF",
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': app_colors['text'],
                                                          'margin': '0%'
                                                      }
                                                  ),
                                                  html.Div(
                                                      className='DD_div',
                                                      children=[
                                                          #html.Label(['Arrondissement'], style={'font-weight':'bold','font-size': '1rem', 'color':'white'}),
                                                          dcc.Dropdown( #Dropdown dept
                                                              id='DD_name_ligne_input',
                                                              options=
                                                              [dict(label=x, value=x)
                                                               for x in arrets_ligne["ligne"].unique()],
                                                              placeholder="Selectionnez un arrondissement",
                                                              style = {
                                                                  # 'color': 'white',
                                                                  'backgroundColor': 'transparent',
                                                              }

                                                          ),
                                                          dcc.Dropdown( #Dropdown adresse
                                                              id='DD_nom_input',
                                                              options=
                                                              [dict(label=x, value=x)
                                                               for x in arrets_ligne["nom"].unique()],
                                                              placeholder="Selectionnez une adresse",
                                                              style = {
                                                                  'backgroundColor': 'transparent',

                                                              }


                                                          ),
                                                      ]
                                                  ),

                                                  dt.DataTable(
                                                      id='output_datatable',

                                                      #[df_tweets.to_dict('records'), [{'Date': i, 'User': i,'User': i}, for i in indf_tweets ],#[{'Date': i, 'User': i,'User': i}]
                                                      columns=[{'name': 'Date', 'id': 'Date'},
                                                               #{'name': 'User', 'id': 'User'},
                                                               {'name': 'Tweet', 'id': 'Tweet'}],


                                                      page_size=6,
                                                      style_as_list_view=True,
                                                      style_data={
                                                          #'width':'50px',
                                                          'overflow':'hidden',
                                                          'textOverflow' : 'ellipsis',
                                                          'color': 'white',
                                                          'backgroundColor': 'transparent',
                                                          'whiteSpace': 'normal',
                                                          'width': 'auto',

                                                      },
                                                      style_table={
                                                          'overflowX': 'auto'
                                                      },
                                                      style_cell={
                                                          'overflow': 'hidden',
                                                          'textOverflow': 'ellipsis',
                                                          'textAlign': 'left',

                                                      },
                                                      style_header={
                                                          'backgroundColor': 'rgb(50, 50, 50)',
                                                          'color': 'white',
                                                          'fontWeight': 'bold',
                                                          'border': '1px solid black'
                                                      },
                                                      style_cell_conditional=[
                                                          {'if': {'column_id': 'code_insee_commune'},
                                                           'width': '5%'}
                                                      ]

                                                  ),


                                              ]#end children

                                          )

                                      ]
                                  ),

                                  #Map hist
                                  html.Div(className='map_hist',
                                           children=[
                                               html.Div(

                                                   dcc.Graph(
                                                       className='map',
                                                       id="map_output",

                                                       #figure=fig_map

                                                   )
                                               ),
                                               html.Div(

                                                   dcc.Graph(
                                                       className='hist',
                                                       id="hist1_output",
                                                       figure=fig_hist

                                                   )


                                               ),
                                               html.Div(

                                                   dcc.Graph(
                                                       className='hist',
                                                       id='hist2_output',
                                                       figure=fig_hist

                                                   )


                                               )
                                           ]
                                           )


                              ])

                      ]#end children

                      )

########################################################################################################################
# CALLBACK
########################################################################################################################



@app.callback(
    Output('map_output', 'figure'),

    Input('DD_name_ligne_input',"value"),
    Input('DD_nom_input',"value")
)
def update_map_map(DD_name_ligne_input,DD_nom_input) :
    map_feltred = arrets_ligne.copy()

    # if  not DD_dept_input :
    #     raise PreventUpdate
    # else :
    if DD_name_ligne_input :
        map_feltred = map_feltred[map_feltred.ligne == DD_name_ligne_input]



    elif DD_nom_input:
        map_feltred = map_feltred[(map_feltred.nom==DD_nom_input)]


    ######################################## MAP ###############################################
    px.set_mapbox_access_token(open(r"\Users\ganza\OneDrive\Bureau\gitripo\twitter_kafka_elk_pipeline\app\mapbox_token.txt").read())
    fig = px.scatter_mapbox(map_feltred, lat='lat', lon='lon',
                            mapbox_style='carto-darkmatter',
                            hover_data=['ligne','nom'], color="ligne",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=12, zoom=11.2)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0,})

    fig.update_layout(coloraxis_showscale=False)
    #fig.update_traces(hovertemplate=None)map_feltred
    fig.update_layout(
        plot_bgcolor=app_colors['background'],
        paper_bgcolor=app_colors['background'],
        font_color=app_colors['text'],
        margin={"r":0,"t":0,"l":0,"b":0})

    return fig

@app.callback(

    Output('output_datatable', 'data'),
    Input('DD_name_ligne_input',"value")
)
# def update_map_map(DD_name_ligne_input) :
#     df_feltred = pd.DataFrame(get_tweets("RER_A"))
#
#     if   DD_name_ligne_input :
#     #
#     #     table_feltred = df_feltred[(df_feltred.ligne==DD_name_ligne_input) ]
#
#         print(type(df_feltred))
#
#         return df_feltred.to_dict('records')
def update_map_map(DD_name_ligne_input):
    df_feltred = pd.DataFrame(get_tweets("RER_A")).set_index('Date')
    if DD_name_ligne_input:
        data1 = df_feltred
        data1.to_csv("df_feltred.csv")
        data2 = pd.read_csv("df_feltred.csv", sep=",")

        #data2 = df_feltred.to_dict('records')


    # print(data[0]['Date'])
        # print(data[0]['User'])
        # print(data[0]['Tweet'])
        # data_json = json.dumps(data, default=str)
        # print(len(data2))
        return data2.to_dict('records')




app.config.suppress_callback_exceptions = True

#app.run_server(debug=True, use_reloader=True)
app.run_server(debug=False, use_reloader=True, port=8053)

