# 📝 Module Introduction & What are Utility Containers for Support Tasks?

## 🚀 Utility Containers Là Gì?

`Utility Containers` là các container được thiết kế để chạy các lệnh hỗ trợ hoặc bổ sung, không chứa logic ứng dụng chính mà phục vụ các tác vụ phụ như cài đặt, cấu hình, hoặc debug.

---

### Ví dụ với `npm init`:

Để chạy `npm init`, bạn cần môi trường Node.js. Thay vì cài Node.js trực tiếp trên máy host (có thể gây xung đột môi trường), bạn sử dụng một container có sẵn môi trường Node.js.

**Utility Container:** Dùng image `node` để chạy `npm init` mà không cần cài Node.js trên host.

```bash
docker run -v $(pwd):/app -w /app node npm init
```

**Giải thích:**

- `-v $(pwd):/app`: Ánh xạ thư mục hiện tại vào `/app` trong container.

- `-w /app`: Đặt thư mục làm việc.

- `node`: Image chứa môi trường Node.js.

- `npm init`: Lệnh được thực thi.

---

## So sánh với Application Containers

| Đặc Điểm      | Application Containers                | Utility Containers                        |
|---------------|--------------------------------------|-------------------------------------------|
| **Mục đích**  | Chạy ứng dụng chính (ví dụ: myapp).  | Thực hiện lệnh hỗ trợ (ví dụ: npm init).  |
| **Thực thi**  | Chạy CMD và khởi động ứng dụng.      | Thực thi lệnh tùy chỉnh hoặc bổ sung.     |
| **Ví dụ**     | `docker run myapp` → Chạy ứng dụng.  | `docker run node npm init` → Khởi tạo dự án. |

---

## Tại sao phù hợp với Docker?

`Utility Containers` tận dụng image (như `node`) để cung cấp môi trường cần thiết, đảm bảo tính cách ly và đồng nhất của Docker. Không cần cài Node.js trên host → Tránh xung đột môi trường, giữ hệ thống sạch sẽ.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Utility Containers chạy lệnh hỗ trợ (như `npm init`) trong môi trường cách ly.

✅ Không cần cài đặt trên host: Dùng image (ví dụ: `node`) để đảm bảo tính chuẩn Docker.

✅ Khác Application Containers: Hỗ trợ, không khởi động app chính.

### 🚀 Dùng Utility Containers để xử lý tác vụ hiệu quả và đồng nhất!