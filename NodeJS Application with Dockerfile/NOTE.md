# Notes về Các Lệnh Docker

## 1. `docker build .`
Lệnh này dùng để **xây dựng một image từ Dockerfile**.

### **Dấu `.` là gì?**
- Dấu `.` đại diện cho **thư mục hiện tại**, nơi Docker sẽ tìm **Dockerfile** để xây dựng image.
- Nếu muốn chỉ định thư mục khác, có thể thay `.` bằng đường dẫn cụ thể, ví dụ:
  ```sh
  docker build /path/to/directory
  ```
- Nếu muốn đặt tên cho image, dùng `-t`:
  ```sh
  docker build -t my-node-app .
  ```
  Lệnh này tạo ra image có tên `my-node-app`.

---

## 2. `docker run IMAGE_ID`
Lệnh này dùng để **tạo và chạy một container từ image đã có**.

### **Giải thích**
- `IMAGE_ID`: ID của image mà bạn muốn chạy.
- Nếu không biết IMAGE_ID, có thể dùng tên của image:
  ```sh
  docker run my-node-app
  ```
- Khi chạy lệnh này, Docker sẽ tạo ra một container từ image đã có và khởi chạy nó.

---

## 3. `docker stop CONTAINER_ID`
Lệnh này dùng để **dừng một container đang chạy**.

### **Giải thích**
- `CONTAINER_ID`: ID của container mà bạn muốn dừng.
- Nếu không nhớ ID, xem danh sách container đang chạy bằng:
  ```sh
  docker ps
  ```
- Sau đó, dùng:
  ```sh
  docker stop <CONTAINER_ID>
  ```
  để dừng container đó.

---

## 4. `docker run -p 3000:80 IMAGE_ID`
Lệnh này dùng để **chạy container và ánh xạ cổng giữa container và máy chủ**.

### **Giải thích `-p 3000:80`**
- `-p` (publish): Dùng để ánh xạ (mapping) **cổng từ localhost vào container**.
- `3000:80`:
  - **3000** → Cổng trên **máy chủ (localhost)**.
  - **80** → Cổng bên trong **container**.

### **Ví dụ**
- Nếu ứng dụng trong container chạy trên cổng **80**, nhưng bạn muốn truy cập từ `localhost:3000`, bạn dùng `-p 3000:80`.
- Sau đó, bạn có thể mở trình duyệt và truy cập:
  ```
  http://localhost:3000
  ```

---

## **Tóm tắt nhanh**
| Lệnh | Mô tả |
|------|------|
| `docker build .` | Xây dựng image từ Dockerfile trong thư mục hiện tại |
| `docker run IMAGE_ID` | Chạy container từ image đã có |
| `docker stop CONTAINER_ID` | Dừng container đang chạy |
| `docker run -p 3000:80 IMAGE_ID` | Chạy container và ánh xạ cổng 3000 trên máy chủ với cổng 80 trong container |

---