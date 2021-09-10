import tkinter
from tkinter import *
from tkinter import messagebox
import os

def main():

    def Close_main():
        window.destroy()
        
    window = tkinter.Tk()
    window.title("Result Calculator GUI")
    window.geometry ("520x600")
    window.resizable(0,0)
    window.iconbitmap('icon.ico')
    #window.configure(background = "Black")

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
            Final = f"Percentage: {perc_int}% "
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


    def savefile():
            
        name = name_entry.get()
        if len(name) > 1:
            file = open("Student_names.txt","r")
            for line in file:
                word = line.rstrip(",").split(",")
                if name in word:
                    found = 1
                    break;
                else:
                    found = 0

            if found == 1:
                messagebox.showerror("Error", "Name already exist !")

            if found == 0:
                file_names = open("Student_names.txt","a")
                file_names.write(name)
                file_names.write(",")

                file = open("Result_data.txt","a")

                file.write("Student Name: " + name)
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

                file.write(f"Percentage: {percentage_data}% ")
                file.write("\n")
                file.write(30*"*")
                file.write("\n")
                file.close()

                messagebox.showinfo("Save", "Your data has been stored successfully.")

        else:
            messagebox.showerror("Error", "Name cannot be empty or is invalid. Try again !")

    def save_name():
        def Close_sub():
            save_window.destroy()
            main()
            
        global sub1_name,sub2_name,sub3_name,sub4_name,sub5_name
        global sub1_mark,sub2_mark,sub3_mark,sub4_mark,sub5_mark
        global percentage_data
        global name_entry

        try:
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

            percentage_data = ( float(sub1_data.get()) + float(sub2_data.get()) + float(sub3_data.get()) + float(sub4_data.get()) + float(sub5_data.get()) )/ 5 

            window.destroy()
            save_window = tkinter.Tk()
            save_window.title("Save")
            save_window.geometry ("300x300")
            save_window.resizable(0,0)
            
            saveframe1 = Frame(save_window)
            saveframe2 = Frame(save_window)
            saveframe3 = Frame(save_window)
            
            name = Label(saveframe1, text = "Student Name", font = ("Arial Bold",10))
            name.grid(column =0, row =0, padx = 10)
            saveframe1.pack()
            
            name_entry = Entry(saveframe2,  width="20", font = ("Arial Bold",10),fg="Black", borderwidth = 0)
            name_entry.grid(column =0, row =1, padx = 10)
            saveframe2.pack()
            
            save = Button(saveframe3, text= "Save Marks",font = ("Arial Bold",10),fg="Red", command = savefile)
            save.grid(column = 0, row = 0, padx = 10, pady = 10)
            
            restart = Button(saveframe3, text= "Add more data",font = ("Arial Bold",10),fg="Red", command = Close_sub)
            restart.grid(column = 0, row = 1, padx = 10)
            saveframe3.pack()
            
            save_window.mainloop()

        except:
            error = messagebox.showerror("Error", "Invalid Input. Check Again !!")
            

    save_btn = Button(frame4, text= "Tick to Save",font = ("Arial Bold",10),fg="Red", command = save_name, state = DISABLED)
    save_btn.grid(column = 1, row = 1, padx = 10)

    frame4.pack()

    exit_button = Button(frame4, text="Exit Program", fg="Red", command=Close_main)
    exit_button.grid(column = 2, row = 1, padx = 10)

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
main()