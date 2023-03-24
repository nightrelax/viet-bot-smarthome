### ĐÂY LÀ HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER CHO PI ZERO WIRLESS, MODUN MIC USB TỪ IMAGE CÓ SẴN

### STEP1. Download bộ Image cho Raspberry Pi đã cài đặt sẵn

Download bộ Image cho Raspberry Pi đã cài đặt sẵn cho tất cả các loại Mic tại Link sau

[GOOGLE DRIVE FILE NÉN 1.4G](https://drive.google.com/file/d/1SZwM6F2k0eiubYJ0VcXg47Me68E9WReX/view?usp=sharing)

### STEP2. Ghi vào thẻ SD

2.1. Dùng Win32IMG để ghi vào thẻ nhớ SD

### STEP3. Khai báo WiFi

3.1. Sử dụng Notepad ++ để tạo file có tên là wpa_supplicant.conf trong thư mục boot của thẻ nhớ

3.2. Set định dạng File
Định dạng file Unix (Edit -> EOL converion -> UNIX/OSX Format là Unix (LF)), nội dung là các tham số tên SSID và mật khẩu tương ứng

3.3. Đặt nội dung
Chú ý, tham số country có thể đổi sang us hoặc vn tùy theo cài đặt tại bộ phát WiFi
```sh
country=vn
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="testing"
    psk="testingPassword"
}
```
3.4. Save lại nội dung File

3.5. Tạo một file rỗng có tên là SSH
có thể tải file SSH mẫu chuẩn ở link này

### STEP4. Kết nối và điều chỉnh

4.1. Kết nối

4.1.1. Cắm thẻ nhớ vào Pi Zero 2 W/Pi 3B+/Pi4 và boot lên

4.1.2. Tìm địa chỉ IP của pi và sử dụng SSH để truy cập từ xa vào Console

4.1.3. Nhập Username và password đăng nhập (pi/vietbot)

4.2. Nâng dung lượng của OS cho Full thẻ

4.2.1. Chạy lệnh sau

```sh
sudo raspi-config
```
4.2.2. Chọn Advance

4.2.3. Chọn Expand File System

4.2.4. Chọn OK và chờ vài s

4.2.5. Chọn Yes để Reboot

### STEP5. Khai báo Mic USB (Mic USB thường và Mic Respeaker USB)

5.1. Thống kê ID của Mic USB và Loa 

Chạy lệnh sau để biết ID của Mic USB
```sh
arecord -l
```
sau đó chạy lệnh sau để biết ID của Loa

```sh
aplay -l
```
Lưu lại thông tin về card_id và device_id ở mỗi kết quả lệnh

Ví dụ card_id là 1, device_id là 0

5.2. Khai báo Default cho ALSA

Chạy lệnh sau 

```sh
sudo nano /usr/share/alsa/alsa.conf
```
Cửa sổ nano hiện lên, tìm tới 2 dòng sau
```sh
# defaults
defaults.ctl.card 0
defaults.pcm.card 0

```
Thay thế ký tự '0' bằng kết quả đã lưu cho <card_id>, ví dụ nếu card_id là 1

```sh
# defaults
defaults.ctl.card 1
defaults.pcm.card 1

```

tiếp tục tìm tới 2 dòng sau
```sh
# defaults
defaults.pcm.device 0
defaults.pcm.subdevice 0

Thay thế ký tự '0' bằng kết quả đã lưu cho <device_id>, ví dụ device_id là 0, thì không phải thay

5.3. Chọn đúng Speaker (Trong trường hợp dùng các dòng Pi có cổng 3.5)

5.3.1. Chạy lệnh

```sh
sudo raspi-config
```

5.3.2. Vào các mục mục System Option, Audio, chọn USB Audio rồi Enter, chọn OK rồi Finish

5.3.3 Chọn Reboot hoặc bỏ qua Reboot, sau đó reboot bằng lệnh:

```sh
sudo reboot
```

5.4. Đưa Account đang dùng (Ví dụ pi) vào group root

Chạy lệnh sau
```sh
sudo usermod -aG root pi
```
5.5. fix lỗi bot không hoạt động sau 1 thời gian.

Chạy lệnh sau
```sh
sudo usermod -aG audio root
```

5.6. Reboot lại Pi
Chạy lệnh sau
```sh
sudo reboot
```
5.7. Test loa và mic sau khi cài

5.7.1. Test loa bằng lệnh sau
```sh
speaker-test -t wav -c 2
```
5.7.2. Test Mic bằng lệnh sau 
Ghi âm
```sh
arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
```
Phát lại
```sh
aplay --format=S16_LE --rate=16000 out.raw
```
5.7.3. Test stream giữa Mic và Loa bằng lệnh sau
```sh
arecord --format=S16_LE --rate=16000 | aplay --format=S16_LE --rate=16000
```