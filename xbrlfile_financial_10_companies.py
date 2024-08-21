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
    "xbrl_file\Xbrl_Search_20240820_134037\S100TL6G\XBRL\PublicDoc\jpcrp030000-asr-001_E02529-000_2024-03-31_01_2024-06-21.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134126\S100TP3N\XBRL\PublicDoc\jpcrp030000-asr-001_E02778-000_2024-03-31_01_2024-06-21.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134142\S100TG6G\XBRL\PublicDoc\jpcrp030000-asr-001_E03061-000_2024-02-29_01_2024-05-30.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134227\S100SD9V\XBRL\PublicDoc\jpcrp030000-asr-001_E03217-000_2023-08-31_01_2023-11-30.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134244\S100TQZC\XBRL\PublicDoc\jpcrp030000-asr-001_E01772-000_2024-03-31_01_2024-06-25.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134257\S100TXFX\XBRL\PublicDoc\jpcrp030000-asr-001_E02142-000_2024-03-31_01_2024-06-28.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134311\S100TO15\XBRL\PublicDoc\jpcrp030000-asr-001_E31748-000_2024-03-31_01_2024-06-20.xbrl",
    "xbrl_file\Xbrl_Search_20240820_134355\S100TN7R\XBRL\PublicDoc\jpcrp030000-asr-001_E04425-000_2024-03-31_01_2024-06-20.xbrl"
]

# タグとコンテキストは全社共通と仮定
key = "jppfs_cor:NetSales"
context_ref = "CurrentYearDuration_NonConsolidatedMember"

# 各企業から売上高を取得
for i, file_path in enumerate(xbrl_file_paths):
    revenue = get_revenue_from_xbrl(file_path, key, context_ref)
    print(f"企業{i+1}の売上高：{revenue}")