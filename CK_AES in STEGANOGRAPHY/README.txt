*CBC Mode :(file cbc)
- Khi làm việc với khối lượng dữ liệu lớn(>128 bit) để thực hiện mã hoá AES,
chúng ta cần chia nhỏ dữ liệu thành từng khối 128 bit để có thể thực hiện 
mã hoá trên từng khối, việc liên kết các khối theo mode cbc.

*Steganography :
- kĩ thuật ẩn tin trong ảnh
- thay thế các bit ít thông tin bằng các bit dữ liệu sau mã hoá
- dù kẻ tấn công có thu được dữ liệu từ ảnh thì dữ liệu cũng đã được mã hoá
bởi aes, chuỗi thông tin đó coi như vô nghĩa

*Phần lập trình:(file steganography)
-Sử dụng tkinter để code giao diện
-sử dụng PIL để thao tác trên ảnh
-Thuật toán steganography sử dụng tính chẵn lẻ (mô tả trong comment code)
-2 chức năng chính : ẩn tin và lấy tin ra khỏi ảnh giấu tin
- file(stegano_being_attacked): mô tả dữ liệu thu được nếu bị phá steganography

