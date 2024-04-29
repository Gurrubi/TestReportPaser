Ejecucion del script:

Te deberás posicionar en el directorio de este archivo con la terminal y entonces ejecutar: python3 main.py
Una vez ejecutado se generará un archivo .txt, sigue leyendo.

Funcionamiento:

Este programa se encarga de parsear los archivos TestReport.md, a un archivo .txt que se guarda en este mismo directorio con el código c++ de los test, además lo
parsea de forma que no tengas que compilar y ejecutar por cada test, si no que con compilar y ejecutar una vez es suficiente. Hay algunos test que fallan por como
esta hecho el TestReport.md, asi que cuando compileis os dará error, comentad los test que os dan error, en netbeans os aparecerán algunas lineas en rojo, y ya
probadlos por vuestra cuenta.

Una vez compilado, comentado los test que ocasionen error (son pocos), entonces tendreís que ejecutar, y os aparecerá en la ejecución si habeís pasado los test
correspondientes.

Cosas que hay que tener en cuenta para el funcionamiento correcto del programa:
	· Arrojar dentro de este directorio el archivo TestReport.md correspondiente a parsear (Ahora mismo tiene el de Kmer3)
	· En el archivo parseInput.py, existe una variable: ID_FINAL_TEST, que tendreís que modificar para otros test diferentes de Kmer3, esta variable contiene el ID del ultimo test a parsear.
	· Necesitas tener instalado python en tu ordenador
	· Para la ejecución del script abre una terminal con el directorio donde esta este archivo y ejecute el siguiente comando: python3 main.py
