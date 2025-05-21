# 📝 Working with Environment Variables & ".env" Files

## 📌 Tổng Quan

Biến môi trường (`environment variables`) trong Docker cho phép cấu hình ứng dụng linh hoạt mà không cần hardcode giá trị.  

Theo tài liệu chính thức của Docker, biến môi trường có thể được thiết lập qua Dockerfile, lệnh `docker run`, hoặc file `.env`, giúp quản lý cấu hình dễ dàng.

---

## 🚀 Lợi Ích Của Biến Môi Trường

- 🔄 Linh hoạt: Thay đổi giá trị mà không cần sửa code (ví dụ: port, API key).

- 🔒 Bảo mật: Tránh hardcode thông tin nhạy cảm trong code.

- ♻️ Tái sử dụng: Dùng cùng image trong các môi trường khác nhau (development, production).

**Ví dụ tổng quát trong server.js:**

```js
app.listen(process.env.PORT); // Dùng biến PORT để chạy server
```

---

## 🔍 Cách Thiết Lập Biến Môi Trường

### Trường Hợp 1 Biến

- **Trong Dockerfile:**  

  Sử dụng lệnh ENV để đặt giá trị mặc định.

  ```
  ENV PORT=80
  EXPOSE $PORT
  ```

  Container sẽ chạy server trên cổng 80 (nếu không bị ghi đè).

- **Khi chạy container:**  

  Ghi đè biến bằng `--env` hoặc `-e`.

  ```
  docker run --env PORT=8080 my-image
  # Hoặc ngắn hơn
  docker run -e PORT=8080 my-image
  ```

---

### Trường Hợp Nhiều Biến Với File .env

- **Tạo file .env trong dự án:**

  ```
  PORT=8080
  API_KEY=your-secret-key
  ```

- **Dùng file .env khi chạy container:**

  ```
  docker run --env-file ./.env my-image
  ```

- **Trong Dockerfile có làm được không?** Không, ENV trong Dockerfile không hỗ trợ đọc file `.env` trực tiếp. File `.env` chỉ dùng ở runtime với `--env-file`.

---

## 🔍 So Sánh Các Phương Pháp

| Phương Pháp         | Ưu Điểm                                 | Nhược Điểm                                         | Khi Dùng                        |
|---------------------|------------------------------------------|----------------------------------------------------|----------------------------------|
| ENV trong Dockerfile| Giá trị mặc định rõ ràng, nhúng vào image| Hardcode, không linh hoạt, có thể lộ qua docker history | Giá trị cố định, không nhạy cảm (như cổng mặc định) |
| --env hoặc -e       | Linh hoạt, dễ ghi đè khi chạy            | Phải nhập thủ công, không tiện với nhiều biến       | Thay đổi nhanh 1-2 biến         |
| --env-file .env     | Quản lý nhiều biến dễ dàng, không nhúng vào image | Cần file riêng, phải cẩn thận không commit file .env | Nhiều biến, cần bảo mật (như production) |

---

## 📝 Ghi Chú Bảo Mật

🔐 **Một ghi chú quan trọng về biến môi trường và bảo mật:**  

- Tùy thuộc vào loại dữ liệu bạn lưu trong biến môi trường, bạn có thể không muốn bao gồm dữ liệu nhạy cảm trực tiếp trong Dockerfile.

- Thay vào đó, hãy sử dụng một file biến môi trường riêng chỉ được dùng khi chạy container (ví dụ: với `docker run`).  

- Nếu không, giá trị sẽ bị "nhúng vào image" và mọi người có thể đọc được qua lệnh `docker history <image>`. 

- Với một số giá trị, điều này không quan trọng, nhưng với thông tin đăng nhập, khóa bí mật, v.v., bạn chắc chắn muốn tránh điều đó!  

- Nếu dùng file riêng, giá trị không nằm trong image vì bạn chỉ định file đó khi chạy `docker run`. Nhưng hãy đảm bảo không commit file riêng đó vào kho lưu trữ mã nguồn nếu bạn dùng hệ thống kiểm soát phiên bản.

---

## 🛠️ Best Practices

- Dùng `--env-file .env` cho dữ liệu nhạy cảm hoặc nhiều biến, đặc biệt ở production.

- Không commit file .env vào kho mã nguồn (thêm vào .gitignore).

- Kiểm tra `docker history` để đảm bảo không lộ thông tin.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Biến môi trường linh hoạt, dùng trong server.js (như process.env.PORT).

✅ Thiết lập: ENV trong Dockerfile, --env hoặc --env-file .env khi chạy.

✅ Bảo mật: Dùng file .env cho runtime, không nhúng dữ liệu nhạy cảm vào image.

✅ Best practice: Kết hợp ENV cho mặc định, .env cho production.

---

### 🚀 Biến môi trường giúp cấu hình Docker an toàn và hiệu quả!