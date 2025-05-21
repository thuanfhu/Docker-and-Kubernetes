# 📝 Introduction to Networking (Cross-)Container Communication

## 📌 Tổng Quan

🌐 Docker networking cho phép container giao tiếp với nhau, với host, hoặc với thế giới bên ngoài (WWW).

---

## 🚀 Các Trường Hợp Giao Tiếp

### 1️⃣ Container to WWW

- **Mô tả:** Container giao tiếp với internet (ví dụ: tải dữ liệu từ API công cộng).

- **Yêu cầu:** Container cần truy cập mạng bên ngoài, thường qua default bridge network.

- **Cấu hình:** Không cần đặc biệt nếu host có internet.

- **Ví dụ:** Container chạy ứng dụng gọi API:  

  `https://api.example.com`

---

### 2️⃣ Container to Local Host Machine

- **Mô tả:** Container giao tiếp với dịch vụ trên host (ví dụ: database, Redis).

- **Dịch vụ thường gặp:** Database (MySQL, PostgreSQL - cổng 3306, 5432), Cache (Redis - cổng 6379), Message Queue (RabbitMQ - cổng 5672).

- **Cách thực hiện:** Dùng `host.docker.internal` (Windows/Mac) hoặc IP host (Linux) để truy cập.

- **Ví dụ:** Container gọi database trên host:  

  `mysql://host.docker.internal:3306`

---

### 3️⃣ Container to Container

- **Mô tả:** Container giao tiếp với nhau (ví dụ: ứng dụng web gọi database).

- **Cách thực hiện:** Dùng user-defined network để hỗ trợ DNS resolution.

- **Ví dụ:**  

  - Tạo network: `docker network create my-net`

  - Chạy container:  

    `docker run --network my-net --name web my-web-app`  
    `docker run --network my-net --name db postgres`

  - Container web gọi db qua tên:  

    `postgres://db:5432`

---

## 🔍 Best Practices: Phân Chia Trách Nhiệm Container

- **Nguyên tắc:** Mỗi container chỉ nên đảm nhiệm một trách nhiệm duy nhất (Single Responsibility Principle).

- **Ví dụ phân chia:** Container cho code (Node.js app), database (PostgreSQL, MySQL), cache (Redis), proxy (Nginx).

- **Lợi ích:** Dễ mở rộng, quản lý, bảo trì và tối ưu hiệu suất (mỗi container chỉ xử lý một tác vụ).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Container to WWW: Giao tiếp trực tiếp qua internet.

✅ Container to Host: Gọi dịch vụ host (MySQL, Redis) qua host.docker.internal.

✅ Container to Container: Dùng user-defined network, giao tiếp qua tên.

✅ Best Practices: Một container một trách nhiệm (code, DB, cache).

---

### 🚀 Hiểu networking để kết nối container hiệu quả!