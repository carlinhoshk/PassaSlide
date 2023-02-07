from flask import Flask, render_template
import os, sys
import pyautogui


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/up')
def up():
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    
    #pyautogui.scroll(100)
    
    return render_template('index.html')

    
@app.route('/down')
def down():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    
    #pyautogui.scroll(-100)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
