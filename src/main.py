from data_loader import loadData

def main(): 
    path = "assets/Clientes.xlsx"

    try:
        df = loadData(path)
        print("Dados carregados com sucesso")
        print(df.head())
    except Exception as e:
        print(f"Ocorreu um erro ao realizar o carregamento dos dados: {e}")

if __name__ == "__main__":
    main()        