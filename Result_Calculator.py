import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Result Calculator GUI")
window.geometry ("520x600")
window.resizable(0,0)
# window.configure(background = "Black")

frame1 = Frame(window, bg = "Yellow")
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame(window)
frame5 = Frame(window)
                                        # FRAME 1 (TITLE)

topic1 = Label(frame1, text = "Result Calculator GUI", font = ("Arial Bold",20),fg="#34eb43", bg = "Yellow").pack()
topic1 = Label(frame1, text = "Ver: 1.2 Updated: July 2021 | USN: 1CR20CS196", font = ("Arial Bold",10),fg="Blue", bg = "Yellow", height = "2").pack()
frame1.pack(fill = "x")

                                        # FRAME 2 (Subject + Mark Obtained)
    

topic2 = Label(frame2, text = "Subject Name", font = ("Arial Bold",14))
topic2.grid(column =0, row =0, padx = 10)

topic3 = Label(frame2, text = "Mark Obtained", font = ("Arial Bold",14))
topic3.grid(column =1, row =0, padx = 50, pady = 10)


                            # Subject Name

sub_1 = Entry(frame2,  width="20", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub_1.grid(column =0, row =1, padx = 30)
sub_1.insert(0, "Subject_1")

sub_2 = Entry(frame2,  width="20", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub_2.grid(column =0, row =2, pady = 10)
sub_2.insert(0, "Subject_2")

sub_3 = Entry(frame2,  width="20", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub_3.grid(column =0, row =3, padx = 20)
sub_3.insert(0, "Subject_3")

sub_4 = Entry(frame2,  width="20", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub_4.grid(column =0, row =4, pady = 10)
sub_4.insert(0, "Subject_4")

sub_5 = Entry(frame2,  width="20", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub_5.grid(column =0, row =5, padx = 20)
sub_5.insert(0, "Subject_5")

                            # Mark

sub1_data = Entry(frame2, width="12", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub1_data.grid(column =1, row =1)

sub2_data = Entry(frame2, width="12", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub2_data.grid(column =1, row =2)

sub3_data = Entry(frame2, width="12", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub3_data.grid(column =1, row =3)

sub4_data = Entry(frame2, width="12", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub4_data.grid(column =1, row =4)

sub5_data = Entry(frame2, width="12", font = ("Arial Bold",12),fg="Red", borderwidth = 0)
sub5_data.grid(column =1, row =5)

frame2.pack(fill = "x")

                                        # FRAME 3 (Button + Check Box)
    
def chk():       
    if chk_state.get() == 1:
        button['state'] = NORMAL
        button.configure(text="Calculate Mark")
        
        save_btn['state'] = NORMAL
        save_btn.configure(text="Save Mark")

    if chk_state.get() == 0:
        button['state'] = DISABLED
        button.configure(text="Tick to Calculate")
        
        save_btn['state'] = DISABLED
        save_btn.configure(text="Tick to Save")

chk_state = IntVar()
Check = Checkbutton(frame3, text = "Above data are correctly entered.", var = chk_state, onvalue=1, offvalue=0, command=chk)
Check.grid(column = 0, row = 0, pady = 20)


def calculate():
    
    global perc_int, Grade;

    try:    
                                        # Getting mark for user and printing below submit button 
    
        sub1data = float(sub1_data.get())
        result1 = f"{sub_1.get()}: {sub1data}"
        mark1.configure(text = result1, fg="Black")

        sub2data = float(sub2_data.get())
        result2 = f"{sub_2.get()}: {sub2data}"
        mark2.configure(text = result2, fg="Black")    

        sub3data = float(sub3_data.get())
        result3 = f"{sub_3.get()}: {sub3data}"
        mark3.configure(text = result3, fg="Black")

        sub4data = float(sub4_data.get())
        result4 = f"{sub_4.get()}: {sub4data}"
        mark4.configure(text = result4, fg="Black")

        sub5data = float(sub5_data.get())
        result5 = f"{sub_5.get()}: {sub5data}"
        mark5.configure(text = result5, fg="Black")


                                             # Failed when mark is less than 40
        if sub1data < 40:
            Remark = f"{sub_1.get()}: {sub1data} (F)"
            mark1.configure(text = Remark,fg="Red")
        if sub2data < 40:
            Remark = f"{sub_2.get()}: {sub2data} (F)"
            mark2.configure(text = Remark,fg="Red")
        if sub3data < 40:
            Remark = f"{sub_3.get()}: {sub3data} (F)"
            mark3.configure(text = Remark,fg="Red")
        if sub4data < 40:
            Remark = f"{sub_4.get()}: {sub4data} (F)"
            mark4.configure(text = Remark,fg="Red")
        if sub5data < 40:
            Remark = f"{sub_5.get()}: {sub5data} (F)"
            mark5.configure(text = Remark,fg="Red")

                                            # Invalid mark when mark is greater than 100 or smaller than 0
        if sub1data > 100 or sub1data < 0:
            Remark = f"{sub_1.get()}: Invalid"
            mark1.configure(text = Remark,fg="Red")
        if sub2data > 100 or sub2data < 0:
            Remark = f"{sub_2.get()}: Invalid"
            mark2.configure(text = Remark,fg="Red")
        if sub3data > 100 or sub3data < 0:
            Remark = f"{sub_3.get()}: Invalid"
            mark3.configure(text = Remark,fg="Red")
        if sub4data > 100 or sub4data < 0:
            Remark = f"{sub_4.get()}: Invalid"
            mark4.configure(text = Remark,fg="Red")
        if sub5data > 100 or sub5data < 0:
            Remark = f"{sub_5.get()}: Invalid"
            mark5.configure(text = Remark,fg="Red")

                                            # Calculating Percentage by converting user-string into float

        perc_int = ( float(sub1_data.get()) + float(sub2_data.get()) + float(sub3_data.get()) + float(sub4_data.get()) + float(sub5_data.get()) )/ 5 
        Final = f"Percentage:{perc_int}% "
        perc.configure(text = Final, fg="Green")


                                            # Grading According to percentage

        if perc_int <= 100 and perc_int >= 90:
            Grade = "Grade: A+"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <= 89 and perc_int >= 80:
            Grade = "Grade: A"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <= 79 and perc_int >= 70:
            Grade = "Grade: B+"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <= 69 and perc_int >= 60:
            Grade = "Grade: B"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <= 59 and perc_int >= 50:
            Grade = "Grade: C+"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <= 49 and perc_int >= 40:
            Grade = "Grade: C"
            grade.configure(text = Grade,fg="Green")
        elif perc_int <40:
            Grade = "Grade: F- Failed"
            grade.configure(text = Grade,fg="red")
            perc.configure(fg="Red")

                                            # Invalid Grading/Percentage when mark is above 100 or negative

        if perc_int > 100 or sub1data > 100 or sub2data > 100 or sub3data > 100 or sub4data > 100 > sub5data:
            Grade = "Grade: Invalid"
            grade.configure(text = Grade,fg="Blue")

            Percentage = "Percentage: Invalid" 
            perc.configure(text = Percentage,fg="Blue")

        if perc_int < 0 or sub1data < 0 or sub2data < 0 or sub3data < 0 or sub4data < 0 or sub5data < 0:
            Grade = "Grade: Invalid"
            grade.configure(text = Grade,fg="Blue")

            Percentage = "Percentage: Invalid" 
            perc.configure(text = Percentage,fg="Blue")

                                            # Error message when no input
                
    except:
        error = messagebox.showerror("Error", "Invalid Input. Check Again !!")
        
frame3.pack()



button = Button(frame4, text= "Tick to Calculate",font = ("Arial Bold",10),fg="Red", state = DISABLED, command = calculate)
button.grid(column = 0, row = 1)

def save():


    try:

        perc_int = ( float(sub1_data.get()) + float(sub2_data.get()) + float(sub3_data.get()) + float(sub4_data.get()) + float(sub5_data.get()) )/ 5 

        window2 = tkinter.Tk()
        window2.title("Storing Data")
        window2.geometry ("420x200")
        window2.resizable(0,0)

        w2_frame1 = Frame(window2, bg = "Yellow")
        w2_frame2 = Frame(window2)
                                                # FRAME 1 (TITLE)

        topic1 = Label(w2_frame1, text = "Result Calculator GUI", font = ("Arial Bold",20),fg="#34eb43", bg = "Yellow").pack()
        topic1 = Label(w2_frame1, text = "Saving User Data", font = ("Arial Bold",10),fg="Blue", bg = "Yellow", height = "2").pack()
        w2_frame1.pack(fill = "x")

                                                # FRAME 2
            

        Name_topic = Label(w2_frame2, text = "Your Full Name: ", font = ("Arial Bold",12))
        Name_topic.grid(column =0, row =0, pady = 10, padx = 10)

        name_entry = Entry(w2_frame2, width="30")
        name_entry.grid(column =1, row =0, padx = 10)

        def submit():
            username = name_entry.get()

            if len(username) > 2:

                sub1_name = sub_1.get()
                sub2_name = sub_2.get()
                sub3_name = sub_3.get()
                sub4_name = sub_4.get()
                sub5_name = sub_5.get()

                sub1_mark = sub1_data.get()
                sub2_mark = sub2_data.get()
                sub3_mark = sub3_data.get()
                sub4_mark = sub4_data.get()
                sub5_mark = sub5_data.get()

                file = open("My_Result.txt","w")
                file.write("Student Name: " + username)
                file.write("\n")
                file.write("\n")

                file.write("Subject Name: " + sub1_name)
                file.write("\n")
                file.write("Mark: " + sub1_mark)
                file.write("\n")
                file.write("\n")

                file.write("Subject Name: " + sub2_name)
                file.write("\n")
                file.write("Mark: " + sub2_mark)
                file.write("\n")
                file.write("\n")

                file.write("Subject Name: " + sub3_name)
                file.write("\n")
                file.write("Mark: " + sub3_mark)
                file.write("\n")
                file.write("\n")

                file.write("Subject Name: " + sub4_name)
                file.write("\n")
                file.write("Mark: " + sub4_mark)
                file.write("\n")
                file.write("\n")

                file.write("Subject Name: " + sub5_name)
                file.write("\n")
                file.write("Mark: " + sub5_mark)
                file.write("\n")
                file.write("\n")

                file.write(f"Percentage: {perc_int}% ")
                file.write("\n")
                file.write("\n")

                file.close()
                messagebox.showinfo("Save", "Your data has been stored successfully.")
                window2.destroy()
                

            else:
                error = messagebox.showerror("Error", "Invalid Name. Check Again !!")
                window2.destroy()
                window2.mainloop()

        submit_btn = Button(w2_frame2, text= "Save",font = ("Arial Bold",10),fg="Red", command = submit)
        submit_btn.grid(column =1, row =1, padx = 10)
        w2_frame2.pack(fill = "x")

    except:
        
        error = messagebox.showerror("Error", "Invalid Input. Check Again !!")

        
save_btn = Button(frame4, text= "Save Marks",font = ("Arial Bold",10),fg="Red", command = save, state = DISABLED)
save_btn.grid(column = 1, row = 1, padx = 10)

frame4.pack()
        
                                            # FRAME 5 ( OUTPUT DATA )
        
mark1 = Label(frame5, text = " ", font = ("Arial Bold",12))
mark2 = Label(frame5, text = " ", font = ("Arial Bold",12))
mark3 = Label(frame5, text = " ", font = ("Arial Bold",12))
mark4 = Label(frame5, text = " ", font = ("Arial Bold",12))
mark5 = Label(frame5, text = " ", font = ("Arial Bold",12))

perc =  Label(frame5, text = " ", font = ("Arial Bold",12), pady =10)

grade =  Label(frame5, text = " ", font = ("Arial Bold",12))

mark1.grid(column =0, row =0)
mark2.grid(column =0, row =1)
mark3.grid(column =0, row =2)
mark4.grid(column =0, row =3)
mark5.grid(column =0, row =4)

perc.grid(column =0, row =5)

grade.grid (column =0, row =6)

frame5.pack()
window.mainloop()