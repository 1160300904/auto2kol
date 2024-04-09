import  pyautogui
import time
import  pytesseract
import  random



#
# time.sleep(3)
# oneLocation = pyautogui.locateOnScreen('playbutton.png')
# print(oneLocation)
# pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
# pyautogui.click()
#
while 1:
    time.sleep(3)
    oneLocation = pyautogui.locateOnScreen('playbutton.png')
    print(oneLocation)
    pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
    pyautogui.click()


    time.sleep(3)
    oneLocation = pyautogui.locateOnScreen('jiaolianmoshi2.png')
    print(oneLocation)
    pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
    pyautogui.click()

    time.sleep(3)
    oneLocation = pyautogui.locateOnScreen('danrenpipei.png')
    print(oneLocation)
    pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
    pyautogui.click()


    #while queding
    notfoundyet=1
    while notfoundyet==1:
        try:
            time.sleep(3)
            oneLocation = pyautogui.locateOnScreen('queding.png')
        except Exception:
            pass
        else:
            pyautogui.moveTo(oneLocation.left + oneLocation.width / 2, oneLocation.top + oneLocation.height / 2)
            pyautogui.click()
            notfoundyet=0

    #while zhunbei
    notfoundyet=1
    while notfoundyet==1:
        try:
            time.sleep(3)
            oneLocation = pyautogui.locateOnScreen('zhunbei.png')
        except Exception:
            pass
        else:
            pyautogui.moveTo(oneLocation.left + oneLocation.width / 2, oneLocation.top + oneLocation.height / 2)
            pyautogui.click()
            notfoundyet=0


    time.sleep(660)


    #投降
    try:
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(3)
        oneLocation = pyautogui.locateOnScreen('faqitouxiang.png')
        print(oneLocation)
        pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
        time.sleep((1))
        pyautogui.click()
        time.sleep((1))
        pyautogui.click()
    except Exception:
        pass


    #认输确定
    time.sleep(3)
    oneLocation = pyautogui.locateOnScreen('renshuqueding.png')
    print(oneLocation)
    pyautogui.moveTo(oneLocation.left+oneLocation.width/2,oneLocation.top+oneLocation.height/2)
    pyautogui.click()

    #while 结束返回
    notfoundyet=1
    while notfoundyet==1:
        try:
            time.sleep(3)
            oneLocation = pyautogui.locateOnScreen('jieshufanhui.png')
        except Exception:
            pass
        else:
            pyautogui.moveTo(oneLocation.left + oneLocation.width / 2, oneLocation.top + oneLocation.height / 2)
            pyautogui.click()
            notfoundyet=0

    time.sleep(random.randint(60,100))