from selenium_profiles.webdriver import Chrome

kwargs = {}

driver = Chrome(
    # 只能指定之一"cdp", "options", "proxy"
    # profile["options"]，只能是之一："sandbox", "headless", "load_images", "incognito", "touch", "app", "gpu",
    #                               "proxy", "args", "capabilities", "experimental_options", "adb", "adb_package",
    #                               "use_running_app",
    #                               "extension_paths",
    profile=None,
    chrome_binary=None,
    executable_path=None,
    # 默认是webdriver.ChromeOptions()，有项to_capabilities
    options=None,
    duplicate_policy="warn-add",
    safe_duplicates=[],

    # 合到base_drivers，根据选项找到的webdriver会在这里的前面
    base_drivers=None,
    # 一起决定用uc还是wire里的还是wire里的uc
    # seleniumwire_options合到kwargs
    # 不用uc的话，会自己配置一些script选项
    uc_driver=True, seleniumwire_options={},
    # 这个干啥的？？？
    injector_options={},
    # driverless模块的参数
    driverless_options=None,
    # 增加seleniumwire_options:seleniumwire_options,
    # 增加driver_executable_path: executable_path
    # 增加options
    **kwargs,
)

from seleniumwire.webdriver import Chrome, ChromeOptions

# 自己起了个代理，DriverCommonMixin
driver1 = Chrome(
    # auto_config=True时，seleniumwire_options里的选项会合并到chrome_options里
    # 代理地址: addr, port
    # 代理里用：ca_cert, ca_key, verify_ssl, suppress_connection_errors, disable_capture
    seleniumwire_options={},
    # 前者优先，是selenium.webdriver.ChromeOptions
    chrome_options={}, options={}
)

# selenium.webdriver.chromium.webdriver.ChromiumDriver
# webdriver的位置，在options里指定，但会通过运行selenium-manager，得到的输出里再解析一遍，得到driver_path，以及browser_path
# 通过service起一个子进程webdriver，--port必有，可选--append-log，--readable-timestamp，--log-path
# port通过临时起个监听，看看哪个行就用哪个
# ChromiumDriver继承自selenium.webdriver.remote.webdriver.WebDriver
# 通过port，以及remote类的方法，向webdriver发送命令

from seleniumwire.undetected_chromedriver.v2 import Chrome
driver2 = Chrome(

)

driver2.get()

# https://chromedriver.storage.googleapis.com/LATEST_RELEASE
# 114.0.5735.90
