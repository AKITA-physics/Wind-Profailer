import requests
from bs4 import BeautifulSoup
import urllib.request
import io
import os
import shutil
import tarfile

# パラメータ
year = 2020 # データを取得する年数

# -----------------------------------------------------------------月から末尾を特定する関数---------------------------------------------------------------
def month_day(month):
    if month in [1,3,5,7,8,10,12]:
        last_day = 31
    elif month in [4,6,9,11]:
        last_day = 30
    elif month in [2]:
        last_day = 28
    return last_day

# --------------------------------------------------------webサイトからファイルのURLを取得する関数---------------------------------------------------------
def extract_urls_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    list_urls = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('IUPC'):
            list_urls.append(href)
    return list_urls

# --------------------------------------------------webサイトからファイルのURLを取得し、リストにまとめる---------------------------------------------------
for month in range(1,12+1):
    for day in range(1,month_day(month)+1):
        if day < 10 and month < 10:
            # ウェブページのURLを指定して実行
            webpage_url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/0'+str(month)+'/0'+str(day)+'/'
        elif day >= 10 and month < 10:
            # ウェブページのURLを指定して実行
            webpage_url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/0'+str(month)+'/'+str(day)+'/'
        elif day < 10 and month >= 10:
            # ウェブページのURLを指定して実行
            webpage_url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/'+str(month)+'/0'+str(day)+'/'
        elif day >= 10 and month >= 10:
            # ウェブページのURLを指定して実行
            webpage_url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/'+str(month)+'/'+str(day)+'/'
        list_urls = extract_urls_from_webpage(webpage_url)

        #--------------------------------------------------------------------データの取得-------------------------------------------------------------------------
        # 高層データのURL
        for part_url in list_urls:
            if day < 10 and month < 10:
                # ウェブページのURLを指定して実行
                url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/0'+str(month)+'/0'+str(day)+'/'+str(part_url)
            elif day >= 10 and month < 10:
                # ウェブページのURLを指定して実行
                url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/0'+str(month)+'/'+str(day)+'/'+str(part_url)
            elif day < 10 and month >= 10:
                # ウェブページのURLを指定して実行
                url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/'+str(month)+'/0'+str(day)+'/'+str(part_url)
            elif day >= 10 and month >= 10:
                # ウェブページのURLを指定して実行
                url = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/wprof/original/'+str(year)+'/'+str(month)+'/'+str(day)+'/'+str(part_url)
            
            # ファイルをダウンロード
            response = urllib.request.urlopen(url)
            
            # tar.gzファイルを展開
            with tarfile.open(fileobj=io.BytesIO(response.read()), mode='r:gz') as tar:
                tar.extractall()
        #-----------------------------------------------------------指定したファイルを特定のファイルに移す-----------------------------------------------------------------
        # ディレクトリ内の全ファイルを走査
        for filename in os.listdir("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究"):
            for j in range(41,50+1):
                if filename[4:6] == str(j):
                    source_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究", filename)
                    # ファイルを処理するコードをここに記述
                    # print(f"該当ファイル: {source_file_path}"
                    if j == 41:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47406_47417_47423.send" %(year), filename)
                    elif j == 42:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47585_47587_47590_47570.send" %(year), filename)
                    elif j == 43:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47626_47629_47674.send" %(year), filename)
                    elif j == 44:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47612_47640_47656.send" %(year), filename)
                    elif j == 45:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47636_47663_47616.send" %(year), filename)
                    elif j == 46:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47755_47893_47898.send" %(year), filename)
                    elif j == 47:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47819_47815_47822.send" %(year), filename)
                    elif j == 48:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47800_47805_47836_47912.send" %(year), filename)
                    elif j == 49:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47678_47795_47746.send" %(year), filename)
                    elif j == 50:
                        destination_file_path = os.path.join("C:\\Users\\AKITA KOSUKE\\Box\\1_修士課程研究\\高層データ\\%04d_47848_47909_47945.send" %(year), filename)
                    
                    # ファイルを移動する
                    shutil.move(source_file_path, destination_file_path)
                    # print(f"ファイルを移動しました: {destination_file_path}")
        print(month, day)