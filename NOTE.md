# 📝 **Introducing Multi-Stage Builds**

## 🚀 Tổng Quan

`Multi-stage builds` cho phép xây dựng image Docker hiệu quả bằng cách sử dụng nhiều stage (giai đoạn) trong một `Dockerfile`, mỗi stage có thể phục vụ mục đích khác nhau.

---

## 🔍 Chi Tiết Về Multi-Stage Builds

- **Chức năng:** Tối ưu hóa image bằng cách loại bỏ các file và dependency không cần thiết từ quá trình xây dựng, tạo image nhỏ gọn và an toàn hơn.

- **Tình huống sử dụng:** Phù hợp khi cần biên dịch mã nguồn (như Node.js hoặc Go) rồi chỉ giữ runtime, hoặc tách build và runtime environment (như Node.js với Nginx).

- **Tại sao cần:** Giảm kích thước image, cải thiện bảo mật (loại bỏ công cụ build), và đơn giản hóa quy trình CI/CD.

- **Lệnh RUN:** Thực thi các lệnh trong container tại thời điểm build, như cài đặt gói hoặc biên dịch mã, nhưng chỉ áp dụng trong stage hiện tại.

- **Cú pháp Multi-Stage:**

  - **Bắt đầu bằng FROM:** Mỗi stage mới bắt đầu với `FROM <image>`, định nghĩa base image (ví dụ: `FROM node:18`).

  - **Đặt tên stage với AS:** Gán tên cho stage (ví dụ: `AS builder`) để tham chiếu sau này.

  - **Sử dụng COPY --from:** Sao chép artifact từ stage cũ sang stage mới (ví dụ: `COPY --from=builder /app /app`), đảm bảo chỉ lấy nội dung cần thiết.

**Tổng quát syntax:**

```dockerfile
# Stage 1: Build
FROM <base-image> AS <stage-name>
RUN <build-commands>
COPY <source> <destination>

# Stage 2: Runtime
FROM <runtime-image>
COPY --from=<stage-name> <source> <destination>
CMD ["<command>"]
```

---

## 🎯 Ví Dụ Cụ Thể: Node.js với Nginx

```dockerfile
# Stage 1: Build Node.js application
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Giải thích chi tiết:**

- **Stage 1 (builder):** Dùng node:18 để cài đặt dependency (`npm install`) và build ứng dụng (`npm run build`). Kết quả lưu ở `/app/build`.

- **Stage 2 (Nginx):** Dùng nginx:alpine làm runtime, sao chép thư mục build từ stage builder (`COPY --from=builder /app/build /usr/share/nginx/html`) để phục vụ static files.

- **Lợi ích:** Image cuối chỉ chứa Nginx và file build, loại bỏ Node.js và công cụ build, giảm kích thước và rủi ro bảo mật.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Mục đích: Tối ưu hóa image, loại bỏ dependency không cần thiết.

✅ Ứng dụng: Biên dịch mã và tách runtime, như Node.js với Nginx.

✅ Cú pháp: Sử dụng FROM, AS, và COPY --from để quản lý stage.

✅ Ví dụ: Build Node.js rồi serve bằng Nginx, giữ image nhỏ gọn.

---

### 🚀 **Sử dụng multi-stage builds để xây dựng image hiệu quả và an toàn!**