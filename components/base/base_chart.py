import plotly.graph_objects as go


def apply_chart_theme(
    figure: go.Figure,
):
    """
    Apply HireMate chart styling.
    """

    figure.update_layout(
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20,
        ),
        height=350,
        font=dict(
            family="Inter",
            size=14,
        ),
        legend=dict(
            orientation="h",
            y=-0.2,
        ),
    )

    return figure
