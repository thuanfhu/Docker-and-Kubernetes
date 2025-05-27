# 📝 Adding More Utility Containers

## 🚀 Tổng Quan

Thêm các container tiện ích (`Utility Containers`) như **artisan** và **npm** để hỗ trợ phát triển Laravel:  

- **artisan** chạy lệnh Laravel CLI  

- **npm** quản lý gói JavaScript.

---

## 🔍 Giải Thích Dịch Vụ

### File `docker-compose.yaml`

```yaml
name: PHP Laravel Dockerized

services:
  server:
    image: nginx:stable-alpine
    ports:
      - '8080:80'
    volumes:
      - ./src:/var/www/html
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - php
      - mysql

  php:
    build:
      context: ./
      dockerfile: php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated

  mysql:
    image: mysql:9.3.0
    env_file:
      - ./env/mysql.env

  composer:
    build:
      context: ./
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html

  artisan:
    build:
      context: ./
      dockerfile: php.dockerfile
    volumes:
      - ./src:/var/www/html
    entrypoint: ["php", "/var/www/html/artisan"]

  npm:
    image: node:14
    working_dir: /var/www/html
    entrypoint: ["npm"]
    volumes:
      - ./src:/var/www/html
```

---

### Dịch vụ **artisan**:

- `build: context: ./` và `dockerfile: php.dockerfile`: Dùng cùng php.dockerfile với dịch vụ PHP, đảm bảo môi trường PHP phù hợp.

- `volumes: - ./src:/var/www/html`: Bind mount thư mục src để truy cập mã nguồn Laravel.

- `entrypoint: ["php", "/var/www/html/artisan"]`: Chạy lệnh php artisan, công cụ CLI của Laravel, cho phép thực thi các lệnh như migrate, seed, v.v.

---

### Dịch vụ **npm**:

- `image: node:14`: Dùng image Node.js phiên bản 14.

- `working_dir: /var/www/html`: Đặt thư mục làm việc để khớp với mã nguồn Laravel.

- `entrypoint: ["npm"]`: Định nghĩa lệnh chính là npm, dùng để quản lý gói JavaScript (như cài đặt Tailwind CSS).

- `volumes: - ./src:/var/www/html`: Bind mount để đồng bộ thư viện JavaScript (như node_modules) với host.

---

## Chạy Lệnh Migrate Với Artisan

Chạy lệnh để áp dụng migration cho cơ sở dữ liệu Laravel:

```sh
docker compose run artisan migrate
```

**Giải thích:**  
- `docker compose run artisan`: Chạy dịch vụ artisan từ docker-compose.yaml.  

- `migrate`: Tham số cho entrypoint, chạy lệnh `php artisan migrate`, tạo bảng trong cơ sở dữ liệu MySQL.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Artisan Container: Dùng php.dockerfile, chạy php artisan với entrypoint (ví dụ: migrate).

✅ NPM Container: Dùng node:14, quản lý gói JavaScript với entrypoint: ["npm"].

✅ Bind Mount: Cả hai dịch vụ mount ./src:/var/www/html để đồng bộ mã nguồn và thư viện.

✅ Lệnh Migrate: `docker compose run artisan migrate` áp dụng migration cho DB.

---

### 🚀 Thêm Utility Containers để hỗ trợ phát triển Laravel hiệu quả!