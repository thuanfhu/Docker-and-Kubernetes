# Dockerfile Cơ Bản Cho Node.js

## 1. Dockerfile Tạo Ra Image Hay Container?
Dockerfile **không trực tiếp tạo container**, mà nó được dùng để **tạo image**. Sau đó, từ image này, bạn có thể tạo ra nhiều container.

### **Quy trình:**
1. **Dockerfile → Image**
   - Khi chạy:
     ```sh
     docker build -t my-node-app .
     ```
   - Docker đọc `Dockerfile`, thực thi từng lệnh và tạo ra một **image**.
   
2. **Image → Container**
   - Khi chạy:
     ```sh
     docker run -p 3000:3000 my-node-app
     ```
   - Docker tạo một **container** từ image này và khởi chạy ứng dụng bên trong container.

**Tóm tắt:**
| Thành phần | Vai trò |
|------------|--------|
| **Dockerfile** | Chứa hướng dẫn để tạo image |
| **Image** | Mẫu (template) chứa ứng dụng sẵn sàng chạy |
| **Container** | Một instance đang chạy của image |

---

## 2. `WORKDIR` Là Gì? Nếu Không Có `WORKDIR` Thì Docker Làm Việc Ở Đâu?
- Nếu không có `WORKDIR`, Docker sẽ mặc định làm việc trong **thư mục root (`/`)** của container.
- Khi sử dụng `WORKDIR`, nó giúp tổ chức file gọn gàng và dễ quản lý.

Ví dụ:
```dockerfile
WORKDIR /app
```
- Từ đây, các lệnh tiếp theo sẽ thực hiện trong `/app`.

---

## 3. `COPY . ./` vs `COPY . /app` Là Gì?
### `COPY . ./`
- Nếu **có `WORKDIR /app`**, câu lệnh này sẽ sao chép nội dung thư mục hiện tại vào `/app`.
- Nếu **không có `WORKDIR`**, nó sẽ sao chép vào thư mục root `/`.

### `COPY . /app`
- Luôn sao chép nội dung thư mục hiện tại vào `/app`.
- Không phụ thuộc vào `WORKDIR`.

**Khi nào dùng cái nào?**
| Trường hợp | Nên dùng |
|-----------|---------|
| Có `WORKDIR /app` | `COPY . ./` |
| Không có `WORKDIR` | `COPY . /app` |

---

## 4. `EXPOSE` Là Gì? Có Cần Thiết Không?
`EXPOSE` **không tự mở cổng**, mà chỉ tài liệu hóa rằng container đang sử dụng cổng này.

Ví dụ:
```dockerfile
EXPOSE 3000
```
- Nhưng để truy cập ứng dụng, bạn cần chạy container với `-p`:
  ```sh
  docker run -p 3000:3000 my-node-app
  ```

| Trường hợp | Cần `EXPOSE`? | Cần `-p` khi chạy? |
|-----------|--------------|-------------------|
| Chạy Docker đơn giản | ❌ Không cần | ✅ Bắt buộc |
| Dùng Docker Compose | ✅ Nên có | ✅ Bắt buộc |
| Dùng Kubernetes | ✅ Bắt buộc | ✅ Cấu hình qua service |

---

## 5. `RUN` vs `CMD`
| Lệnh | Khi nào chạy? | Chạy trong giai đoạn nào? | Tác dụng? |
|------|--------------|--------------------|---------|
| **`RUN`** | Khi **build image** (`docker build`) | Chạy **một lần** khi build | Thực thi lệnh và lưu kết quả vào image |
| **`CMD`** | Khi **container khởi động** (`docker run`) | Chạy **mỗi lần container restart** | Xác định lệnh mặc định khi chạy container |

### `RUN` – Chạy Khi Build Image
```dockerfile
RUN npm install
```
- Chỉ chạy **một lần** khi Docker build image.
- Các thư viện được cài đặt sẽ được lưu vào image.

### `CMD` – Chạy Khi Container Khởi Động
```dockerfile
CMD ["node", "server.js"]
```
- Chạy **mỗi lần container khởi động lại**.
- Nếu container bị stop và start lại, `CMD` sẽ chạy lại.

#### ❌ **Sai lầm phổ biến**: Dùng `RUN` để chạy server
```dockerfile
RUN node server.js  # Sai vì chỉ chạy khi build, không chạy khi container khởi động
```
Thay vào đó, phải dùng:
```dockerfile
CMD ["node", "server.js"]  # Đúng!
```

> 📌 **Lưu ý**: Nếu bạn không chỉ định `CMD`, thì `CMD` của **base image** sẽ được thực thi. Nếu không có `CMD` và cũng không có base image, bạn sẽ gặp lỗi.

---

## 6. Dockerfile Đầy Đủ Cho Node.js
```dockerfile
# Chọn image Node.js làm base
FROM node:18

# Đặt thư mục làm việc
WORKDIR /app

# Copy file package.json trước để cài đặt dependencies
COPY package*.json ./
RUN npm install

# Copy toàn bộ mã nguồn
COPY . ./

# Mở cổng container (chỉ tài liệu hóa, không mở cổng thực tế)
EXPOSE 3000

# Chạy ứng dụng khi container khởi động
CMD ["node", "server.js"]
```

---

## 7. Chạy Ứng Dụng Với Docker
1. **Build image:**
   ```sh
   docker build -t my-node-app .
   ```
2. **Chạy container:**
   ```sh
   docker run -p 3000:3000 my-node-app
   ```
3. **Kiểm tra container đang chạy:**
   ```sh
   docker ps
   ```
4. **Dừng container:**
   ```sh
   docker stop <container_id>
   ```

---

## 8. Tóm Tắt Kiến Thức Quan Trọng
✅ **Dockerfile tạo image, container được tạo từ image**  
✅ **`WORKDIR` giúp tổ chức file, nếu không có thì mặc định là `/`**  
✅ **`COPY . ./` phụ thuộc vào `WORKDIR`, `COPY . /app` thì không**  
✅ **`EXPOSE` không tự mở cổng, cần `-p` để kết nối với localhost**  
✅ **`RUN` chỉ chạy khi build image, `CMD` chạy mỗi khi container khởi động**  
✅ **Không dùng `RUN node server.js`, mà phải dùng `CMD ["node", "server.js"]`**  
✅ **Muốn chạy ứng dụng trên localhost, dùng `docker run -p 3000:3000`**  

---