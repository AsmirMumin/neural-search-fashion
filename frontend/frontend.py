import streamlit as st

from helper import (
    get_matches,
    print_stars,
    get_matches_from_image,
    facets,
)
from config import (
    TOP_K,
    SERVER,
    DEBUG
)

filters = {
    "$and": {
        "price": {},
        "rating": {},
        "season": {},
        "category": {},
        "gender": {},
        "baseColor": {},
        # "year": {},
    }
}

title = "Neural Search for Fashion Products 👕"

st.set_page_config(page_title=title, layout="wide")

# Sidebar
st.sidebar.title("Options")

input_media = st.sidebar.radio(label="Search using...", options=["text", "image"])


filters["$and"]["category"]["$in"] = st.sidebar.multiselect(
    "Category", facets.category, default=facets.category
)

filters["$and"]["gender"]["$in"] = st.sidebar.multiselect(
    "Gender", facets.gender, default=facets.gender
)
filters["$and"]["season"]["$in"] = st.sidebar.multiselect(
    "Season", facets.season, default=facets.season
)
(
    filters["$and"]["price"]["$gte"],
    filters["$and"]["price"]["$lte"],
) = st.sidebar.slider("Price", 4.99, 499.99, (4.99, 499.99))

filters["$and"]["rating"]["$gte"] = st.sidebar.slider("Minimum rating", 0, 5, 0)
limit = st.sidebar.slider(
    label="Maximum results",
    min_value=int(TOP_K / 3),
    max_value=TOP_K * 3,
    value=TOP_K,
)
filters["$and"]["baseColor"]["$in"] = st.sidebar.multiselect(
    "Color", facets.color, default=facets.color
)
# (
# filters["$and"]["year"]["$gte"],
# filters["$and"]["year"]["$lte"],
# ) = st.sidebar.slider("Year", 2007, 2019, (2007, 2019))


if DEBUG:
    with st.sidebar.expander("Debug"):
        server = st.text_input(label="Server", value=SERVER)
else:
    server = SERVER

st.sidebar.title("About")

st.sidebar.markdown(
    """This example lets you use a *textual* description to search through *images* of fashion items using [Jina](https://github.com/jina-ai/jina/).

#### Why are the images so pixelated?

To speed up indexing, low-resolution graphics were used.

"""
)

st.sidebar.markdown(
    "[Repo link](https://github.com/AsmirMumin/neural-search-fashion)"
)

# Main area
st.title(title)

if input_media == "text":
    text_query = st.text_input(label="Search term", placeholder="Blue shirt")
    text_search_button = st.button("Search")
    if text_search_button:
        matches = get_matches(
            input=text_query,
            limit=limit,
            filters=filters,
            server=server,
        )

elif input_media == "image":
    image_query = st.file_uploader(label="Image file")
    image_search_button = st.button("Search")
    if image_search_button:
        matches = get_matches_from_image(
            input=image_query,
            limit=limit,
            filters=filters,
            server=server,
        )

if "matches" in locals():
    for match in matches:
        pic_cell, desc_cell, price_cell = st.columns([1, 6, 1])
        pic_cell.image(match.tags["image_url"])
        desc_cell.markdown(
            f"##### {match.tags['productDisplayName']} {print_stars(match.tags['rating'])}"
        )
        desc_cell.markdown(
            f"*{match.tags['masterCategory']}*, *{match.tags['subCategory']}*, *{match.tags['articleType']}*, *{match.tags['baseColour']}*, *{match.tags['season']}*, *{match.tags['usage']}*, *{match.tags['year']}*"
        )
        price_cell.button(key=match.id, label=str(match.tags["price"]))
