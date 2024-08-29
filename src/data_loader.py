import pandas as pd

def loadData(filePath: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(filePath)
        return df
    except Exception as e:
        print(f"Ocorreu um erro ao realizar o carregamento dos dados: {e}")
        raise