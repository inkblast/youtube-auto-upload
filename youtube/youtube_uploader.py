import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import *
import direct_upload
import schedule_upload
import datetime
import youtubelogin
import delete_videos
import scheduleoption4
import subprocess
import smtplib
from email.message import EmailMessage
import uuid
from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests
import tkinter.messagebox
import os
import cryptocode
from ttkbootstrap import Style
import base64
import my_image

 

icon=my_image.image.encode()
icondata= base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "yticon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()


def get_today_date():
        r=requests.get('https://www.calendardate.com/todays.htm')
        soup =BeautifulSoup(r.text,'html.parser')
        a=soup.find_all(id='tprg')[6].get_text().replace(' ','').replace('-','')
        return a


def connection_check():
    try:
        urllib2.urlopen('http://google.com',timeout=1)
        return True
    except:
        return False   

def license_key_checker():

        if connection_check()==True:

                try:    
                        cwd = os.getcwd()
                        f=open(f'{cwd}//licensekey.txt','r')
                        read_key=f.readline().rstrip()
                        decripted_key=cryptocode.decrypt(read_key, "BD2225409@slt")
                        if decripted_key!=False:
                      

                                if decripted_key.split(':')[0]==str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip():
                                    if int(decripted_key.split(':')[2])>int(get_today_date()):
                                                            pass
                                    else:
                                            main_frame.destroy()
                                            root=Tk()
                                            root.withdraw()

                                            tkinter.messagebox.showinfo("warning","Key expired")
                                else:
                                            main_frame.destroy()
                                            root=Tk()
                                            root.withdraw()

                                            tkinter.messagebox.showinfo("warning","Error-You are using different device")
                        else:
                                main_frame.destroy()
                                root=Tk()
                                root.withdraw()

                                tkinter.messagebox.showinfo("warning","Invalid key")
                                                    
                                            
                                                                      

                        


                except:
                        main_frame.destroy()
                        request_licence__frame()
        else:
                main_frame.destroy()
                root=Tk()
                root.withdraw()

                tkinter.messagebox.showinfo("warning","Please check your internet connection")




