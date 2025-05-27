# 📝 Fixing Laravel Permission Issues in Docker Setup

---

## 🚀 Tổng Quan

Lỗi `Permission denied` trong Laravel Dockerized xảy ra do quyền truy cập không đồng bộ giữa host và container. Cách fix bao gồm cập nhật 3 file Docker (`composer.dockerfile`, `php.dockerfile`, `nginx.dockerfile`) và file `docker-compose.yaml`, sau đó chạy các lệnh để tạo và chạy ứng dụng Laravel.

---

## 🔍 Phân Tích Cách Fix và File Cấu Hình

### 1. File `composer.dockerfile`

```dockerfile
FROM composer:latest
RUN addgroup -g 1000 laravel && adduser -G laravel -g laravel -s /bin/sh -D laravel
USER laravel
WORKDIR /var/www/html
ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]
```

**Giải thích chi tiết:**

- `FROM composer:latest`: Dùng image chính thức của Composer, cung cấp công cụ quản lý gói PHP.

- `RUN addgroup -g 1000 laravel && adduser ...`: Tạo nhóm laravel (GID 1000) và user laravel (UID 1000), phù hợp với môi trường dev trên Windows, tránh xung đột quyền.

- `USER laravel`: Chuyển sang user laravel để chạy container, đảm bảo quyền phù hợp với bind mount từ host.

- `WORKDIR /var/www/html`: Đặt thư mục làm việc khớp với mã nguồn Laravel.

- `ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]`: Định nghĩa lệnh chính là composer, với `--ignore-platform-reqs` để bỏ qua kiểm tra phiên bản PHP/extension, phù hợp cho môi trường Docker.

> **Fix bug:** Dùng user laravel (UID 1000) để đồng bộ quyền với host, tránh lỗi Permission denied khi Composer ghi file (như vendor).

---

### 2. File `php.dockerfile`

```dockerfile
FROM php:8.4-rc-fpm-alpine
WORKDIR /var/www/html
COPY src .
RUN docker-php-ext-install pdo pdo_mysql
RUN addgroup -g 1000 laravel && adduser -G laravel -g laravel -s /bin/sh -D laravel
USER laravel
# RUN chown -R laravel:laravel .
```

**Giải thích chi tiết:**

- `FROM php:8.4-rc-fpm-alpine`: Dùng image PHP 8.4 với FastCGI Process Manager (FPM), phiên bản Alpine (nhẹ).

- `WORKDIR /var/www/html`: Đặt thư mục làm việc là nơi chứa mã nguồn Laravel.

- `COPY src .`: Sao chép mã nguồn từ thư mục src trên host vào `/var/www/html` trong image, đảm bảo mã nguồn có sẵn.

- `RUN docker-php-ext-install pdo pdo_mysql`: Cài extension PHP pdo và pdo_mysql để hỗ trợ kết nối MySQL.

- `RUN addgroup -g 1000 laravel && adduser ...`: Tạo user laravel (UID 1000) như trên.

- `USER laravel`: Chuyển sang user laravel để chạy container, đồng bộ quyền với host.

- `# RUN chown -R laravel:laravel .`: Dòng này bị comment, nếu bỏ comment sẽ cấp quyền sở hữu toàn bộ `/var/www/html` cho user laravel, nhưng không cần thiết vì bind mount sẽ ghi đè.

> **Fix bug:** Dùng user laravel để chạy PHP-FPM, đảm bảo quyền ghi vào storage (đã được cấp trên host bằng icacls).  
`COPY src .` giúp đồng bộ quyền từ host ngay từ bước build.

---

### 3. File `nginx.dockerfile`

```dockerfile
FROM nginx:stable-alpine
WORKDIR /etc/nginx/conf.d
COPY nginx/nginx.conf .
RUN mv nginx.conf default.conf
WORKDIR /var/www/html
COPY src .
```

**Giải thích chi tiết:**

- `FROM nginx:stable-alpine`: Dùng image Nginx phiên bản stable trên Alpine, nhẹ và tối ưu.

- `WORKDIR /etc/nginx/conf.d`: Đặt thư mục làm việc là nơi chứa file config của Nginx.

- `COPY nginx/nginx.conf .`: Sao chép file nginx.conf từ host vào thư mục `/etc/nginx/conf.d`.

- `RUN mv nginx.conf default.conf`: Đổi tên file thành default.conf để phù hợp với cấu trúc config của Nginx Alpine.

- `WORKDIR /var/www/html`: Chuyển thư mục làm việc sang nơi chứa mã nguồn Laravel.

