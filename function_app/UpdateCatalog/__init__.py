def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a request to update a catalog item.")

    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]
    database_name = "CatalogDatabase"
    container_name = "CatalogCollection"

    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    try:
        catalog_item = req.get_json()
        container.upsert_item(catalog_item)
        return func.HttpResponse(
            json.dumps({"message": "Catalog item updated successfully!"}),
            status_code=200
        )
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
