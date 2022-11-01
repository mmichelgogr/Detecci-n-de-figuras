# Detección de figuras

El algoritmo que se siguió para la detección fue codificando una función que obtuviera el contorno de las figuras (findContours) una vez obtenida el contorno se contaron la cantidad de lados que cada figura tenía (approxPolyDP), entonces con la cantidad de aristas se podía definir el tipo de polígono que se encontraba en la imagen. Esto se aplicó sobre una lectura de la imagen origianl en forma binaria.

En el caso de los círculos se mandó llamar la función de la librería OpenCV que permite indentificar circunferencias en una imagen. Finalmente se trazaban los vértices de los polígonos, el centro de los círculos y un breve texto que nombrara a la figura geométrica correspondiente.

| Imagen Original | Resultado |
| ------ | ------ |
| ![figura1](https://user-images.githubusercontent.com/117127601/199140955-05d761cd-c733-401c-a0ea-799fc0c876b8.png) | ![f1](https://user-images.githubusercontent.com/117127601/199141168-1eba2cc4-037b-4382-854c-f4c38a0a8680.PNG) |
| ![figura2](https://user-images.githubusercontent.com/117127601/199140953-72789ea7-a7bc-477c-a5d2-d8400fd97726.png) | ![f2](https://user-images.githubusercontent.com/117127601/199141174-7723d453-e810-4a8a-8330-24584b2b366d.PNG) |
