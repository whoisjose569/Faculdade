import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Ambiente: Leitura dos dados
base = pd.read_csv("Inteligencia Artificial\IrisClassifierBot\iris.data")

# Sensores: Extração de dados
previsores = base.iloc[:, :4].values
classe = base.iloc[:, 4].values

# Atuadores: Preparação dos dados
label_encoder = LabelEncoder()
classe = label_encoder.fit_transform(classe)

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# Método de Aprendizagem: Treinamento do modelo
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.35, random_state=0)

classificador = GaussianNB()
classificador.fit(previsores_treinamento, classe_treinamento)

# Modelo de Raciocínio: Realização de previsões
previsoes = classificador.predict(previsores_teste)

# Performance: Avaliação do modelo
matriz = confusion_matrix(classe_teste, previsoes)
acuracia = accuracy_score(classe_teste, previsoes)

# Imprimir resultados
print("Matriz de Confusão:")
print("                                 |  Setosa  | Versicolor | Virginica  | Quantidade Real")
for i in range(len(matriz)):
    if i == 0:
        print("Valores previstos como Setosa    |", end=" ")
    elif i == 1:
        print("Valores previstos como Versicolor|", end=" ")
    elif i == 2:
        print("Valores previstos como Virginica |", end=" ")
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:<9}", end=" ")
    if i == 0:
        print(f"| {sum(matriz[i]):<14}")
    elif i == 1:
        print(f"| {sum(matriz[i]):<14}")
    elif i == 2:
        print(f"| {sum(matriz[i]):<14}")
print(f"Acurácia: {acuracia * 100:.2f}% ")
