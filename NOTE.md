# 📝 Creating a Compose File & Diving into the Compose File Configuration

## 📌 Tổng Quan

📝 `Docker Compose` sử dụng file `docker-compose.yaml` để định nghĩa và chạy nhiều container. File YAML yêu cầu thụt lề chính xác để thể hiện phụ thuộc giữa các cấp cấu hình, bao gồm top-level elements như version, name, services, volumes, networks.

---

## 🚀 Cấu Hình File docker-compose.yaml

### 1️⃣ Top-Level Elements: version và name

- **version (Obsolete):** Trước đây dùng để chỉ định phiên bản `Compose Specification`, nhưng theo tài liệu 2025, nó chỉ mang tính thông tin và đã lỗi thời. Compose tự động chọn schema mới nhất để validate file, cảnh báo nếu có trường không nhận diện được.
  
  ```
  version: "3.9"  # Cảnh báo: obsolete
  ```

- **name:** Định nghĩa tên dự án, dùng nếu không override thủ công. Được truy xuất qua biến môi trường `COMPOSE_PROJECT_NAME`.

  ```yaml
  name: myapp
  services:
    foo:
      image: busybox
      command: echo "I'm running ${COMPOSE_PROJECT_NAME}"
  ```

> 📚 Tham khảo thêm tại: https://docs.docker.com/reference/compose-file/version-and-name/

---

### 2️⃣ Cấu Trúc Cơ Bản & Thụt Lề

**Thụt lề:** 2 khoảng trắng mỗi cấp, ví dụ:

  ```yaml
  name: myapp
  services:
    mongodb:  # Cấp 1
      image: mongo  # Cấp 2
  ```

**Cấp phụ thuộc:**

  - `services`: Cấp 1, chứa các container.

  - `mongodb`: Cấp 2, tên service (container).

  - `image`, `environment`: Cấp 3, thuộc tính của service.

---

### 3️⃣ Biến Môi Trường

- **Cách 1: Dùng environment:**

  ```yaml
  services:
    mongodb:
      image: mongo
      environment:
        MONGO_INITDB_ROOT_USERNAME: thuanflu
        MONGO_INITDB_ROOT_PASSWORD: mySecretPassword
  ```

- **Cách 2: Dùng env_file:**

  ```yaml
  services:
    mongodb:
      image: mongo
      env_file:
        - ./env/mongo.env
  ```

  **Giải thích env_file:** Trỏ đến thư mục `env` chứa file `mongo.env` có  

  ```
  MONGO_INITDB_ROOT_USERNAME=thuanflu
  MONGO_INITDB_ROOT_PASSWORD=mySecretPassword
  ```

---

### 4️⃣ Network

- **Mặc định:** Docker Compose tự động tạo một user-defined bridge network cho tất cả services, hỗ trợ DNS resolution.

- **Tùy chỉnh:**

  ```yaml
  services:
    mongodb:
      image: mongo
      networks:
        - my-network
  ```

---

### 5️⃣ Image

**Nguồn image:**

  - `image: mongo`: Image từ Docker Hub.

  - `image: my-custom-app`: Custom image (phải build từ Dockerfile trước).

---

### 6️⃣ Volumes

- **Cú pháp trong services:**

  ```yaml
  services:
    mongodb:
      image: mongo
      volumes:
        - mongo-data:/data/db  # Named Volume
        - /data/temp           # Anonymous Volume
        - ./mongo-data:/data/db  # Bind Mount
  ```

- **Khai báo top-level volumes (chỉ áp dụng cho Named Volume):**

  ```yaml
  volumes:
    mongo-data:
  ```

---

### 7️⃣ Các Tag -p, --rm, -d

- **-p (ports):**
  ```yaml
  services:
    mongodb:
      image: mongo
      ports:
        - "27017:27017"
  ```

- **-d (detached mode):** Dùng lệnh `docker compose up -d`.

- **--rm (auto-remove):** Dùng lệnh `docker compose up --rm`.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ File YAML: Thụt lề 2 khoảng trắng, có version, name, services.

✅ Biến môi trường: environment hoặc env_file.

✅ Network: Mặc định tự tạo, tùy chỉnh nếu cần.

✅ Volumes: Cú pháp - <name>:/path, /path, hoặc ./path:/path.

✅ Cổng: Dùng ports, các tag như --rm, -d qua lệnh.

---

### 🚀 Tạo file Compose chuẩn để quản lý ứng dụng hiệu quả!