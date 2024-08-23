from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

def get_revenue_from_xbrl(file_path, key, context_ref):
    # XBRLファイルから売上高を取得する関数
    parser = EdinetXbrlParser()
    try:
        xbrl_object = parser.parse_file(file_path)
        revenue = xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
        return revenue
    except Exception as e:
        return f"データの取得に失敗しました。：{e}"
    
# 10社分のXBRLファイルパスをリストにまとめる
xbrl_file_paths = [
    "xbrl_file\Xbrl_Search_20240820_133855\S100TR7I\XBRL\PublicDoc\jpcrp030000-asr-001_E02144-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240820_133918\S100TS7P\XBRL\PublicDoc\jpcrp030000-asr-001_E01777-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134257\S100TXFX\XBRL\PublicDoc\jpcrp030000-asr-001_E02142-000_2024-03-31_01_2024-06-28.xbrl",
    "xbrl_file\Xbrl_Search_20240821_151530\S100TPY6\XBRL\PublicDoc\jpcrp030000-asr-001_E02213-000_2024-03-31_01_2024-06-21.xbrl",
    "xbrl_file\Xbrl_Search_20240821_151723\S100TRUD\XBRL\PublicDoc\jpcrp030000-asr-001_E02362-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152239\S100TS9K\XBRL\PublicDoc\jpcrp030000-asr-001_E01570-000_2024-03-31_01_2024-06-27.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152326\S100TQWG\XBRL\PublicDoc\jpcrp030000-asr-001_E25303-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152355\S100T45G\XBRL\PublicDoc\jpcrp030000-asr-001_E00990-000_2023-12-31_01_2024-03-26.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152852\S100TXZ3\XBRL\PublicDoc\jpcrp030000-asr-001_E01773-000_2024-03-31_01_2024-06-28.xbrl",
    "xbrl_file\Xbrl_Search_20240821_152907\S100T58N\XBRL\PublicDoc\jpcrp030000-asr-001_E02274-000_2023-12-31_01_2024-03-28.xbrl"
]

# タグとコンテキストは全社共通と仮定
key = "jppfs_cor:NetSales"
context_ref = "CurrentYearDuration_NonConsolidatedMember"

# 各企業から売上高を取得
for i, file_path in enumerate(xbrl_file_paths):
    revenue = get_revenue_from_xbrl(file_path, key, context_ref)
    print(f"企業{i+1}の売上高：{revenue}")