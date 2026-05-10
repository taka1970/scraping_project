import pandas as pd
from datetime import datetime
import os

def save_to_csv(items, filename="data/output.csv"):
    if not items:
        print("Warning: 保存するデータが空です。")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    # price を数値に変換
    for item in items:
        item["date"] = today
        if item["price"]:
            item["price"] = int(item["price"].replace(",", ""))

    df_new = pd.DataFrame(items)

    # ファイルが存在しない → 新規作成
    if not os.path.exists(filename):
        df_new.to_csv(filename, index=False, encoding="utf-8-sig")
        print(f"Saved {len(items)} rows to {filename}")
        return

    # 存在する → 追記
    df_existing = pd.read_csv(filename)
    df_all = pd.concat([df_existing, df_new], ignore_index=True)
    df_all.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"Saved {len(items)} rows to {filename}")
