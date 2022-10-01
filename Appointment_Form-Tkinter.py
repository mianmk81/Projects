"""A Appointment Schedule window written in Python with Tkinter"""
import tkinter as tk
from tkinter import ttk
import json


#creating root window
root = tk.Tk()
#title of the window 
root.title('Appointment Schedule')

#window size and customization
root.geometry('750x600+300+300')
root.resizable(False, False)
# Widgets 

#label to show title
#font for the setup of the titale font size
title = tk.Label(
  root,
  text='Schedule your Appointment',
  font=('Arial 20 bold'),
  fg='black'
)
frame1 = ttk.LabelFrame(root, text='Personal Info')
frame2 = ttk.LabelFrame(root, text='Schedule Appointment')
frame3 = ttk.LabelFrame(root, text='Medical History')
frame4 = ttk.LabelFrame(root)
#for string using string var 
# age this will ask the user to check the bo if they are older than 18 
age_var = tk.BooleanVar()
age_inp = tk.Checkbutton(
  frame1, variable=age_var, text='Check this box if you are a legal adult?'
)

#this will ask for the name of the patient 
name_var = tk.StringVar(frame1)
name_label = ttk.Label(frame1, text=' What is your name?')
name_inp = tk.Entry(frame1, textvariable=name_var)

#this will ask for the reason of scheduling an appointment
reason_var = tk.StringVar(frame2)
reason_label = ttk.Label(frame2, text="Tell us why youre seeking an appointment : ")
reason_inp = tk.Entry(frame2, textvariable=reason_var)

#this will ask the patient what kind of symptoms they are having
symp_var = tk.StringVar(frame2)
symp_label = ttk.Label(frame2, text='What symptoms do you have: ')
symp_inp = tk.Entry(frame2, textvariable=symp_var)

#asking for pain level, this will be a counter that goes from 0-10
pain_var = tk.IntVar(frame2, value=1)
pain_label = ttk.Label(frame2, text='How much pain are you feeling 1-10?')

#seeting the increment of the counter and setting the counter
pain_inp = ttk.Spinbox(
  frame2,
  textvariable=pain_var,
  from_=1,
  to=10,
  increment=1
)

#asking for they date they are available 
date_var = tk.StringVar(frame2)
date_label = ttk.Label(frame2, text='Date you are avaiable (mm/dd/yyyy) : ')
date_inp = tk.Entry(frame2, textvariable=date_var)

#asking for their avalible time they are available 
time_var = tk.StringVar(frame2)
time_label = ttk.Label(frame2, text='Time you are avaiable: ')
time_inp = tk.Entry(frame2, textvariable=time_var)

#asking for social security to pull ip personal info or previous records 
social_var = tk.StringVar(frame1)
social_label = ttk.Label(frame1, text=' Social Security Number: ')
social_inp = tk.Entry(frame1, textvariable=social_var)

phone_var = tk.StringVar(frame1)
phone_label = ttk.Label(frame1, text=' What is your phone number: ')
phone_inp = tk.Entry(frame1, textvariable=phone_var)

#asking if they have any allergies, if yes  then explain
allergy_var = tk.StringVar(frame3)
allergy_label = ttk.Label(frame3, text='Do you have any Allergies And if Yes explain what.: ')
allergy_inp = tk.Entry(frame3, textvariable=allergy_var)

#doctor they prefer, this will be a drop down list of the doctors
Doc_var = tk.StringVar(value='Any')
Doc_label = ttk.Label(frame2,text='Doctor you are visiting?')

#name of the docotrs in the varial called Doc_choices
Doc_choices = (
  'Any', 'Dr.Phil', 'Dr.Ivo "Eggman" Robotnik ', 'Dr.Eggnog', 'Dr.Dopamine', 'Dr.Shaun Murphy'
)
Doc_inp = ttk.OptionMenu(
  frame2, Doc_var, *Doc_choices
)

#asking if the person had their covid vaccine, this will be a yes and no option, ech having there on frames
covid_label = tk.Label(frame3, text='Do you have your Covid Vaccine')

#frame for the yes options
covid_frame = tk.Frame(frame3)
covid_var = tk.BooleanVar()
covid_yes_inp = tk.Radiobutton(
  covid_frame,
  text='Yes',
  value=True,
  variable=covid_var
)