- `COPY src .`: Sao chép mã nguồn từ host vào image, đảm bảo Nginx có mã nguồn sẵn.

> **Fix bug:** Thay vì dùng `image: nginx:stable-alpine` và mount file config, bạn build image từ `nginx.dockerfile`. Điều này đảm bảo config và mã nguồn được đóng gói vào image, tránh lỗi quyền khi mount trên Windows.

---

### 4. File `docker-compose.yaml`

```yaml
version: '3.8'
services:
  server:
    build:
      context: .
      dockerfile: dockerfiles/nginx.dockerfile
    ports:
      - '8000:80'
    volumes:
      - ./src:/var/www/html
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - php
      - mysql

  php:
    build:
      context: .
      dockerfile: dockerfiles/php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated

  mysql:
    image: mysql:5.7
    env_file:
      - ./env/mysql.env

  composer:
    build:
      context: ./dockerfiles
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html

  artisan:
    build:
      context: .
      dockerfile: dockerfiles/php.dockerfile
    volumes:
      - ./src:/var/www/html
    entrypoint: ['php', '/var/www/html/artisan']

  npm:
    image: node:14
    working_dir: /var/www/html
    entrypoint: ['npm']
    volumes:
      - ./src:/var/www/html
```

**Giải thích chi tiết:**

- `version: '3.8'`: Sử dụng phiên bản 3.8 của Docker Compose (tương thích với Docker Engine).

- `services.server`: Đổi từ `image: nginx:stable-alpine` sang build từ `nginx.dockerfile`.

- `ports: - '8000:80'`: Ánh xạ cổng 8000 trên host với cổng 80 trong container.

- `volumes: - ./src:/var/www/html`: Bind mount mã nguồn từ host để đồng bộ thay đổi.

- `depends_on: - php - mysql`: Đảm bảo php và mysql khởi động trước server.

- `services.php`: Build từ `php.dockerfile`, giữ bind mount với `:delegated` để tối ưu hiệu suất trên Windows.

- `services.mysql`: Dùng `mysql:5.7` (thay vì 9.3.0) để đảm bảo tương thích với Laravel.

- `services.composer`, `artisan`, `npm`: Giữ nguyên cấu hình, dùng bind mount để đồng bộ mã nguồn.

> **Fix bug:** Dùng build thay vì image cho server, đảm bảo quyền và config được đóng gói đúng. Bind mount `./src:/var/www/html` kết hợp với user laravel (UID 1000) để tránh lỗi quyền.

---

## 🔧 Các Lệnh Chạy Sau Khi Cập Nhật

### 1. Tạo Dự Án Laravel

```sh
docker compose run --rm composer create-project --prefer-dist laravel/laravel .
```

**Giải thích chi tiết:**  
- `docker compose run --rm composer`: Chạy dịch vụ composer và xóa container sau khi hoàn thành.

- `create-project --prefer-dist laravel/laravel .`: Tạo dự án Laravel mới, tải bản phân phối (zip) nhanh hơn clone, lưu vào thư mục hiện tại (.) trên host qua bind mount.

---

### 2. Khởi Động Dịch Vụ

```sh
docker compose up -d --build server
```

**Giải thích chi tiết:**  
- `docker compose up -d`: Chạy các dịch vụ ở chế độ nền (detached).

- `--build`: Xây dựng lại image (như nginx.dockerfile), đảm bảo dùng cấu hình mới.

- `server`: Chỉ chạy dịch vụ server, nhưng depends_on đảm bảo php và mysql cũng khởi động.

---

### 3. Chạy Migration

```sh
docker compose run artisan migrate
```

**Giải thích chi tiết:**  
- `docker compose run artisan`: Chạy dịch vụ artisan để thực thi lệnh Laravel CLI.

- `migrate`: Thực thi `php artisan migrate`, tạo bảng trong cơ sở dữ liệu MySQL.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Fix lỗi quyền: Dùng user laravel (UID 1000) trong php.dockerfile và composer.dockerfile, đồng bộ quyền với host.

✅ nginx.dockerfile: Build image với config và mã nguồn, tránh lỗi quyền khi mount.

✅ docker-compose.yaml: Dùng build cho server, giữ bind mount để đồng bộ mã nguồn.

✅ Lệnh chạy: Tạo dự án, khởi động dịch vụ, và chạy migration với docker compose.

---

### 🚀 Fix thành công lỗi quyền và chạy Laravel mượt mà trong Docker!