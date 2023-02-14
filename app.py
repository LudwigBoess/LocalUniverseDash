import os
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go

fixed_colors = [
    "rgb(232, 245, 171)",
    "rgb(220, 219, 137)",
    "rgb(209, 193, 107)",
    "rgb(199, 168, 83)",
    "rgb(186, 143, 66)",
    "rgb(170, 121, 60)",
    "rgb(151, 103, 58)",
    "rgb(129, 87, 56)",
    "rgb(104, 72, 53)",
    "rgb(80, 59, 46)",
    "rgb(57, 45, 37)",
    "rgb(34, 30, 27)",
    "rgb(3, 35, 51)",
    "rgb(13, 48, 100)",
    "rgb(53, 50, 155)",
    "rgb(93, 62, 153)",
    "rgb(126, 77, 143)",
    "rgb(158, 89, 135)",
    "rgb(193, 100, 121)",
    "rgb(225, 113, 97)",
    "rgb(246, 139, 69)",
    "rgb(251, 173, 60)",
    "rgb(246, 211, 70)",
    "rgb(231, 250, 90)",
    "rgb(41, 24, 107)",
    "rgb(42, 35, 160)",
    "rgb(15, 71, 153)",
    "rgb(18, 95, 142)",
    "rgb(38, 116, 137)",
    "rgb(53, 136, 136)",
    "rgb(65, 157, 133)",
    "rgb(81, 178, 124)",
    "rgb(111, 198, 107)",
    "rgb(160, 214, 91)",
    "rgb(212, 225, 112)",
    "rgb(253, 238, 153)",
    "rgb(51, 19, 23)",
    "rgb(79, 28, 33)",
    "rgb(108, 36, 36)",
    "rgb(135, 47, 32)",
    "rgb(157, 66, 25)",
    "rgb(174, 88, 20)",
    "rgb(188, 111, 19)",
    "rgb(199, 137, 22)",
    "rgb(209, 164, 32)",
    "rgb(217, 192, 44)",
    "rgb(222, 222, 59)",
    "rgb(224, 253, 74)",
    "rgb(3, 5, 18)",
    "rgb(25, 25, 51)",
    "rgb(44, 42, 87)",
    "rgb(58, 60, 125)",
    "rgb(62, 83, 160)",
    "rgb(62, 109, 178)",
    "rgb(72, 134, 187)",
    "rgb(89, 159, 196)",
    "rgb(114, 184, 205)",
    "rgb(149, 207, 216)",
    "rgb(192, 229, 232)",
    "rgb(234, 252, 253)",
    "rgb(0, 0, 0)",
    "rgb(16, 16, 16)",
    "rgb(38, 38, 38)",
    "rgb(59, 59, 59)",
    "rgb(81, 80, 80)",
    "rgb(102, 101, 101)",
    "rgb(124, 123, 122)",
    "rgb(146, 146, 145)",
    "rgb(171, 171, 170)",
    "rgb(197, 197, 195)",
    "rgb(224, 224, 223)",
    "rgb(254, 254, 253)",
    "rgb(63, 5, 5)",
    "rgb(101, 6, 13)",
    "rgb(138, 17, 9)",
    "rgb(96, 95, 95)",
    "rgb(119, 118, 118)",
    "rgb(142, 141, 141)",
    "rgb(166, 166, 165)",
    "rgb(193, 192, 191)",
    "rgb(222, 222, 220)",
    "rgb(239, 248, 90)",
    "rgb(230, 210, 41)",
    "rgb(220, 174, 25)",
    "rgb(253, 253, 204)",
    "rgb(206, 236, 179)",
    "rgb(156, 219, 165)",
    "rgb(111, 201, 163)",
    "rgb(86, 177, 163)",
    "rgb(76, 153, 160)",
    "rgb(68, 130, 155)",
    "rgb(62, 108, 150)",
    "rgb(62, 82, 143)",
    "rgb(64, 60, 115)",
    "rgb(54, 43, 77)",
    "rgb(39, 26, 44)",
    "rgb(230, 240, 240)",
    "rgb(191, 221, 229)",
    "rgb(156, 201, 226)",
    "rgb(129, 180, 227)",
    "rgb(115, 154, 228)",
    "rgb(117, 127, 221)",
    "rgb(120, 100, 202)",
    "rgb(119, 74, 175)",
    "rgb(113, 50, 141)",
    "rgb(100, 31, 104)",
    "rgb(80, 20, 66)",
    "rgb(54, 14, 36)",
    "rgb(214, 249, 207)",
    "rgb(186, 228, 174)",
    "rgb(156, 209, 143)",
    "rgb(124, 191, 115)",
    "rgb(85, 174, 91)",
    "rgb(37, 157, 81)",
    "rgb(7, 138, 78)",
    "rgb(13, 117, 71)",
    "rgb(23, 95, 61)",
    "rgb(25, 75, 49)",
    "rgb(23, 55, 35)",
    "rgb(17, 36, 20)",
    "rgb(253, 237, 176)",
    "rgb(250, 205, 145)",
    "rgb(246, 173, 119)",
    "rgb(240, 142, 98)",
    "rgb(231, 109, 84)",
    "rgb(216, 80, 83)",
    "rgb(195, 56, 90)",
    "rgb(168, 40, 96)",
    "rgb(138, 29, 99)",
    "rgb(107, 24, 93)",
    "rgb(76, 21, 80)",
    "rgb(47, 15, 61)",
    "rgb(254, 252, 205)",
    "rgb(239, 225, 156)",
    "rgb(221, 201, 106)",
    "rgb(194, 182, 59)",
    "rgb(157, 167, 21)",
    "rgb(116, 153, 5)",
    "rgb(75, 138, 20)",
    "rgb(35, 121, 36)",
    "rgb(11, 100, 44)",
    "rgb(18, 78, 43)",
    "rgb(25, 56, 34)",
    "rgb(23, 35, 18)",
    "rgb(241, 236, 236)",
    "rgb(230, 209, 203)",
    "rgb(221, 182, 170)",
    "rgb(213, 156, 137)",
    "rgb(205, 129, 103)",
    "rgb(196, 102, 73)",
    "rgb(186, 74, 47)",
    "rgb(172, 44, 36)",
    "rgb(149, 19, 39)",
    "rgb(120, 14, 40)",
    "rgb(89, 13, 31)",
    "rgb(60, 9, 17)",
    "rgb(254, 245, 244)",
    "rgb(222, 224, 210)",
    "rgb(189, 206, 181)",
    "rgb(153, 189, 156)",
    "rgb(110, 173, 138)",
    "rgb(65, 157, 129)",
    "rgb(25, 137, 125)",
    "rgb(18, 116, 117)",
    "rgb(25, 94, 106)",
    "rgb(28, 72, 93)",
    "rgb(25, 51, 80)",
    "rgb(20, 29, 67)",
    "rgb(167, 119, 12)",
    "rgb(197, 96, 51)",
    "rgb(217, 67, 96)",
    "rgb(221, 38, 163)",
    "rgb(196, 59, 224)",
    "rgb(153, 97, 244)",
    "rgb(95, 127, 228)",
    "rgb(40, 144, 183)",
    "rgb(15, 151, 136)",
    "rgb(39, 153, 79)",
    "rgb(119, 141, 17)",
    "rgb(167, 119, 12)",
    "rgb(23, 28, 66)",
    "rgb(41, 58, 143)",
    "rgb(11, 102, 189)",
    "rgb(69, 144, 185)",
    "rgb(142, 181, 194)",
    "rgb(210, 216, 219)",
    "rgb(230, 210, 204)",
    "rgb(213, 157, 137)",
    "rgb(196, 101, 72)",
    "rgb(172, 43, 36)",
    "rgb(120, 14, 40)",
    "rgb(60, 9, 17)",
    "rgb(16, 31, 63)",
    "rgb(38, 62, 144)",
    "rgb(30, 110, 161)",
    "rgb(60, 154, 171)",
    "rgb(140, 193, 186)",
    "rgb(217, 229, 218)",
    "rgb(239, 226, 156)",
    "rgb(195, 182, 59)",
    "rgb(115, 152, 5)",
    "rgb(34, 120, 36)",
    "rgb(18, 78, 43)",
    "rgb(23, 35, 18)",
    "rgb(20, 29, 67)",
    "rgb(28, 72, 93)",
    "rgb(18, 115, 117)",
    "rgb(63, 156, 129)",
    "rgb(153, 189, 156)",
    "rgb(223, 225, 211)",
    "rgb(241, 218, 206)",
    "rgb(224, 160, 137)",
    "rgb(203, 101, 99)",
    "rgb(164, 54, 96)",
    "rgb(111, 23, 91)",
    "rgb(51, 13, 53)",
    "rgb(103,0,31)",
    "rgb(178,24,43)",
    "rgb(214,96,77)",
    "rgb(244,165,130)",
    "rgb(253,219,199)",
    "rgb(255,255,255)",
    "rgb(224,224,224)",
    "rgb(186,186,186)",
    "rgb(135,135,135)",
    "rgb(77,77,77)",
    "rgb(26,26,26)",
    "rgb(165,0,38)",
    "rgb(215,48,39)",
    "rgb(244,109,67)",
    "rgb(253,174,97)",
    "rgb(254,224,144)",
    "rgb(255,255,191)",
    "rgb(224,243,248)",
    "rgb(171,217,233)",
    "rgb(116,173,209)",
    "rgb(69,117,180)",
    "rgb(49,54,149)"]


