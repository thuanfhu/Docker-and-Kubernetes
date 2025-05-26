# 📝 Using Docker Compose

## 🚀 Giới Thiệu Docker Compose

`Docker Compose` là công cụ quản lý nhiều container qua file `docker-compose.yaml`, giúp định nghĩa và chạy ứng dụng đa container. Chúng ta sẽ xây dựng một Utility Container để chạy `npm init`.

---

### 1. File Dockerfile

Tạo file `Dockerfile` với nội dung:

```dockerfile
FROM node:14-alpine
WORKDIR /app
ENTRYPOINT ["npm"]
```

**Giải thích:**

- `FROM node:14-alpine`: Dùng image Node.js nhẹ.

- `WORKDIR /app`: Đặt thư mục làm việc.

- `ENTRYPOINT ["npm"]`: Định nghĩa lệnh chính là npm.

---

### 2. File docker-compose.yaml

Tạo file `docker-compose.yaml` với nội dung:

```yaml
name: utility-container
services:
  npm:
    build: ./
    stdin_open: true
    tty: true
    volumes:
      - ./:/app
    entrypoint:
      - npm
```

**Giải thích:**

- `name: utility-container`: Đặt tên dự án.

- `services.npm`: Dịch vụ npm, build từ thư mục hiện tại (`build: ./`).

- `stdin_open: true` và `tty: true`: Bật chế độ tương tác.

- `volumes: - ./:/app`: Ánh xạ thư mục host vào `/app`.

- `entrypoint: - npm`: Định nghĩa lệnh chính (tương thích với Dockerfile).

---

### 3. Chạy Lệnh Với Docker Compose

Chạy container và thực thi `npm init` với cú pháp chuẩn:

```bash
docker compose run --rm npm init
```

**Giải thích:**

- `docker compose run`: Chạy một dịch vụ từ file `docker-compose.yaml`.

- `--rm`: Xóa container sau khi hoàn thành (theo tài liệu Docker, tối ưu hóa tài nguyên).

- `npm`: Tên dịch vụ trong file `docker-compose.yaml`.

- `init`: Tham số cho `ENTRYPOINT ["npm"]`, chạy `npm init`.

**Kết quả:** Tạo file `package.json` trong thư mục host (`./`).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Docker Compose: Quản lý container qua `docker-compose.yaml`.

✅ Dockerfile: Định nghĩa môi trường với `ENTRYPOINT ["npm"]`.

✅ Chạy lệnh: `docker compose run --rm npm init` để thực thi `npm init`.

✅ Volume: Ánh xạ `./:/app` để lưu kết quả.

### 🚀 Sử dụng Docker Compose để quản lý Utility Container hiệu quả!