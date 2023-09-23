from fastapi import FastAPI
from pydantic import BaseModel
import jsonify
import requests

class Item(BaseModel):
    name: str
    description: str 
    price: float
    tax: float 


app = FastAPI()



@app.route("/webhook/", methods=["POST","GET"])
async def create_item(item: Item):
    #SI HAY DATOS RECIBIDOS VIA GET
    if requests.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        if requests.args.get('hub.verify_token') == "HolaNovato":
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return requests.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    #RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data=requests.get_json()
    
    return jsonify({data}, 200)


