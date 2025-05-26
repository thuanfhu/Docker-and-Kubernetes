# 📝 Utilizing ENTRYPOINT

## 🚀 ENTRYPOINT vs CMD Trong Dockerfile

Dockerfile sử dụng `ENTRYPOINT` và `CMD` để định nghĩa cách chạy container, với sự khác biệt trong cách xử lý lệnh.

---

### So Sánh

| Đặc Điểm    | ENTRYPOINT                                 | CMD                                         |
|-------------|--------------------------------------------|---------------------------------------------|
| **Mục đích**    | Định nghĩa lệnh chính không thể ghi đè dễ dàng. | Định nghĩa lệnh mặc định, dễ bị ghi đè.      |
| **Cách sử dụng**| Chạy như lệnh cố định, có thể thêm tham số.     | Chạy như mặc định, bị thay thế khi chạy container. |
| **Ví dụ**       | `ENTRYPOINT ["npm"]` + `init` → Chạy `npm init`. | `CMD ["node"]` + `npm init` → Ghi đè thành `npm init`. |

---

### Ví Dụ Với `npm init`

**Với CMD:**

```dockerfile
FROM node:14-alpine
CMD ["node"]
```

Chạy:

```bash
docker run -it my-image npm init
```

`CMD ["node"]` bị ghi đè, container chạy `npm init` và thoát.

---

**Với ENTRYPOINT:**

```dockerfile
FROM node:14-alpine
ENTRYPOINT ["npm"]
```

Chạy:

```bash
docker run -it my-image init
```

`ENTRYPOINT ["npm"]` giữ lệnh chính, `init` là tham số, chạy `npm init`.

**Thêm lệnh:**

```bash
docker run -it my-image install express --save
```

Chạy `npm install express --save`, tạo file `package.json` với dependency.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ ENTRYPOINT: Lệnh cố định, thêm tham số khi chạy (ví dụ: ENTRYPOINT ["npm"] + init).

✅ CMD: Lệnh mặc định, bị ghi đè (ví dụ: CMD ["node"] + npm init).

✅ Chọn đúng: Dùng ENTRYPOINT cho lệnh chính, CMD cho mặc định dễ thay đổi.

### 🚀 Sử dụng ENTRYPOINT để tối ưu hóa cách chạy container!