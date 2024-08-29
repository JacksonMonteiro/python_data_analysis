from src.data_loader import loadData
from src.processing import process

def main(): 
    path = "assets/Clientes.xlsx"

    try:
        df = loadData(path)
        df.columns = df.columns.str.strip()
        
        metrics = process(df)

        print(f"Faturamento médio: R$ {metrics['faturamentoMedio']:.2f} \n")
        print(f"Serviços com maior frequência: \n{metrics['servicoFrequente']} \n")
        print(f"Parceiros com maior frequência: \n{metrics['parceiroFrequente']} \n")
        print(f"Nichos com maior frequência: \n{metrics['nichoFrequente']} \n")
        print(f"Prospecção mais eficiente: \n{metrics['prospeccao']} \n")
    except Exception as e:
        print(f"Ocorreu um erro ao realizar o carregamento dos dados: {e}")

if __name__ == "__main__":
    main()        