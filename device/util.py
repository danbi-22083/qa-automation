from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
# 원격 연결 시 해당 디바이스의 IP 주소를 입력
device = client.device('192.168.0.9:5555')


class init_appium():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    # 테스트에 사용되는 디바이스의 IP 주소를 입력
    desired_caps['deviceName'] = '192.168.0.9:5555'
    desired_caps['automationname'] = 'Appium'
    desired_caps['newCommandTimeout'] = 9000
    desired_caps['appPackage'] = 'com.danbiedu.wink.student'
    desired_caps['appActivity'] = 'com.danbiedu.wink.student.MainActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)


class appium_fn(object):
    init_appium.driver.implicitly_wait(15)

    def findElement(self, ele):
        fn = init_appium.driver.find_element(ele)
        return fn

    # 왼쪽의 content 안써주면 에러남
    def AppiumBy(self, content_title):
        content = AppiumBy.ACCESSIBILITY_ID, content_title
        return content


class adb_fn(object):
    __app_PackageName = 'com.danbiedu.wink.student'
    __app_pid = ""

    def tapAnywhere(self):
        device.shell('input touchscreen tap 1245 500')

    def clearLog(self):
        device.shell('logcat -c')

    def getPackageName(self):
        return self.__app_PackageName

    def getPid(self, packagename):
        pid = device.shell('pidof ' + packagename)
        return pid

    def getLogWithPid(self, pid):
        log = device.shell('logcat -d --pid=' + pid)
        return log