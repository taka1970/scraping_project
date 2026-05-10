import pandas as pd
import matplotlib.pyplot as plt

def plot_price_history(csv_path="data/output.csv"):
    df = pd.read_csv(csv_path)

    # 日付を datetime 型に変換
    df["date"] = pd.to_datetime(df["date"])

    # 日付でソート
    df = df.sort_values("date")

    # グラフ描画
    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["price"], marker="o", linestyle="-", color="blue")

    plt.title("Nintendo Switch 価格推移")
    plt.xlabel("日付")
    plt.ylabel("価格（円）")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_price_history()
