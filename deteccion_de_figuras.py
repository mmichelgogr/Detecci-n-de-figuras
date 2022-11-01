!wget https://raw.githubusercontent.com/DRMiguelAR/UP_Interpretacion/master/orillas/figura1.png
!wget https://raw.githubusercontent.com/DRMiguelAR/UP_Interpretacion/master/orillas/figura2.png


import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy import pi, floor, cos, sin, sqrt, zeros

def find_figures(imgName):
  figuras = cv2.imread(imgName, 0)
  figurasFinal = cv2.imread(imgName, cv2.IMREAD_COLOR)
  plt.title("Imagen Original") 
  
  circulos = cv2.HoughCircles(figuras, cv2.HOUGH_GRADIENT, 2, 100, 100, 250, 100)
  circulos = np.uint16(np.around(circulos))

  if len(circulos[0] > 1):
    circulo(circulos)
    for i in circulos[0,:]:
                        #x, y del centro y el radio
      cv2.circle(figurasFinal, (i[0], i[1]), i[2], (0, 187, 255), 10)      

  #Filtro que suaviza la imagen
  kernel = np.ones((5,5),np.float32)/25
  fig2 = cv2.filter2D(figuras,-1,kernel)

  #obtener una imagen binaria desde la imagen filtrada
  _, imgBinaria = cv2.threshold(fig2, 245, 255, cv2.THRESH_BINARY_INV)
  #findContours() encuentra los lados
  contornos, _ = cv2.findContours(imgBinaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  #por cada figura encontrada se sacan sus lados con approxPolyDP
  for figura in contornos:
    epsilon = 0.01 * cv2.arcLength(figura, True)
    lados = cv2.approxPolyDP(figura, epsilon, True)
    i, j = lados[0][0]
    
    if len(lados) == 3:
      cv2.drawContours(figurasFinal, [lados], 0, (0, 255, 0), 10)
      cv2.putText(figurasFinal, "Triangulo", (i, j+100), cv2.FONT_ITALIC, 1, 0, 2)
      print("Coordenadas del Triangulo: ")
      printCoords(lados)
    elif len(lados) == 4:
      cv2.drawContours(figurasFinal, [lados], 0, (128, 0, 255), 10)
      cv2.putText(figurasFinal, "Cuadrado", (i, j+100), cv2.FONT_ITALIC, 1, 0, 2)
      print("Coordenadas del Cuadrado: ")
      printCoords(lados)
    elif len(lados) == 5:
      cv2.drawContours(figurasFinal, [lados], 0, (255, 159, 5), 10)
      cv2.putText(figurasFinal, "Pentagono", (i, j+100), cv2.FONT_ITALIC, 1, 0, 2)
      print("Coordenadas del Pentágono: ")
      printCoords(lados)
    elif len(lados) < 3:
      cv2.drawContours(figurasFinal, [lados], 0, (255, 0, 0), 10)
      cv2.putText(figurasFinal, "Linea", (i, j+100), cv2.FONT_ITALIC, 1, 0, 2)
      print("Coordenadas de la Línea: ")
      printCoords(lados)
    else:
      if len(circulos[0] != 1):
        cv2.putText(figurasFinal, "Circulo", (i, j+150), cv2.FONT_ITALIC, 1, 0, 2)
        cv2.circle(figurasFinal, (circulos[0][0][0], circulos[0][0][1]), 5, (0, 187, 255), 10)
        #cv.circle(fig2, centerOfCircle, radius, color, thickness)
  
  esquinas = cv2.cornerHarris(fig2,3,5,0.04)
  esquinas = esquinas>esquinas.max()*0.01 #filtro

  h,w = esquinas.shape
  for i in range(1,h-1):
    for j in range(1,w-1):
      if esquinas[i-1][j-1] or esquinas[i-1][j] or esquinas[i-1][j+1] or\
      esquinas[i][j-1] or esquinas[i][j+1] or\
      esquinas[i+1][j-1] or esquinas[i+1][j] or esquinas[i+1][j+1]:
        esquinas[i][j] =False

  np.unique(esquinas, return_counts = True)
  np.argwhere(esquinas)
  coords = np.argwhere(esquinas)
  x=[coord[0]for coord in coords]
  y=[coord[1]for coord in coords]
  plt.imshow(figurasFinal)
  plt.plot(y,x,"x", markersize = 5, markeredgewidth = 2)

  plt.title("Figuras Encontradas : " + imgName) 
  plt.show()


def printCoords(lados):
  x=[lados[0][0][0]for edge in lados]
  y=[lados[0][0][1]for edge in lados]
  print(x)
  print(y)

def circulo(circulos):
  if len(circulos[0]) != 1:
    for i in range(0,len(circulos[0][0])):
      print("Circulo Radio:" + str(circulos[0][i][2]) + " las coordenadas del centro son: " + str(circulos[0][i][0])+ " , " + str(circulos[0][i][1]))
  if len(circulos[0][0]) == 1:
    print("Circulo Radio:" + str(circulos[0][0][2]) + " las coordenadas del centro son: " + str(circulos[0][0][0])+ " , " + str(circulos[0][0][1]))

find_figures("figura1.png")

find_figures("figura2.png")
