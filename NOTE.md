# 📝 Introducing Volumes

## 📌 Tổng Quan

**Volumes** là các thư mục trên ổ cứng máy chủ (host machine) được _mount_ (làm sẵn có, ánh xạ) vào container, cho phép lưu trữ dữ liệu vĩnh viễn. Theo tài liệu chính thức của Docker, volumes khác biệt với cách xử lý dữ liệu trong image và cung cấp giải pháp linh hoạt để quản lý dữ liệu.

---

## 🚀 Khái Niệm Volumes

- **Nguồn gốc:** Volumes là thư mục trên máy chủ, ví dụ `/some-path`, được gắn vào một đường dẫn trong container, như `/app/user-data`.
- **Đặc tính:** Dữ liệu trong volume tồn tại ngay cả khi container dừng hoặc khởi động lại, đảm bảo tính liên tục.
- **Mục đích:** Container có thể ghi dữ liệu vào volume và đọc từ nó, giúp lưu trữ thông tin quan trọng như tài khoản người dùng hoặc cơ sở dữ liệu.

---

## 🔍 So Sánh Với COPY Trong Dockerfile

| Đặc Điểm         | Volumes                                   | COPY Trong Dockerfile                |
|------------------|-------------------------------------------|--------------------------------------|
| Thời điểm áp dụng| Dữ liệu được gắn khi container chạy.      | Dữ liệu được sao chép khi build image.|
| Tính linh hoạt   | Dữ liệu thay đổi được, dynamic.           | Dữ liệu cố định, không thay đổi sau build.|
| Vị trí lưu trữ   | Trên host machine (thông qua volume).     | Trong image, read-only.              |
| Mục đích         | Lưu dữ liệu vĩnh viễn, như log hoặc DB.   | Nhúng code, thư viện vào image.      |
| Tính bền vững    | Dữ liệu tồn tại qua nhiều container.      | Mất khi build lại image mới.         |

> **Ví dụ:**  
> Với `COPY`, file cấu hình được nhúng vào image trong giai đoạn build và không thay đổi.  
> Trong khi đó, volume cho phép container ghi dữ liệu mới (như log) vào một thư mục trên host, giữ nguyên khi container dừng.

---

## 🎯 Ưu Điểm Của Volumes

- **Bền vững:** Dữ liệu không mất khi container dừng hoặc khởi động lại.
- **Tách biệt:** Tách dữ liệu khỏi image, giúp quản lý dễ dàng hơn.
- **Chia sẻ:** Có thể dùng chung giữa nhiều container.

---

## ⚠️ Lưu Ý Quan Trọng

❌ **Không thay thế image:** Volumes không lưu code ứng dụng mà chỉ quản lý dữ liệu.

✅ **Phù hợp cho dữ liệu quan trọng:** Sử dụng volumes thay vì lưu dữ liệu trong container tạm thời.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Volumes là thư mục trên host được mount vào container.

✅ Dữ liệu trong volumes tồn tại qua các lần dừng/khởi động container.

✅ Khác COPY: Volumes dynamic, COPY fixed trong image.

✅ Dùng volumes để lưu dữ liệu vĩnh viễn như DB hoặc file quan trọng.

---

## 🚀 Khám phá volumes để quản lý dữ liệu hiệu quả trong Docker!
