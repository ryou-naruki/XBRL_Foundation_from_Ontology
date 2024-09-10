from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from bs4 import BeautifulSoup

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_paths = [
    "xbrl_file\Xbrl_Search_20240820_133855\S100TR7I\XBRL\AuditDoc\jpaud-aai-cc-001_E02144-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240820_133918\S100TS7P\XBRL\AuditDoc\jpaud-aai-cc-001_E01777-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134257\S100TXFX\XBRL\AuditDoc\jpaud-aai-cc-001_E02142-000_2024-03-31_01_2024-06-28.xbrl",
    "xbrl_file\Xbrl_Search_20240821_151530\S100TPY6\XBRL\AuditDoc\jpaud-aai-cc-001_E02213-000_2024-03-31_01_2024-06-21.xbrl",
    "xbrl_file\Xbrl_Search_20240821_151723\S100TRUD\XBRL\AuditDoc\jpaud-aai-cc-001_E02362-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152239\S100TS9K\XBRL\AuditDoc\jpaud-aai-cc-001_E01570-000_2024-03-31_01_2024-06-27.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152326\S100TQWG\XBRL\AuditDoc\jpaud-aai-cc-001_E25303-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152355\S100T45G\XBRL\AuditDoc\jpaud-aai-cc-001_E00990-000_2023-12-31_01_2024-03-26.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152852\S100TXZ3\XBRL\AuditDoc\jpaud-aai-cc-001_E01773-000_2024-03-31_01_2024-06-28.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152907\S100T58N\XBRL\AuditDoc\jpaud-aai-cc-001_E02274-000_2023-12-31_01_2024-03-28.xbrl"
]

# おまけ：正規表現を用いてディレクトリ内すべてのXBRLファイルから情報を抽出する(上記のxbrl_file_pathsを以下に変えればディレクトリ内にあるXBRLファイルすべてを対象にKAMを抽出できる)
# xbrl_file_paths = glob.glob(r"xbrl_file\*2024*\*\XBRL\AuditDoc\*aai*.xbrl")


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