def main_frame():
        global expiredate

        style = Style(theme='cyborg')
        root = style.master





        root.title("YT Auto Upload Scheduler")
        root.wm_iconbitmap(tempFile)


        root.geometry("500x600")
        root.resizable(width =False, height=False)


        select_video_folder = None
        def select_folder():
            global select_video_folder
            select_video_folder = filedialog.askdirectory()
            video_folder.config(text='Selected',style='success.TButton')


        def getdate():
            date = datepicker.selection_get()
            day = date.strftime("%Y-%m-%d")
            return day



        select_profile_folder = None
        def select_profile():
            global select_profile_folder
            select_profile_folder = filedialog.askdirectory()
            select_profile_button.config(text='Selected',style='success.TButton')


        def create_profile():
            global new_profile_folder
            new_profile_folder = filedialog.askdirectory()
            create_profile_button.config(text= 'Created',style='success.TButton')
            youtubelogin.login(new_profile_folder)


        def upload():
            license_key_checker()
            global select_video_folder
            global select_profile_folder
            direct_upload.func(select_video_folder,video_type.get(),select_profile_folder,input_addcard.get())


        def schedule():
            license_key_checker()
            global select_video_folder
            global select_profile_folder
            if videouploadoption.get() ==1:
                schedule_upload.func(select_video_folder,video_type.get(),deltime=timeinterval.get(),profilepath=select_profile_folder,addcardinput=input_addcard.get())

            elif videouploadoption.get() ==2:
                schedule_upload.func(select_video_folder, video_type.get(),fromtime=sttime(fromtime.get()),totime=sttime(totime.get()),date=getdate(), deltime=timeinterval.get(),profilepath=select_profile_folder,addcardinput=input_addcard.get())

            elif videouploadoption.get() ==3:
                schedule_upload.func(select_video_folder, video_type.get(), fromtime=sttime(timepicker.get()),date=getdate(),
                                     deltime=timeinterval.get(),nm=no_of_videos.get(),profilepath=select_profile_folder,addcardinput=input_addcard.get())
            elif videouploadoption.get() ==4:
                scheduleoption4.func(select_video_folder, video_type.get(),profilepath=select_profile_folder,fromtime=sttime(timepicker.get()),date=getdate(),nm=no_of_videos.get(),addcardinput=input_addcard.get())    


        def sttime(st):
            t = st +":"+"00"


            return t








        def delete_all_videos():
            license_key_checker()
            global select_profile_folder
            delete_videos.delete(select_profile_folder)


        select_profile_button = ttk.Button(root, text="Select profile",style='info.TButton', command=lambda: select_profile())
        select_profile_button.place(x=200, y=10)
        create_profile_button = ttk.Button(root, text="Create profile",style='info.TButton', command=lambda: create_profile())
        create_profile_button.place(x=375, y=80)
        upload_button = ttk.Button(root, text="Direct upload",style='info.TButton', command=lambda: upload())
        upload_button.place(x=30, y=510)
        schedule_button = ttk.Button(root, text="Schedule upload", style='info.TButton', command=lambda: schedule())
        schedule_button.place(x=350, y=510)
        video_folder =ttk.Button(root, text="Select video folder", style='info.TButton', command=lambda: select_folder())

        video_folder.place(x=350, y=10)
        delete_button = ttk.Button(root, text="Delete all videos",style='info.TButton' , command=lambda: delete_all_videos())
        delete_button.place(x=200,y = 560)



        video_type_options = ["select video type","short video","long video"]
        def change(event):


            selection = video_type.current()


            if video_type_options[selection]=='long video':

                                    input_addcard.config(state=NORMAL)
                                    delete_button.config(state=DISABLED)
                                    video_folder.config(state=NORMAL)
                                    upload_button.config(state=NORMAL)
            elif video_type_options[selection]=='short video':

                                    input_addcard.config(state=DISABLED) 
                                    delete_button.config(state=DISABLED)
                                    video_folder.config(state=NORMAL) 
                                    upload_button.config(state=NORMAL)
            elif video_type_options[selection]=='select video type':

                                    input_addcard.config(state=DISABLED) 
                                    delete_button.config(state=NORMAL) 
                                    video_folder.config(state=DISABLED) 
                                    upload_button.config(state=DISABLED)
                                    schedule_button.config(state=DISABLED)


        video_type = ttk.Combobox(root, style='danger.TCombobox',values=video_type_options)
        video_type.place(x=20,y = 10)
        video_type.current(0)
        video_type.bind("<<ComboboxSelected>>", change)
        def sel():
                selection = "You selected the option " + str(videouploadoption.get())

                if videouploadoption.get() ==0:
                            schedule_button.config(state=DISABLED)
                            timeinterval.config(state=DISABLED)
                            upload_button.config(state=NORMAL)
                            datepicker.config(state=DISABLED)
                            fromtime.config(state=DISABLED)
                            totime.config(state=DISABLED)
                            no_of_videos.config(state=DISABLED)

                elif videouploadoption.get() ==1:
                            fromtime.config(state=DISABLED)
                            totime.config(state=DISABLED)

                            datepicker.config(state=DISABLED)
                            timepicker.config(state=DISABLED)
                            no_of_videos.config(state=DISABLED)
                            upload_button.config(state=DISABLED)
                            timeinterval.config(state=NORMAL) 
                            schedule_button.config(state=NORMAL)
                elif videouploadoption.get() ==2:
                                fromtime.config(state=NORMAL)
                                totime.config(state=NORMAL)
                                timeinterval.config(state=NORMAL)

                                datepicker.config(state=NORMAL)
                                timepicker.config(state=DISABLED)
                                no_of_videos.config(state=DISABLED)
                                upload_button.config(state=DISABLED)
                                schedule_button.config(state=NORMAL) 
                elif videouploadoption.get() ==3:
                                fromtime.config(state=DISABLED)
                                totime.config(state=DISABLED)
                                timeinterval.config(state=NORMAL)
                                datepicker.config(state = NORMAL)
                                timepicker.config(state=NORMAL)
                                no_of_videos.config(state=NORMAL)
                                upload_button.config(state=DISABLED)  
                                schedule_button.config(state=NORMAL) 



                elif videouploadoption.get() ==4:
                            no_of_videos.config(state=NORMAL)
                            schedule_button.config(state=NORMAL)
                            datepicker.config(state = NORMAL)
                            timeinterval.config(state=DISABLED)
                            timepicker.config(state=NORMAL)
                            fromtime.config(state=DISABLED)
                            totime.config(state=DISABLED)
                            upload_button.config(state=DISABLED)  



        videouploadoption = IntVar()
        schedule_option0 = ttk.Radiobutton(root, text="Direct upload",style='info.TRadiobutton', variable=videouploadoption, value=0,
                          command=sel)

        schedule_option0.place(x=20, y=50)
        schedule_option1 = ttk.Radiobutton(root, text="Schedule from now",style='info.TRadiobutton', variable=videouploadoption, value=1,
                          command=sel)

        schedule_option1.place(x=20, y=80)
        schedule_option2 = ttk.Radiobutton(root, text="Schedule Option-2",style='info.TRadiobutton', variable=videouploadoption, value=2,
                          command=sel)

        schedule_option2.place(x=20, y=110)  
        schedule_option3 = ttk.Radiobutton(root, text="Schedule Option-3",style='info.TRadiobutton', variable=videouploadoption, value=3,
                          command=sel)

        schedule_option3.place(x=20, y=140)      
        schedule_option4 = ttk.Radiobutton(root, text="Schedule Option-4",style='info.TRadiobutton', variable=videouploadoption, value=4,
                          command=sel)

        schedule_option4.place(x=20, y=170)    



        times = ['00:00','01:00' ,'02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00'
                 ,'12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']

        global fromtime
        label1 = ttk.Label(root, text='FROM',style='inverse.TLabel')
        label1.place(x=20,y=200)
        fromtime = ttk.Combobox(root, style='danger.TCombobox',value=times,state=DISABLED)
        fromtime.current(0)
        fromtime.bind("<<Comboboxselected>>")
        fromtime.place(x=70,y=200)

        global totime
        label2 = ttk.Label(root,text='TO',style='inverse.TLabel')
        label2.place(x=250,y=200)
        totime = ttk.Combobox(root, style='danger.TCombobox',value=times,state=DISABLED)
        totime.current(0)
        totime.bind("<<Comboboxselected>>")
        totime.place(x=280,y=200)

        global datepicker
        datepicker = Calendar(root,selectmode='day',date_pattern='yyyy-mm-dd',state=DISABLED )
        datepicker.place(x=20,y=270)

        deltatime = ['15','30','45','60','90','120']
        global timepicker
        timepicker = ttk.Combobox(root, style='danger.TCombobox',value=times, state=DISABLED)
        timepicker.current(0)
        timepicker.bind("<<Comboboxselected>>")
        timepicker.place(x=300,y=270)

        label3 = ttk.Label(root,text='time interval',style='inverse.TLabel')
        label3.place(x=20,y=470)
        timeinterval = ttk.Combobox(root, style='danger.TCombobox',value=deltatime)
        timeinterval.current(0)
        timeinterval.bind("<<Comboboxselected>>")
        timeinterval.place(x=120,y=470)


        lable4 = ttk.Label(root, text='Enter number of videos',style='inverse.TLabel')
        lable4.place(x=300,y=330)
        no_of_videos = ttk.Entry(root,width=5)

        no_of_videos.place(x=300,y=370)

        lable5 = ttk.Label(root, text='Input for endcard',style='inverse.TLabel')
        lable5.place(x=300,y=400)
        input_addcard = ttk.Entry(root,width=20)

        input_addcard.place(x=300,y=440)
        telegram_link_label = ttk.Label(root, text='t.me/mmo_tool',style='inverse.TLabel')
        telegram_link_label.place(x=380,y=570)

        expiredate_format=f'expire: {expiredate[4:6]}/{expiredate[6:]}/{expiredate[:4]}'
        expiredate_label = ttk.Label(root, text=expiredate_format,style='inverse.TLabel')
        expiredate_label.place(x=20,y=570)

        schedule_button.config(state=DISABLED)
        timeinterval.config(state=DISABLED)

        datepicker.config(state=DISABLED)
        fromtime.config(state=DISABLED)
        totime.config(state=DISABLED)
        input_addcard.config(state=DISABLED)
        no_of_videos.config(state=DISABLED)
        video_folder.config(state=DISABLED)
        upload_button.config(state=DISABLED)
        style.map("TEntry",fieldbackground=[("active", "white"), ("disabled", "#00151A")])



        root.mainloop()



