from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
import glob

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
xbrl_file_paths = glob.glob(r"XBRL_files\Xbrl_Search_2024*\*\XBRL\PublicDoc\*.xbrl")

# タグとコンテキストは全社共通と仮定
key = "jppfs_cor:NetSales"
context_ref = "CurrentYearDuration_NonConsolidatedMember"

# 各企業から売上高を取得
for i, file_path in enumerate(xbrl_file_paths):
    revenue = get_revenue_from_xbrl(file_path, key, context_ref)
    print(f"企業{i+1}の売上高：{revenue}")