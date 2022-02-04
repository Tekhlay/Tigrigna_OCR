#importing necessary Libraries
import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog
#from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

'''img = cv2.imread('Sample Image datas/Tempo.jpg')
img = cv2.medianBlur(img,1)
#cv2.imshow("Image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (600, 300))
norm_img = (gray-np.min(gray))/(np.max(gray)-np.min(gray))
th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 2)

config = "--psm 3"
text = pytesseract.image_to_string(img,config=config,lang ='tig')
#print("Recognised Text:",text)

#cv2.imshow("Thresould", norm_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

tig_OCR = Tk()
tig_OCR.title("Tigrigna OCR System")
tig_OCR.geometry("650x600+100+10")
tig_OCR.config(bg="#F1E5E4")
tig_OCR.resizable(width=True, height = True)

pad = {'padx' :3, 'pady':3}
imgL = Label(tig_OCR,text="Upload Image", font = ("Times",15,'bold'),bg="#F1E5E4", fg="#C70039").grid(row = 0, column = 0, sticky = W,**pad)

def extract(txt):
    orginal_image = cv2.imread(txt)
    #orginal_image = cv2.medianBlur(orginal_image,1)
    sample_img = cv2.resize(orginal_image,(500,350))
    w,h,t = sample_img.shape
    gray = cv2.cvtColor(sample_img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    texts = pytesseract.image_to_string(orginal_image,lang='tig')
    #print(texts)
    '''mytxt = ""
    pre = 0
    for cnt, text in enumerate(texts.splitlines()):
        if cnt ==0:
            continue
        text = text.split()
        if len(text) == 12:
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            if len(mytxt) ==0:
                pre = y
            if (pre - y >=10 or y-pre >=10):
                print(mytxt)
                Label(tig_OCR, text=mytxt,font = ("Times",15,'bold')).grid(row = 8, column = 2,columnspan = 2, rowspan = 6, **pad)
                mytxt = ""
            mytxt = mytxt + text[11]+" "
            pre = y
        '''
    
    e= Text(tig_OCR, bd = 5, font = ("Times",15,'bold'),width=40,height=10)
    e.grid(row = 8, column = 2, **pad)
    e.insert(END,texts)
    
    s = Scrollbar(tig_OCR, orient="vertical", command=e.yview).grid(row = 8, column = 3, sticky='NS')
    #e.configure(yscrollcommand=s.set)


def extract_button(txt):
    extractbtn = Button(tig_OCR, text ="Extract Text",command=lambda:extract(txt),bg="#2404C3",fg="yellow",font=('Times',15,'bold')).grid(row=7,column=2,**pad)



def openfilename():
    file_types=[("JPG",'*.jpg'),('PNG','*.png'),('TIF','*.tif')]
    filename = filedialog.askopenfilename(filetypes=file_types)
    return filename

def upload():
    x  = openfilename()
    img = Image.open(x)
    #w,h = img.size
    #w = int(w/2)
    #h = int(h/2)
    img = img.resize((250,250),Image.ANTIALIAS)
    #img = img.resize((w,h))
    img = ImageTk.PhotoImage(img)
    upload_img= Label(tig_OCR,image=img)
    upload_img.image = img
    upload_img.grid(row = 0, column = 2,columnspan = 2, rowspan = 6, **pad)
    extract_button(x)

imgbtn = Button(tig_OCR,text = "Browse", command=upload, font = ("Times new Romans",12,'bold'),bg="#2404C3",fg="yellow",height=1,width=6).grid(row = 1, column = 0, sticky = W,**pad)

exit = Button(tig_OCR,text = "Exit", command=tig_OCR.destroy, font = ("Times new Romans",12,'bold'),bg="#2404C3",fg="yellow",height=1,width=6).grid(row = 10, column = 4, sticky = W,**pad)


    
#scrol = Scrollbar(tig_OCR,orient=VERTICAL).grid(row=0, column=1, sticky=NS)

tig_OCR.mainloop()
