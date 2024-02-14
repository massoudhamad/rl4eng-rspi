from Tkinter import *
import RPi.GPIO as GPIO

root = Tk() # create window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.wm_title("Raspberry Pi GUI for LED Control") # window titel
root.config(background = "#dadada") # bachground color

# functions
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
 
# initialize left frame
leftFrame = Frame(root, width=400, height = 400) # frame initialisation
leftFrame.grid(row=0, column=0, padx=10, pady=3) # relative Position and spacing (padding) 

#initialize right frame
rightFrame = Frame(root, width=400, height = 400) # frame initialisation
rightFrame.grid(row=0, column=1, padx=10, pady=3) # relative Position and spacing (padding) 

red_on_button = Button(leftFrame, cursor='spraycan', text="RED\non!", font=('helvetica', 20), background = "#dadada", activebackground = "#ff6666", width=15, padx=10, pady=25, command=red )
message1_label = Label(rightFrame, text = "red LED is off", background = "#e1e1e1" )
exit_button = Button(rightFrame, cursor='pirate', text="Leave", font=('helvetica', 20), activebackground = "#9E9E9E", width=15, padx=40, pady=20, command=root.quit)

red_on_button.grid(row=0, column=0, padx = 10, pady = 10)
message1_label.grid(row=0, column=1, padx = 10, pady = 10)
exit_button.grid(row=6, column=1, padx = 20, pady = 10)
 
root.mainloop() # update GUI  
GPIO.cleanup() # release GPIOs before leaving program


