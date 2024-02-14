from Tkinter import *
import time
import RPi.GPIO as GPIO

#initialize LEDs default state
red_led = 0
green_led = 0
blue_led = 0

# use pin numbers RPi.GPIO Layout
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) Output 
GPIO.setup(11, GPIO.OUT)

# Pin 13 (GPIO 27) Output 
GPIO.setup(13, GPIO.OUT)

# Pin 15 (GPIO 22)  Output 
GPIO.setup(15, GPIO.OUT)

# switch off LEDs
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

def red():

    global red_led
       
    if red_led:
    #########################################
        red_on_button.config(text='RED\non!', background = "#dadada")
        GPIO.output(11, GPIO.LOW)
        leftFrame.config(background = "#dadada")
        message1_label.config(text = "red LED is off", background = "#e1e1e1" )
    #########################################

    else:
    #########################################
        red_on_button.config(text='RED\noff!', background = "#ff0000")
        GPIO.output(11, GPIO.HIGH)
        leftFrame.config(background = "#dadada")
        message1_label.config(text = "red LED is on", background = "#e1e1e1" )
    #########################################

    red_led = not red_led
 
def green():

    global green_led
        
    if green_led:
    #########################################
        green_on_button.config(text='GREEN\non!', background = "#dadada")
        GPIO.output(13, GPIO.LOW)
        leftFrame.config(background = "#dadada")
        message2_label.config(text = "green LED is off", background = "#e1e1e1" )
    #########################################

    else:
    #########################################
        green_on_button.config(text='GREEN\noff!', background = "#00ff00")
        GPIO.output(13, GPIO.HIGH)
        leftFrame.config(background = "#dadada")
        message2_label.config(text = "green LED is on", background = "#e1e1e1" )
    #########################################
        
    green_led = not green_led

def blue():

    global blue_led
        
    if blue_led:
    #########################################
        blue_on_button.config(text='BLUE\non!', background = "#dadada")
        GPIO.output(15, GPIO.LOW)
        leftFrame.config(background = "#dadada")
        message3_label.config(text = "blue LED is off", background = "#e1e1e1" )
    #########################################

    else:
    #########################################
        blue_on_button.config(text='BLUE\noff!', background = "#0000ff")
        GPIO.output(15, GPIO.HIGH)
        leftFrame.config(background = "#dadada")
        message3_label.config(text = "blue LED is on", background = "#e1e1e1" )
    #########################################
        
    blue_led = not blue_led
   


root = Tk() # create window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.wm_title("Raspberry Pi GUI for LED Control") # window titel
root.config(background = "#dadada") # bachground color
 
# initialize left frame
leftFrame = Frame(root, width=400, height = 400) # frame initialisation
leftFrame.grid(row=0, column=0, padx=10, pady=3) # relative Position and spacing (padding) 


# left frame elements
red_on_button = Button(leftFrame, cursor='spraycan', text="RED\non!", font=('helvetica', 20), background = "#dadada", activebackground = "#ff6666", width=15, padx=10, pady=25, command=red )
green_on_button = Button(leftFrame, cursor='spraycan', text="GREEN\non!", font=('helvetica', 20), background = "#dadada", activebackground = "#66ff66", width=15, padx=10, pady=25, command=green )
blue_on_button = Button(leftFrame, cursor='spraycan', text="BLUE\non!", font=('helvetica', 20), background = "#dadada", activebackground = "#6666FF", width=15, padx=10, pady=25, command=blue )


#initialize right frame
rightFrame = Frame(root, width=400, height = 400) # frame initialisation
rightFrame.grid(row=0, column=1, padx=10, pady=3) # relative Position and spacing (padding) 

# right frame elements
message1_label = Label(rightFrame, text = "red LED is off", background = "#e1e1e1" )
message2_label = Label(rightFrame, text = "green LED is off", background = "#e1e1e1" )
message3_label = Label(rightFrame, text = "blue LED is off", background = "#e1e1e1" )
exit_button = Button(rightFrame, cursor='pirate', text="Leave", font=('helvetica', 20), activebackground = "#9E9E9E", width=15, padx=40, pady=20, command=root.quit)


red_on_button.grid(row=0, column=0, padx = 10, pady = 10)
green_on_button.grid(row=1, column=0, padx = 10, pady = 10)
blue_on_button.grid(row=2, column=0, padx = 10, pady = 10)
message1_label.grid(row=0, column=1, padx = 10, pady = 10)
message2_label.grid(row=1, column=1, padx = 10, pady = 10)
message3_label.grid(row=2, column=1, padx = 10, pady = 10)
exit_button.grid(row=6, column=1, padx = 20, pady = 10)
 
root.mainloop() # update GUI  
GPIO.cleanup() # release GPIOs before leaving program
