from playwright.sync_api import sync_playwright

def get_page_html(url: str) -> str:
    """
    Playwright を使って動的サイトの HTML を取得する関数。
    低スペックPCでも安定して動くように最適化済み。
    """

    with sync_playwright() as p:
        # Chromium をヘッドレス（画面なし）で起動 → 軽い
        browser = p.chromium.launch(headless=True)

        # 新しいページを作成
        page = browser.new_page()

        # Cloudflare 対策（User-Agent を偽装）
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

        # ページにアクセス
        page.goto(url, timeout=60000)

        # ネットワークが落ち着くまで待つ（JSレンダリング対策）
        page.wait_for_load_state("networkidle")

        # HTML を取得
        html = page.content()

        # ブラウザを閉じる
        browser.close()

        return html
