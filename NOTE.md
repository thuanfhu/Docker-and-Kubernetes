# 📝 How Docker Resolves IP Addresses?

## 📌 Tổng Quan

🌐 Docker quản lý IP addresses trong container thông qua mạng nội bộ (networking).  

> Docker không thay đổi source code của ứng dụng mà chỉ kiểm soát môi trường chạy, bao gồm việc gán và phân giải IP.

---

## 🚀 Cách Docker Phân Giải IP Addresses

### 1️⃣ Gán IP Tự Động

- Docker tự động gán IP cho container khi chạy trong một network (ví dụ: bridge hoặc user-defined).

- **Kiểm tra IP:**
  ```
  docker container inspect <container-name>
  ```

- **Kết quả:** Tìm IPAddress trong NetworkSettings, ví dụ: `172.17.0.2`.

---

### 2️⃣ Phân Giải Tên Sang IP

- Trong user-defined network, Docker sử dụng DNS resolution để ánh xạ tên container sang IP.

- Ví dụ: Container web gọi db qua tên, Docker tự động phân giải `db` thành IP tương ứng.

---

### 3️⃣ Không Thay Đổi Source Code

- Docker chỉ kiểm soát môi trường (network, runtime) và không sửa đổi source code của ứng dụng.

- Ứng dụng (như app.js) dùng IP hoặc tên container mà Docker cung cấp.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Gán IP: Docker tự động gán IP cho container trong network.

✅ DNS Resolution: User-defined network phân giải tên thành IP.

✅ Không thay đổi code: Docker chỉ quản lý môi trường, không chỉnh sửa source code.

---

### 🚀 Hiểu cách Docker quản lý IP để tối ưu kết nối container!