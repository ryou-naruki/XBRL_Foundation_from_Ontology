from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup
import glob

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_paths = glob.glob(r"xbrl_file\*2024*\*\XBRL\AuditDoc\*aai*.xbrl")

# 対象企業のタグを取得
key = "jpcrp_cor:KeyAuditMattersConsolidatedTextBlock"
context_ref = "FilingDateInstant"

# KAMを抽出
for i, file_path in enumerate(xbrl_file_paths):
    try:
        # XBRLファイルをパース
        edinet_xbrl_object = parser.parse_file(file_path)
        
        # 大きくKAMを取得
        kam = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    
        # BeautifulSoupを使ってHTMLタグを除去
        soup = BeautifulSoup(kam, "html.parser")
        kam_cleaned = soup.get_text()
    
        print(f"企業{i+1} のKAM（タグ除去後）: {kam_cleaned}")
    except Exception as e:
        print(f"企業{i+1}データの抽出に失敗しました。：{e}")