def enter_license_key_frame():

                def check_key():
                  


                             enc_license_key=enter_license_key_label_entry.get()

                             
                           
                             
                             
                             license_key=cryptocode.decrypt(enc_license_key, "BD2225409@slt")

                             
                             if license_key!=False:
                            
                                             if license_key.split(':')[0]==str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip():
                                                        root=Tk()
                                                        root.withdraw()

                                                        tkinter.messagebox.showinfo("msg","Activated")
                                                        cwd = os.getcwd()
                                                        
                                                        f=open(f'{cwd}//licensekey.txt','w')
                                                        f.write(enc_license_key)
                                                        f.close()
                                                        third_window.destroy()

                                             else:
                                                        root=Tk()
                                                        root.withdraw()

                                                        tkinter.messagebox.showinfo("msg","Invalid key")
                                                        third_window.destroy()
                             

                             else:

                                                        root=Tk()
                                                        root.withdraw()

                                                        tkinter.messagebox.showinfo("msg","Invalid key")
                                                        third_window.destroy()
                                                
                                      




                global reference_id
                style = Style(theme='cyborg')
                third_window = style.master 


                third_window.title("YT Auto Upload Scheduler")
                
                third_window.wm_iconbitmap(tempFile)

               

                
                third_window.geometry("400x300")
                third_window.resizable(width =False, height=False)



                reference_id_str=f'Reference id : {reference_id}'
                enter_license_key_label = ttk.Label(third_window, text='Enter your license key',style='success.TLabel',font=('Helvetica', 18))
                enter_license_key_label.place(x=80,y=50)
                reference_id_label = ttk.Entry(third_window,style='info.TEntry',width=42)
                reference_id_label.place(x=50,y=90)
                reference_id_label.insert(0, reference_id_str)
                reference_id_label.configure(state="readonly")
                enter_license_key_label_entry = Entry(third_window,width=50,background='white')
                enter_license_key_label_entry.place(x=22,y=140)



                request_license_key_button = ttk.Button(third_window, text="Submit license key",style='info.TButton', command=lambda: check_key())
                request_license_key_button.place(x=130, y=200)


                third_window.mainloop()




