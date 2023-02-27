Thuật toán AES sử dụng để mã hoá từng khối có độ lớn 128 bit 
*first_aes : lập trình thuật toán AES ban đầu dựa theo lí thuyết :

- Các hàm trong thuật toán:
  + Chuyển đổi thập lục phân về nhị phân , nhị phân về thập phân và ngược lại
  + Các hàm là các phép toán sử dụng trong AES - 128 : hàm ánh xạ Sbox, hàm 
    logic XOR, hàm chuyển hàng ma trận ....

- Test : file > 100kb thuật toán không chạy được
         file < 100kb chạy từ 5 -> 10p : không đáp ứng yêu cầu

*aes : lập trình AES cải thiện tốc độ chạy

- Tìm hiểu thuật toán để định dạng dễ hơn
- Sử dụng Class, định dạng kiểu
- Test : file 2MB chạy 10 - 15s

* Nguồn tham khảo: sách Cryptography and Network Security, 
                   pycrypto documentation.