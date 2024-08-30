import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Button

def plotAll(metrics):
    plt.figure(figsize=(15, 10))
    
    # Gráfico de barras para Serviços
    plt.subplot(2, 2, 1)
    sns.barplot(x=metrics['servicoFrequente'].index, y=metrics['servicoFrequente'].values)
    plt.title('Serviços com Mais Frequência')
    plt.xlabel('Serviço')
    plt.ylabel('Contagem')

    # Gráfico de barras para Parceiros
    plt.subplot(2, 2, 2)
    sns.barplot(x=metrics['parceiroFrequente'].index, y=metrics['parceiroFrequente'].values)
    plt.title('Parceiros com Mais Frequência')
    plt.xlabel('Parceiro')
    plt.ylabel('Contagem')

    # Gráfico de pizza para Nichos
    plt.subplot(2, 2, 3)
    plt.pie(metrics['nichoFrequente'].values, labels=metrics['nichoFrequente'].index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição dos Nichos')

    # Gráfico de barras para Prospecção
    plt.subplot(2, 2, 4)
    sns.barplot(x=metrics['prospeccao'].index, y=metrics['prospeccao'].values)
    plt.title('Prospecção')
    plt.xlabel('Tipo de Prospecção')
    plt.ylabel('Contagem')

    plt.tight_layout()
    plt.show()