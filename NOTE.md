# 📝 Building Images & Understanding Container Names

## 📌 Tổng Quan

🛠️ `Docker Compose` hỗ trợ build image và quản lý container với tên tự động hoặc tùy chỉnh, giúp triển khai ứng dụng hiệu quả.

---

## 🔨 Building Images với `docker compose up --build`

- **Chức năng:** `docker compose up --build` khởi động services và build lại image nếu được khai báo trong file `docker-compose.yaml`.

- **Khi nào dùng:** Khi source code thay đổi (ví dụ: chỉnh sửa file trong thư mục `build: ./backend`), image cần được build lại để phản ánh thay đổi. Nếu không dùng `--build`, Compose sẽ dùng image cũ, không áp dụng thay đổi.

- **Ví dụ:**

  ```yaml
  services:
    backend:
      build: ./backend
  ```

- **Chạy:**

  ```
  docker compose up --build
  ```

  → Build lại image từ thư mục `./backend`, sau đó chạy container.

---

## 🏷️ Quy Ước Tên Container

- **Tự động:** Docker Compose đặt tên container theo mẫu `<project-name>_<service-name>_<index>` (ví dụ: `myapp_backend_1` nếu project là myapp, service là backend).

- **Tùy chỉnh:** Dùng `container_name: <name>` để đặt tên thủ công.

- **Ví dụ:**

  ```yaml
  services:
    backend:
      build: ./backend
      container_name: custom-backend
  ```

  → Container sẽ có tên chính xác là `custom-backend`.

- **Kiểm tra:**

  ```
  docker ps
  ```

---

## ⚠️ Lưu Ý Quan Trọng

❗ `--build` cần thiết khi source code thay đổi, nếu không container sẽ chạy image cũ.

❗ `container_name` phải duy nhất, không trùng với container khác.

❗ Tên tự động tiện cho quản lý mặc định, nhưng `container_name` hữu ích khi cần tên cố định (ví dụ: để gọi trong script).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `docker compose up --build`: Build lại image khi source code thay đổi.

✅ Tên container: Tự động `<project>_<service>_<index>` hoặc tùy chỉnh với `container_name`.

✅ Kiểm tra tên bằng `docker ps`.

---

### 🚀 Build và đặt tên container hiệu quả với Docker Compose!