def request_licence__frame():

        def requestkey():
                    global reference_id
                    second_window.destroy()

                    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

                    msg = EmailMessage()
                    msg.set_content(current_machine_id)
                    reference_id=uuid.uuid4().hex
                    msg['Subject'] = f'License request from youtube uploader: {reference_id}'
                    msg['From'] = "ytscheduleuploader@gmail.com"
                    msg['To'] = "sokleabhim@gmail.com"


                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("ytscheduleuploader@gmail.com", "iicslwnpfbbrtqzo")
                    server.send_message(msg)
                    server.quit()

                    enter_license_key_frame()


       
        style = Style(theme='cyborg')
        second_window = style.master            


        


        second_window.title("YT Auto Upload Scheduler")
        second_window.wm_iconbitmap(tempFile)
        second_window.geometry("400x300")
        second_window.resizable(width =False, height=False)
        no_license_keylablel = ttk.Label(second_window, text='No license key found',style='danger.Inverse.TLabel',font=('Helvetica', 16))
        no_license_keylablel.place(x=105,y=50)
        request_license_key_button = ttk.Button(second_window, text="Request a license key",style='info.TButton',width=15, command=lambda: requestkey())
        request_license_key_button.place(x=130, y=200)
        second_window.mainloop()
 
if connection_check()==True:

        try:    
                cwd = os.getcwd()
                f=open(f'{cwd}//licensekey.txt','r')
                read_key=f.readline().rstrip()
                decripted_key=cryptocode.decrypt(read_key, "BD2225409@slt")
                
                if decripted_key!=False:
              

                        if decripted_key.split(':')[0]==str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip():
                            if int(decripted_key.split(':')[2])>int(get_today_date()):
                                                     expiredate=decripted_key.split(':')[2]
                                                     main_frame() 
                            else:
                                    root=Tk()
                                    root.withdraw()

                                    tkinter.messagebox.showinfo("warning","Key expired")
                        else:
                                    root=Tk()
                                    root.withdraw()

                                    tkinter.messagebox.showinfo("warning","Error-You are using different device")
                else:
                        root=Tk()
                        root.withdraw()

                        tkinter.messagebox.showinfo("warning","Invalid key")
                                            
                                    
                                                              

                


        except:
                request_licence__frame()
else:
        root=Tk()
        root.withdraw()

        tkinter.messagebox.showinfo("warning","Please check your internet connection")

       

