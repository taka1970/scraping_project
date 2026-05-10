import pandas as pd
import matplotlib.pyplot as plt
import re

def plot_price_history(csv_path="data/output.csv"):
    df = pd.read_csv(csv_path)

    # 列名を完全クリーン化（BOM、空白、制御文字、不可視文字を除去）
    df.columns = (
        df.columns
        .str.replace(r"[\ufeff\u200b\u200c\u200d\uFEFF]", "", regex=True)  # BOM/ゼロ幅スペース除去
        .str.replace(r"[^\x20-\x7Eぁ-んァ-ン一-龥0-9_]", "", regex=True)  # 制御文字除去
        .str.strip()
    )

    print("列名:", df.columns.tolist())  # デバッグ用（1回だけ表示される）

    # price 列が存在するかチェック
    if "price" not in df.columns:
        raise ValueError("CSV の列名に 'price' が見つかりません。列名を確認してください。")

    # price を数値に変換
    df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)

    # date が空の行を除外
    df = df.dropna(subset=["date"])
    df = df[df["date"].astype(str).str.strip() != ""]

    # date を文字列として扱う
    df["date"] = df["date"].astype(str)

    # 日付でソート
    df = df.sort_values("date")

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["price"], marker="o", linestyle="-", color="blue")

    plt.title("Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (JPY)")
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.tight_layout()
    plt.show()
