import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import os

precio = 320.45
moneda = 'Bitcoin'
volumen = 1500000
market_cap = 5000000000

data_2015 = None

def procesadoDatos():
    global data_2015
    print(f"Moneda: {moneda}")
    print(f"Precio: ${precio:,.2f}")
    print(f"Volumen de transacciones: {volumen:,}")
    print(f"Market Cap: ${market_cap:,.0f}")
    print("\n" + "-" * 50)  # Separador

    # Cargar los datos
    file_path = "ProyectoPython\src\data\cryptocurrency_historical_prices.csv"
    data = pd.read_csv(file_path)

    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
    else:
        data = pd.read_csv(file_path)
        print("Exploración inicial de los datos:")
        print(data.info())
        print("\nPrimeras 5 filas de los datos:")
        print(data.head())
        data['Fecha'] = pd.to_datetime(data['Fecha'])

    # Exploración inicial
    print("Exploración inicial de los datos:")
    print(data.info())
    print("\nPrimeras 5 filas de los datos:")
    print(data.head())

    # Convertir las fechas al formato datetime
    data['Fecha'] = pd.to_datetime(data['Fecha'])

    # Filtrar datos de 2015
    data_2015 = data[(data['Fecha'] >= '2015-01-01') & (data['Fecha'] <= '2015-12-31')]

    # Identificar valores nulos
    print("\nCantidad de valores nulos por columna en los datos de 2015:")
    print(data_2015.isnull().sum())

    # Reemplazo o eliminación de valores nulos
    data_2015.ffill(axis=0, inplace=True)


    # Estandarizar columnas a mayúsculas
    data_2015.columns = [col.upper() for col in data_2015.columns]

    # Limpiar nombres de las columnas de espacios en blanco (aunque no parece haber ninguno)
    data_2015.columns = data_2015.columns.str.strip()

    # Verificar las columnas
    print("\nColumnas después de la limpieza de los datos:")
    print(data_2015.columns)



    # Ahora imprimimos los datos de una manera más clara usando tabulate
    print("\n==================================================")
    print(tabulate(data_2015[['NOMBRE DE LA MONEDA', 'PRECIO', 'VOLUMEN DE TRANSACCIONES', 'MARKET CAP']].head(),
                headers=['Moneda', 'Precio', 'Volumen de Transacciones', 'Market Cap'], 
                tablefmt='fancy_grid', numalign='right', floatfmt=".2f"))
    print("==================================================")

    print(type(data_2015))

# Gráfico de barras 
def generarGrafico ():
    global data_2015
    if data_2015 is None:
        print("Primero debe procesar los datos")
        return
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='NOMBRE DE LA MONEDA', y='PRECIO', data=data_2015)
    plt.title('Precio de las criptomonedas en 2015')
    plt.xticks(rotation=45)
    
    plt.savefig("Criptomonedas.png")
    
    plt.show()
    print('-'*50)
    
    
def calcularMedia():
    #* Calcular el precio promedio de las criptomonedas en 2015
    global data_2015
    if data_2015 is None:
        print("Primero debe procesar los datos")
        return
    
    precio_promedio = data_2015['PRECIO'].mean()
    
    
    desviacionEstandar = data_2015.groupby('NOMBRE DE LA MONEDA')['PRECIO'].std()
    
    
    desviacionMenor = desviacionEstandar.idxmin()
    menorDesviacion = desviacionEstandar.min()
    
    if pd.isna(desviacionMenor):
        desviacionMenor = 'No hay datos'
        menorDesviacion = 0
    
    print('-'*50)
    print(f"\nEl precio promedio de las criptomonedas en 2015 fue de ${precio_promedio:.2f}")    
    print(f"La criptomoneda con menor desviación estándar es '{desviacionMenor}' con una desviación estándar de {menorDesviacion:.2f}")
    print('-'*50)
    
    
def menu():
    print('='*50)
    print("\tBienvenidos al menu principal")
    print('='*50)
    print()
    print("1. Procesar datos")
    print("2. Generar gráfico")
    print("3. Calcular media")
    print("4. Salir")
    print()
    opcion = int(input("Seleccione una opción: "))
    print()
    if (opcion == 1):
            procesadoDatos()
            menu()
    elif (opcion == 2):
            generarGrafico()
            menu()
    elif (opcion == 3):
            calcularMedia()
            menu()
    elif (opcion == 4):
            print("Gracias por utilizar el programa")
            exit()
    else:
            print("Opción no válida")
            menu()    
        
        
menu()