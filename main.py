import pandas as pd

# df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")
# df = data frame
# print(df)

# d = df.to_dict('list') # imprime un diccionario con los datos de la lista 
# print(sum(d['Quimica'])/6) # calculo total de alumnos por notas de quimica

# d = df.to_dict('records')  
# # print(d[0])
# for alumno in d:
#     if alumno['Nombre'] == 'Sol':
#         print(f'Encontrado el alumno/a: {alumno}')

df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx", index_col='Nombre')
alumno = df.loc['Sol']
print(alumno['Quimica'])