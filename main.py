from fastapi import FastAPI, Request


app = FastAPI()

@app.get("/webhooks")
async def verify():
    # Verifica el token de verificación

    if request.query_params.get("hub.challenge") != "1158201444":
        return Response(content="El desafío no es correcto", status_code=403)

    if request.query_params.get("hub.verify_token") != "wh":
        return Response(content="El token de verificación no es correcto", status_code=403)

    # Devuelve el desafío

    return Response(content="1158201444", status_code=200)
