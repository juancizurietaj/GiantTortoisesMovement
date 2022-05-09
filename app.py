from helpers import *

# App constructor
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# data["new_col"] = data.agg("{0[lat]} {0[month]}".format, axis=1)
# print(data["new_col"].values)


# Methods
methods = html.Div(
    [
        html.H1("Methods: Movement", className="h1"),
        html.P(methods_text_1, className="labels", style={"padding": "0px 20px"}),
        html.P(methods_text_2, className="texts"),
        html.P(methods_text_3, className="texts"),
        html.H1("Methods: Biology", className="h1"),
        html.P(methods_text_1, className="labels", style={"padding": "0px 20px"}),
        html.P(methods_text_2, className="texts"),
        html.P(methods_text_3, className="texts"),
        html.H1("Methods: Health", className="h1"),
        html.P(methods_text_1, className="labels", style={"padding": "0px 20px"}),
        html.P(methods_text_2, className="texts"),
        html.P(methods_text_3, className="texts"),
    ]
)

# Figures

figures = html.Div(
    [
        html.Div(id="tortoise-a",
                 children=[
                     dbc.Card(
                         [
                             html.Div(dcc.Dropdown(id="tortoise-a-selection",
                                                   options=[{"label": "Isabela (Isabela island)", "value": "isabela"},
                                                            {"label": "Emma (Española island)", "value": "emma"},
                                                            {"label": "Herbert (Santa Cruz island)",
                                                             "value": "herbert"}],
                                                   value="isabela",
                                                   clearable=False)),
                             html.Br(),
                         ], className="card-box"
                     ),
                     dbc.Card(
                         [
                             html.Div(html.H2("Tortoise biology and health"), className="labels-container"),
                             html.Div(html.Label("Tortoise dimensions", className="labels"),
                                      className="labels-container"),
                             html.Div(
                                 [
                                     html.Div([
                                         html.Img(src="assets/long_shell.png", height="85rem"),
                                         html.P("Shell length"),
                                         html.P(id="shell-length-a", className="values")
                                     ], style={"text-align": "center"}),
                                     html.Div([
                                         html.Img(src="assets/wide_shell.png", height="85rem"),
                                         html.P("Shell width"),
                                         html.P(id="shell-width-a", className="values")
                                     ], style={"text-align": "center"}),
                                 ], style={"display": "flex", "justify-content": "space-evenly", "padding": "2rem"}
                             ),
                             html.Div(id="health-indicators-a"),
                             html.Br(),
                             html.Hr(),
                             html.Div(html.H2("Tortoise movement"), className="labels-container"),
                             html.P("Select how to display movement data:", style={"align-self": "center"}),
                             html.Div(
                                 dbc.ButtonGroup(
                                     [
                                         dbc.Button("Year", id="year-selection-a", outline=True, color="primary",
                                                    n_clicks=1),
                                         dbc.Button("Month", id="month-selection-a", outline=True, color="primary",
                                                    n_clicks=0),
                                         dbc.Button("Week", id="week-selection-a", outline=True, color="primary",
                                                    n_clicks=0),
                                         dbc.Button("Day", id="day-selection-a", outline=True, color="primary",
                                                    n_clicks=0)
                                     ], size="sm", style={"width": "45%"}
                                 ), style={"text-align": "center"}
                             ),
                             html.Br(),
                             # Indicators
                             html.Div(id="indicators-a", className="indicators-container"),
                             # Distance and altitude plots
                             html.Div([
                                 html.Div(
                                     [
                                         html.Label("Total distance", className="labels"),
                                         html.Div(
                                             dcc.Graph(id="fig-dist-tortoise-a", config={"displayModeBar": False})),
                                     ], style={"width": "50%", "text-align": "center"}
                                 ),
                                 html.Div(
                                     [
                                         html.Label("Elevation average", className="labels"),
                                         html.Div(dcc.Graph(id="fig-elev-tortoise-a", config={"displayModeBar": False}))
                                     ], style={"width": "50%", "text-align": "center"}
                                 )
                             ], style={"display": "flex", "margin-top": "2rem"}),
                             html.Br(),
                             # Heatmap
                             html.Div(
                                 [
                                     html.Label("Geographic distribution", className="labels"),
                                     dcc.Graph(id="fig-tortoise-a", config={"displayModeBar": False})
                                 ], style={"text-align": "center"}
                             ),
                         ], className="card-box-behind"
                     )
                 ]),
        html.Div(dbc.Button(id="add-tortoise-btn", n_clicks=0, className="add-button"), className="button-container"),
        html.Div(id="tortoise-b",
                 children=[
                     dbc.Card(
                         [
                             html.Div(dcc.Dropdown(id="tortoise-b-selection",
                                                   options=[{"label": "Isabela (Isabela island)", "value": "isabela"},
                                                            {"label": "Emma (Española island)", "value": "emma"},
                                                            {"label": "Herbert (Santa Cruz island)",
                                                             "value": "herbert"}],
                                                   value="isabela",
                                                   clearable=False)),
                             html.Br(),
                         ], className="card-box"
                     ),
                     dbc.Card(
                         [
                             html.Div(html.H2("Tortoise biology and health"), className="labels-container"),
                             html.Div(html.Label("Tortoise dimensions", className="labels"),
                                      className="labels-container"),
                             html.Div(
                                 [
                                     html.Div([
                                         html.Img(src="assets/long_shell.png", height="85rem"),
                                         html.P("Shell length"),
                                         html.P(id="shell-length-b", className="values")
                                     ], style={"text-align": "center"}),
                                     html.Div([
                                         html.Img(src="assets/wide_shell.png", height="85rem"),
                                         html.P("Shell width"),
                                         html.P(id="shell-width-b", className="values")
                                     ], style={"text-align": "center"}),
                                 ], style={"display": "flex", "justify-content": "space-evenly", "padding": "2rem"}
                             ),
                             html.Div(id="health-indicators-b"),
                             html.Br(),
                             html.Hr(),
                             html.Div(html.H2("Tortoise movement"), className="labels-container"),
                             html.P("Select how to display movement data:", style={"align-self": "center"}),
                             html.Div(
                                 dbc.ButtonGroup(
                                     [
                                         dbc.Button("Year", id="year-selection-b", outline=True, color="primary",
                                                    n_clicks=1),
                                         dbc.Button("Month", id="month-selection-b", outline=True, color="primary",
                                                    n_clicks=0),
                                         dbc.Button("Week", id="week-selection-b", outline=True, color="primary",
                                                    n_clicks=0),
                                         dbc.Button("Day", id="day-selection-b", outline=True, color="primary",
                                                    n_clicks=0)
                                     ], size="sm", style={"width": "45%"}
                                 ), style={"text-align": "center"}
                             ),
                             html.Br(),
                             # Indicators
                             html.Div(id="indicators-b", className="indicators-container"),
                             # Distance and altitude plots
                             html.Div([
                                 html.Div(
                                     [
                                         html.Label("Total distance", className="labels"),
                                         html.Div(
                                             dcc.Graph(id="fig-dist-tortoise-b", config={"displayModeBar": False})),
                                     ], style={"width": "50%", "text-align": "center"}
                                 ),
                                 html.Div(
                                     [
                                         html.Label("Elevation average", className="labels"),
                                         html.Div(dcc.Graph(id="fig-elev-tortoise-b", config={"displayModeBar": False}))
                                     ], style={"width": "50%", "text-align": "center"}
                                 )
                             ], style={"display": "flex", "margin-top": "2rem"}),
                             html.Br(),
                             # Heatmap
                             html.Div(
                                 [
                                     html.Label("Geographic distribution", className="labels"),
                                     dcc.Graph(id="fig-tortoise-b", config={"displayModeBar": False})
                                 ], style={"text-align": "center"}
                             ),
                         ], className="card-box-behind"
                     )
                 ]),
    ], style={"display": "flex", "flex-direction": "row"}
)

