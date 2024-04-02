# Example using Plotly for visualization
import plotly.graph_objs as go

def generate_csat_chart(csats):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['Call 1', 'Call 2', 'Call 3'], 
        y=csats,
        marker_color='rgb(26, 118, 255)'
    ))
    fig.update_layout(
        title='Customer Satisfaction Score',
        xaxis_title='Call',
        yaxis_title='CSAT',
    )
    return fig
