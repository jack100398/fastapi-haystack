from fastapi import APIRouter, HTTPException

from services.openai_service import expand_query, optimize_content, filter_results
from haystack.schema import Document

from repositories.mysql_repository import MysqlRepository
from repositories.haystack_repository import HaystackRepository

from schemas.sync_request import SyncRequest

router = APIRouter()

haystack_repository = HaystackRepository(index_name="product")
mysql_repository = MysqlRepository(table_name="product")

# 透過hatstack搜尋
@router.get("/search")
def search_products(query: str, top_k: int = 5):
    results = haystack_repository.search(query, top_k)

    # results = [{"id": d.meta["id"], "name": d.meta["name"], "price": d.meta["price"], "score": d.score} for d in results]

    return {"query": query, "results": [r.to_dict() for r in results]}

# 使用openAi進行關鍵字擴充後, 透過hatstack搜尋
@router.get('/search_with_openai')
def serach_with_openai(query: str, top_k: int = 5):
    expanded_query = expand_query(query)

    results = haystack_repository.search(expanded_query, top_k)

    return {"query": expanded_query, "results": [r.to_dict() for r in results]}

# 透過hatstack搜尋後, 使用openAi對搜尋結過再做一次篩選
@router.get('/search_and_filter_by_openai')
def search_and_filter_by_openai(query: str, top_k: int = 5):
    results = haystack_repository.search(query, top_k)

    return {"query": query, "results": filter_results(query, [r.to_dict() for r in results])}

# 寫入haystack商品指定資料
@router.post('/sync')
def sync(request: SyncRequest):
    id = request.id

    product = mysql_repository.get_by_id(id)

    haystack_repository.write(product)

    return {"id": id, "product": product}

# 刪除haystack商品指定資料
@router.delete('/sync/{id}')
def sync(id: int):
    haystack_repository.delete_by_ids([id])

    return {"id": id}
