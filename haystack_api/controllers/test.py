from fastapi import APIRouter
from services.test_haystack_service import retriever
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
router = APIRouter()

@router.get("/search")
def search(query: str, top_k: int = 5):
    docs = retriever.retrieve(query, top_k=top_k)
    results = [
        {
            "id": d.meta.get("id"),
            "name": d.meta.get("name"),
            "price": d.meta.get("price"),
            "score": d.score
        }
        for d in docs
    ]
    return {"query": query, "results": results}


@router.get("/search_with_openAi")
def search(query: str, top_k: int = 5):
    prompt = f"請優化以下搜尋查詢，以便獲得更精確的結果：\n{query}\n請提供更完整的查詢句子。"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是搜尋查詢的優化助手。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()
