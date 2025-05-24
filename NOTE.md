# 📝 Docker Compose: What & Why?

## 📌 Tổng Quan

🛠️ `Docker Compose` là công cụ chính thức của Docker để định nghĩa và chạy nhiều container như một ứng dụng qua file YAML (thường là `docker-compose.yml`). Nó quản lý services, ports, environment variables, volumes, và networks, nhưng có những giới hạn nhất định.

---

## 🚀 Docker Compose Là Gì & Tại Sao Dùng?

### 1️⃣ Định Nghĩa Ứng Dụng Nhiều Container

**Chức năng:** Định nghĩa services (containers), published ports, environment variables, volumes, và networks trong một file.

**Ví dụ file docker-compose.yml:**

  ```yaml
  version: "3.9"
  services:
    web:
      image: nginx
      ports:
        - "8080:80"
      environment:
        - ENV_VAR=value
      volumes:
        - my-volume:/app
      networks:
        - my-network
  volumes:
    my-volume:
  networks:
    my-network:
  ```

**Cấu trúc:**

  - **Services (Containers):** Định nghĩa container (ví dụ: web, db).

  - **Published Ports:** Ánh xạ cổng (ví dụ: 8080:80).

  - **Environment Variables:** Cấu hình biến môi trường.

  - **Volumes:** Lưu trữ dữ liệu vĩnh viễn.

  - **Networks:** Kết nối giữa services.

---

### 2️⃣ Lý Do Sử Dùng

- **Tiện lợi:** Khởi động, dừng toàn bộ ứng dụng bằng một lệnh: `docker compose up`.

- **Hiệu quả:** Quản lý phụ thuộc (như app và database) và cấu hình mạng/volume dễ dàng.

- **Tái sử dụng:** File YAML có thể triển khai trên nhiều môi trường.

---

## ⚠️ Lưu Ý Quan Trọng

❌ Không thay thế Dockerfile: Vẫn cần Dockerfile để xây custom images.

❌ Không thay thế images/containers: Chỉ quản lý, không tạo mới images/containers.

❌ Không phù hợp đa host: Không thiết kế để quản lý nhiều container trên các máy chủ khác nhau (sử dụng Kubernetes cho trường hợp này).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Docker Compose: Quản lý services, ports, env, volumes, networks qua file YAML.

✅ Tại sao dùng: Khởi động dễ, quản lý phụ thuộc, tái sử dụng.

✅ Lưu ý: Không thay thế Dockerfile, images/containers, hoặc multi-host.

✅ Lưu ý: Dùng đúng phiên bản, kiểm tra depends_on, phù hợp dev/test.

---

### 🚀 Dễ dàng triển khai ứng dụng với Docker Compose!