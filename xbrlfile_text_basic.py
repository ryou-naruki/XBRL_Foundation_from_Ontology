from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_path = "xbrl_file/Xbrl_Search_20240820_133855/S100TR7I/XBRL/PublicDoc/jpcrp030000-asr-001_E02144-000_2024-03-31_01_2024-06-25.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

# 対象企業の事業等のリスクを取得
key = "jpcrp_cor:BusinessRisksTextBlock"
context_ref = "FilingDateInstant"

# 非財務情報である事業等のリスクを取得
try:
    business_risk = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    
    # BeautifulSoupを使ってHTMLタグを除去
    soup = BeautifulSoup(business_risk, "html.parser")
    business_risk_cleaned = soup.get_text()
    
    print(f"事業等のリスク（タグ除去後）：{business_risk_cleaned}")
except Exception as e:
    print(f"データの取得に失敗しました。：{e}")