from kivy.app import App
from jnius import autoclass

class MainApp(App):
    def build(self):
        # 啟動 Android 背景服務
        service = autoclass('org.test.myapp.ServiceMyservice')
        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        service.start(mActivity, "")
        return None # 啟動後可關閉介面
