import matplotlib.pyplot as plt
import seaborn as sns

def plotBar(data, title, xlabel, ylabel):
    sns.barplot(x=data.index, y = data.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    plt.show()

def plotPie(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data.values, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()