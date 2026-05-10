from bs4 import BeautifulSoup

def parse_items(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # 商品タイトル
    title_el = soup.select_one("#productTitle")
    title = title_el.get_text(strip=True) if title_el else None

    # 価格（Amazon の価格は a-price-whole）
    price_el = soup.select_one(".a-price-whole")
    price = price_el.get_text(strip=True) if price_el else None

    # Amazon の商品ページは 1 商品なのでリストで返す
    if not title and not price:
        return []

    return [{
        "title": title,
        "price": price,
        "link": None  # 必要なら URL を main.py から渡せる
    }]
