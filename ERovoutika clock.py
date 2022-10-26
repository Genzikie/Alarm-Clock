from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound
from playsound import playsound
from PIL import ImageTk,Image
from threading import *

# gui design
root = Tk()
root.geometry("500x450")
root.title('ERovoutika - Alarm Clock And Timer')
root.iconbitmap("gear.ico")
root.config(bg ='lightsteelblue1')
root.resizable(0,0)

# erovoutika logo
img = ImageTk.PhotoImage(Image.open("erov logo.png"))
img_label = Label(image=img, bg='lightsteelblue1')
img_label.pack()

# clock function
def clock():
    clock_time = time.strftime('%H:%M:%S')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='{courier new} 30', text = '', fg = 'black' ,bg ='lightsteelblue1')
curr_time.pack(side = TOP , pady = 5)
clock()

# Declaration of variables for timer
hr=StringVar()
min=StringVar()
sec=StringVar()
  
# setting the default value as 0
hr.set("00")
min.set("00")
sec.set("00")
  
# Use of Entry class to take input from the user
hourEntry= Entry(root, width=2, font=("{courier new}",18,""),
                 textvariable=hr)
hourEntry.place(x=185, y = 200, anchor=NW)
  
minuteEntry= Entry(root, width=2, font=("{courier new}l",18,""),
                   textvariable=min)
minuteEntry.place(x=249, y = 200, anchor=NW)
  
secondEntry= Entry(root, width=2, font=("{courier new}",18,""),
                   textvariable=sec)
secondEntry.place(x=313, y = 200, anchor=NW)

Label(root, font ='{courier new} 18', text = 'Timer :',   bg ='lightsteelblue1').place(x = 40 ,y = 200)
Label(root, font ='{courier new} 18', text = 'H:',   bg ='lightsteelblue1').place(x = 215 ,y = 200)
Label(root, font ='{courier new} 18', text = 'M:',   bg ='lightsteelblue1').place(x = 279 ,y = 200)
Label(root, font ='{courier new} 18', text = 'S',   bg ='lightsteelblue1').place(x = 343 ,y = 200)

def startTimer():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hr.get())*3600 + int(min.get())*60 + int(sec.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hr.set("{0:2d}".format(hours))
        min.set("{0:2d}".format(mins))
        sec.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Countdown Timer", "Time's up ")
            hr.set("00")
            min.set("00")
            sec.set("00")
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
btnTimer = Button(root, text='Set Countdown Timer', bd='5',
             command= startTimer)
btnTimer.place(x = 185,y = 240)

# threading
def startAlarm():
    t1=Thread(target=Alarm)
    t1.start()

def Alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Wake Up Samurai")
            # Playing sound
            winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Alarm", "Wake Up ")
            hour.set(hours[0])
            minute.set(minutes[0])

Label(root, font ='{courier new} 18', text = 'Alarm :',   bg ='lightsteelblue1').place(x = 40 ,y = 300)

frame = Frame(root)
frame.place(x=185, y=300)

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 

btnAlarm = Button(root, text='Set Alarm', bd='5',
             command= startAlarm)
btnAlarm.place(x = 185,y = 340)


# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
