# Neural Search for Fashion Products

This repo aims to build a image-to-image & text-to-image search engine for fashion products using Jina as a neural search framework. 

The fashion images are retrieved form **[Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small)**.


Jina includes:

- **[DocumentArray](https://docarray.jina.ai)** - Concurrent processing of Documents and push/pull them between machines. Useful for creating embeddings on remote machine with GPU and then indexing and querying locally
- **[Jina Hub](https://hub.jina.ai)** Executors, which integrate deep learning models
- **[Jina Client](https://docs.jina.ai/api/jina.clients/)**, formats the REST request
- **[PQLite](https://hub.jina.ai/executor/pn1qofsj)** allowing us to pre-filter results by price, rating, etc

The front-end is built in [Streamlit](https://streamlit.io/).

## Adapt the model application for your own needs

### Setup

`pip install -r requirements.txt`

### Download and clean up data

You'll want to create your own `get_data.py` since processing logic varies from dataset to dataset. 

### Create embeddings and index your data

This will create embeddings for all images using CLIPImageEncoder, and then store them on disk (with metadata) with PQLiteIndexer.

1. `cd indexer`
2. `python app.py <number_of_docs_to_index>`

By default the number of docs to index is set to 1,000,000.

### Copy over columns

After indexing you'll have a file called `columns.json` in your `indexer` directory. Copy this to the `backend-` directories you want to work with. This will let the user filter by things like price, rating, color, etc (based on what options you present in your front-end). This will overwrite the existing `columns.json` file(s) which are the ones from the fashion search.

### Run search backend

From the repo's root directory:

1. `cd searcher`
2. `python app.py -t <task>` to start the search server(s)

`<task>` can be one of:

- `search`: Open up a RESTful interface for searching. Defaults to port 12345
- `test_text` - Submit a sample text query and return `uri`s of results
- `test_image` - Submit a sample image query and return `uri`s of results

### Run frontend

1. Open a new terminal window/tab, return to same directory
2. `cd frontend`
3. `streamlit run frontend.py`

## With Docker-compose

1. First index the data as stated above
2. In the repo's root directory, run `docker-compose up` 