# 📝 Using Build Arguments (ARG)

## 📌 Tổng Quan

ARG trong Docker cho phép truyền tham số khi build image, giúp tùy chỉnh image mà không cần sửa Dockerfile. Theo tài liệu chính thức của Docker, ARG chỉ tồn tại trong quá trình build, không ảnh hưởng runtime.

---

## 🚀 Dockerfile Hiện Tại

```dockerfile
FROM node:24
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
ARG DEFAULT_PORT=80
ENV PORT=$DEFAULT_PORT
EXPOSE $PORT
CMD ["npm", "start"]
```

Giải thích: `ARG DEFAULT_PORT=80` đặt giá trị mặc định cho port, được gán vào biến môi trường PORT qua ENV.

---

## 🔍 Build Image Với 2 Port Khác Nhau

- **Build với port mặc định (80):**

  ```
  docker build -t my-app:default .
  ```

  Image dùng DEFAULT_PORT=80.

- **Build với port khác (8080):**

  ```
  docker build -t my-app:8080 --build-arg DEFAULT_PORT=8080 .
  ```

  Ghi đè DEFAULT_PORT thành 8080, container mở cổng 8080.

---

## 🔍 Tình Huống Phổ Biến Sử Dụng ARG

Dự án lớn:

- Tùy chỉnh phiên bản dependency (như ARG NODE_VERSION=18 để chọn Node.js).

- Đặt cấu hình build-time (port, proxy, môi trường build).

- Ví dụ: Build image khác nhau cho `dev/test/prod` mà không cần nhiều `Dockerfile`.

**Cách sử dụng:**

- Định nghĩa `ARG` trong `Dockerfile`.

- Truyền giá trị khi build với `--build-arg`.

---

## 🔍 ARG Là Gì Và Tác Dụng?

- **Định nghĩa:** ARG là tham số build-time, chỉ tồn tại trong quá trình build image.

- **Tác dụng:**

  - Tùy chỉnh image mà không sửa Dockerfile.

  - Truyền giá trị động (version, port) khi build.

---

## 🔍 Đặt ARG Ở Đâu Tốt Nhất?

- **Vị trí tối ưu:** Đặt ARG ngay sau FROM hoặc trước bước cần dùng (như ENV, EXPOSE).

- **Lý do:** ARG chỉ có hiệu lực từ lúc khai báo đến cuối build, đặt sớm để dùng ở nhiều bước.

- Trong Dockerfile trên: `ARG DEFAULT_PORT=80` đặt trước ENV và EXPOSE là hợp lý.

> ⚠️ **Lưu ý:** ARG không dùng cho runtime (dùng ENV để truyền vào runtime). Tránh dùng ARG cho dữ liệu nhạy cảm (có thể lộ qua docker history).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ ARG là tham số build-time, tùy chỉnh image linh hoạt.

✅ Ví dụ: Build với --build-arg DEFAULT_PORT=8080.

✅ Dùng khi: Cấu hình build-time (version, port) trong dự án lớn.

✅ Đặt ARG: Sau FROM, trước bước sử dụng.

---

### 🚀 Dùng ARG để build image hiệu quả và linh hoạt!