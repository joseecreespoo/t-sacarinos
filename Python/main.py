from fastapi import FastAPI
from Functions import *

#creamos la api
app = FastAPI()

#implementamos el metodo get para obtener la información a traves de una peticion get

@app.get("/obtenerInformacion")
def obtenerInformacion():
    return FuncionesParaElTrabajito.searchCarIDS()