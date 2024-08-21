from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_path = "xbrl_file/Xbrl_Search_20240820_133855/S100TR7I/XBRL/PublicDoc/jpcrp030000-asr-001_E02144-000_2024-03-31_01_2024-06-25.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

# 対象企業の売上高を取得
key = "jpcrp_cor:NetSalesSummaryOfBusinessResults"
context_ref = "CurrentYearDuration_NonConsolidatedMember"
try:
    current_year_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    print(f"売上高: {current_year_assets}")
except Exception as e:
    print(f"データの取得に失敗しました。:{e}")
