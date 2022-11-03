import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common_util import selenium
import util
import model as md

import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


slnFN = selenium.seleniumFN()
adbFN = util.adb_fn()
apmFN = util.appium_fn()
btn = md.button_location()
title = md.contents_title()


class GoTest(unittest.TestCase):
    driver = util.init_appium.driver
    print('device set')

    def Setup(self):
        print("[Project A Log] : Setup")
        adbFN.clearLog()

    def teardown(self):
        print("[Project A Log] : teardown")
        adbFN.clearLog()

    def test_case1(self):
        print("[Project A Log] : Begin Case1")

        driver = self.driver
        wait = WebDriverWait(driver, 20)
        # driver 를 사용하는 모든 코드에 implicityly_wait 20초 적용
        driver.implicitly_wait(15)

        # 아래 엘리먼트가 보일떄까지 대기
        study_kor = wait.until(slnFN.findClickable(apmFN.AppiumBy(md.contents_title().getKor_1_1_1())))
        study_kor.click()
        print("오늘의 공부 탭 완료")
        # 영상 재생 이력 있는지 확인
        while True:
            logResult = adbFN.getLogWithPid(adbFN.getPid(adbFN.getPackageName()))

            if "https://s.wink.co.kr/r/s/k/1/k_1_01_1_ani.mp4" in logResult:
                print('영상 로드 확인')
                break
            else:
                print('영상 로드 확인 중')
                sleep(1)
        # sleep(15)
        try:
            test_element = wait.until(slnFN.findClickable(slnFN.SlnBy(btn.goFirstXpath())))
        except:
            print('영상 첫 재생?')
            sleep(1)
        else:
            test_element.click()
            print('pass')
            sleep(1)

        sleep(3)
        adbFN.tapAnywhere()
        print('adb 탭 완료')

        try:
            video_close = wait.until(slnFN.findClickable(apmFN.AppiumBy(btn.videoClose())))
        except:
            print('video_close err')
        else:
            video_close.click()
            print('video close 클릭 완료')
            acc = wait.until(slnFN.findClickable(apmFN.AppiumBy(btn.ok())))
            acc.click()
            print('확인 버튼 클릭')

        # [오늘의 공부] 박스 노출 여부 확인
        main_check = apmFN.findElement(By.XPATH, '//android.view.View[@content-desc="오늘의 공부"]')
        print('오늘의 공부 배너 찾음!')
        # is_diplayed 는 지정한 엘리먼트가 보이면 True or False
        main_check_dis = main_check.is_displayed()
        # ele_dis 에 저장된 값에 따라 아래 문구 노출
        if main_check_dis:
            print('메인페이지 복귀')
        else:
            print('엥')

        print("[Project A Log] : End Case1")


def make_suite(testcase: unittest.TestCase, tests: list) -> unittest.TestSuite:
    return unittest.TestSuite(map(testcase, tests))


if __name__ == '__main__':
    suite_1 = make_suite(GoTest, ['test_case1'])
    suites = unittest.TestSuite([suite_1])
    unittest.TextTestRunner(verbosity=2).run(suites)
    unittest.main()
