# 📝 **Launching Only Specific Docker Compose Services**

---

## 🚀 **Tổng Quan**

Sau khi khởi tạo ứng dụng Laravel bằng container `Composer` (sử dụng `docker compose run --rm composer create-project --prefer-dist laravel/laravel .`), chúng ta sẽ tiếp tục chạy các dịch vụ cần thiết khác (**Nginx**, **PHP**, **MySQL**).

---

## 🔍 **Cập Nhật File Cấu Hình**

### 🛠️ **1. File `docker-compose.yaml`**

Cập nhật file `docker-compose.yaml` với dịch vụ server (Nginx):

```yaml
name: PHP Laravel Dockerized

services:
  server:
    image: nginx:stable-alpine
    ports:
      - "8080:80"
    volumes:
      - ./src:/var/www/html           # Bind mount src từ host
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro  # Cập nhật đường dẫn config
    depends_on:
      - php
      - mysql
  php:
    build:
      context: ./dockerfiles
      dockerfile: php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated
  mysql:
    image: mysql:9.3.0
    env_file:
      - ./env/mysql.env
  composer:
    build:
      context: ./dockerfiles
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html
```

**Giải thích chi tiết:**

- Đổi tên dịch vụ: Từ **nginx** thành **server** cho rõ vai trò web server.

- **Bind mount** `./src:/var/www/html`: Nginx cần mã nguồn Laravel trong `/var/www/html` để phục vụ. Bind mount từ `./src` (thư mục host chứa mã nguồn) đảm bảo Nginx truy cập mã nguồn và file public của Laravel.

- **Cập nhật volume config:** Thay `/etc/nginx/nginx.conf` bằng `/etc/nginx/conf.d/default.conf` để phù hợp với cấu trúc Nginx Alpine, mount file config chỉ đọc (`:ro`).

- **depends_on:** Đảm bảo **server** phụ thuộc vào **php** và **mysql**, các dịch vụ này khởi động trước để Nginx hoạt động ổn định.

---

### 📝 **2. Cập Nhật File `src/.env`**

Cập nhật file `.env` trong thư mục `src` (tạo bởi Composer):

```env
DB_CONNECTION=mysql
DB_HOST=mysql        # mysql container (define in docker-compose file)
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=thuanflu
DB_PASSWORD=secret
```

**Giải thích chi tiết:**

- Thay `DB_CONNECTION=sqlite` bằng `mysql` để dùng MySQL.

- `DB_HOST=mysql`: Trỏ đến dịch vụ mysql trong docker-compose.yaml, tận dụng DNS của Docker network.

- Cập nhật thông tin từ `mysql.env` (`DB_USERNAME`, `DB_PASSWORD`) để khớp với container MySQL.

---

### 🚦 **3. Chạy Dịch Vụ Cụ Thể**

Thay vì `docker compose up -d server php mysql`, chỉ chạy dịch vụ server:

```bash
docker compose up -d --build server
```

**Giải thích chi tiết:**

- `docker compose up -d`: Khởi động dịch vụ ở chế độ nền (detached).

- `--build`: Xây dựng lại image nếu có thay đổi trong Dockerfile (nếu không có thay đổi, Docker sử dụng cache để tối ưu thời gian).

- `server`: Chỉ chạy dịch vụ server, nhưng `depends_on` đảm bảo php và mysql cũng khởi động trước.

- **Tác dụng của depends_on:** Đảm bảo thứ tự khởi động, tránh lỗi kết nối từ server đến php hoặc mysql khi chúng chưa sẵn sàng.

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **Chạy dịch vụ cụ thể:** Dùng `docker compose up -d --build server` với depends_on.

✅ **Bind mount:** `./src:/var/www/html` cung cấp mã nguồn cho Nginx.

✅ **Cập nhật .env:** Đặt `DB_HOST=mysql` để kết nối với MySQL container.

✅ **--build:** Xây lại image nếu cần, dùng cache nếu không thay đổi.

---

### 🚀 **Khởi động dịch vụ cần thiết một cách hiệu quả với Docker Compose!**