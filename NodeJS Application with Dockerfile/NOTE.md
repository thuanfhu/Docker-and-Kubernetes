# 📝 Docker: Image Layers & Caching

## 📌 Image Layers trong Docker

Docker Image không phải là một file đơn lẻ, mà được tạo thành từ **nhiều lớp (layers)**. Mỗi câu lệnh trong `Dockerfile` tạo ra một layer mới.

🛠 **Ví dụ về layers trong Dockerfile:**

```dockerfile
FROM node:18      # Layer 1: Image base
WORKDIR /app      # Layer 2: Thiết lập thư mục làm việc
COPY package*.json ./  # Layer 3: Copy package.json để caching
RUN npm install   # Layer 4: Cài đặt dependencies
COPY . ./         # Layer 5: Copy toàn bộ source code
CMD ["node", "server.js"]  # Layer 6: Lệnh khởi động
```

---

## 🚀 **Cơ chế cache của Dockerfile**

Docker sử dụng **caching thông minh** để tăng tốc quá trình build. Khi một layer không thay đổi, Docker sẽ sử dụng lại cache thay vì build lại.

📌 **Cách cache hoạt động:**

- Nếu Docker thấy một lệnh (`RUN`, `COPY`, ...) **giống hệt** với build trước, nó sẽ **dùng lại layer đã cache**.
- Khi một layer thay đổi, **tất cả các layer sau đó cũng bị build lại**.

---

## ❓ **Tại sao nên COPY package**\*.json và RUN npm install trước?

### ✅ **Cách tối ưu Dockerfile để tận dụng cache:**

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./  # Copy file package.json trước
RUN npm install         # Cài đặt dependencies (chỉ chạy lại nếu package.json thay đổi)
COPY . ./               # Copy toàn bộ source code sau cùng
CMD ["node", "server.js"]
```

### 🔥 **Lợi ích của việc làm này:**

1. **Tận dụng cache tối đa:**
   - Nếu bạn chỉ thay đổi code (không thay đổi `package.json`), Docker sẽ \*\*không chạy lại \*\***`npm install`** → Tiết kiệm thời gian build.
   - Nếu bạn đổi package hoặc thêm thư viện, Docker chỉ build lại từ `RUN npm install` trở đi.
2. **Giảm thời gian build đáng kể**, đặc biệt với dự án lớn.

📌 **Sai lầm thường gặp:** Nếu bạn `COPY . ./` trước `RUN npm install`, Docker sẽ mất cache khi có bất kỳ thay đổi nào trong code, khiến nó phải cài lại toàn bộ dependencies mỗi lần build.

---

## 📌 Kết luận

✅ **Docker Image gồm nhiều layers**, mỗi câu lệnh tạo một layer.

✅ **Docker cache các layers để tối ưu build**, nhưng chỉ khi nội dung không thay đổi.

✅ **COPY package.json trước RUN npm install** giúp giảm thời gian build.

🚀 **Tận dụng cache đúng cách = Build nhanh hơn, tiết kiệm tài nguyên!**