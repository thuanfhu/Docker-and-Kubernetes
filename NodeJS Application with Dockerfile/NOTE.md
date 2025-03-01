# 📝 Docker: Quản lý Container - Stop, Start, Attach & Logs

## 🚀 1. `docker stop` vs `docker start`

### 🔹 `docker stop CONTAINER_ID`
Lệnh này **dừng container** đang chạy một cách an toàn bằng cách gửi tín hiệu `SIGTERM` đến tiến trình chính trong container.

📌 **Cách hoạt động:**
- Container nhận tín hiệu `SIGTERM`, có thời gian để tắt an toàn.
- Nếu container không dừng sau thời gian mặc định (~10 giây), Docker gửi `SIGKILL` để buộc dừng ngay lập tức.

📌 **Ví dụ:**
```sh
docker stop my-container  # Dừng container có tên "my-container"
```

---

### 🔹 `docker start CONTAINER_ID`
Lệnh này **khởi động lại một container đã bị dừng** mà không tạo mới.

📌 **Điểm khác biệt quan trọng:**
- `docker start` **không bị chặn terminal** như `docker run`, vì nó mặc định chạy container ở **Detached Mode**.
- Khi dùng `docker start`, container chạy nền mà không hiện log trực tiếp.

📌 **Ví dụ:**
```sh
docker start my-container  # Khởi động container đã dừng trước đó
```

---

## 🎭 2. Attached vs Detached Mode

### 🔹 **Attached Mode (`docker run` mặc định)**
- Khi chạy container với `docker run`, terminal **bị chặn (blocking)** và hiển thị toàn bộ output/log từ container.
- Nếu bạn nhấn `Ctrl + C`, container sẽ bị dừng.

📌 **Ví dụ:**
```sh
docker run nginx  # Chạy container nginx ở chế độ Attached
```

### 🔹 **Detached Mode (`docker run -d`)**
- Container chạy **ngầm (background)** mà không hiển thị log trong terminal.
- Terminal **không bị chặn**, bạn có thể tiếp tục gõ lệnh khác.

📌 **Ví dụ:**
```sh
docker run -d --name my-nginx nginx  # Chạy nginx ở chế độ Detached
```

### 🔹 **Mặc định của `docker start`**
- `docker start` luôn chạy container ở **Detached Mode**.
- Nếu muốn xem log trực tiếp sau khi start, bạn cần dùng thêm `docker logs -f` hoặc `docker attach`.

📌 **Ví dụ:**
```sh
docker start my-container  # Chạy container ở Detached Mode
```

### 🔹 **Chuyển từ Attached Mode sang Detached Mode**
Để thoát khỏi chế độ **Attached Mode** mà không dừng container, nhấn tổ hợp phím:
- `Ctrl + P` rồi `Ctrl + Q`

📌 **Ví dụ:**
```sh
docker run --name my-app nginx  # Chạy nginx ở Attached Mode
# Nhấn Ctrl + P rồi Ctrl + Q để chuyển sang Detached Mode
```

---

## 📜 3. Xem logs của container

### 🔹 `docker logs CONTAINER_ID`
Hiển thị toàn bộ logs của container (stdout và stderr).

📌 **Ví dụ:**
```sh
docker logs my-container  # Xem log của container
```

### 🔹 `docker logs -f CONTAINER_ID` (Follow logs)
- Xem log **trực tiếp theo thời gian thực**, tương tự `tail -f` trong Linux.
- Dùng `Ctrl + C` để thoát khỏi chế độ xem log trực tiếp.

📌 **Ví dụ:**
```sh
docker logs -f my-container  # Theo dõi log của container đang chạy
```

---

## 🔗 4. `docker attach` - Kết nối lại container đang chạy
Lệnh `docker attach` giúp **kết nối terminal với container đang chạy ở Detached Mode**.

📌 **Điểm quan trọng:**
- Khi `docker attach`, terminal sẽ bị chặn và hiển thị toàn bộ output của container.
- Nếu bạn nhấn `Ctrl + C`, container sẽ bị dừng (trừ khi nó có handler `SIGINT`).
- Nếu chỉ muốn xem log mà không bị chặn terminal, nên dùng `docker logs -f`.

📌 **Ví dụ:**
```sh
docker attach my-container  # Kết nối lại container đang chạy
```

🚀 **Tóm lại:**
- `docker stop` dừng container an toàn.
- `docker start` khởi động lại container ở **Detached Mode**.
- `docker run` mặc định là **Attached Mode**, nhưng có thể chạy ở **Detached Mode** với `-d`.
- `docker logs` xem log container, `-f` để theo dõi trực tiếp.
- `docker attach` kết nối lại container đang chạy, nhưng có thể khiến container dừng nếu không cẩn thận.
- **Chuyển từ Attached Mode sang Detached Mode** bằng `Ctrl + P`, `Ctrl + Q`.

👉 **Dùng `docker logs -f` để xem log mà không ảnh hưởng đến container!**