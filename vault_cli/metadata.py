import importlib.metadata
from typing import Mapping, Optional



def extract_metadata() -> Mapping[str, Optional[str]]:

    metadata_obj = importlib.metadata.metadata("vault-cli")

    return {
        "author": metadata_obj["author"],
        "email": metadata_obj["author-email"],
        "license": metadata_obj["license"],
        "url": metadata_obj["home-page"],
        "version": metadata_obj["version"],
    }
