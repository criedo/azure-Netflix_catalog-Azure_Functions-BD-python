def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a request to delete a catalog item.")

    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]
    database_name = "CatalogDatabase"
    container_name = "CatalogCollection"

    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    try:
        item_id = req.params.get("id")
        partition_key = req.params.get("partition_key")
        container.delete_item(item=item_id, partition_key=partition_key)
        return func.HttpResponse(
            json.dumps({"message": "Catalog item deleted successfully!"}),
            status_code=200
        )
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
