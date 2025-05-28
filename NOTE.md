# 📝 Running & Publishing the App (on EC2)

---

## 🚀 Tổng Quan

Hướng dẫn chạy và publish ứng dụng Node.js trên AWS EC2 bằng Docker sau khi truy cập qua SSH.

---

## 🔍 Các Bước Thực Hiện

### Chạy container

```sh
sudo docker run -p 80:80 --rm --name nodejs-container -d thuanphu1612/nodejs-application:deploy
```

**Giải thích:**  
- `sudo`: Chạy với quyền root để đảm bảo đủ quyền.  

- `-p 80:80`: Ánh xạ cổng 80 từ host (EC2) đến cổng 80 trong container.  

- `--rm`: Xóa container khi dừng (tối ưu tài nguyên).  

- `--name nodejs-container`: Đặt tên container.  

- `-d`: Chạy container ở chế độ nền (detached).  

- `thuanphu1612/nodejs-application:deploy`: Image đã đẩy lên Docker Hub.

> Lưu ý: Phải mở cổng 80 (HTTP công khai) trong security group (inbound rules) của EC2 để có thể truy cập ứng dụng qua public DNS hoặc public IP.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Chạy container: Dùng `sudo docker run` với các tùy chọn phù hợp để khởi động ứng dụng.

✅ Cấu hình mạng: Mở cổng 80 trong security group để truy cập public DNS/IP.

---

### 🚀 Chạy và xuất bản ứng dụng Node.js thành công trên EC2!