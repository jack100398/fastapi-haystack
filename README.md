# 搜尋引擎 DEMO

## 專案建置
1. 啟動
    ```
    docker compose up -d
    ```
2. 觀察 fastApi 服務狀況
    ```
    docker compose logs fastapi -f

    等出現類似以下輸出後, 才是api服務建置完成
    INFO:     Started server process [8]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
3. PostMan測試url, 可參考app.py做延伸
    ```
    http://localhost:8000/product/search?query=airpod
    http://localhost:8000/product/search_with_openai?query=airpod
    ```
4. 結束開發
    ```
    docker compose down
    ```

## 技術
- docker-compose
- fastapi
- haystack
- openAi
- elasticsearch

## 環境檔案介紹
- docker-compose.yml => docker 服務管理器
- Dockerfile => fastapi 服務主體建置檔
- requirements.txt => fastapi(python) 環境需要安裝的套件, 在Dockerfile build時會進行安裝

## 專案結構介紹
- haystack_api => 專案資料夾
- app.py => 總進入點, 可視同 laravel index.php
- controllers => 控制器, 程式與api主流程控制
- repositories => 資料控制
- services => 商業邏輯程式區塊
- schemas => 資料結構定義

## 檔案介紹
- haystack_api/controllers/product.py - 商品搜尋引擎demo
- haystack_api/repositories/haystack_repository.py - haystack 共用邏輯, 注入索引名稱後, 可對單一資料集進行操作
- haystack_api/repositories/mysql_repository.py - mysql 共用邏輯, 注入資料表名稱後, 可對單一資料表進行操作
- haystack_api/schemas/sync_request.py - 需同步項目資料結構
- haystack_api/services/openai_service.py - OpenAi(ChatGpt) 呼叫Demo
- haystack_api/controllers/test.py - haystack 測試用, 使用 memory 進行存放, 環境重啟後內容會消失
- haystack_api/services/test_haystack_service.py - haystack 測試用
  