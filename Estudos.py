from sklearn.tree import DecisionTreeClassifier
horas = [[1], [2], [5], [6], [10]]
resultado = [0, 0, 1, 1, 0]

modelo = DecisionTreeClassifier()
modelo.fit(horas, resultado)
previsao = modelo.predict([[3], [7], [8], [9]])
print(previsao)