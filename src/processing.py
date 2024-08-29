import pandas as pd

def process(df: pd.DataFrame) -> dict:
    df['Valor'] = df['Valor'].replace('[R$ ,]', '', regex=True).astype(float)
    
    faturamentoMedio = df['Valor'].mean()
    
    servicoFrequente = df[['Serviço']].value_counts()
    servicos = "\n".join([f"{index[0]}: {value}" for index, value in servicoFrequente.items()])
    
    parceiroFrequente = df[['Parceiro']].value_counts()
    parceiros = "\n".join([f"{index[0]}: {value}" for index, value in parceiroFrequente.items()])
    
    nichoFrequente = df[['Nicho']].value_counts()
    nichos = "\n".join([f"{index[0]}: {value}" for index, value in nichoFrequente.items()])
    
    prospeccaoFrequente = df[['Prospecção']].value_counts()
    prospeccoes = "\n".join([f"{index[0]}: {value}" for index, value in prospeccaoFrequente.items()])
    
    return {
        'faturamentoMedio': faturamentoMedio,
        'servicoFrequente': servicos,
        'parceiroFrequente': parceiros,
        'nichoFrequente': nichos,
        'prospeccao': prospeccoes,
    }