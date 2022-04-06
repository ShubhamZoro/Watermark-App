
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image, ImageTk

def watermark(file ,water_mark_text):
    image = Image.open(file)

    image_width=image.size
    image_height = image.size
    draw = ImageDraw.Draw(image)
    # It is done to increase the font sizeof text  with image if it will be fixed number like 50 then for high resolution image it will appear small
    font_size=int(image_width/8)

    font=ImageFont.truetype('arial.ttf',font_size)
    # add watermark
    draw.text((int(image_width/2), int(image_height/2)),water_mark_text ,fill='#FFF', stroke_fill="#222", anchor='ms',
               font=font)

    # to show the image
    image.show()







def open_file():
    file=filedialog.askopenfilename(initialdir='Users/shubh/Downloads')
    watermark(file,"Shubham Shekhar")


window=Tk()
window.title("Water Mark APP")
window.geometry('300x200')

lable=Label(text="Select the image",font=("Arial", 25))
lable.pack()
lable.place(relx=0.5, rely=0.3, anchor=CENTER)
Button1=Button(text="select image",command=open_file)
Button1.pack()
Button1.place(relx=0.5, rely=0.5, anchor=CENTER)
window.mainloop()

