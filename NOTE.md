# 📝 A Look at Read-Only Volumes

## 📌 Tổng Quan

Read-only volumes trong Docker là cách gắn các thư mục hoặc volume vào container với quyền chỉ đọc (read-only), giúp bảo vệ dữ liệu khỏi bị thay đổi.

---

## 🚀 Lệnh Và Cách Hoạt Động

**Lệnh hiện tại:**

```
docker run -d -p 3000:80 --rm --name my-container -v feedback:/app/feedback -v path-to-host:/app:ro -v /app/node_modules -v /app/temp nodejs-app:volumes
```

**Ý nghĩa:**

- `-v path-to-host:/app:ro`: Gắn thư mục từ máy chủ (host) vào `/app` trong container, chỉ cho phép đọc.

- `-v feedback:/app/feedback`: Tạo volume tên feedback để lưu file feedback, cho phép đọc và ghi.

- `-v /app/node_modules` và `-v /app/temp`: Tạo volume ẩn danh để bảo vệ thư viện và lưu file tạm, cho phép đọc và ghi.

---

## ❓ Tại sao dùng `:ro`?

`:ro` bảo vệ code (như `server.js`, `feedback.html`) từ `path-to-host`, đảm bảo container chỉ đọc, không ghi. 

Trong `server.js`, container đọc `feedback.html` để hiển thị form, nhưng không sửa file, nên `:ro` rất phù hợp.

---

## 🔍 Quyền Truy Cập và Đồng Bộ Dữ Liệu

### 📂 Quyền Đọc/Ghi Của Từng Thư Mục

| Thư mục              | Loại Volume         | Quyền truy cập      | Ghi chú                                                                 |
|----------------------|--------------------|---------------------|-------------------------------------------------------------------------|
| `/app`               | Bind Mount (`:ro`) | Chỉ đọc             | Chứa code từ host, không thể ghi. Nếu ghi sẽ báo lỗi "read-only file system". |
| `/app/feedback`      | Named Volume       | Đọc và ghi          | Lưu file feedback (vd: `title.txt`), không liên quan đến host.          |
| `/app/temp`          | Anonymous Volume   | Đọc và ghi          | Lưu file tạm (vd: `temp-title.txt`), không liên quan đến host.          |
| `/app/node_modules`  | Anonymous Volume   | Đọc và ghi*         | Chứa thư viện từ image, bảo vệ khỏi Bind Mount ghi đè. Code hiện tại không ghi vào đây. |

> 📝 **Lưu ý:** Container mặc định có thể đọc và ghi vào mọi thư mục trong layer của nó, trừ khi bị giới hạn bởi `:ro` hoặc quyền hệ thống.

---

## 🔄 Dữ Liệu Di Chuyển Như Thế Nào?

### 🖥️ Từ máy chủ (host) đến container

- Sửa file trong `path-to-host` (như thêm `console.log("Hello")` vào `server.js`) sẽ tự động cập nhật trong `/app` của container nhờ Bind Mount.

- Ví dụ: Sửa `feedback.html` trên host, truy cập http://localhost:3000, bạn sẽ thấy giao diện mới ngay lập tức, không cần build lại image.

### 📦 Từ container đến máy chủ (host)

- Container không thể ghi ngược lên `path-to-host`, vì `/app` là read-only (`:ro`).

- Ví dụ: Nếu `server.js` cố tạo file mới trong `/app`, sẽ báo lỗi.

### 🔁 Thay đổi trong container và ảnh hưởng đến volume/host

- **/app/feedback:** Khi gửi feedback, `server.js` tạo file `title.txt` trong `/app/feedback`. File này lưu trong volume feedback, host không thấy, nhưng volume cập nhật và giữ file ngay cả khi container dừng.

- **/app/temp:** `server.js` tạo file tạm `temp-title.txt`, sau đó xóa. File này lưu trong volume ẩn danh, host không thấy, nhưng volume cập nhật cho đến khi container bị xóa.

- **/app/node_modules:** Code hiện tại không ghi vào đây. Nếu có thay đổi (như cài thư viện mới), volume ẩn danh sẽ lưu, host không thấy.

> 💡 **Tóm lại:** Thay đổi trong container chỉ lưu vào volume, không ảnh hưởng host.

---

## 📝 Tóm Lại Quyền và Đồng Bộ

- **Quyền:** `/app` chỉ đọc, `/app/feedback` và `/app/temp` đọc + ghi.

- **Đồng bộ:** Sửa host → container (qua Bind Mount), container → volume (không host).

- **Ví dụ:** Sửa code trên host, container cập nhật ngay. Gửi feedback, file lưu trong volume, host không thấy.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `:ro` tạo read-only volume, bảo vệ `/app` khỏi bị ghi.

✅ Quyền: `/app` chỉ đọc, `/app/feedback` và `/app/temp` đọc + ghi.

✅ Đồng bộ: Sửa host → container (qua Bind Mount), container → volume (không host).

✅ Lợi ích: Bảo vệ code, quản lý dữ liệu động an toàn.

---

### 🚀 Read-only volumes giúp kiểm soát dữ liệu trong Docker dễ dàng!