app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simulating the LOcal Web'),
    dcc.Graph(id="3d-scatter-plot-x-graph"),
    html.P("Mass Range:"),
    dcc.RangeSlider(
        id='3d-scatter-plot-x-range-slider',
        min=0, max=9, step=1.0
    ),
])

@app.callback(
    Output("3d-scatter-plot-x-graph", "figure"), 
    Input("3d-scatter-plot-x-range-slider", "value") )
def update_bar_chart(slider_range):

    df = pd.read_csv("data.csv")
    # low, high = slider_range
    # mask = (df.p > low) & (df.p < high)
    
    fig = go.Figure()

    # Add scatter trace with medium sized markers
    fig.add_trace(
        go.Scatter3d(
            mode='markers',
            x=df.x,
            y=df.y,
            z=df.z,
            marker=dict(
                color='gray',
                size=1,
                opacity=0.5,
                line=dict(
                    color='gray',
                    width=0
                )
            ),
            showlegend=True,
            name="Data"
        )
    )

    clusters = pd.read_csv('cluster_names.txt')

    count = 0
    for cluster in clusters.name:

        filename = os.path.join("data", f"{cluster}.csv")
        df_local = pd.read_csv(filename)

        fig.add_trace(
                go.Scatter3d(
                    mode='markers',
                    x=[df_local.iloc[0,0]],
                    y=[df_local.iloc[0,1]],
                    z=[df_local.iloc[0,2]],
                    marker=dict(
                        color=fixed_colors[count],
                        size=5,
                        opacity=0.5,
                        line=dict(
                            color='MediumPurple',
                            width=0
                        )
                    ),
                    legendgroup=cluster,
                    name=cluster
                )
            )

        Nrows = len(df_local.iloc[:,1])

        if Nrows > 1:

            for i in range(1,Nrows):

                fig.add_trace(
                        go.Scatter3d(
                            mode='lines',
                            x=[df_local.iloc[i,0], df_local.iloc[i,3]],
                            y=[df_local.iloc[i,1], df_local.iloc[i,4]],
                            z=[df_local.iloc[i,2], df_local.iloc[i,5]],
                            marker=dict(
                                color=fixed_colors[count],
                                size=5,
                                opacity=0.5,
                            ),
                            legendgroup=cluster,
                            name=cluster,
                            showlegend=False
                        )
                    )

        count += 1
    
    fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.02,
                xanchor="right",
                x=1,
                #traceorder="reversed",
                title_font_family="Times New Roman",
                font=dict(
                    family="Courier",
                    size=12,
                    color="black"
                ),
                bgcolor="LightSteelBlue",
                bordercolor="Black",
                borderwidth=2
            ),
            # xaxis=dict(title_text="X [Mpc]", titlefont=dict(size=30)),
            # yaxis=dict(title_text="Y [Mpc]", titlefont=dict(size=30)),
            # zaxis=dict(title_text="Z [Mpc]", titlefont=dict(size=30)),
            width=1600, height=1200
        )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)