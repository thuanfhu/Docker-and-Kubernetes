# 📝 Managing Docker Volumes

## 📌 Tổng Quan

`Docker Volumes` là cách lưu trữ dữ liệu bền vững ngoài container, giúp quản lý file dễ dàng. Theo tài liệu chính thức của Docker, bạn có thể tạo, liệt kê, kiểm tra, xóa, và dọn dẹp volume bằng các lệnh cụ thể.

---

## 🚀 Các Lệnh Quản Lý Volume

### 📋 Liệt kê volume (`docker volume ls`)

- Hiển thị tất cả volume hiện có.

- Ví dụ:

  ```
  docker volume ls
  ```

- Kết quả: Danh sách volume với cột DRIVER và VOLUME NAME.

---

### ➕ Tạo volume (thủ công hoặc tự động)

- **Thủ công:**  

  Tạo volume trước với:

  ```
  docker volume create my-volume
  ```

- **Tự động:**  

  Khi chạy container với `-v`, Docker tự tạo volume nếu chưa tồn tại:

  ```
  docker run -v my-volume:/app/data my-image
  ```

---

### 🔎 Kiểm tra chi tiết (`docker volume inspect`)

- Xem thông tin chi tiết của volume, như đường dẫn lưu trữ:

  ```
  docker volume inspect my-volume
  ```

- Kết quả: Hiển thị JSON với thông tin như "Mountpoint" (thường là `/var/lib/docker/volumes/my-volume/_data` trên Linux).

---

### 🗑️ Xóa volume (`docker volume rm`)

- Xóa volume cụ thể:

  ```
  docker volume rm my-volume
  ```

- Lỗi: Nếu volume đang được container sử dụng, sẽ báo lỗi "volume is in use". Dừng hoặc xóa container trước (sử dụng `docker rm` với force `-f` nếu cần).

---

### 🧹 Dọn dẹp volume (`docker volume prune`)

- Xóa tất cả volume không được sử dụng:

  ```
  docker volume prune
  ```
  
- ⚠️ Cảnh báo: Xác nhận trước, vì lệnh này xóa vĩnh viễn volume không liên kết container.

---

## ⚠️ Lưu Ý Quan Trọng

❌ Không xóa volume đang dùng: Dừng container trước khi `docker volume rm`.

✅ Quản lý cẩn thận: Dùng `docker volume ls` và `inspect` để theo dõi.

✅ Dọn dẹp định kỳ: `docker volume prune` giúp tiết kiệm dung lượng.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Liệt kê: `docker volume ls`

✅ Tạo: `docker volume create` hoặc `-v` khi chạy

✅ Kiểm tra: `docker volume inspect`

✅ Xóa: `docker volume rm`, chú ý container sử dụng

✅ Dọn dẹp: `docker volume prune` cho volume thừa

---

### 🚀 Quản lý volume hiệu quả để tối ưu hóa Docker!
