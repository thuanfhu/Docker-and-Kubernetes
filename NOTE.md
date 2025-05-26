# 📝 Building a First Utility Container

## 🚀 Tạo Utility Container

`Utility Containers` dùng để chạy các lệnh hỗ trợ (như `npm init`) trong môi trường cách ly. Chúng ta sẽ xây dựng một `Utility Container` dựa trên image `node:14-alpine`.

---

### 1. Tạo Dockerfile

Tạo file `Dockerfile` với nội dung:

```dockerfile
FROM node:14-alpine
WORKDIR /app
```

**Giải thích:**

- `FROM node:14-alpine`: Dùng image nhẹ của Node.js phiên bản 14.

- `WORKDIR /app`: Đặt thư mục làm việc mặc định là `/app`.

---

### 2. Build Image

Build image với tên `node-utils`:

```bash
docker build -t node-utils .
```

---

### 3. Chạy Utility Container

Chạy container để thực thi `npm init`, ánh xạ thư mục host vào container:

```bash
docker run -it -v $(pwd):/app node-utils npm init
```

**Giải thích:**

- `-it`: Chạy tương tác với terminal.

- `-v $(pwd):/app`: Ánh xạ thư mục hiện tại trên host vào `/app` trong container.

- `node-utils`: Image vừa build.

- `npm init`: Lệnh ghi đè CMD mặc định, khởi tạo dự án Node.js.

**Kết quả:** File `package.json` được tạo trong thư mục host.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Utility Container: Dùng image như `node:14-alpine` để chạy lệnh hỗ trợ.

✅ Dockerfile: Thiết lập môi trường với `FROM` và `WORKDIR`.

✅ Volume với `-v`: Ánh xạ thư mục host để lưu kết quả (như `package.json`).

✅ Lệnh `npm init`: Ghi đè CMD mặc định để thực thi tác vụ.

### 🚀 Tạo Utility Container để chạy lệnh cách ly và hiệu quả!