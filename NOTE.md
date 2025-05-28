# 📝 Installing Docker on a Virtual Machine

## 🚀 Tổng Quan

Hướng dẫn cài đặt Docker trên một máy ảo AWS EC2 với Amazon Linux, đảm bảo môi trường sẵn sàng để chạy container.

---

## 🔍 Các Bước Cài Đặt

### Cập nhật hệ thống

```sh
sudo yum update -y
```

`Giải thích`: Cập nhật tất cả các gói trên Amazon Linux để đảm bảo hệ thống chạy phiên bản mới nhất, sử dụng `-y` để tự động xác nhận.

---

### Cài đặt Docker

```sh
sudo amazon-linux-extras install docker
```

`Giải thích`: Sử dụng lệnh AWS-specific `amazon-linux-extras` để cài Docker, được tối ưu cho Amazon Linux.  

> Lưu ý: Đây là cách cài đặt đặc trưng cho EC2, nhưng nếu dùng nhà cung cấp khác, bạn nên tham khảo hướng dẫn chính thức trên Docker Docs (phần "Server").

---

### Khởi động Docker

```sh
sudo service docker start
```

`Giải thích`: Khởi động dịch vụ Docker với sudo để chạy dưới quyền root, đảm bảo đầy đủ quyền hạn. Sau lệnh này, bạn có thể bắt đầu sử dụng các lệnh Docker như `docker run`.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Cập nhật: `sudo yum update -y` đảm bảo hệ thống mới nhất.

✅ Cài Docker: `sudo amazon-linux-extras install docker` cho AWS EC2, hoặc dùng Docker Docs cho nhà cung cấp khác.

✅ Khởi động: `sudo service docker start` kích hoạt Docker để sẵn sàng.

---

### 🚀 Cài đặt Docker thành công trên AWS EC2 để bắt đầu container hóa!