from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

parser = EdinetXbrlParser()

# 対象のXBRLファイルを指定
xbrl_file_path = ""
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

# 対象企業の売掛金を取得
key = ""
context_ref = ""
current_year_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
