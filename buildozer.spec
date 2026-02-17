[app]

# (str) 應用程式標題
title = Python API Node

# (str) 套件名稱
package.name = pythonapinode

# (str) 套件域名 (唯一識別碼)
package.domain = org.michaelli1976

# (str) 原始碼目錄 (main.py 所在位置)
source.dir = .

# (list) 原始碼包含的副檔名
source.include_exts = py,png,jpg,kv,atlas

# (str) 應用程式版本
version = 0.1

# (list) 應用程式依賴項
requirements = python3,kivy,requests,flask,pyjnius,certifi

# (str) 支援的方向 (landscape, portrait, all)
orientation = portrait

# (bool) 全螢幕模式
fullscreen = 0

# (list) Android 權限
android.permissions = INTERNET,FOREGROUND_SERVICE,WAKE_LOCK

# (int) Android API 目標版本
android.api = 31

# (int) Android 最低 API 版本
android.minapi = 21

# (str) Android NDK 版本
android.ndk = 25b

# (str) Android SDK 版本
android.sdk = 31

# (bool) 自動接受 SDK 授權
android.accept_sdk_license = True

# (str) Android 架構
android.archs = arm64-v8a,armeabi-v7a

# (list) Android 服務
services = Myservice:service.py

# (str) Android 入口點
android.entrypoint = org.kivy.android.PythonActivity

# (bool) 啟用 Android 備份
android.allow_backup = True

[buildozer]

# (int) 日誌級別 (0 = 錯誤, 1 = 資訊, 2 = 除錯)
log_level = 2

# (int) 在 root 上顯示警告
warn_on_root = 1