maps = html.Div(dbc.Card([html.Br(), html.Br(), html.Label("TO BE DEVELOPED"), html.Br(), html.Br()], className="card-box"))

# Tabs
tab1 = tab_creator("METHODS", methods)
tab2 = tab_creator("FIGURES", figures)
tab3 = tab_creator("GEOGRAPHIC EXPLORATION", maps)
tab4 = tab_creator("OPEN DATA", downloads)

tabs = dbc.Tabs([tab1, tab2, tab3, tab4])

app.layout = html.Div(
    [
        header,
        tabs,
        footer
    ]
)


@app.callback(
    Output("tortoise-a", "style"),
    Output("tortoise-b", "style"),
    Output("add-tortoise-btn", "n_clicks"),
    Output("add-tortoise-btn", "children"),
    Output("fig-tortoise-a", "figure"),
    Output("year-selection-a", "n_clicks"),
    Output("month-selection-a", "n_clicks"),
    Output("week-selection-a", "n_clicks"),
    Output("day-selection-a", "n_clicks"),
    Output("fig-tortoise-b", "figure"),
    Output("year-selection-b", "n_clicks"),
    Output("month-selection-b", "n_clicks"),
    Output("week-selection-b", "n_clicks"),
    Output("day-selection-b", "n_clicks"),
    Output("fig-dist-tortoise-a", "figure"),
    Output("fig-elev-tortoise-a", "figure"),
    Output("indicators-a", "children"),
    Output("health-indicators-a", "children"),
    Output("shell-length-a", "children"),
    Output("shell-width-a", "children"),
    Output("fig-dist-tortoise-b", "figure"),
    Output("fig-elev-tortoise-b", "figure"),
    Output("indicators-b", "children"),
    Output("health-indicators-b", "children"),
    Output("shell-length-b", "children"),
    Output("shell-width-b", "children"),
    Input("add-tortoise-btn", "n_clicks"),
    Input("tortoise-a-selection", "value"),
    Input("tortoise-b-selection", "value"),
    Input("year-selection-a", "n_clicks"),
    Input("month-selection-a", "n_clicks"),
    Input("week-selection-a", "n_clicks"),
    Input("day-selection-a", "n_clicks"),
    Input("year-selection-b", "n_clicks"),
    Input("month-selection-b", "n_clicks"),
    Input("week-selection-b", "n_clicks"),
    Input("day-selection-b", "n_clicks"),

)
def update_layout(add_tortoise_click, tortoise_a, tortoise_b, year_click_a, month_click_a, week_click_a, day_click_a,
                  year_click_b,
                  month_click_b, week_click_b, day_click_b):
    # Layout distribution:
    if add_tortoise_click % 2 != 0:
        lay_tort_a = {"width": "45%"}
        lay_tort_b = {"width": "45%"}
        add_tortoise_btn_children = "Remove tortoise"
    elif add_tortoise_click % 2 == 0:
        lay_tort_a = {"width": "85%"}
        lay_tort_b = {"display": "None"}
        add_tortoise_btn_children = "Add a tortoise"

    # FIRST TORTOISE
    # Data selection:
    if tortoise_a == "isabela":
        dfA = data_isabela
        zoomA = 10
    elif tortoise_a == "emma":
        dfA = data_emma
        zoomA = 14
    else:
        dfA = data_herbert
        zoomA = 14

    dfA["year"] = dfA["year"].astype(int)
    dfA["week"] = dfA["week"].astype(int)

    lat_centerA = dfA["lat"].median()
    lon_centerA = dfA["lon"].median()

    # Heatmap features:
    ## Default values (year):
    animation_value = "year"
    category_orders = {}
    figA = create_heat_map(dfA, lat_centerA, lon_centerA, animation_value, category_orders, zoomA)
    figA_dist = line_charts_distance(dfA, "year", "distance")
    figA_elev = line_charts_elevation(dfA, "year", "altitude")

    # Layout
    indicators_layout = create_indicators_layout(dfA, "year", "distance")

    # Biology layout
    shell_length_a = str(float(data_health[data_health["ID"] == tortoise_a]["Largo curvo"])) + "cm"
    shell_width_a = str(float(data_health[data_health["ID"] == tortoise_a]["Ancho curvo"])) + "cm"
    shell_length_b = str(float(data_health[data_health["ID"] == tortoise_b]["Largo curvo"])) + "cm"
    shell_width_b = str(float(data_health[data_health["ID"] == tortoise_b]["Ancho curvo"])) + "cm"
    # Health layout
    df_healthA = data_health[data_health["ID"] == tortoise_a]
    df_healthB = data_health[data_health["ID"] == tortoise_b]

    health_layoutA = html.Div([
        html.Div(html.Label("Health indicators", className="labels"), style={"text-align": "center"}),
        html.Br(),
        html.Div(
            [
                create_health_indicators(df_healthA, "Globulos rojos", "Min Globulos rojos",
                                         "Max Globulos rojos", "Red cells"),
                create_health_indicators(df_healthA, "Solidos totales", "Min Solidos totales",
                                         "Max Solidos totales", "Total solids"),
                create_health_indicators(df_healthA, "Glucosa", "Min Glucosa",
                                         "Max Glucosa", "Glucose"),
                create_health_indicators(df_healthA, "Calcio", "Min Calcio",
                                         "Max Calcio", "Calcium"),
                create_health_indicators(df_healthA, "Fosforo", "Min Fosforo",
                                         "Max Fosforo", "Phosphorum"),
                create_health_indicators(df_healthA, "Albumina", "Min Albumina",
                                         "Max Albumina", "Albumin"),
            ], style={"display": "flex"}
        )
    ], style={"background-color": "#eaeaea", "padding": "3rem"})

    health_layoutB = html.Div([
        html.Div(html.Label("Health indicators", className="labels"), style={"text-align": "center"}),
        html.Br(),
        html.Div(
            [
                create_health_indicators(df_healthB, "Globulos rojos", "Min Globulos rojos",
                                         "Max Globulos rojos", "Red cells"),
                create_health_indicators(df_healthB, "Solidos totales", "Min Solidos totales",
                                         "Max Solidos totales", "Total solids"),
                create_health_indicators(df_healthB, "Glucosa", "Min Glucosa",
                                         "Max Glucosa", "Glucose"),
                create_health_indicators(df_healthB, "Calcio", "Min Calcio",
                                         "Max Calcio", "Calcium"),
                create_health_indicators(df_healthB, "Fosforo", "Min Fosforo",
                                         "Max Fosforo", "Phosphorum"),
                create_health_indicators(df_healthB, "Albumina", "Min Albumina",
                                         "Max Albumina", "Albumin"),
            ], style={"display": "flex"}
        )
    ], style={"background-color": "#eaeaea", "padding": "3rem"})

    if year_click_a > 0:
        animation_value = "year"
        year_click_a = 0
        figA = figA
        figA_dist = figA_dist
        figA_elev = figA_elev
        indicators_layout = indicators_layout

    elif month_click_a > 0:
        animation_value = "month"
        month_click_a = 0
        category_orders = {"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                                     "Nov", "Dec"]}
        figA = create_heat_map(dfA, lat_centerA, lon_centerA, animation_value, category_orders, zoomA)
        figA_dist = line_charts_distance(dfA, "month", "distance")
        figA_elev = line_charts_elevation(dfA, "month", "altitude")
        indicators_layout = create_indicators_layout(dfA, "month", "distance")

    elif week_click_a > 0:
        animation_value = "week"
        week_click_a = 0
        ordered_values = sorted(dfA["week"].unique())
        category_orders = {"week": ordered_values}
        figA = create_heat_map(dfA, lat_centerA, lon_centerA, animation_value, category_orders, zoomA)
        figA_dist = line_charts_distance(dfA, "week", "distance")
        figA_elev = line_charts_elevation(dfA, "week", "altitude")
        indicators_layout = create_indicators_layout(dfA, "week", "distance")

    elif day_click_a > 0:
        animation_value = "yday"
        day_click_a = 0
        ordered_values = sorted(dfA["yday"].unique())
        category_orders = {"yday": ordered_values}
        figA = create_heat_map(dfA, lat_centerA, lon_centerA, animation_value, category_orders, zoomA)
        figA_dist = line_charts_distance(dfA, "yday", "distance")
        figA_elev = line_charts_elevation(dfA, "yday", "altitude")
        indicators_layout = create_indicators_layout(dfA, "date", "distance")

    # SECOND TORTOISE
    # Data selection:
    if tortoise_b == "isabela":
        dfB = data_isabela
        zoomB = 10
    elif tortoise_b == "emma":
        dfB = data_emma
        zoomB = 14
    else:
        dfB = data_herbert
        zoomB = 14

    dfB["year"] = dfB["year"].astype(int)
    dfB["week"] = dfB["week"].astype(int)
    lat_centerB = dfB["lat"].median()
    lon_centerB = dfB["lon"].median()

    # Heatmap features:
    category_ordersB = {}
    figB = create_heat_map(dfB, lat_centerB, lon_centerB, animation_value, category_ordersB, zoomB)
    figB_dist = line_charts_distance(dfB, "year", "distance")
    figB_elev = line_charts_elevation(dfB, "year", "altitude")
    indicators_layoutB = create_indicators_layout(dfB, "year", "distance")


    if year_click_b > 0:
        year_click_b = 0
        figB = figB
        figB_dist = figB_dist
        figB_elev = figB_elev
        indicators_layoutB = indicators_layoutB

    elif month_click_b > 0:
        animation_value = "month"
        month_click_b = 0
        category_ordersB = {"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                                     "Nov", "Dec"]}
        figB = create_heat_map(dfB, lat_centerB, lon_centerB, animation_value, category_ordersB, zoomB)
        figB_dist = line_charts_distance(dfB, "month", "distance")
        figB_elev = line_charts_elevation(dfB, "month", "altitude")
        indicators_layoutB = create_indicators_layout(dfB, "month", "distance")

    elif week_click_b > 0:
        animation_value = "week"
        week_click_b = 0
        ordered_values = sorted(dfB["week"].unique())
        category_ordersB = {"week": ordered_values}
        figB = create_heat_map(dfB, lat_centerB, lon_centerB, animation_value, category_ordersB, zoomB)
        figB_dist = line_charts_distance(dfB, "week", "distance")
        figB_elev = line_charts_elevation(dfB, "week", "altitude")
        indicators_layoutB = create_indicators_layout(dfB, "week", "distance")

    elif day_click_b > 0:
        animation_value = "yday"
        day_click_b = 0
        ordered_values = sorted(dfB["yday"].unique())
        category_ordersB = {"yday": ordered_values}
        figB = create_heat_map(dfB, lat_centerB, lon_centerB, animation_value, category_ordersB, zoomB)
        figA_dist = line_charts_distance(dfB, "yday", "distance")
        figA_elev = line_charts_elevation(dfB, "yday", "altitude")
        indicators_layoutB = create_indicators_layout(dfB, "date", "distance")

    return lay_tort_a, lay_tort_b, add_tortoise_click, add_tortoise_btn_children, \
           figA, year_click_a, month_click_a, week_click_a, day_click_a, \
           figB, year_click_b, month_click_b, week_click_b, day_click_b, \
           figA_dist, figA_elev, indicators_layout, health_layoutA, shell_length_a, shell_width_a, \
           figB_dist, figB_elev, indicators_layoutB, health_layoutB, shell_length_b, shell_width_b


if __name__ == '__main__':
    app.run_server(debug=True)
