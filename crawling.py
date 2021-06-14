import sys
from selenium import webdriver
from time import sleep
sys.stdout = open('result2.json', 'w')

def hasxpath():
    try:
        driver.find_element_by_class_name('classroom-modal__backdrop')
        driver.find_element_by_css_selector('.classroom-modal__backdrop svg').click()
        driver.implicitly_wait(2)
        return True
    except:
        return False

options = webdriver.ChromeOptions()
options.add_argument('window-size=1280,1197')

driver = webdriver.Chrome('./chromedriver', options=options)
driver.implicitly_wait(3)

driver.get(url='https://auth.fastcampus.co.kr/sign-in?client_id=fc%3Aclient%3Ab2e&response_type=token&redirect_uri=https%3A%2F%2Fbusiness.fastcampus.co.kr%2F&scope=b2e')
sleep(3)
# 로그인
driver.find_element_by_id('user-email').send_keys('alsltnpf1209@gmail.com')
driver.find_element_by_id('user-password').send_keys('12345678')
driver.find_element_by_css_selector('.btn__flex button').click()
driver.implicitly_wait(3)

# 최근 수강한 강의 선택
driver.find_element_by_css_selector('#app > div > div.fcb2e-content > div:nth-child(1) > div.fcb2e-curation-list__content > div.fcb2e-slider > div > div:nth-child(1) > div.fcb2e-curation-course-complete-poster > div.fcb2e-curation-course-complete-poster__mask.fcb2e-curation-course-complete-poster__mask--normal').click()
driver.implicitly_wait(3)

# 이어보기
hasxpath()

# 수업 Part 선택
partList = driver.find_elements_by_css_selector('.classroom-sidebar-clip__chapter .classroom-sidebar-clip__chapter__title__text')
objList = []

# for inx, part in enumerate(partList):
for i in range(26,len(partList)):
    idx = i + 1
    obj = {}
    partList[i].click()
    driver.implicitly_wait(3)
    hasxpath()
    partTitle = partList[i].text
    obj['partTitle'] = partTitle
    classItems = []
    # 수업 선택
    classList = driver.find_elements_by_css_selector(f"#app > div > div.classroom-layout.classroom-layout--theme-b2e > aside > div > div:nth-child({idx}) > div > div.fc-accordion-menu__content > div > div > div")
    for index, clas in enumerate(classList):
        clas.click()
        driver.implicitly_wait(5)
        hasxpath()

        classTitle = driver.find_element_by_css_selector('span.classroom-sidebar-clip__chapter__clip__title.classroom-sidebar-clip__chapter__clip__title--active').text

        iframe = driver.find_element_by_css_selector('iframe')
        driver.switch_to_frame(iframe)
        src = driver.find_element_by_css_selector('video').get_attribute("src")
        classItem = {}
        classItem['classTitle'] = classTitle
        classItem['src'] = src

        classItems.append(classItem)
        obj['lesson'] = classItems
        driver.switch_to_default_content()

    objList.append(obj)

print(objList)
sys.stdout.close()

