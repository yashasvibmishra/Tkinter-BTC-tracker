from tkinter import *
import tkinter.messagebox
import threading
import requests
from datetime import datetime
import json
import threading

# add some new features 
class Bitcoin():
    def __init__(self,root):
        self.root=root
        self.root.title("Bitcoin price - Opening & Closing")
        self.root.geometry("500x350")
        self.root.configure(background="white")

        self.root.resizable(0,0)

    
        def on_enter1(e):
            but_bitcoin['background']="black"
            but_bitcoin['foreground']="red"
            but_bitcoin['activebackground']="black"
            but_bitcoin['activeforeground']="red"
            but_bitcoin['relief']="flat"

  
        def on_leave1(e):
            but_bitcoin['background']="SystemButtonFace"
            but_bitcoin['foreground']="SystemButtonText"
            but_bitcoin['activebackground']="SystemButtonFace"
            but_bitcoin['activeforeground']="SystemButtonText"
            but_bitcoin['relief']="flat"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="red"
            but_clear['activebackground']="black"
            but_clear['activeforeground']="red"
            but_clear['relief']="flat"

  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"
            but_clear['activebackground']="SystemButtonFace"
            but_clear['activeforeground']="SystemButtonText"
            but_clear['relief']="flat"




        def bitcoins():
            try:

                clear()
               
                response=requests.get('https://www.bitstamp.net/api/ticker/bitcoin')
                json_response=json.loads(response.text)
                open_rate=json_response['open']
                highest_rate=round(float(json_response['high']),2)
                lowest_rate=round(float(json_response['low']),2)
                latest_rate=json_response['last']
                updated_at=datetime.fromtimestamp(int(json_response['timestamp']))
                updated_at=updated_at.strftime('%Y-%m-%d %H:%M:%S')
                volume=json_response['volume']
                volume=round(float(volume),2)
                volume=str(volume)
                volume=volume+" BTC"
                volume=volume.replace(".",",")
                volume=volume.replace("BTC"," BTC")
                

              

                info=f"""
Opening Rate of Bitcoin: {str(open_rate)}

Highest Rate of Bitcoin : {str(highest_rate)}

lowest Rate of Bitcoin :{str(lowest_rate)}

Latest Rate of Bitcoin  :{str(latest_rate)}

Updated Rate of Bitcoin :{str(updated_at)}

Volume of Bitcoin :{str(volume)}




                    """
                text.insert("end",info)
                   
            except Exception as e:
                print(e)
                tkinter.messagebox.showerror("Error","Network Error")


        
        def thread_score():
            t=threading.Thread(target=bitcoins)
            t.start()

        def clear():
            text.delete("1.0","end")


        mainframe=Frame(self.root,width=500,height=350,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=100,relief="ridge",bd=3,bg="yellow")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=243,relief="ridge",bd=3)
        secondframe.place(x=0,y=100)
        
        but_bitcoin=Button(firstframe,width=13,text="BTC",font=('consolas',12),cursor="hand2",command=thread_score)
        but_bitcoin.place(x=60,y=28)
        but_bitcoin.bind("<Enter>",on_enter1)
        but_bitcoin.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=13,text="CLEAR CONSOLE",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=290,y=28)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)
        
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('consolas',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
       

if __name__ == "__main__":
    root=Tk()
    app=Bitcoin(root)
    root.mainloop()
