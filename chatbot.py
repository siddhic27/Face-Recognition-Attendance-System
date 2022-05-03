from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind("<Return>",self.enter_func)


        main_frame=Frame(self.root,bd=4,bg="dodger blue",width=610)
        main_frame.pack()

        img_chat=Image.open(r"C:\Users\siddh\Desktop\final\project images\chatbot.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_lbl=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=730,compound=LEFT,image=self.photoimg,text="Chat Me",font=("arial",30,"bold"),fg="sky blue",bg="white")
        Title_lbl.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=("arial",14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        
        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg="sky blue",bg="white")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("times new roman",16,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="SEND",command=self.send,font=("arial",13,"bold"),width=8,bg="dodger blue",)
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=("times new roman",15,"bold"),width=8,bg="dodger blue",)
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=""
        self.label_2=Label(btn_frame,text=self.msg,font=("arial",14,"bold"),fg="sky blue",bg="white")
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)

    #==========function declaration===========

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete("1.0",END)
        self.entry.set("")


    def send(self):
        send="\t\t\t"+"You: "+self.entry.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg="Please Enter Some Input"
            self.label_2.config(text=self.msg,fg="red")

        else:
            self.msg=""
            self.label_2.config(text=self.msg,fg="red")

        
        if(self.entry.get()=="hello"):
            self.text.insert(END,"\n\n"+"BOT: Hi")

        elif(self.entry.get()=="hi"):
            self.text.insert(END,"\n\n"+"BOT: Hello")
        
        elif(self.entry.get()=="ok"):
            self.text.insert(END,"\n\n"+"BOT: Yes")

        elif(self.entry.get()=="how are you?"):
            self.text.insert(END,"\n\n"+"BOT: Fine and You?")

        elif(self.entry.get()=="Fantastic"):
            self.text.insert(END,"\n\n"+"BOT: Nice to hear")

        elif(self.entry.get()=="what is your name?"):
            self.text.insert(END,"\n\n"+"BOT: mr. Bot")


        elif(self.entry.get()=="Can you  speak Marathi"):
            self.text.insert(END,"\n\n"+"BOT: I'm still learning it..")

        elif(self.entry.get()=="How does Face Recognition work?"):
            self.text.insert(END,"\n\n"+"BOT: Facial Recognition is way of\nrecognizing a human face through\ntechnology.A facial recognition\nsystem uses biometrics to map\nfacial features from aphotographer\nor video.")

        elif(self.entry.get()=="How does facial recognition work step by step?"):
            self.text.insert(END,"\n\n"+"BOT: Step1: Face Detection.The camera\ndetects and locates the image of a face,\nneither alone or in a crowd. ...\nStep2: Face analysis. Next,an image of\n the face is captured and analyzed.  ...\nStep3: Converting the image to data.\nThe face captures process transforms analog information\ninto a set of digital information based on the person's\nfacial features. ...\nStep4: Finding Match. Your  Faceprint is compared\nagainst a database of other known faces.")

        elif(self.entry.get()=="How many countries use facial recognition?"):
            self.text.insert(END,"\n\n"+"BOT:In use 98\nApproved,but not implemented  12\nConsidering facial recognition technology  13\nNo evidence of use 68 ")

        elif(self.entry.get()=="Where you save all records?"):
            self.text.insert(END,"\n\n"+"BOT: In Database")

        elif(self.entry.get()=="What is ChatBot?"):
            self.text.insert(END,"\n\n"+"BOT: A ChatBot is a computer\nprogram that's designed to\nsimulate human conversation")

        elif(self.entry.get()=="Bye"):
            self.text.insert(END,"\n\n"+"BOT: Thank You For Chatting")

        else:
            self.text.insert(END,"\n\n"+"BOT: Sorry! I didn't get it")

        
if __name__ == "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
