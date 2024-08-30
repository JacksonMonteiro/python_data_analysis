from src.data_loader import loadData
from src.processing import process
from src.visualization import plotAll

def main(): 
    path = "assets/Clientes.xlsx"

    try:
        df = loadData(path)
        df.columns = df.columns.str.strip()
        
        metrics = process(df)

        plotAll(metrics)    
    except Exception as e:
        print(f"Ocorreu um erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()        