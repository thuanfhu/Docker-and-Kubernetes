# 📝 Docker: Images are Read Only!

## 📌 Images trong Docker là "Read Only"

Docker Images là **bất biến (immutable)**, tức là chúng **không thể bị thay đổi** sau khi đã được tạo. Mọi container được khởi chạy từ image sẽ sử dụng đúng dữ liệu ban đầu của image mà **không bị ảnh hưởng bởi các thay đổi bên ngoài**.

---

## ❓ Tại sao khi thay đổi source code, container mới vẫn dùng code cũ?

Khi bạn build một Docker Image từ `Dockerfile`, nó tạo ra một **bản snapshot cố định** của source code và các dependencies.

🛠 **Ví dụ:**

```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

-   `COPY . .` sao chép mã nguồn vào image.
-   Khi image được build (`docker build -t my-app .`), nó đóng gói source code vào image.
-   Mọi container tạo ra từ image này đều **dùng source code cũ** (tại thời điểm build), ngay cả khi bạn thay đổi mã nguồn gốc trên máy.

📌 **Lý do:** Docker không tự động cập nhật image khi bạn thay đổi source code.

---

## 🔄 Cách cập nhật source code khi chạy container

### ✅ **Cách 1: Build lại image** (Phù hợp với production)

Nếu bạn thay đổi source code, cần build lại image:

```sh
docker build -t my-app .
```

Sau đó, chạy container mới từ image mới:

```sh
docker run -p 3000:3000 my-app
```

### ✅ **Cách 2: Dùng Volume để mount source code** (Phù hợp với development)

Thay vì copy code vào image, bạn có thể **mount thư mục chứa source code vào container**:

```sh
docker run -p 3000:3000 -v $(pwd):/app my-app
```

-   `-v $(pwd):/app` gán thư mục hiện tại (`$(pwd)`) vào thư mục `/app` trong container.
-   Khi bạn sửa code trên máy, container sẽ thấy thay đổi ngay lập tức.

---

## 📌 Kết luận

✅ Docker Images là **bất biến (Read Only)**, source code không thay đổi khi tạo container mới.  
✅ Nếu cần cập nhật code, bạn phải **build lại image** hoặc **dùng Volume để mount source code**.

🚀 **Dùng volume cho development, build lại image cho production!**
