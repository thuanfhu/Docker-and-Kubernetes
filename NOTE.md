# 📝 Working with Multiple Containers

## 📌 Tổng Quan

🧩 `Docker Compose` quản lý nhiều container qua file `docker-compose.yaml`, hỗ trợ kết nối network, tùy chỉnh build, ports, volumes, và phụ thuộc giữa services.

---

## 🔗 Tên Container và Kết Nối Network

- Docker Compose tự động tạo tên container theo mẫu `<project-name>_<service-name>_<index>` (ví dụ: `multi-container-app_mongodb_1`), kiểm tra bằng `docker ps`.

- Trong network mặc định (user-defined bridge), các service gọi nhau bằng tên khai báo trong file (như `mongodb`, `backend`), nhờ tính năng DNS resolution.

---

## ⚙️ Cấu Hình build

- **Cách 1 (ngắn gọn):** `build: <path>` – dùng khi không cần đổi tên file Dockerfile hoặc thêm args.

  ```
  build: ./backend
  ```

- **Cách 2 (chi tiết):** Khi cần đổi tên Dockerfile hoặc thêm build-time variables.

  ```yaml
  build:
    context: ./backend  # Thư mục chứa Dockerfile
    dockerfile: CustomDockerfile  # Tên file tùy chỉnh
    args:  # Biến build-time
      build_arg: value
  ```

- **Mục đích:** Build custom image từ thư mục hoặc file Dockerfile.

---

## 🌐 Cấu Hình ports

- **Cú pháp:** `- '<host-port>:<container-port>'` (ví dụ: `- '80:80'`).

- **Chi tiết:** Ánh xạ cổng host sang container, hỗ trợ cả TCP/UDP.

- **Ví dụ:** `- '80:80/tcp'` hoặc `- '8080:80/udp'`.

---

## 💾 Cấu Hình volumes

- **Cú pháp:** `- <source>:<destination>`

- **Named Volume:** `- data:/data/db`

- **Anonymous Volume:** `- /data/temp`

- **Bind Mount:** `- ./host-path:/container-path`

- **Mục đích:** Lưu dữ liệu vĩnh viễn hoặc ánh xạ thư mục host.

---

## 🔗 Cấu Hình depends_on

- **Cú pháp:** `- <service-name>` (ví dụ: `- mongodb`)

- **Chi tiết:** Đảm bảo service được khởi động trước, nhưng không chờ sẵn sàng (cần healthcheck nếu cần).

- **Ví dụ:** `- backend` đảm bảo backend chạy trước frontend.

---

## 🖥️ Cấu Hình stdin_open và tty

- `stdin_open: true`: Giữ stdin mở, tương đương `-i` trong docker run, cho phép nhập liệu.

- `tty: true`: Tạo terminal (TTY), tương đương `-t`, hỗ trợ giao diện tương tác.

- **Kết hợp:** Thay thế `--it` trong docker run, dùng cho debugging hoặc chạy shell.

---

## 📄 File docker-compose.yaml Đầy Đủ

```yaml
name: multi-container-app
services:
  mongodb:
    image: mongo
    volumes:
      - data:/data/db
    env_file:
      - ./env/mongo.env
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
      args:
        build_arg: value
    ports:
      - '80:80'
    volumes:
      - node-logs:/app/logs
      - /app/node_modules
      - ./backend:/app
    env_file:
      - ./env/backend.env
    depends_on:
      - mongodb
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - '3000:3000'
    volumes:
      - ./frontend/src:/app/src
    stdin_open: true
    tty: true
    depends_on:
      - backend
volumes:
  data:
  node-logs:
```

---

## ⚠️ Lưu Ý Quan Trọng

❗ Tên container tự động sinh, dùng tên service trong network.

❗ build cần context và dockerfile chính xác nếu dùng cú pháp chi tiết.

❗ depends_on không đảm bảo service sẵn sàng, kết hợp healthcheck nếu cần.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Tên container tự sinh, gọi qua tên service trong network.

✅ build: `<path>` hoặc `context, dockerfile, args`.

✅ ports: `<host>:<container>`.

✅ volumes: `<source>:<dest>`.

✅ depends_on: `- <service>`.

✅ stdin_open + tty: Thay `--it`.

---

### 🚀 Quản lý nhiều container hiệu quả với Compose!