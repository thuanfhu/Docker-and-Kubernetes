# 🗑️ Docker: Deleting Images & Containers

## 🔹 1. Điều kiện để xóa Container và Image

Trước khi xóa Container hoặc Image, cần hiểu một số điều kiện quan trọng:

### 🛑 Không thể xóa Container đang chạy

- Nếu container đang chạy, bạn **không thể xóa** nó ngay lập tức.
- Cần **dừng container trước** khi xóa.

✅ **Dừng và xóa container:**

```sh
docker stop <CONTAINER_ID>
docker rm <CONTAINER_ID>
```

✅ **Xóa container đang chạy bằng cách ép buộc:**

```sh
docker rm -f <CONTAINER_ID>
```

### 🛑 Không thể xóa Image đang được container sử dụng

- Nếu một Image đang có container chạy hoặc đã được tạo từ nó, **không thể xóa Image** trừ khi container đó bị xóa trước.

✅ **Kiểm tra container nào đang sử dụng Image:**

```sh
docker ps -a --filter ancestor=<IMAGE_ID>
```

✅ **Xóa container trước khi xóa Image:**

```sh
docker rm <CONTAINER_ID>
docker rmi <IMAGE_ID>
```

### 🛑 Dangling Images là gì?

- **Dangling images** là những images không có tag và không được tham chiếu bởi bất kỳ container nào.
- Chúng thường xuất hiện sau khi build image mới mà không gán tag.

✅ **Kiểm tra dangling images:**

```sh
docker images -f dangling=true
```

✅ **Xóa tất cả dangling images:**

```sh
docker image prune
```

📌 **Lưu ý:** Dangling images không có container nào sử dụng nên có thể xóa an toàn.

---

## 🔹 2. Xóa Containers

### 🗑️ Xóa một container cụ thể

```sh
docker rm <CONTAINER_ID>
```

### 🗑️ Xóa nhiều containers cùng lúc

```sh
docker rm <CONTAINER_ID_1> <CONTAINER_ID_2> <CONTAINER_ID_3>
```

### 🚀 Xóa tất cả containers đã dừng

```sh
docker container prune
```

- **Lệnh này sẽ xóa tất cả containers đã bị dừng**.
- **Cần xác nhận trước khi xóa** (có thể bỏ qua bằng `-f`).

```sh
docker container prune -f
```

📌 **Lưu ý:** Containers đang chạy sẽ **không bị xóa** khi sử dụng `docker container prune`.

---

## 🔹 3. Xóa Images

### 🗑️ Xóa một image cụ thể

```sh
docker rmi <IMAGE_ID>
```

### 🗑️ Xóa nhiều images cùng lúc

```sh
docker rmi <IMAGE_ID_1> <IMAGE_ID_2> <IMAGE_ID_3>
```

### 🚀 Xóa tất cả images không sử dụng

```sh
docker image prune
```

- **Chỉ xóa images không có container nào đang sử dụng.**

Nếu muốn xóa **tất cả images không sử dụng và dangling images**, chạy:

```sh
docker image prune -a
```

📌 **Lưu ý:** Nếu một image đang được container sử dụng, bạn **không thể xóa nó** trừ khi xóa container trước.

✅ **Xóa container trước khi xóa image:**

```sh
docker rm <CONTAINER_ID>
docker rmi <IMAGE_ID>
```

---

## 🔹 4. Kiểm tra danh sách Containers và Images

### 📋 Danh sách tất cả containers

```sh
docker ps -a
```

### 📋 Danh sách tất cả images

```sh
docker images
```

### 📋 Kiểm tra containers đã dừng

```sh
docker ps -f status=exited
```

---

## 🔹 5. Xóa tất cả Containers và Images cùng lúc

🚀 **Xóa tất cả containers và images không sử dụng**:

```sh
docker system prune
```

🚀 **Xóa tất cả containers và images bao gồm cả những cái đang bị dangling**:

```sh
docker system prune -a
```

📌 **Lưu ý:**

- `docker system prune` **không xóa containers đang chạy**.
- `docker system prune -a` **xóa tất cả images không dùng đến**.

---

## 🔹 6. Tóm lược

✔️ **Không thể xóa container đang chạy, cần stop trước**

✔️ **Không thể xóa Image nếu có container sử dụng nó**

✔️ **Dangling images là những images không có tag và không được tham chiếu bởi container nào**

✔️ **Dùng `docker container prune` để xóa containers đã dừng**

✔️ **Dùng `docker image prune` để xóa images không sử dụng**

✔️ **Dùng `docker system prune` để dọn dẹp toàn bộ Docker**

✔️ **Kiểm tra containers và images trước khi xóa để tránh mất dữ liệu**

🚀 **Dọn dẹp Docker đúng cách giúp tiết kiệm tài nguyên và tối ưu hệ thống!**