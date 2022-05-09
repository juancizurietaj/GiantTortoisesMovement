import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly_express as px
from dash import dcc, Input, Output, State, html, dash_table
import plotly.graph_objs as go
import numpy as np

# Data load
data_emma = pd.read_feather(
    r"C:\Users\juancarlos.izurieta\Documents\R projects\GiantTortoisesMovement\giant_tortoises_EMMA_v2.feather")
data_isabela = pd.read_feather(
    r"C:\Users\juancarlos.izurieta\Documents\R projects\GiantTortoisesMovement\giant_tortoises_ISABELA_v2.feather")
data_herbert = pd.read_feather(
    r"C:\Users\juancarlos.izurieta\Documents\R projects\GiantTortoisesMovement\giant_tortoises_HERBERT_v2.feather")

data_health = pd.read_csv(
    r"C:\Users\juancarlos.izurieta\Documents\R projects\GiantTortoisesMovement\health_bio_data.csv")

px.set_mapbox_access_token(
    "pk.eyJ1IjoianVhbmNpenVyaWV0YSIsImEiOiJja3d6NGlheWIwcm9wMm9ydXF1Zmp3aWI0In0.kncVhoBEkMHLhHRw3fig4g")

color_gradients = ["rgb(57, 73, 155)", "rgb(87, 72, 157)", "rgb(112, 70, 157)", "rgb(134, 68, 156)",
                   "rgb(155, 65, 151)", "rgb(174, 62, 146)", "rgb(191, 59, 138)", "rgb(206, 59, 129)",
                   "rgb(219, 61, 118)", "rgb(229, 66, 107)", "rgb(237, 74, 95)", "rgb(243, 84, 83)", "rgb(246, 96, 70)",
                   "rgb(246, 109, 56)", "rgb(244, 123, 41)"]

color_gradients_gray = ["rgb(240, 240, 240)", "rgb(235, 235, 235)", "rgb(230, 230, 230)", "rgb(225, 225, 225)", "rgb(220, 220, 220)",
                        "rgb(215, 215, 215)", "rgb(210, 210, 210)", "rgb(205, 205, 205)", "rgb(200, 200, 200)", "rgb(195, 195, 195)",
                        "rgb(190, 190, 190)", "rgb(185, 185, 185)"]

header = html.Div(
    [
        html.Img(src=r"./assets/de_logo.png",
                 width="130px",
                 style={'display': 'inline-block', "padding": "10px"}),
        html.H4("Giant Tortoises Movement, Biology & Health",
                style={'display': 'inline-block', "color": "white", 'marginLeft': 30, "bottom": 0})
    ], style={"background": "#333f54", 'display': 'inline-block', "width": "100%"}
)

footer = html.Div(
    [
        html.Div(
            [
                html.Img(src="assets/donor_logo.png",
                         height="60px",
                         style={"padding": "0px 15px", "display": "inline-block", "margin-top": "0px"}),
                html.P("Descripción del proyecto donde se enmarcan los datos, créditos a instituciones participantes.",
                       className="footer-grant")
            ]
        ),
        html.Div(
            [
                html.Img(src="assets/fcd_logo.png",
                         height="85px",
                         style={"padding": "0px 15px", "display": "inline-block", "margin-top": "0px"}),
                # html.P("©Fundación Charles Darwin", className="footer-fcd"),
                html.P("Creado por el Departamento de Tecnologías, Información, Investigación y Desarrollo (TIID)",
                       className="footer-tiid")
            ], style={"text-align": "right"}
        )
    ], style={"display": "flex", "justify-content": "space-between", "padding": ""}
)


def tab_creator(label_name, content):
    tab = dbc.Tab(content, label=label_name,
                  tab_style={'backgroundColor': '#e9ebef'},
                  active_label_style={'color': '#333f54', 'fontWeight': 'bold'},
                  label_style={'color': 'gray'})
    return tab


def create_download_cards(iconA, labelA, textA, buttonA, iconB, textB, labelB, buttonB, iconC, labelC, textC, buttonC):
    downloads = html.Div(
        [
            dbc.Card([html.Div(html.Img(src=iconA, height=50), className="downloads-card-item"),
                      html.Div(html.Label(labelA, className="labels"),
                               className="downloads-card-item"),
                      html.Div(html.P(textA),
                               className="downloads-card-item"),
                      html.Div(dbc.Button(buttonA, size="m"), className="downloads-card-item")],
                     body=True, className="downloads-card-container"),
            dbc.Card([html.Div(html.Img(src=iconB, height=50), className="downloads-card-item"),
                      html.Div(html.Label(labelB, className="labels"),
                               className="downloads-card-item"),
                      html.Div(html.P(textB),
                               className="downloads-card-item"),
                      html.Div(dbc.Button(buttonB, size="m"), className="downloads-card-item")],
                     body=True, className="downloads-card-container"),
            dbc.Card([html.Div(html.Img(src=iconC, height=50), className="downloads-card-item"),
                      html.Div(html.Label(labelC, className="labels"),
                               className="downloads-card-item"),
                      html.Div(html.P(textC),
                               className="downloads-card-item"),
                      html.Div(dbc.Button(buttonC, size="m"), className="downloads-card-item")],
                     body=True, className="downloads-card-container")
        ], className="downloads-container"
    )

    return downloads


