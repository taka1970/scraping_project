import asyncio
import os
from scraper.fetch import fetch_page
from scraper.parser import parse_items
from scraper.save import save_to_csv

# どこから実行してもプロジェクトフォルダに移動する（タスクスケジューラ対策）
os.chdir(os.path.dirname(os.path.abspath(__file__)))

URL = "https://www.amazon.co.jp/dp/B0C2KKR2QH"

async def main():
    print("Fetching page...")
    html = await fetch_page(URL)   # ← ここが最重要（await 必須）

    print("Parsing items...")
    items = parse_items(html)

    print("Saving to CSV...")
    save_to_csv(items)

    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
