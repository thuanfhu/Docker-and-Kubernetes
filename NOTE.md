# 📝 Introducing Docker Networks: Elegant Container-to-Container Communication

## 📌 Tổng Quan

🌐 `Docker networks` giải quyết vấn đề giao tiếp container bằng cách cho phép container gọi nhau qua tên thay vì IP. 

> Khác với volumes, network không tự động tạo qua `docker run` mà phải tạo thủ công bằng `docker network create`.

---

## 🚀 Cách Thực Hiện

### 1️⃣ Tạo Network Thủ Công

Tạo user-defined network:

```
docker network create my-network
```

💡 **Lưu ý:** Default bridge network không hỗ trợ DNS resolution, nên cần user-defined network.

---

### 2️⃣ Chạy Container Dịch Vụ (MongoDB)

Chạy container MongoDB trong network:

```
docker run -d --name mongodb --network my-network mongo
```

- `--network my-network`: Gắn container vào network vừa tạo.

- Không cần `-p` cho MongoDB: Vì giao tiếp nội bộ giữa container không yêu cầu cổng ra host.

---

### 3️⃣ Chạy Container Ứng Dụng

Cập nhật mã ứng dụng để gọi MongoDB qua tên container thay vì IP:

```js
mongoose
  .connect('mongodb://mongodb:27017/swfavorites')
  .then(() => {
    app.listen(3000);
  })
  .catch((err) => {
    console.log(err);
  });
```

Chạy container ứng dụng:

```
docker run -d --name my-app --network my-network -p 3000:3000 my-app-image
```

- `--network my-network`: Đảm bảo container my-app cùng network với mongodb.

- Dùng `-p 3000:3000`: Cần nếu muốn truy cập ứng dụng từ host (localhost:3000).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Tạo network: `docker network create my-network`.

✅ Chạy container: Dùng `--network` để gắn container vào network.

✅ Kết nối qua tên: Gọi container bằng tên (ví dụ: `mongodb:27017`).

✅ `-p` cần khi: Truy cập container từ host, không cần cho giao tiếp nội bộ.

---

### 🚀 Docker network giúp container giao tiếp dễ dàng qua tên!