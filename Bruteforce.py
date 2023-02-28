import random
import pyautogui
chars = " abcdefghijklmnopqrstuvwxyz0123456789.!?"
chars_list = list(chars)
title="Bruteforcer 2.0"
password = pyautogui.password("Enter Your Password ! ): ",title)
guess_password = ""
while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    print(str(guess_password))
    if(guess_password == list(password)):
        screen = str(guess_password)
        password_found=pyautogui.password(screen,"The password is ",)
        print("The password is : "+ "".join(guess_password))
        break
