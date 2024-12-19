import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a request to create a catalog item.")

    # Carregar variáveis de ambiente
    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]
    database_name = "CatalogDatabase"
    container_name = "CatalogCollection"

    # Conexão com o Cosmos DB
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Processar entrada
    try:
        catalog_item = req.get_json()
        container.create_item(body=catalog_item)
        return func.HttpResponse(
            json.dumps({"message": "Catalog item created successfully!"}),
            status_code=201
        )
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
