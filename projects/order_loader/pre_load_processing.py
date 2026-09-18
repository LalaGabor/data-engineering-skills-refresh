import json, logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def clean_records(records):
    logger.info("Starting clean %s", records)
    cleaned_records = []
    #try:
    for item in records:
        clean_name = item["name"].strip().lower()
        clean_email = item["email"].strip().lower()
        clean_username = item["username"].strip().lower()
        cleaned_item = {**item, "name":clean_name, "username":clean_username, "email":clean_email}
        cleaned_records.append(cleaned_item)
    return cleaned_records
