def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a request to get catalog items.")

    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]
    database_name = "CatalogDatabase"
    container_name = "CatalogCollection"

    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    try:
        items = [item for item in container.read_all_items()]
        return func.HttpResponse(
            json.dumps(items),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
