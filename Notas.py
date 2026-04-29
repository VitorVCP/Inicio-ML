from sklearn.linear_model import LinearRegression
horas = [[1], [2], [3], [4], [5]]
notas = [2, 4, 6, 8, 10]

modelo = LinearRegression()
modelo.fit(horas, notas)
resultado = modelo.predict([[4]])[0]
if resultado > 10:
    resultado = 10
print(resultado)