def create_heat_map(df, lat_center, lon_center, animation_value, category_orders, zoom):
    fig = px.density_mapbox(df, lat='lat', lon='lon', radius=5, opacity=1,
                            center=dict(lat=lat_center, lon=lon_center),
                            mapbox_style="satellite", animation_frame=animation_value,
                            category_orders=category_orders,
                            zoom=zoom)
    fig.update_layout(margin=dict(t=1, l=1, r=1))

    return fig


# def create_dist_chart(df, time):
#     dfb = df.groupby([time])["distance"].mean()
#     fig = px.line(dfb)
#     return fig
#
#
# def create_elev_chart(df, time):
#     dfb = df.groupby([time])["altitude"].mean()
#     fig = px.line(dfb)
#     fig.update_traces(mode="markers+lines",
#                       hovertemplate=None,
#                       line=dict(color="rgb(57, 73, 155)"))
#     fig.update_layout(hovermode="x")
#     fig.update_layout(legend=dict(
#         orientation="h",
#         yanchor="bottom",
#         y=1.02,
#         xanchor="right",
#         x=1
#     ))
#     return fig

def line_charts_elevation(df, time_unit, metric):
    if time_unit == "year":
        df = df.groupby([time_unit])[metric].mean()
        fig = px.line(data_frame=df, x=df.index, y=df.values, height=350, labels={
                     "y": "Elevation",
                     "year": "year"
                 })
        fig.update_traces(mode="markers+lines",
                          hovertemplate=None,
                          line=dict(color="rgb(57, 73, 155)"))
        fig.update_layout(hovermode="x", xaxis=dict(tickformat='d'))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_layout(margin=dict(t=1, b=1, l=1, r=1))
    else:
        category_orders = {"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                                     "Nov", "Dec"]}
        df = df.groupby(["year", time_unit])[metric].mean().reset_index()
        df = df[df[metric] > 0]
        # print(df)
        fig = px.line(data_frame=df, x=df[time_unit], y=df[metric],
                      color=df["year"], category_orders=category_orders,
                      color_discrete_sequence=color_gradients_gray,
                      height=350)
        means = df.groupby([time_unit])[metric].mean().reset_index()
        fig.add_traces(go.Scatter(
            name='Average',
            x=means[time_unit],
            y=means[metric],
            mode='lines',
            line=dict(color="rgb(57, 73, 155)"),
        ))
        fig.update_traces(mode="markers+lines", hovertemplate=None)
        fig.update_layout(hovermode="x", xaxis=dict(tickformat='d'))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_layout(margin=dict(t=1, b=1, l=1, r=1))

    return fig


def line_charts_distance(df, time_unit, metric):
    if time_unit == "year":
        df = df.groupby([time_unit])[metric].sum()
        fig = px.line(data_frame=df, x=df.index, y=df.values, height=350, labels={"y": "Distance", "year": "year"}, hover_data={"distance": ':.1f'})
        fig.update_traces(mode="markers+lines",
                          hovertemplate=None,
                          line=dict(color="rgb(244, 123, 41)"))
        fig.update_layout(hovermode="x", xaxis=dict(tickformat='d'))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_layout(margin=dict(t=1, b=1, l=1, r=1))
    else:
        category_orders = {"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                                     "Nov", "Dec"]}
        df = df.groupby(["year", time_unit])[metric].sum().reset_index()
        df = df[df[metric] > 0]
        # print(df)
        fig = px.line(data_frame=df, x=df[time_unit], y=df[metric],
                      color=df["year"], category_orders=category_orders,
                      color_discrete_sequence=color_gradients_gray,
                      height=350)
        means = df.groupby([time_unit])[metric].mean().reset_index()
        fig.add_traces(go.Scatter(
            name='Average',
            x=means[time_unit],
            y=means[metric],
            mode='lines',
            line=dict(color="rgb(244, 123, 41)"),
        ))
        fig.update_traces(mode="markers+lines", hovertemplate=None)
        fig.update_layout(hovermode="x", xaxis=dict(tickformat='d'))
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_layout(margin=dict(t=1, b=1, l=1, r=1))

    return fig


# def create_continous_error_line_chart(df, time_column, values_column):
#     # df = df.groupby([time_column])[values_column].sum()
#     # print(means)
#     means = df.groupby([time_column])[values_column].mean()
#     maxs = df.groupby([time_column])[values_column].max()
#     mins = df.groupby([time_column])[values_column].min()
#     stds = df.groupby([time_column])[values_column].std()
#     fig = go.Figure([
#         go.Scatter(
#             name='Average',
#             x=means.index,
#             y=means.values,
#             mode='lines',
#             line=dict(color='rgb(31, 119, 180)'),
#         ),
#         go.Scatter(
#             name='Upper Bound',
#             x=means.index,
#             y=means.values + stds.values,
#             mode='lines',
#             marker=dict(color="#444"),
#             line=dict(width=0),
#             showlegend=False
#         ),
#         go.Scatter(
#             name='Lower Bound',
#             x=means.index,
#             y=mins.values,
#             marker=dict(color="#444"),
#             line=dict(width=0),
#             mode='lines',
#             fillcolor='rgba(68, 68, 68, 0.3)',
#             fill='tonexty',
#             showlegend=False
#         )
#     ])
#
#     return fig


def create_indicators_layout(df, time_unit, metric):
    if time_unit == "year":
        threshold_dp = 5000
    elif time_unit == "month":
        threshold_dp = 400
    elif time_unit == "week":
        threshold_dp = 90
    elif time_unit == "date":
        threshold_dp = 12

    # Grouping df (total distance traveled per unit of time)
    tot_dist = df.groupby([time_unit]).agg({metric: ["sum"], "timestamp": ["nunique"]}).reset_index(col_level=1)
    tot_dist.columns = [time_unit, "total distance", "data points"]
    tot_dist_complete = tot_dist[tot_dist["data points"] >= threshold_dp]
    print(tot_dist_complete)
    time_period_above_thrshld = len(tot_dist["data points"][tot_dist["data points"] >= threshold_dp])
    # Values for complete years
    ind_mean = tot_dist_complete["total distance"].mean()
    ind_median = tot_dist_complete["total distance"].median()
    ind_max = tot_dist_complete["total distance"].max()
    ind_min = tot_dist_complete["total distance"].min()
    ind_std = tot_dist_complete["total distance"].std()
    # Breakdown per time unit
    if time_unit == "year":
        bkdwn_tbl = tot_dist
    elif time_unit == "month":
        bkdwn_tbl = df.groupby(["year", "month"]).agg({metric: ["sum"], "timestamp": ["nunique"]}).reset_index(
            col_level=1)
        bkdwn_tbl.columns = ["year", "month", "total distance", "data points"]
        tot_dist_complete = bkdwn_tbl[bkdwn_tbl["data points"] >= threshold_dp]
        ind_mean = tot_dist_complete["total distance"].mean()
        ind_median = tot_dist_complete["total distance"].median()
        ind_max = tot_dist_complete["total distance"].max()
        ind_min = tot_dist_complete["total distance"].min()
        ind_std = tot_dist_complete["total distance"].std()
    elif time_unit == "week":
        bkdwn_tbl = df.groupby(["year", "week"]).agg({metric: ["sum"], "timestamp": ["nunique"]}).reset_index(
            col_level=1)
        bkdwn_tbl.columns = ["year", "week", "total distance", "data points"]
        tot_dist_complete = bkdwn_tbl[bkdwn_tbl["data points"] >= threshold_dp]
        ind_mean = tot_dist_complete["total distance"].mean()
        ind_median = tot_dist_complete["total distance"].median()
        ind_max = tot_dist_complete["total distance"].max()
        ind_min = tot_dist_complete["total distance"].min()
        ind_std = tot_dist_complete["total distance"].std()
    elif time_unit == "date":
        bkdwn_tbl = df.groupby(["year", "date"]).agg({metric: ["sum"], "timestamp": ["nunique"]}).reset_index(
            col_level=1)
        bkdwn_tbl.columns = ["year", "date", "total distance", "data points"]
        tot_dist_complete = bkdwn_tbl[bkdwn_tbl["data points"] >= threshold_dp]
        ind_mean = tot_dist_complete["total distance"].mean()
        ind_median = tot_dist_complete["total distance"].median()
        ind_max = tot_dist_complete["total distance"].max()
        ind_min = tot_dist_complete["total distance"].min()
        ind_std = tot_dist_complete["total distance"].std()

    time_period = len(df["year"].unique())

    labels = html.Div(
        [
            html.Div(html.Label("Average", className="indicator-labels"), className="indicator-element-container"),
            html.Div(html.Label("Median", className="indicator-labels"), className="indicator-element-container"),
            html.Div(html.Label("Max", className="indicator-labels"), className="indicator-element-container"),
            html.Div(html.Label("Min", className="indicator-labels"), className="indicator-element-container"),
            html.Div(html.Label("Std. Dev.", className="indicator-labels"), className="indicator-element-container"),
        ], style={"display": "flex"}
    )

    values = html.Div(
        [
            html.Div(html.P(str(round(ind_mean, 2)) + "m", className="values"),
                     className="indicator-element-container"),
            html.Div(html.P(str(round(ind_median, 2)) + "m", className="values"),
                     className="indicator-element-container"),
            html.Div(html.P(str(round(ind_max, 2)) + "m", className="values"), className="indicator-element-container"),
            html.Div(html.P(str(round(ind_min, 2)) + "m", className="values"), className="indicator-element-container"),
            html.Div(html.P(str(round(ind_std, 2)) + "m", className="values"), className="indicator-element-container"),
        ], style={"display": "flex"}
    )

    layout = html.Div([html.Div([
        html.Label("Total distance traveled per " + time_unit + " in meters", className="labels"),
        html.P("Results showed for " +
               str(time_period_above_thrshld) +
               " " + time_unit +
               " with data above threshold in a " +
               str(time_period) + " years time period", style={"margin": "0"}),
        html.P("(Threshold is set to " + str(threshold_dp) + " data points per " + time_unit + ")",
               style={"font-size": ".8rem", "color": "gray"})
    ]), labels, values], style={"text-align": "center"})

    return layout



def create_health_indicators(df, metric, col_min, col_max, metric_label):
    value = float(df[metric])
    min_value = float(df[col_min])
    max_value = float(df[col_max])
    range = max_value - min_value
    bottom_value = min_value - (range * .25)
    top_value = max_value + (range * .25)
    array = [bottom_value, min_value, value, max_value, top_value]
    array_norm = (array - np.min(array)) / (np.max(array) - np.min(array))
    if value < min_value or value > max_value:
        fill_color = "warning",
    else:
        fill_color = "success"

    layout = html.Div([html.Div(html.Label(metric_label, className="labels"), className="labels-container"),
                       dbc.Progress(value=array_norm[2]*100, label=str(value), color=fill_color, className="meter-a", style={"background-color": "#fff"}),
                       html.Div(html.P("Ref: " + str(min_value) + " (min) to " + str(max_value) + " (max)", style={"font-size": "0.75rem", "margin": "0", "color": "gray"}), className="labels-container"),
                       dbc.Progress([
                           dbc.Progress(value=array_norm[1]*100, color="warning", bar=True),
                           dbc.Progress(value=(1-(array_norm[1]*2))*100, color="success", bar=True),
                           dbc.Progress(value=array_norm[1]*100, color="warning", bar=True),
                       ], style={"height": "0.25rem", "margin-left": "1rem", "margin-right": "1rem"}),
                       ], style={"width": "25%"})
    return layout


iconA = "assets/icon_metadata.png"
labelA = "Descarga de metadatos"
textA = "Los metadatos son 'datos acerca de los datos'. Describen el contenido, la calidad, el formato y otras características de este conjuntos de los datos. También incluyen las formas de citación, créditos y licencias de los datos."
buttonA = "Descargar metadatos"

iconB = "assets/icon_dix.png"
labelB = "Descarga de diccionario de datos"
textB = "Es el significado de cada una de los 'campos' o 'variables' del conjunto de datos. Muestra el significado de cada encabezado del conjunto de datos y la descripción de los datos que contiene."
buttonB = "Descargar diccionario de datos"

iconC = "assets/icon_data.png"
labelC = "Descarga los datos abiertos"
textC = "Los datos abiertos son el conjunto de datos detrás de este Data Explorer. Tienen un formato tabular (.csv) y muestran los datos en su forma más desagregada."
buttonC = "Descargar los datos abiertos"

downloads = create_download_cards(iconA, labelA, textA, buttonA, iconB, textB, labelB, buttonB, iconC, labelC, textC,
                                  buttonC)

# Methods

methods_text_1 = "¿How do we get this data?"
methods_text_2 = "Condimentum vitae sapien pellentesque habitant morbi. Convallis posuere morbi leo urna molestie at. Semper quis lectus nulla at volutpat diam ut venenatis tellus. Netus et malesuada fames ac turpis. Ut enim blandit volutpat maecenas volutpat blandit."
methods_text_3 = "Ullamcorper malesuada proin libero nunc consequat interdum varius. Ut placerat orci nulla pellentesque dignissim enim sit amet. Commodo elit at imperdiet dui accumsan sit amet nulla facilisi. Convallis convallis tellus id interdum velit laoreet id"
