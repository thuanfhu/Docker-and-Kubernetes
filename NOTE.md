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

- **Dangling images** là những images **không có tag hợp lệ** (`<none>`), thường xuất hiện khi:
  - Build một image mới mà không gán tag.
  - Một image cũ bị thay thế trong quá trình build.
- Chúng **không được tham chiếu bởi bất kỳ container nào** nhưng không phải tất cả images không sử dụng đều là dangling images.

✅ **Kiểm tra dangling images:**

```sh
docker images -f dangling=true
```

✅ **Xóa tất cả dangling images:**

```sh
docker image prune
```

📌 **Lưu ý:** `docker image prune` **chỉ xóa dangling images**.

✅ **Xóa tất cả images không sử dụng (bao gồm cả dangling images và images có tag nhưng không container nào tham chiếu):**

```sh
docker image prune -a
```

📌 **Khác biệt giữa `docker image prune` và `docker image prune -a`:**
- `docker image prune` **chỉ xóa dangling images** (images có tag `<none>`).
- `docker image prune -a` **xóa tất cả images không có container nào tham chiếu**, bao gồm cả dangling images và những images có tag nhưng không được sử dụng.
- **Nếu container của image bị stop nhưng chưa bị xóa, `docker image prune -a` vẫn không thể xóa image đó.**

✅ **Xóa container trước khi chạy `docker image prune -a`:**
```sh
docker rm <CONTAINER_ID>
docker image prune -a
```

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

✔️ **Dangling images là những images không có tag hợp lệ (`<none>`) và không được container nào tham chiếu**

✔️ **`docker image prune` chỉ xóa dangling images**

✔️ **`docker image prune -a` xóa tất cả images không có container nào tham chiếu, bao gồm cả dangling images và images có tag nhưng không được sử dụng**

✔️ **Nếu container của image bị stop nhưng chưa bị xóa, `docker image prune -a` vẫn không thể xóa image đó**

✔️ **Dùng `docker container prune` để xóa containers đã dừng**

✔️ **Dùng `docker system prune` để dọn dẹp toàn bộ Docker**

✔️ **Kiểm tra containers và images trước khi xóa để tránh mất dữ liệu**

🚀 **Dọn dẹp Docker đúng cách giúp tiết kiệm tài nguyên và tối ưu hệ thống!**