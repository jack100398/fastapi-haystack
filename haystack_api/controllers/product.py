from fastapi import APIRouter, HTTPException

from services.openai_service import expand_query, optimize_content, filter_results
from haystack.schema import Document

from repositories.mysql_repository import MysqlRepository
from repositories.haystack_repository import HaystackRepository

router = APIRouter()

haystack_repository = HaystackRepository(index_name="product")
mysql_repository = MysqlRepository(table_name="product")

@router.get("/search")
def search_products(query: str, top_k: int = 5):
    results = haystack_repository.search(query, top_k)

    # results = [{"id": d.meta["id"], "name": d.meta["name"], "price": d.meta["price"], "score": d.score} for d in results]

    return {"query": query, "results": [r.to_dict() for r in results]}

@router.get('/search_with_openai')
def serach_with_openai(query: str, top_k: int = 5):
    expanded_query = expand_query(query)

    results = haystack_repository.search(expanded_query, top_k)

    return {"query": expanded_query, "results": [r.to_dict() for r in results]}

@router.get('/search_and_filter_by_openai')
def search_and_filter_by_openai(query: str, top_k: int = 5):
    results = haystack_repository.search(query, top_k)

    return {"query": query, "results": filter_results(query, [r.to_dict() for r in results])}
