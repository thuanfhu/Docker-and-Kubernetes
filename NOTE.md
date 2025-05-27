# 📝 **Creating a Laravel App via the Composer Utility Container**

---

## 🚀 **Tổng Quan**

Sử dụng container **Composer** trong Docker Compose để tạo ứng dụng Laravel mới, tận dụng môi trường cách ly mà không cần cài Composer trên máy host. Lệnh `docker compose run` sẽ thực thi tác vụ này.

---

## 🔍 **Thực Hiện Tạo Ứng Dụng**

### 🛠️ **1. File `docker-compose.yaml`**

Dịch vụ composer đã được định nghĩa:

```yaml
name: PHP Laravel Dockerized

services:
  composer:
    build:
      context: ./dockerfiles
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html
```

**Giải thích:** Dịch vụ composer ánh xạ `./src` vào `/var/www/html` để lưu mã nguồn Laravel.

---

### 🛠️ **2. File `composer.dockerfile`**

File composer.dockerfile đã có:

```dockerfile
FROM composer:latest
WORKDIR /var/www/html
ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]
```

**Giải thích:** Định nghĩa môi trường Composer với ENTRYPOINT để chạy lệnh composer.

---

### 🚦 **3. Chạy Lệnh Tạo Laravel**

Thực thi lệnh để tạo ứng dụng Laravel:

```bash
docker compose run --rm composer create-project --prefer-dist laravel/laravel .
```

**Giải thích chi tiết:**

- `docker compose run` : Chạy một lần dịch vụ composer từ file docker-compose.yaml.

- `--rm` : Xóa container sau khi hoàn thành, tối ưu tài nguyên.

- `composer` : Tên dịch vụ trong docker-compose.yaml.

- `create-project` : Tạo dự án mới từ gói Composer.

- `--prefer-dist` : Tải bản phân phối (zip) thay vì clone, nhanh hơn.

- `laravel/laravel` : Gói chính thức của Laravel.

- `.` : Lưu mã nguồn vào thư mục hiện tại (.) trên host (qua bind mount `./src`).

**Kết quả:** Thư mục `./src` chứa ứng dụng Laravel hoàn chỉnh.

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **Composer Container:** Dùng để tạo Laravel với `docker compose run`.

✅ **Lệnh:** `docker compose run --rm composer create-project --prefer-dist laravel/laravel .` tạo dự án.

✅ **Bind Mount:** `./src:/var/www/html` đồng bộ mã nguồn từ host.

✅ **--prefer-dist:** Tải bản phân phối nhanh, hiệu quả.

---

### 🚀 **Tạo Laravel App dễ dàng với Composer Container!**