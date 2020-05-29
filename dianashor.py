import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data,x):
    if x == 1:
        
        for i in range(410, 535):
            for j in range(250, 290):
                if data[i, j] < 100:
                    hit("up")
                    return
            
        # Draw the rectangle for birds
        for i in range(450, 630):
            for j in range(220, 247):
                if data[i, j] < 100:
                    hit("up")
                    return

                
    elif x == 0:
        
        for i in range(410, 535):
            for j in range(250, 290):
                if data[i, j] > 100:
                    
                    hit("up")
                    return
            
        # Draw the rectangle for birds
        for i in range(420, 570):
            for j in range(220, 247):
                if data[i, j] > 100:
                    hit("up")
                    return
    return
def chakecolor(data):
    for i in range(415,420):
        for j in range(170,180):
            if data[i, j] < 100:
                return 0;
            elif data[i, j] > 100:
                return 1;
            

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        bgcolor = chakecolor(data)
        isCollide(data,bgcolor)
        '''
        # print(asarray(image))
       
        # Draw the rectangle for cactus
        for i in range(430, 490):
            for j in range(245, 290):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(430, 490):
            for j in range(220, 244):
                data[i, j] = 171

        image.show()
        
        break 
        '''
      

