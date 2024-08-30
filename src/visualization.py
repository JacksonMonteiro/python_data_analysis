import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plotAll(metrics):    
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "domain"}],  
               [{"type": "domain"}, {"type": "xy"}]],  
        subplot_titles=("Serviços com Mais Frequência", "Parceiros com Mais Frequência", 
                        "Distribuição dos Nichos", "Prospecção")
    )

    
    fig.add_trace(
        go.Bar(x=metrics['servicoFrequente'].index, y=metrics['servicoFrequente'].values, name='Serviços'),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(labels=metrics['parceiroFrequente'].index, values=metrics['parceiroFrequente'].values, name='Parceiros'),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Pie(labels=metrics['nichoFrequente'].index, values=metrics['nichoFrequente'].values, name='Nichos'),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Bar(x=metrics['prospeccao'].index, y=metrics['prospeccao'].values, name='Prospecção'),
        row=2, col=2
    )

    fig.update_layout(title_text="Análise de Métricas", showlegend=True)
        
    fig.show()