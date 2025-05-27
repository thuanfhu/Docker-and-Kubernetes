# 📝 **Adding a Composer Utility Container**

---

## 🚀 **Tổng Quan**

Thêm container **Composer** để quản lý các thư viện PHP (như Laravel dependencies) trong dự án. Container này được định nghĩa trong `docker-compose.yaml` và xây dựng từ `composer.dockerfile`, sử dụng bind mount để đồng bộ mã nguồn.

---

## 🔍 **Giải Thích File Cấu Hình**

### 1. File `docker-compose.yaml`

Cập nhật file `docker-compose.yaml` với dịch vụ composer:

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
  composer:
    build:
      context: ./dockerfiles
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html
```

**Giải thích chi tiết:**

- **services.composer:** Dịch vụ Composer, xây dựng từ `composer.dockerfile` trong `./dockerfiles`.

- **build.context:** Thư mục chứa file `composer.dockerfile`.

- **build.dockerfile:** Chỉ định file build.

- **volumes:** Bind mount thư mục `./src` (mã nguồn Laravel) vào `/var/www/html` trong container.

> Lý do bind mount: Cần đồng bộ mã nguồn và thư viện (như vendor) giữa host và container Composer. Vì Composer tải các gói phụ thuộc vào `/var/www/html`, bind mount đảm bảo các thay đổi (như composer install) được phản ánh trực tiếp trên host, phục vụ cho container PHP.

---

### 2. File `composer.dockerfile`

Tạo file `composer.dockerfile` với nội dung:

```dockerfile
FROM composer:latest
WORKDIR /var/www/html
ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]
```

**Giải thích chi tiết:**

- **FROM composer:latest:** Dùng image chính thức của Composer, chứa công cụ quản lý gói PHP.

- **WORKDIR /var/www/html:** Đặt thư mục làm việc là nơi mã nguồn Laravel được mount.

- **ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]:** ENTRYPOINT định nghĩa lệnh chính là composer, chạy khi container khởi động. `--ignore-platform-reqs` bỏ qua các yêu cầu về phiên bản PHP/extension trên host/container, cho phép cài đặt gói ngay cả khi môi trường không khớp.

> Tại sao cần `--ignore-platform-reqs`? Trong môi trường phát triển, host có thể không có PHP hoặc phiên bản không khớp với container. Tùy chọn này đảm bảo Composer hoạt động, nhưng cần kiểm tra tương thích khi triển khai sản phẩm.

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **Composer Container:** Xây từ composer:latest, dùng để quản lý gói PHP.

✅ **Bind Mount:** Ánh xạ ./src:/var/www/html để đồng bộ mã nguồn và thư viện.

✅ **ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]:** Chạy composer với tùy chọn bỏ qua yêu cầu môi trường, đảm bảo cài đặt linh hoạt.

✅ **Mục đích:** Hỗ trợ cài đặt dependencies (như composer install) cho Laravel.

---

### 🚀 **Thêm Composer Container để quản lý thư viện dễ dàng!**