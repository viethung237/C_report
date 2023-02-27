#import modules
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import  os
import cbc
import binascii

class IMG_Stegno:
    output_image_size = 0
    
    #khoi tao giao dien goc
    def main(self, root):
        root.title('ImageSteganography by HUST')
        root.geometry('900x650')
        root.resizable(width =False, height=False)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()
        
        title = Label(frame,text='ET E9 Image Steganography')
        title.config(font=('Verdana',25, 'bold'))
        title.grid(pady=10)
        title.config(bg = '#e3f4f1')
        title.grid(row=1)
        #chuc nang giau tin
        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14,bg = '#e3f4f1' )
        encode.config(font=('Helvetica',14), bg='#e8c1c7')
        encode.grid(row=2)
        #chuc nang giai ma tin
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14,bg = '#e3f4f1')
        decode.config(font=('Helvetica',14), bg='#e8c1c7')
        decode.grid(pady = 12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)



    #ham quay tro lai giao dien trc
    def back(self,frame):
        frame.destroy()
        self.main(root)

    
    #khoi tao giao dien giau tin
    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image you want to hide text :')
        label1.config(font=('Verdana',25, 'bold'),bg = '#e3f4f1')
        label1.grid()
        #tao chuc nang chon anh
        button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        #chuc nang cancel
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',18),bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()

    #khoi tao giao dien lay tin
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#e3f4f1')
        label1.grid()
        label1.config(bg = '#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()


    #khoi tao giao dien giau tin 2
    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        #chon anh tu directory
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            #hien thi anh ra giao dien
            my_img = Image.open(myfile)
            new_image = my_img.resize((400,300))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Helvetica',14,'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            #tao box dien text
            label2 = Label(e_pg, text='Enter the message')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            #huy de quay lai man hinh ban dau
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Helvetica',14), bg='#e8c1c7')
            encode_button.grid(pady=1)
            data = text_a.get("1.0", "end-1c")
            #tao chuc nang giau tin
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('Helvetica',14), bg='#e8c1c7')
            button_back.grid(pady=1)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()





    #khoi tao giao dien lay tin 2
    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :self.frame_3(d_F3))
            button_back.config(font=('Helvetica',14),bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()


    #ham lay tin
    def decode(self, image):
        
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                key = b'Sixteen byte key'
                iv = b'Sixteen byte iv.'
                return self.aes_dec(data, key, iv).replace('0','')

    #tra ve list chua data la cac chuoi nhi phan 8 bit
    def generate_Data(self,data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    #LSB function
    def modify_Pix(self,pix, data):
        """B1 : lấy từng bộ 3 pixel của ảnh, chuyển dữ liệu cần giấu thành list các chuỗi nhị phân 8 bit
           B2 : Đối với mỗi bộ ba pixel, phương thức sẽ kiểm tra từng bit trong số tám bit có ý nghĩa nhỏ nhất để xem liệu nó có cần được sửa đổi hay không dựa trên giá trị nhị phân tương ứng trong danh sách data.
             Nếu giá trị nhị phân là 0 và bit có ý nghĩa nhỏ nhất của giá trị pixel là số lẻ,
               thì nó sẽ trừ 1 khỏi giá trị pixel để làm cho nó trở thành số chẵn. 
             Nếu giá trị nhị phân là 1 và bit có ý nghĩa nhỏ nhất của giá trị pixel là số chẵn, 
             nó sẽ trừ 1 khỏi giá trị pixel để làm cho nó trở thành số lẻ. """
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # dung ham iter va next de trich ra 3 pixel 1 vong
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            #gia tri pixel cuoi dung de danh dau phan ket thuc cua ma dc an vao
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    
    #an tin
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    
    # ma hoa aes
    def aes_enc(self,data,key,iv):
        
        data_bytes = data.encode('utf-8')
        cbc_mode = cbc.CbcMode(key,iv)
        data_to_image = cbc_mode.encrypt(data_bytes)
        data_hex = binascii.hexlify(data_to_image).decode('utf-8')
        return data_hex
    #giai ma aes
    def aes_dec(self,data,key,iv):
        data2 = binascii.unhexlify(data)
        cbc_mode = cbc.CbcMode(key,iv)
        data_decrypt = cbc_mode.decrypt(data2)
        return data_decrypt.decode('utf-8')
            
            

    #thuc hien chuc nang giau tin     
    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Enter text in TextBox")
        else:
            key = b'Sixteen byte key'
            iv = b'Sixteen byte iv.'
            newImg = myImg.copy()
            self.encode_enc(newImg,self.aes_enc(data,key,iv))
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved")
    
    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


#vong lap GUI
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
