[app]

# 基本資訊
title = Python API Node
package.name = pythonapinode
package.domain = org.michaelli1976

# 原始碼
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本
version = 0.1

# 🔥 簡化依賴項 - 先測試基本功能
requirements = python3,kivy

# 顯示設定
orientation = portrait
fullscreen = 0

# Android 設定
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# 🔥 暫時移除服務
# services = Myservice:service.py

[buildozer]
log_level = 2
warn_on_root = 0





