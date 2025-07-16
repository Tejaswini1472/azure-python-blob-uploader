import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

# Function 1
@app.route(route="upload_handler", auth_level=func.AuthLevel.ANONYMOUS)
def upload_handler(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function upload_handler triggered.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "Please provide a name in query or body.",
            status_code=200
        )

# Function 2
@app.route(route="upload_handler_v2", auth_level=func.AuthLevel.ANONYMOUS)
def upload_handler_v2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function upload_handler_v2 triggered.')
    return func.HttpResponse("This is v2 of the upload handler.")

# Function 3 - Blob trigger

@app.blob_trigger(arg_name="myblob", path="tejafirstcontainer/{name}", connection="BlobStorageConnectionString")
def BlobTrigger(myblob: func.InputStream):
    logging.info(f"Processed blob: Name: {myblob.name}, Size: {myblob.length} bytes")

# Function 4
@app.route(route="upload_handler_v3", auth_level=func.AuthLevel.ANONYMOUS)
def upload_handler_v3(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function upload_handler_v3 triggered.')
    return func.HttpResponse("This is v3 of the upload handler.")
