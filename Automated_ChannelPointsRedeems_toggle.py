import webbrowser
import pyautogui
import pyperclip
import time
import os


#This script Requeieres a 1920 x 1080 pixels wide screen in order to fuction
#It's reliant of Pixel positions on the screen so any other screen size will not work as intended - use at your own risk
#Make sure the Browser URL opens in your 1080p screen
#You can ensure this opening a new browser tab on your 1080p screen

url = "https://www.twitch.tv/popout/lucypyre/reward-queue"
webbrowser.open(url, new=0, autoraise=True)
time.sleep(3)
repeats = 22
currentrepeat = 0
tabnum = 4
tabcurrent = 0
Click_variable_x = 45 
Click_variable_y = 183 #start at Hydrate
pyautogui.press('f11')
time.sleep(0.1)
pyautogui.moveTo(45, 183)
while currentrepeat < repeats:
    
    if currentrepeat == 12:
        pyautogui.moveTo(45, 407)
        pyautogui.scroll(-5000, x=50, y=407)
        time.sleep(0.2)    
    pyautogui.doubleClick(x=Click_variable_x, y=Click_variable_y)
    pyautogui.rightClick(x=383, y=24)
    pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.click(x=1787, y=567)
    pyautogui.click(x=1589, y=594)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite('checked')
    pyautogui.doubleClick(x=1498, y=635)
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    if text == 'true':
        pyautogui.moveTo(386, 21)
        pyautogui.click(x=386, y=21)
    if currentrepeat== 0: #posture check
        Click_variable_y = 183
    if currentrepeat== 1: #posture check
        Click_variable_y = 239
    if currentrepeat== 2: #Glasses on/off
        Click_variable_y = 347
    if currentrepeat== 3: #PigTails
        Click_variable_y = 403 
    if currentrepeat== 4: #Wha~o
        Click_variable_y = 463
    if currentrepeat== 5: #Nya
        Click_variable_y = 627 
    if currentrepeat== 6: #ASMR mode
        Click_variable_y = 738 
    if currentrepeat== 7: #Stretch
        Click_variable_y = 797
    if currentrepeat== 8: #Wet/No Wet
        Click_variable_y = 852
    if currentrepeat== 9: #Ara ara
        Click_variable_y = 903 
    if currentrepeat== 10: #Yamete Kudasai
        Click_variable_y = 963
    if currentrepeat== 11: #Yeehaw
        Click_variable_y = 534
    if currentrepeat== 12: #BlackHair
        Click_variable_y = 592
    if currentrepeat== 13: #Moan
        Click_variable_y = 648
    if currentrepeat== 14: #Thigh Slap
        Click_variable_y = 704 
    if currentrepeat== 15: #Kid Voice
        Click_variable_y = 760
    if currentrepeat== 16: #Mommy Voice
        Click_variable_y = 811 
    if currentrepeat== 17: #Cat Girl Mode
        Click_variable_y = 871
    if currentrepeat== 18: #Old Model Voice
        Click_variable_y = 926 
    if currentrepeat== 19: #Swear Jar
        Click_variable_y = 981
    if currentrepeat== 20: #End Stream
        Click_variable_y = 1040                                                                                                   

    currentrepeat = currentrepeat+1
    
