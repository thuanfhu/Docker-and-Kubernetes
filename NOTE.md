# 📝 **Managing & Updating the Container / Image**

## 🚀 Tổng Quan

Quy trình cập nhật ứng dụng Node.js sau khi thêm chức năng mới: build và push image từ host, sau đó cập nhật container trên AWS EC2.

---

## 🔍 Các Bước Quản Lý và Cập Nhật

### **Trên Host Machine (Build & Push Image)**

**Build image mới**

```bash
docker build -t thuanphu1612/nodejs-application:deploy .
```

_Giải thích:_ Tạo image mới từ mã nguồn đã cập nhật, gắn tag `thuanphu1612/nodejs-application:deploy`.

---

**Push image lên Docker Hub**

```bash
docker push thuanphu1612/nodejs-application:deploy
```

_Giải thích:_ Đẩy image mới lên repository trên Docker Hub để triển khai.

---

### **Trên AWS EC2 (Cập Nhật Container)**

**Dừng container cũ**

```bash
sudo docker stop <container cũ>
```

_Giải thích:_ Dừng container đang chạy (thay `<container cũ>` bằng tên hoặc ID container, ví dụ: `nodejs-container`)

---

**Tải image mới**

```bash
sudo docker pull thuanphu1612/nodejs-application:deploy
```

_Giải thích:_ Tải phiên bản mới nhất của image từ Docker Hub.

---

**Chạy container mới**

```bash
sudo docker run --rm -p 80:80 --name nodejs-container -d thuanphu1612/nodejs-application:deploy
```

_Giải thích:_ Khởi động container mới với image vừa tải, ánh xạ cổng 80, tự xóa khi dừng (`--rm`), và chạy ở chế độ nền (`-d`).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Host: Build và push image mới với `docker build` và `docker push`.

✅ EC2: Dừng container cũ, tải image mới (`docker pull`), và chạy container mới.

✅ Tối ưu: Dùng `--rm` để dọn dẹp container sau khi dừng.

---

### 🚀 **Cập nhật ứng dụng Node.js trên EC2 thành công!**