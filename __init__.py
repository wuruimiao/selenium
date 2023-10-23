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
driver.get("https://www.baidu.com")
