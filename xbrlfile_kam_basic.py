from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_path = "xbrl_file\Xbrl_Search_20240820_133855\S100TR7I\XBRL\AuditDoc\jpaud-aai-cc-001_E02144-000_2024-03-31_01_2024-06-25.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

# タクソノミを指定
key = "jpcrp_cor:KeyAuditMattersConsolidatedTextBlock"
context_ref = "FilingDateInstant"

# KAMを取得
try:
    kam = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    
    # BeautifulSoupを使ってHTMLタグを除去
    soup = BeautifulSoup(kam, "html.parser")
    kam_cleaned = soup.get_text()
    
    print(f"監査上の主要な検討事項（タグ除去後）：{kam_cleaned}")
except Exception as e:
    print(f"データの取得に失敗しました。：{e}")