class contents_title():
    __kor_1_1_1 = '단계별 한글 1단계 1회 1일차 <눈, 코, 입, 빵>'

    def getKor_1_1_1(self):
        return self.__kor_1_1_1


class button_location():
    __goFirst = '//android.view.View[@content-desc="DanbiEdu"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]'
    __videoClose = 'Close Close'
    __ok = '확인 '
    # __todayStudyBanner = '//android.view.View[@content-desc="오늘의 공부"]'
    __todayStudyBanner = '오늘의 공부'

    def goFirstXpath(self):
        return self.__goFirst

    def videoClose(self):
        return self.__videoClose

    def ok(self):
        return self.__ok

    def todayStudyBanner(self):
        return self.__todayStudyBanner
