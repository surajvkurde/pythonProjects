from tkinter import *

root=Tk()
#siz of window
root.geometry("900x500")
def getvals():
    print("Accepted")

#label for page
title1 = Label(root,text="Registration form Using Python", font="ar 15 bold").grid(row=0,column=3)

#define fields and add to grid
name= Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry =  Entry(root,textvariable = gendervalue)
emergencyentry = Entry(root,textvariable = emergencyvalue)
paymentmodeentry = Entry(root,textvariable = paymentmodevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

chechbtn = Checkbutton(text = "Rememeber me?", variable = checkvalue)
chechbtn.grid(row=6,column=3)

#submit button
Button(text="Submit",command="getvals").grid(row=7,column=3) 


root.mainloop()