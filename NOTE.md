# 📝 Types of Drivers in Docker Networks

## 📌 Tổng Quan

🌐 `Docker Networks` hỗ trợ nhiều loại driver, ảnh hưởng đến cách các container giao tiếp. Driver mặc định là **bridge**, cho phép container tìm nhau qua tên trong cùng mạng. Bạn có thể chọn driver khi tạo mạng bằng tùy chọn `--driver`.

---

## 🚀 Các Loại Driver

### 1️⃣ Bridge (Mặc Định)

- **Mô tả:** Driver mặc định, cho phép container trong cùng mạng tìm nhau qua tên.

- **Tạo mạng:**

  ```
  docker network create --driver bridge my-net
  ```

- Nếu dùng bridge, có thể bỏ `--driver` vì nó là mặc định.

---

### 2️⃣ Các Driver Khác

- **host:** Loại bỏ sự cô lập giữa container và host, dùng chung localhost. Phù hợp cho container độc lập.

- **overlay:** Kết nối nhiều Docker daemon (trên các máy khác nhau), chỉ hoạt động trong Swarm mode (hiện gần như lỗi thời).

- **macvlan:** Gán địa chỉ MAC tùy chỉnh cho container, dùng để giao tiếp qua MAC.

- **none:** Vô hiệu hóa toàn bộ networking.

- **Third-party plugins:** Cài plugin bên thứ ba để thêm tính năng tùy chỉnh.

> 💡 **Lưu ý:** Driver bridge thường phù hợp nhất cho hầu hết các trường hợp.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Bridge: Driver mặc định, hỗ trợ tìm container qua tên.

✅ Các driver khác: host (chung localhost), overlay (Swarm), macvlan (MAC tùy chỉnh), none (tắt mạng), plugins (tùy chỉnh).

✅ Khuyến nghị: Dùng bridge cho đa số tình huống.

---

### 🚀 Chọn driver phù hợp để tối ưu hóa mạng Docker!