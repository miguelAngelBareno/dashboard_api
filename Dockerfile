#imagen a utilizar con su correspondiente version
FROM python:3.8
#sirve para poder ver los mensajes de log tal cual como si estuviera en un entorno virtal
ENV PYTHONUNBUFFERED=1

RUN apt-get update
#Creacion de carpeta dentro del contenedor
RUN mkdir /code

#indicacion de cual va ha ser la carpeta de trabajo
WORKDIR /code

#copia del archivo de requerimentos(directorio amfrition actual) hacia la carpeta interna del contenedor
COPY ./requirements.txt /code/
# COPY ./requirements.txt /code/

#ejecuta el siguiente comando en el contenedor
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# EXPOSE 8000

#comando de consola para iniciar el servidor, y exponer el puerto 8000  a externos
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]