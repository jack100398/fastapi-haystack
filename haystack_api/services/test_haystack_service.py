from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import EmbeddingRetriever
from haystack.schema import Document

# 初始化 DocumentStore (純記憶體)
document_store = InMemoryDocumentStore(embedding_dim=384)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="intfloat/e5-small-v2"
)

docs = [
    Document(content="Apple iPhone 15 Pro Max with A17 chip", meta={"id": 1, "name": "iPhone 15 Pro Max", "price": 49900}),
    Document(content="Samsung Galaxy S24 Ultra with powerful camera", meta={"id": 2, "name": "Galaxy S24 Ultra", "price": 38900}),
    Document(content="Sony WH-1000XM5 noise cancelling headphones", meta={"id": 3, "name": "Sony WH-1000XM5", "price": 11900}),
    Document(content="Apple MacBook Pro 16 inch with M3 chip", meta={"id": 4, "name": "MacBook Pro 16", "price": 79900}),
    Document(content="Dell XPS 15 high-performance laptop", meta={"id": 5, "name": "Dell XPS 15", "price": 59900}),
    Document(content="ASUS ROG Zephyrus G14 gaming laptop", meta={"id": 6, "name": "ROG Zephyrus G14", "price": 48900}),
    Document(content="Apple iPad Pro 12.9 inch with M2 chip", meta={"id": 7, "name": "iPad Pro 12.9", "price": 35900}),
    Document(content="Samsung Galaxy Tab S9 Ultra", meta={"id": 8, "name": "Galaxy Tab S9 Ultra", "price": 29900}),
    Document(content="Logitech MX Master 3S Wireless Mouse", meta={"id": 9, "name": "MX Master 3S", "price": 3500}),
    Document(content="Razer DeathAdder V3 Pro gaming mouse", meta={"id": 10, "name": "DeathAdder V3 Pro", "price": 4500}),
    Document(content="Apple AirPods Pro 2nd Generation", meta={"id": 11, "name": "AirPods Pro 2", "price": 6990}),
    Document(content="Bose QuietComfort Ultra headphones", meta={"id": 12, "name": "Bose QC Ultra", "price": 12900}),
    Document(content="Sony Alpha 7 IV full-frame mirrorless camera", meta={"id": 13, "name": "Sony A7 IV", "price": 79900}),
    Document(content="Canon EOS R8 mirrorless camera", meta={"id": 14, "name": "Canon EOS R8", "price": 49900}),
    Document(content="Nikon Z6 II mirrorless camera", meta={"id": 15, "name": "Nikon Z6 II", "price": 59900}),
    Document(content="DJI Air 3 drone with 4K camera", meta={"id": 16, "name": "DJI Air 3", "price": 45900}),
    Document(content="GoPro HERO12 Black action camera", meta={"id": 17, "name": "GoPro HERO12", "price": 13900}),
    Document(content="Samsung 55 inch Neo QLED 4K TV", meta={"id": 18, "name": "Samsung Neo QLED 55", "price": 35900}),
    Document(content="LG OLED C3 65 inch 4K TV", meta={"id": 19, "name": "LG OLED C3 65", "price": 54900}),
    Document(content="Sony Bravia XR A80L OLED TV 55 inch", meta={"id": 20, "name": "Sony Bravia XR A80L", "price": 49900}),
    Document(content="Microsoft Surface Pro 9 2-in-1 laptop", meta={"id": 21, "name": "Surface Pro 9", "price": 45900}),
    Document(content="Apple Watch Series 9 45mm", meta={"id": 22, "name": "Apple Watch Series 9", "price": 14900}),
    Document(content="Garmin Fenix 7X Pro multisport GPS watch", meta={"id": 23, "name": "Garmin Fenix 7X", "price": 25900}),
    Document(content="Fitbit Sense 2 health smartwatch", meta={"id": 24, "name": "Fitbit Sense 2", "price": 8990}),
    Document(content="Anker 737 Power Bank (PowerCore 24K)", meta={"id": 25, "name": "Anker 737 Power Bank", "price": 4990}),
    Document(content="Belkin BoostCharge Pro 3-in-1 wireless charger", meta={"id": 26, "name": "Belkin 3-in-1 Charger", "price": 6990}),
    Document(content="Philips Hue White and Color Ambiance starter kit", meta={"id": 27, "name": "Philips Hue Starter Kit", "price": 8990}),
    Document(content="Dyson V15 Detect Absolute cordless vacuum", meta={"id": 28, "name": "Dyson V15 Detect", "price": 23900}),
    Document(content="Xiaomi Mi Air Purifier 4 Pro", meta={"id": 29, "name": "Xiaomi Air Purifier 4 Pro", "price": 7990}),
    Document(content="Panasonic NN-CD87KS 4-in-1 microwave oven", meta={"id": 30, "name": "Panasonic Microwave Oven", "price": 14900}),
]

document_store.write_documents(docs)
document_store.update_embeddings(retriever=retriever)
