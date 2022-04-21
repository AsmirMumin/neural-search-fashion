# Neural Search for Fashion Products

This repo aims to build a image-to-image & text-to-image search engine for fashion products using Jina as a neural search framework. 

The fashion images are retrieved form **[Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small)**.



Jina includes:

- **[DocumentArray](https://docarray.jina.ai)** - Concurrent processing of Documents and push/pull them between machines. Useful for creating embeddings on remote machine with GPU and then indexing and querying locally
- **[Jina Hub](https://hub.jina.ai)** Executors, which integrate deep learning models
- **[Jina Client](https://docs.jina.ai/api/jina.clients/)**, formats the REST request
- **[PQLite](https://hub.jina.ai/executor/pn1qofsj)** allowing us to pre-filter results by price, rating, etc

The front-end is built in [Streamlit](https://streamlit.io/).
