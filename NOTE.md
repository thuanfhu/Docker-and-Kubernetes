# 📝 Docker Compose Up & Down

## 📌 Tổng Quan

⚙️ `Docker Compose` cung cấp hai lệnh chính: `docker compose up` để khởi động ứng dụng và `docker compose down` để dừng và dọn dẹp tài nguyên, với các tùy chọn phổ biến giúp quản lý container, volume, network hiệu quả, theo tài liệu chính thức.

---

## 🚀 Lệnh docker compose up

**Chức năng:** Khởi động tất cả services được định nghĩa trong `docker-compose.yaml`, tự động tạo network và volume nếu cần.

**Tùy chọn phổ biến:**

  - **-d (detached):** Chạy container ở chế độ nền, không chiếm terminal. Ví dụ:

    ```
    docker compose up -d
    ```

  - **--build:** Build lại images từ Dockerfile trước khi khởi động, đảm bảo dùng phiên bản mới nhất. Ví dụ:

    ```
    docker compose up --build
    ```

  - **--scale <service>=<num>:** Điều chỉnh số lượng instance của service (phổ biến cho load balancing). Ví dụ:

    ```
    docker compose up --scale web=3
    ```

---

## 🔍 Lệnh docker compose down

**Chức năng mặc định:** Dừng và xóa tất cả container được quản lý bởi file Compose, xóa network do Compose tạo, giữ lại volumes và images.

**Network:** Xóa user-defined network do Compose tự động tạo (ví dụ: my-network), nhưng không ảnh hưởng đến default bridge network.

**Volumes:** Không xóa theo mặc định, nhưng thêm `-v` sẽ xóa toàn bộ volumes được khai báo trong file.

**Tùy chọn phổ biến:**

  - **-v, --volumes:** Xóa tất cả volumes được định nghĩa trong file `docker-compose.yaml` sau khi dừng container. Ví dụ:

    ```
    docker compose down -v
    ```

  - **--rmi <type>:** Xóa images liên quan (phổ biến với local cho custom images). Ví dụ:
  
    ```
    docker compose down --rmi local
    ```

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ up: Khởi động với -d (nền), --build (build lại), --scale (scale service).

✅ down: Xóa container, network (trừ default bridge), giữ volumes (xóa với -v).

✅ Tùy chọn down: -v (xóa volumes), --rmi local (xóa images custom).

---

### 🚀 Quản lý ứng dụng dễ dàng với Compose Up & Down!