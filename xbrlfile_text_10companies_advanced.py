from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup
import pandas as pd
import glob

parser = EdinetXbrlParser()

# カラム名と対応するXBRLタグのリスト
keys = {
    '会社名': "jpcrp_cor:CompanyNameCoverPage",
    '事業等のリスク': "jpcrp_cor:BusinessRisksTextBlock",
}

context_ref = "FilingDateInstant"

# データを一時的に保存するリスト
data_list = []

# XBRLファイルを対象に指定
xbrl_file_paths = glob.glob(r"xbrl_file\*2024*\*\XBRL\PublicDoc\*.xbrl")

# 各XBRLファイルでカラムの内容を取得するループ処理
for i, file_path in enumerate(xbrl_file_paths):
    try:
        # XBRLファイルをパース
        edinet_xbrl_object = parser.parse_file(file_path)
        
        # 会社ごとのデータを一時的に保存する辞書
        data = {}
        company_name = "不明"
        
        # 各項目についてデータを取得
        for column_name, key in keys.items():
            try:
                value = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
                
                # 取得したデータを確認（デバッグ用）
                print(f"企業{i+1} - {column_name}: {value}")
                
                # もし事業等のリスクでHTMLが含まれている場合、タグを除去
                if column_name == '事業等のリスク':
                    soup = BeautifulSoup(value, "html.parser")
                    value = soup.get_text()
                    
                # 会社名を取得して保存（エラーメッセージ用）
                if column_name == '会社名':
                    company_name = value
                    
                # データを辞書に保存
                data[column_name] = value
                
            except Exception as e:
                # データ取得失敗時に空データを入れる
                data[column_name] = None
                print(f"'{column_name}'の取得に失敗しました。企業名: {company_name} ファイル: {file_path} エラー: {e}")
                
        # デバッグ用に辞書をプリント
        print(f"企業{i+1}のデータ: {data}")
                
        # データがある場合にリストに追加
        if data:
            data_list.append(data)
        
    except Exception as e:
        print(f"企業名: {company_name}のデータの取得に失敗しました。ファイル: {file_path} エラー: {e}")

# データフレームに変換
df = pd.DataFrame(data_list)

# 処理完了後、データフレーム全体を表示
print(df)

# データフレームをCSVに出力
df.to_csv("business_risks_output.csv", index=False, encoding='utf-8-sig')
