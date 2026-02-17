import requests, os, time

# 遠端檔案網址 (請替換成你的網址)
VERSION_URL = "https://gist.githubusercontent.com/MichaelLi1976/8f963d9173ddf35b7fdce121980aa919/raw/90fe4b64cb1453e49fc48ef05d543a8ce02a64c3/version.txt"
CODE_URL = "https://gist.githubusercontent.com/MichaelLi1976/8f963d9173ddf35b7fdce121980aa919/raw/90fe4b64cb1453e49fc48ef05d543a8ce02a64c3/api_logic.py"

def run_update_and_exec():
    while True:
        try:
            # 1. 版本檢查
            remote_v = requests.get(VERSION_URL).text.strip()
            local_v = ""
            if os.path.exists("v.txt"):
                with open("v.txt", "r") as f: local_v = f.read().strip()

            # 2. 有新版才下載
            if remote_v != local_v:
                code = requests.get(CODE_URL).text
                with open("logic.py", "w") as f: f.write(code)
                with open("v.txt", "w") as f: f.write(remote_v)
            
            # 3. 執行下載的程式碼
            exec(open("logic.py").read(), globals())
            break
        except:
            time.sleep(10) # 失敗則每 10 秒重試

if __name__ == '__main__':
    run_update_and_exec()
