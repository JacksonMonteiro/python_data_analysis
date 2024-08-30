import pandas as pd

def process(df: pd.DataFrame) -> dict:
    df['Valor'] = df['Valor'].replace('[R$ ,]', '', regex=True).astype(float)
    
    faturamentoMedio = df['Valor'].mean()
    
    servicoFrequente = df['Serviço'].value_counts()    
    parceiroFrequente = df['Parceiro'].value_counts()    
    nichoFrequente = df['Nicho'].value_counts()    
    prospeccaoFrequente = df['Prospecção'].value_counts()
    
    return {
        'faturamentoMedio': faturamentoMedio,
        'servicoFrequente': servicoFrequente,
        'parceiroFrequente': parceiroFrequente,
        'nichoFrequente': nichoFrequente,
        'prospeccao': prospeccaoFrequente,
    }