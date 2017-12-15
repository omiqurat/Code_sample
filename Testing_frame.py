
import tkinter as Tkinter
import logging
from tkinter import *
import Testing_live_plot_0 as test
import datetime
import shutil
import os
import clock as clk
## import i2c_layer_2 as layer2



class main():
    def log_file(self):
        # create logger with 'spam_application'
        global date
        self.logger = logging.getLogger('testing_frame')
        self.logger.setLevel(logging.DEBUG)
        date_in=clk.clock_run()
        file_name=str(date_in[3])+'-'+str(date_in[4])+'-'+str(date_in[5])+'['+str(date_in[2])+'-'+str(date_in[1])+'-'+str(date_in[0])+']'+".log"

        # T.insert(END, " \n" +str(file_name) + "created ")
        print(file_name)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(file_name)
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.info('start ')



    def connection_check(self):

        # global sample,seconds,minutes,hours,day,month,year,power_status_byte,status,timer_value,sampling_time
        # sample,seconds,minutes,hours,day,month,year,power_status_byte,status,timer_value,sampling_time=layer2.Read_system_status()
        # T.delete("1.0",END)
        # T.insert(END, "  Connected  ")
        ### call the log function
        self.log_file()

        test.top_frame().show_time()

        #test.top_frame()

    ####################  FILE BROWSER    ##############

    def browse(self):
        global path

        toplevel0 = Toplevel()

        toplevel0.title("File Browser ")

        toplevel0.overrideredirect(True)
        toplevel0.geometry("%dx%d+0+0" % (700,400))
        #toplevel0.geometry("{0}x{1}+0+0".format(toplevel0.winfo_screenwidth(), toplevel0.winfo_screenheight()))
        list=Listbox(toplevel0,width=36,height=30,fg='darkblue',font = ('Arial', 11, 'bold'))
        scroll=Scrollbar(toplevel0,command=list.yview)

        scroll.pack(side=LEFT,fill=Y)
        list.pack(side=LEFT)
        list.configure(yscrollcommand=scroll.set)

        files = [f for f in os.listdir('.') if re.match(r'[0-9]+.*\.csv',f)]

        p = Tkinter.Text(toplevel0, height = 3,width = 25,bg='lightblue',fg='darkblue',font = ('Arial', 11, 'bold', 'italic'))
        p.pack(side=TOP,anchor=E,padx=20,pady=20)
        p.insert(END, "  USB CONNECTED")

        list.place(x=5,y=5)

        for item in range (len(files)):
            list.insert(END,files[item])
            print(files)
        def assure_path_exists():
                dir=os.path.dirname('/home/pi/project/USB/measurement/')
                print(dir)
                if not os.path.exists(dir):
                       os.makedirs(dir)
        assure_path_exists()

        ####### DELETE BUTTON FUNCTION##########


        def delete():
            toplevel1 = Toplevel()
            toplevel1.title("File Browser ")

            toplevel1.geometry("%dx%d+0+0" % (700,400))
            toplevel1.overrideredirect(True)
            #toplevel1.geometry("{0}x{1}+0+0".format(toplevel0.winfo_screenwidth(), toplevel0.winfo_screenheight()))
            k= Tkinter.Text(toplevel1, height = 8,width = 100,bg='lightblue',fg='darkblue',font = ('Arial', 15, 'bold', 'italic'))

            k.pack(side=TOP,padx=20,pady=20)
            value=str((list.get(ACTIVE)))
            k.insert(END, "  DELETE file : " + value +" ? " )


            ###### confirmation of Delete Function #################

            def YES():
                #value=str((list.get(ACTIVE)))
                try :
                    full_path = os.path.realpath(value)
                    list.bind(' <<ListboxSelect>>',value)
                    os.remove(full_path)
                    list.update()
                    #list.update_idletasks()
                    selection=list.curselection()
                    list.delete(selection[0])
                   
                    print(full_path + "\n")
                    print ("this is selected",value)
                    k.delete("1.0",END)
                    k.insert(END, "  Deleted successfully")
                    print("file deleted successfully ")
                    #toplevel1.quit()
                    toplevel1.destroy()
                except :
                    k.delete("1.0",END)
                    k.insert(END, " files not found ")




#             button24= Tkinter.Button(toplevel1, text=" YES",width=30, command=YES)
#             button24.pack(side=BOTTOM,anchor=N,padx=20,pady=20)

#             button23= Tkinter.Button(toplevel1, text=" CANCEL",width=30, command=toplevel1.destroy)
#             button23.pack(side=BOTTOM,anchor=N,padx=20,pady=20)


        ######## COPY TO USB  BUTTON  FUNCTION #########


        def copy_to_USB():
            value=str((list.get(ACTIVE)))
            source= os.path.realpath(value)
            list.bind(' <<ListboxSelect>>',value)

            # USB name must be changed to 'USB1' in order for auto copy to work
            


            destination = "/home/pi/project/USB/measurement/%s.csv" % value


            try:
                # Copy file to destination
                shutil.copy2(source, destination)
                list.update_idletasks()
                p.delete("1.0",END)
                p.insert(END, " copy successfully ")
                print("copy successfully ")
                # E.g. source and destination is the same location
            except shutil.Error as e:
                p.delete("1.0",END)
                p.insert(END, " copy Unsuccessful ")
                print("Error: %s" % e)
                # E.g. source or destination does not exist
            except IOError as e:
                p.delete("1.0",END)
                p.insert(END, " copy Unsuccessful ")
                print("Error: %s" % e.strerror)



#         button11 = Tkinter.Button(toplevel0, text=" DELETE ",width=30,command=delete)
#         button11.pack(side=TOP,anchor=E,padx=20,pady=20)

#         #
#         button12 = Tkinter.Button(toplevel0, text=" COPY TO USB  ",width=30,command=copy_to_USB)
#         button12.pack(side=TOP,anchor=E,padx=20,pady=20)
#         # #
        button13= Tkinter.Button(toplevel0, text=" CLOSE ",width=30, command=toplevel0.destroy)
        button13.pack(side=TOP,anchor=E,padx=20,pady=20)




########### MAIN TOP FRAME ############
#######################################

app = Tk()
app.title("HOKI DOKI ")
app.geometry("%dx%d+0+0" % (700,400))
app.overrideredirect(True)
#app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))



label = Label(app, text=" WELCOME TO YOUR NEW GENERATION HEALTH CARE  ", height=0, width=400)

button1 = Button(app, text="CONNECT",height = 3, width=30,font = ('Arial', 15, 'bold', 'italic'), command=main().connection_check)
label.pack()
button1.pack(side='top',padx=5,pady=5)

button_browse = Tkinter.Button(app, text='FILES ',height = 3,fg='black', width=30,font = ('Arial', 15, 'bold', 'italic'),command=main().browse) ###,command=self.browse
button_browse.pack(side='top',padx=5,pady=5)

b = Button(app, text="Quit", width=30, height = 3,font = ('Arial', 15, 'bold', 'italic'),command=app.destroy)
b.pack(side='top',padx=5,pady=5)


app.mainloop()
