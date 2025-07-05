import winreg

class AutoStart:
    @staticmethod
    def ensure_startup(app_name, exe_path):
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
        except Exception:
            pass  # Silently ignore startup failure
