# 📝 Different Ways of Running Commands in Containers

## 🚀 Các Cách Chạy Lệnh Trong Container

Docker cung cấp nhiều cách để chạy lệnh trong container, từ chạy trực tiếp đến ghi đè lệnh mặc định, phù hợp với các nhu cầu khác nhau.

---

### 1. Chạy Container Với Chế Độ Tương Tác

**Cú pháp:**

```bash
docker run -it node
```

**Ý nghĩa:**

- `-i`: Interactive, giữ STDIN mở.

- `-t`: TTY, cung cấp terminal tương tác.

Chạy container `node` và mở shell để nhập lệnh (theo CMD mặc định trong image node là `node`).

---

### 2. Chạy Container Nền Rồi Thực Thi Lệnh

**Bước 1:** Chạy container ở chế độ nền (detached):

```bash
docker run -it -d node
```

- `-d`: Detached, chạy container ở chế độ nền.

- Trả về container ID, ví dụ: `abc123`.

**Bước 2:** Chạy lệnh trong container đang chạy:

```bash
docker exec -it abc123 npm init
```

- `docker exec`: Thực thi lệnh trong container đang chạy.

- Thích hợp khi cần chạy nhiều lệnh trong cùng container.

---

### 3. Ghi Đè Lệnh Mặc Định Khi Chạy Container

**Cú pháp:**

```bash
docker run -it node npm init
```

**Ý nghĩa:**

- Ghi đè CMD mặc định của image node (mặc định là `node`) bằng `npm init`.

- Container chạy `npm init` và thoát ngay sau khi hoàn thành.

**Lưu ý:** Chỉ chạy một lệnh duy nhất, không tái sử dụng container.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Tương tác trực tiếp: `docker run -it node` để mở shell.

✅ Chế độ nền + exec: `docker run -it -d` rồi `docker exec -it <name> npm init` để chạy nhiều lệnh.

✅ Ghi đè lệnh: `docker run -it node npm init` chạy lệnh duy nhất và thoát.

✅ Chọn cách phù hợp: Dùng exec để tái sử dụng container, ghi đè cho tác vụ một lần.

### 🚀 Linh hoạt chạy lệnh trong container với các cách trên!