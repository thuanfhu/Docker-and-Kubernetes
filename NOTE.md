# 📝 Pushing our local Image to the Cloud

---

## 🚀 Tổng Quan

Có hai cách để triển khai ứng dụng lên AWS EC2: `push mã nguồn trực tiếp` hoặc `push image đã xây dựng`. Nên chọn phương pháp xây dựng image cục bộ (Option 2) và push lên Docker Hub để triển khai.

---

## 🔍 Bảng So Sánh Hai Phương Pháp Triển Khai

| Phương Pháp 1: Triển Khai Mã Nguồn                | Phương Pháp 2: Triển Khai Image Đã Xây Dựng         |
|---------------------------------------------------|-----------------------------------------------------|
| 🛠️ Xây dựng image trên máy chủ từ xa              | 🏗️ Xây dựng image trước khi triển khai (ví dụ: trên máy cục bộ) |
| 📤 Đẩy mã nguồn lên máy chủ từ xa, chạy docker build rồi docker run | 🚀 Chỉ cần thực thi docker run                      |
| 🤔 Độ phức tạp không cần thiết                     | ✅ Tránh công việc không cần thiết trên máy chủ từ xa |

---

## 🔧 Các Bước Triển Khai Với Option 2

### Xây dựng image cục bộ

```sh
docker build -t thuanphu1612/nodejs-application:deploy .
```

`Giải thích`:  

- Tạo image với tên `thuanphu1612/nodejs-application:deploy` từ Dockerfile trong thư mục hiện tại (`.`).  
Tên này khớp với repository trên Docker Hub, nên không cần dùng `docker tag`.  

- Nếu đổi tên (ví dụ: `thuanphu1612/new-name:deploy`), image ID vẫn giữ nguyên, chỉ tên thay đổi (xem bảng dưới).

---

| Tên Image                          | Image ID   | Ghi Chú                        |
|-------------------------------------|------------|--------------------------------|
| thuanphu1612/old-name:deploy        | abc123...  | Image gốc                      |
| thuanphu1612/new-name:deploy        | abc123...  | Cùng ID, chỉ đổi tên bằng tag  |

---

### Đẩy image lên Docker Hub

```sh
docker push thuanphu1612/nodejs-application:deploy
```

`Giải thích`: Tải image lên repository `thuanphu1612/nodejs-application` trên Docker Hub với tag `deploy`.

---

### Xác thực nếu cần

```sh
docker login
```

`Giải thích`: Nếu gặp lỗi xác thực, chạy `docker login`, nhập username và password Docker Hub để cấp quyền đẩy image.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Phương pháp: Chọn Option 2 để xây dựng image cục bộ, đẩy lên Docker Hub.

✅ Lệnh: `docker build -t ...`, `docker push`, và `docker login` nếu cần.

✅ Image ID: Giữ nguyên khi đổi tên bằng `docker tag`, chỉ tên thay đổi.

---

### 🚀 Đẩy image thành công lên cloud và triển khai dễ dàng trên AWS EC2!