#frame for the no options
covid_no_inp = tk.Radiobutton(
  covid_frame,
  text='No!!!',
  value=False,
  variable=covid_var
)

#button weidget for the submittion of the appointment
submit_btn = tk.Button(frame4, text='Schedule')

output_var = tk.StringVar(value='')
output_line = ttk.Label(
  frame4,
  textvariable=output_var,
  anchor='w',
  justify='left'
)
title.grid(row=0, columnspan=2)

frame1.grid(row=5, padx=25, pady=10)
frame2.grid(row=6, padx=25, pady=10)
frame3.grid(row=7, padx=25, pady=10)
frame4.grid(row=9, padx=25, pady=10)

# positions of all the label creted previously 


name_label.grid(row=4, column=0, sticky='w')
reason_label.grid(row=6, sticky='w')
symp_label.grid(row=8, sticky='w')
pain_label.grid(row=10, sticky='w')
date_label.grid(row=12, sticky='w')
time_label.grid(row=14, sticky='w')
social_label.grid(row=16, sticky='w')
phone_label.grid(row=18, sticky='w')
Doc_label.grid(row=20, sticky='w')
allergy_label.grid(row=22, sticky='w')
covid_label.grid(row=27, sticky='w')

# places for the widget of th input value that we have to enter

age_inp.grid(row=2, columnspan=2, sticky='we')
name_inp.grid(row=4, column=1, sticky='W' )
reason_inp.grid(row=6, column=1, sticky='NSEW', columnspan=2 )
symp_inp.grid(row=8, column=1, sticky='NSEW', columnspan=2 )
pain_inp.grid(row=10, column=1, sticky='NSEW', columnspan=2)
date_inp.grid(row=12, column=1, sticky='NSEW', columnspan=2)
time_inp.grid(row=14, column=1, sticky='NSEW', columnspan=2)
social_inp.grid(row=16, column=1, sticky='NSEW', columnspan=2)
phone_inp.grid(row=18, column=1, sticky='NSEW', columnspan=2)
Doc_inp.grid(row=20, column=1, sticky='NSEW', columnspan=2)
allergy_inp.grid(row=22, column=1, sticky='NSEW', columnspan=2)
covid_frame.grid(row=30, columnspan=2, stick=tk.W)
covid_yes_inp.pack(side='left', fill='x', ipadx=150, ipady=5)
covid_no_inp.pack(side='left', fill='x', ipadx=150, ipady=5)


#position for the submit button 
submit_btn.grid(row=10, column=1, sticky='W')
output_line.grid(row=100, columnspan=2, sticky='NSEW')


root.columnconfigure(1, weight=1)

root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

#empty dictionary
data = {

}
# action performed after pressing the sbmitt button
# This will take the name and the appointment date in the variables called name and date
#later this will print a statement saying when is the appoinment scheduled for and under whose name 

def on_submit():
  """To be run when the user submits the form"""
  # Vars all use 'get()' to retreive their variables
  age = age_var.get()
  name = name_var.get()
  social = social_var.get()
  phone = phone_var.get()
  reason = reason_var.get()
  symptoms = symp_var.get()
  pain = pain_var.get()
  date = date_var.get()
  time = time_var.get()
  doctor = Doc_var.get()
  allergies = allergy_var.get()
  covid = covid_var.get()

  #add the data to the dictionary
  data["Age"]=age
  data["Name"]=name
  data["Social Security"]= social
  data["Phone Number"]= phone
  data["Reason"]= reason
  data["Symptoms"]= symptoms
  data["Pain Level"]= pain
  data["Date"]=date
  data["Time"]=time
  data["Doctor Vsiting"]=doctor
  data["Known Allergies"]=allergies
  data["Covid Vaccine"]=covid
  
  # Update the text in our output
  output = f'Your Appointment is Scheduled for {date}.' f' Under the name of {name}.\n', 'Have a nice day.'

#upload the data to the Jsaon file
  print(json.dumps(data))
  with open("Patients_data.json", "a") as file:
    json.dump(data, file)
    file.write("\n")
    file.write("\n")
  file.close()
  print(file)
  
  output_var.set(output)


# configure the button to trigger submission
submit_btn.configure(command=on_submit)

###############
# Execute App #
###############

root.mainloop()
