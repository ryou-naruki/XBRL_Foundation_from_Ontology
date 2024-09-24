from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup
import glob
import re

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_paths = glob.glob(r"xbrl_file\*2024*\*\XBRL\PublicDoc\*.xbrl")


# 対象企業のタグを取得
key = "jpcrp_cor:BusinessRisksTextBlock"
context_ref = "FilingDateInstant"

# 非財務情報である事業等のリスクを取得
for i, file_path in enumerate(xbrl_file_paths):
    try:
        # XBRLファイルをパース
        edinet_xbrl_object = parser.parse_file(file_path)
        
        # 事業等のリスクを取得
        business_risk = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    
        # BeautifulSoupを使ってHTMLタグを除去
        soup = BeautifulSoup(business_risk, "html.parser")
        business_risk_cleaned = soup.get_text()
        
        # 空白や改行を取り除く
        business_risk_cleaned = re.sub(r'\s', '', business_risk_cleaned).strip()
    
        print(f"企業{i+1}事業等のリスク：{business_risk_cleaned}")
    except Exception as e:
        print(f"企業{i+1}データの取得に失敗しました。：{e}")