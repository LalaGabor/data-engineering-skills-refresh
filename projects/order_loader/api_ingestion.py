# Get Test JSON from https://jsonplaceholder.typicode.com/users

import requests, logging, json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

source_api = "https://jsonplaceholder.typicode.com/users"

def ingest_api():
    logger.info("Starting load via api at %s", source_api)
    # ingest the data from api
    try:
        ingest = requests.get(source_api, timeout=10)
        # check if the ingest was successful
        if ingest.status_code in range(200,300):
            data = ingest.json()
            if not isinstance(data,list):
                raise ValueError("data is not a list")
            for record in data:
                if not isinstance(record, dict):
                    raise ValueError("record is not a dictionary")
            required_keys = ["id", "name"]
            for record in data:
                for key in required_keys:
                    if key not in record:
                        raise ValueError(f"required {key} missing")
            logger.info("Loaded %s records", len(data))
            return data
        else:
            # if unsuccessful print error and raise Exception
            logger.error("API request failed with status %s",ingest.status_code)
            raise Exception
    except json.JSONDecodeError:
        logger.error("json invalid from %s", source_api)
        raise
    except requests.exceptions.Timeout:
        logger.error("timeout loading from %s", source_api)
        raise


    