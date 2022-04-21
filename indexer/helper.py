from docarray import DocumentArray, Document
from config import DATA_DIR, CSV_FILE
import random
import os

def generate_price(minimum=4.95, maximum=499.99):
    price = random.randrange(minimum, maximum)

    return price


def remove_tensor(doc):
    doc.tensor = None

    return doc


def process_doc(doc):
    if hasattr(doc, "id"):
        filename = f"{DATA_DIR}/{doc.id}.jpg"
        if os.path.isfile(filename):
            doc.uri = filename

            # Generate fake price
            doc.tags["price"] = generate_price()

            # Generate fake rating based on id
            random.seed(int(doc.id))  # Ensure reproducability
            doc.tags["rating"] = random.randrange(0, 5)
            doc = doc.load_uri_to_image_tensor()

    return doc


def csv_to_docarray(file_path=CSV_FILE, max_docs=100):
    docs = DocumentArray.from_csv(file_path, size=max_docs)
    docs.apply(process_doc)

    return docs


def get_columns(document):
    """
    Return a list of tuples, each tuple containing column name and type
    """
    # tags = document.tags.to_dict()
    tags = document.tags
    names = list(tags.keys())
    types = list(tags.values())
    columns = []

    for field, value in zip(names, types):
        try:
            value = int(value)  # Handle year better
        except:
            pass

        if isinstance(value, str):
            value = "str"
        elif isinstance(value, int):
            value = "int"

        col = (field, value)
        columns.append(col)

    return columns
