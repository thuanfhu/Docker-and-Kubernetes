# 📝 **Adding a MySQL Container**

---

## 🚀 **Tổng Quan**

Thêm container **MySQL** để cung cấp cơ sở dữ liệu cho ứng dụng Laravel, kết nối với container PHP. Container này được định nghĩa trong `docker-compose.yaml` với các biến môi trường từ file `mysql.env`, đảm bảo cấu hình an toàn và linh hoạt.

---

## 🔍 **Giải Thích File Cấu Hình**

### 1. File `docker-compose.yaml`

Cập nhật file `docker-compose.yaml` với dịch vụ mysql:

```yaml
name: PHP Laravel Dockerized

services:
  nginx:
    image: nginx:stable-alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
  php:
    build:
      context: ./dockerfiles
      dockerfile: php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated
  mysql:
    image: mysql:9.3.0
    env-file:
      - ./env/mysql.env
```

**Giải thích chi tiết:**

- **services.mysql:** Định nghĩa dịch vụ MySQL, sử dụng image `mysql:9.3.0`.

- **image:** Dùng image MySQL chính thức từ Docker Hub, đảm bảo tính ổn định.

- **env-file:** Tải các biến môi trường từ file `mysql.env` (ví dụ: MYSQL_DATABASE, MYSQL_USER, v.v.) để cấu hình MySQL mà không cần hardcode trong file YAML.

---

### 2. File `mysql.env`

Tạo file `mysql.env` với nội dung:

```env
MYSQL_DATABASE=laravel
MYSQL_USER=thuanflu
MYSQL_PASSWORD=secret
MYSQL_ROOT_PASSWORD=secret
```

**Giải thích chi tiết:**

- **MYSQL_DATABASE=laravel:** Tạo cơ sở dữ liệu tên laravel khi container khởi động.

- **MYSQL_USER=thuanflu:** Tạo người dùng MySQL với tên thuanflu.

- **MYSQL_PASSWORD=secret:** Mật khẩu cho người dùng thuanflu.

- **MYSQL_ROOT_PASSWORD=secret:** Mật khẩu cho tài khoản root MySQL.

> Lưu ý: Theo tài liệu Docker, sử dụng file `.env` giúp bảo mật thông tin nhạy cảm, tránh commit vào version control.

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **MySQL Container:** Dùng mysql:9.3.0, cấu hình qua env-file.

✅ **mysql.env:** Định nghĩa MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_ROOT_PASSWORD.

✅ **Kết nối:** PHP container sẽ dùng thông tin này để liên kết với MySQL (cần cấu hình thêm trong Laravel).

✅ **Bảo mật:** Sử dụng file .env để quản lý thông tin nhạy cảm.

---

### 🚀 **Thêm MySQL Container để hoàn thiện cơ sở dữ liệu cho Laravel!**