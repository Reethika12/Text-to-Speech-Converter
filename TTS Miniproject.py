from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from tkinter.ttk import Combobox
from gtts import gTTS
from tkinter import messagebox
import PyPDF2
import pyttsx3
import easyocr
import webbrowser
import os
import clipboard
from playsound import playsound
from tkinter.filedialog import askopenfilename
import threading
#image to text
def image2text():
    def extract_text():
        filepath = filedialog.askopenfilename(title='Open Image File', filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if not filepath:
            return
        reader = easyocr.Reader(['en'])
        result = reader.readtext(filepath)

        extracted_text = ''
        for res in result:
            extracted_text += res[1] + ' '

        text_display.delete(1.0, END)  
        text_display.insert(END, extracted_text)
        
    def cls1():
         text_display.delete(1.0, END)
    
    def select():
        text_display.tag_add('sel','1.0','end')
        text_display.tag_config('sel',foreground='brown')     
     
    ocrwindow = Tk()
    ocrwindow.title('Image Text Extractor')
    ocrwindow.geometry("1000x580+200+80")
    ocrwindow.configure(bg='#B3ECD4')
    ocrwindow.resizable(False,False)
    Label(ocrwindow,text="Image to Text Converter",font="Arial 20 bold",fg="black").pack(fill="x",pady=15)


    extract_button = Button(ocrwindow, text='Extract Text', command=extract_text)
    extract_button.place(x=485,y=500)


    text_display = Text(ocrwindow, height=50, width=30,font='TimesNewRoman 20', bg='white',relief= GROOVE, wrap= WORD,bd=0)
    text_display.place(x=30,y=150,width=940,height=180)
    
    clear_btn = Button(ocrwindow,text = "Clear",command= cls1,width=10)
    clear_btn.place(x=300,y=400)#,padx=80,pady=100
    
    copy_b=Button(ocrwindow,text='copy',command=lambda:text_display.event_generate("<<Copy>>"),width=10)
    copy_b.place(x=500,y=400)
    
    select_all=Button(ocrwindow,text='Select All',command=select,width=10)
    select_all.place(x=700,y=400)
    
    ocrwindow.mainloop()
    
#textreader
tts= pyttsx3.init()
def texts():
    
    def speaknow():
        text= text_box.get(1.0,END)
        gender= gender_box.get()
        speed = speed_box.get()
        voices = tts.getProperty('voices')
        
        def setvoice():
            if gender=='Male':
                tts.setProperty('voice',voices[0].id)
                tts.say(text)
                tts.runAndWait()
                
            else:
                tts.setProperty('voice', voices[1].id)
                tts.say(text)
                tts.runAndWait()
            
        if(text):
                if(speed == 'Fast'):
                    tts.setProperty('rate',250)
                    setvoice()
                elif (speed == 'Medium'):
                    tts.setProperty('rate',150)
                    setvoice()
                else:
                    tts.setProperty('rate',60)
                    setvoice()
    def  download():
        text= text_box.get(1.0,END)
        gender= gender_box.get()
        speed = speed_box.get()
        voices = tts.getProperty('voices')
        
        def setvoice():
            if gender=='Male':
                tts.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                tts.save_to_file(text,'text.mp3')
                tts.runAndWait()
                
            else:
                tts.setProperty('voice', voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                tts.save_to_file(text,'text.mp3')
                tts.runAndWait()
            
        if(text):
                if(speed == 'Fast'):
                    tts.setProperty('rate',250)
                    setvoice()
                elif (speed == 'Medium'):
                    tts.setProperty('rate',150)
                    setvoice()
                else:
                    tts.setProperty('rate',60)
                    setvoice()
    
    def cls1():
         text_box.delete(1.0, END)
                       
        
    import tkinter as tk
    gttswindow = Tk()
    gttswindow.title('Text-to-Speech')
    gttswindow.geometry("1000x580+200+80")
    gttswindow.configure(bg='#9384D1')
    gttswindow.resizable(False,False)

    #Upper Frame
    upper_frame= Frame(gttswindow, bg='#FFDCB6', width=1200,height=130)
    upper_frame.place(x=0,y=0)

    #Title
    Label(upper_frame,text='Text to Speech Converter', font='TimesNewRoman 40 bold',
        bg='#FFDCB6', fg='black').place(x=200,y=35)


    #Text box input
    text_box = Text(gttswindow, font='TimesNewRoman 20', bg='white',relief= GROOVE, wrap= WORD,bd=0)
    text_box.place(x=30,y=150,width=940,height=180)

    #Gender Selection
    gender_box= Combobox(gttswindow,values=['Male','Female'], font=' TimesNewRoman 12', state='r',width=15)
    gender_box.place(x=310,y=350)
    gender_box.set('Male')

    #Speed Selection
    speed_box = Combobox(gttswindow,values=['Fast','Medium','Slow'], font= 'TimesNewRoman 12',state='r',width=15)
    speed_box.place(x=540,y=350)
    speed_box.set('Medium')

    #Play Button
    play_btn= Button(gttswindow,text='Play',compound=LEFT, bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= speaknow)
    play_btn.place(x=430,y=400)
    
    #Save Button
    save_btn=Button(gttswindow,text='Save',compound=LEFT,bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= download)
    save_btn.place(x=430,y=500)
    
    #clear
    clear_btn = Button(gttswindow, compound=RIGHT,text = "Clear",bg='white',width=10,font='TimesNewRoman 14 bold',
                    borderwidth = '0.1c',command= cls1)
    clear_btn.place(x=430,y=450)


    gttswindow.mainloop()   

    
 #pdfreader
def readers():
    
    window = Tk()
    window.title("Audiobook")
    window.geometry('650x500')
    window.resizable(False,False)
    def cls2():
        textboxp.delete(1.0, END)
    def audio_():
        speaker = pyttsx3.init()
        speaker.say(textboxp.get("1.0",END))
        speaker.runAndWait()
    def thread():
        x = threading.Thread(target=audio_)
        x.start()
    def tpages():
        filelocation = askopenfilename()
        book = open(filelocation, 'rb')
        pdfReader = PyPDF2.PdfReader(book,strict=False)
        pages= len(pdfReader.pages)
        plabel = Label(tab2, text="total pages:" + str(pages))
        plabel.grid(row=3,column=12)
    def pdf_():
        filelocation = askopenfilename()
        book = open(filelocation, 'rb')
        pdfReader = PyPDF2.PdfReader(book,strict=False)
        pages= len(pdfReader.pages)
        plabel = Label(tab2, text="total pages:" + str(pages))
        plabel.grid(row=3,column=12)
        p1 = int(e1.get())
        p2 = int(e2.get())
        for x in range(p2-1,p1-2,-1):
            page = pdfReader.pages[x]
            text = page.extract_text()
            textboxp.insert(1.0,text)
    tab_control = ttk.Notebook(window)
    tab2 = Frame(tab_control)
    tab_control.add(tab2, text='PDF')
    label1 = Label(tab2, text = "Select a pdf file", font = ("Arial", 15),background = 'white')
    label1.grid(row = 0, column = 12, sticky=E+W)

    scroll = Scrollbar(tab2)
    scroll.grid(row = 1 , column = 13, sticky= "ns")
    textboxp= Text(tab2, height = 13, width = 50, wrap = "word",yscrollcommand = scroll.set)
    textboxp.grid(row= 1 , column = 12, sticky = "nsew")

    plabel1 = Label(tab2, text="First page")
    plabel1.grid(row=2,column=11, pady=5,padx=10,sticky= W)
    plabel3 = Label(tab2, text="Last page")
    plabel3.grid(row=2,padx=10,column=13,sticky= E)
    e1=Entry(tab2, width = 10)
    e1.grid(row=3,column=11, pady=5,padx=10,sticky= W)
    e2=Entry(tab2, width = 10)
    e2.grid(row=3,padx=10,column=13,sticky= E)


    button1 = Button(tab2, text = "Open",command = pdf_)
    button1.grid(pady = 10,row = 4,column=12)


    button1 = Button(tab2, text = "Convert",command =thread)
    button1.grid(pady = 10,row = 5,column=12)

    button1 = Button(tab2, text = "Clear",command = cls2)
    button1.grid(pady = 20,padx=10,row = 6, column = 11, sticky = W)

    button1 = Button(tab2, text = "Close",command = quit)
    button1.grid(pady = 20,padx=10,row = 6, column = 13, sticky=E)

    button1 = Button(tab2, text = "Check No.of Pages",command = tpages)
    button1.grid(pady = 20,padx=10,row = 6, column = 12)

    scroll.config(command = textboxp.yview)
    tab_control.grid(row = 0, column =1)

    window.mainloop()
        

def open_contact_form():
    def submit_contact_form():
    # Here you can handle the submission of the contact form data
    # For this example, we'll just print the data
        print("Name:", entry_name.get())
        print("Email:", entry_email.get())
        print("Message:", text_message.get("1.0", "end-1c"))
        message = text_message.get("1.0", "end-1c")
        if message.strip():  # Check if the message is not empty
        # Display a message box indicating the message is sent
            messagebox.showinfo("Message Sent", "Your message has been sent successfully!")
        else:
        # Display a message box if the message is empty
            messagebox.showwarning("Empty Message", "Please enter a message before sending.")

    
    # Create a new window for the contact form
    contact_form_window = tk.Toplevel(window)
    contact_form_window.geometry('500x500')
    
    # Add widgets to the contact form window
    # (e.g., labels, entry fields, buttons for the contact form)
    # Example label in the contact form window
    label = ttk.Label(contact_form_window, text="Contact Form")
    label.pack()
    label_name = ttk.Label(contact_form_window, text="Name:")
    label_name.pack()

    # Entry field for the name
    entry_name = ttk.Entry(contact_form_window, width=30)
    entry_name.pack()

    # Example label for email
    label_email = ttk.Label(contact_form_window, text="Email:")
    label_email.pack()

    # Entry field for email
    entry_email = ttk.Entry(contact_form_window, width=30)
    entry_email.pack()

    # Example message label
    label_message = ttk.Label(contact_form_window, text="Message:")
    label_message.pack()

    # Text field for the message
    text_message = tk.Text(contact_form_window, height=10, width=40)
    text_message.pack()

    # Button to submit the contact form
    submit_button = ttk.Button(contact_form_window, text="Submit", command=submit_contact_form)
    submit_button.pack()

# Function to handle the "Submit" button in the contact form



# Function to handle the "Contact us" button click
def contact_button_click(event):
    open_contact_form()  

window = Tk()
window.title('TTS')
window.geometry('750x650')

heading_label = ttk.Label(window, text='Find everything you want', font=('Helvetica', 20),foreground='lightgrey',background='purple')
heading_label.pack(pady=20)

c_button = ttk.Button(window, text='Image2text', command=image2text, width=20)
c_button.pack(pady=10)

f_button = ttk.Button(window, text='Textreader', command=texts, width=20)
f_button.pack(pady=10)

g_button = ttk.Button(window, text='Pdfreader', command=readers, width=20)
g_button.pack(pady=10)

contact_us_button = ttk.Button(window, text='Contact us', width=25)
# Bind the button click event to the contact_button_click function
contact_us_button.bind("<Button-1>", contact_button_click)
contact_us_button.pack(pady=10)


exit_button = ttk.Button(window, text='Exit', command=quit, width=25)
exit_button.pack(pady=10)

window.configure(bg='#B7EDEE')    
window.eval('tk::PlaceWindow . center')

window.mainloop()     