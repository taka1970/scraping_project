from playwright.async_api import async_playwright

async def fetch_page(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,  # ← Amazon 対策：必ず False
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True
        )

        page = await context.new_page()

        # Amazon の bot 検知を回避
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        """)

        # タイムアウトを 90 秒に延長
        await page.goto(url, timeout=90000, wait_until="domcontentloaded")

        html = await page.content()
        await browser.close()
        return html
