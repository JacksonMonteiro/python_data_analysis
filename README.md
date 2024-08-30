# Análise de métricas

Este projeto realiza a leitura, processamento e visualização de dados de uma planilha Excel utilizando a biblioteca Pandas para análise de dados e Plotly para visualização gráfica. O objetivo é fornecer métricas sobre os dados e exibi-las de maneira interativa.


## Pré-requisitos

- Python 3.7 ou superior
- As seguintes bibliotecas Python:
  - pandas
  - openpyxl
  - plotly

### Instalando as Dependências

Execute o comando abaixo no terminal para instalar todas as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como Executar o Projeto

1. Coloque o arquivo Excel com os dados na pasta `assets` com o nome `Clientes.xlsx`. Certifique-se de que a planilha segue o mesmo formato das colunas utilizadas no projeto.

2. Para executar o projeto, você pode usar o script `app.bat` (no Windows) ou executar diretamente o comando:

```bash
python main.py
```

## Detalhes de Implementação

### Carregamento de Dados

O módulo `data_loader.py` contém a função `loadData(filePath: str)`, que é responsável por carregar os dados do arquivo Excel especificado.

### Processamento de Dados

O módulo `processing.py` processa os dados carregados, gerando métricas como:

- Faturamento médio (`faturamentoMedio`)
- Serviços mais frequentes (`servicoFrequente`)
- Parceiros mais frequentes (`parceiroFrequente`)
- Nichos mais frequentes (`nichoFrequente`)
- Tipo de prospecção mais frequente (`prospeccaoFrequente`)

### Visualização de Dados

O módulo `visualization.py` utiliza Plotly para criar gráficos interativos. A função `plotAll(metrics)` exibe um dashboard com as métricas geradas, apresentando gráficos de barras e gráficos de pizza.

## Executando o Projeto via Script `.bat`

No Windows, você pode criar um arquivo `.bat` para facilitar a execução do projeto sem precisar rodar o comando no terminal. Crie um arquivo `app.bat` com o seguinte conteúdo:

```bat
@echo off
python src/main.py
pause
```

## Possíveis Melhorias

- **Interatividade:** Aumentar a interatividade dos gráficos utilizando funcionalidades avançadas do Plotly.
- **Dashboard Web:** Migrar o projeto para uma interface web utilizando frameworks como Dash, Flask ou Streamlit.
