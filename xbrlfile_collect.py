import requests
import datetime
import os 

def make_day_list(start_date, end_date):
    print("start_date:", start_date)
    print("end_date:", end_date)
    
    period = end_date - start_date
    period = int(period.days)
    day_list = []
    for d in range(period + 1):
        day = start_date + datetime.timedelta(days=d)
        day_list.append(day)
    
    return day_list

# 有価証券報告書を取得してくる関数
def make_doc_id_list(day_list):
    securities_report_doc_list = []
    for index, day in enumerate(day_list):
        url = "https://disclosure.edinet-fsa.go.jp/api/v2/documents.json"
        params = {"date": day.strftime("%Y-%m-%d"), "type": 2, "Subscription-Key":"ec5a18a342df4b4d946eff27ed326005"} # Subscription-Keyは自分のAPIキーを使用
    
        
        
        res = requests.get(url, params=params)
        json_data = res.json()
        print(day)
        
        if "results" in json_data:
            for num in range(len(json_data["results"])):
                ordinance_code = json_data["results"][num]["ordinanceCode"]
                form_code = json_data["results"][num]["formCode"]
                
                if ordinance_code =="010"and form_code =="030000":
                    print(json_data["results"][num]["filerName"], json_data["results"][num]["docDescription"],
                        json_data["results"][num]["docID"])
                    securities_report_doc_list.append(json_data["results"][num]["docID"])
                    
    return securities_report_doc_list

# XBRLファイルをZIP形式でダウンロードする関数
def download_xbrl_in_zip(securities_report_doc_list, number_of_lists):
    save_dir = "G:/マイドライブ/XBRL_file/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for index, doc_id in enumerate(securities_report_doc_list):
        print(doc_id, ":", index + 1, "/", number_of_lists)
        url =f"https://disclosure.edinet-fsa.go.jp/api/v2/documents/{doc_id}"
        params = {"type": 1,  "Subscription-Key":"ec5a18a342df4b4d946eff27ed326005"} # Subscription-Keyは自分のAPIキーを使用
        filename = os.path.join(save_dir, f"{doc_id}.zip")
        res = requests.get(url, params=params, stream=True)
        
        if res.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in res.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Downloaded and Saved: {filename}")
        else:
            print(f"Failed to download file {doc_id}, status code: {res.status_code}")    
  
# 上記2つの関数を実行する  
def main():
    # 集める期間を設定する
    start_date = datetime.date(2024, 5, 1) # 随時変更
    end_date = datetime.date(2024, 5, 31) # 随時変更
    day_list = make_day_list(start_date, end_date)
    
    securities_report_doc_list = make_doc_id_list(day_list)
    number_of_lists = len(securities_report_doc_list)
    print("number_of_lists: ", number_of_lists)
    print("get_list: ", securities_report_doc_list)
    
    download_xbrl_in_zip(securities_report_doc_list, number_of_lists)
    print("download finish")
    
    
if __name__ == "__main__":
    main()