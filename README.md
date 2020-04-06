# Automatización básica en Python

Link de las diapositivas --> https://docs.google.com/presentation/d/1U2NhWyWJL4YH0wy0bHYXUyWiEI2YL7XoclPgeSkBwok/edit?usp=sharing

Setup
----------

 - Verificar que se tiene Python 3.6.X instalado
``` shell
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more informatio
```
 - Instalar pip
``` shell
$ sudo apt install python3-pip
```
 - Instalar [Python bindings for Selenium](https://pypi.python.org/pypi/selenium)
``` shell
$ pip3 install selenium
```
 - Descargar [geckodriver](https://github.com/mozilla/geckodriver/releases) y poner la ruta del ejecutable en el PATH. 
``` shell
$ export PATH=$PATH:/path/to/geckodriver

```
 - Clonar este repo
``` shell
$ git clone https://github.com/Nany262/automatizacion-basica-python.git
```

Corre el script
----------
``` shell
$ python3 automation_practice_script.py
```