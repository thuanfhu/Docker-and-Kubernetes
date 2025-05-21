# 📝 A Look at Read-Only Volumes

## 📌 Tổng Quan

`Read-only volumes` trong Docker là các thư mục được gắn vào container với quyền chỉ đọc (read-only), giúp bảo vệ dữ liệu không bị container thay đổi.

---

## 🚀 Lệnh Và Cách Hoạt Động

**Lệnh Cụ Thể:**

```
docker run -d -p 3000:80 --rm --name my-container -v feedback:/app/feedback -v path-to-host:/app:ro -v /app/node_modules -v /app/temp nodejs-app:volumes
```

**Ý nghĩa:**

- `-v path-to-host:/app:ro`: Ánh xạ thư mục từ host vào `/app` trong container, nhưng chỉ cho phép đọc.

- `-v feedback:/app/feedback`: Tạo Named Volume để lưu file feedback, cho phép đọc và ghi.

- `-v /app/node_modules` và `-v /app/temp`: Tạo Anonymous Volumes để bảo vệ node_modules và lưu file tạm, cho phép đọc và ghi.

---

## ❓ Tại Sao Dùng `:ro`?

- `:ro` (read-only) được thêm vào Bind Mount `/app` để bảo vệ code (như `server.js`, `feedback.html`) trên host. Container chỉ được đọc, không được ghi vào `/app`.

- Ví dụ từ source code: `server.js` cần đọc `feedback.html` từ `/app/pages` để hiển thị form, nhưng không cần ghi vào `/app`. Dùng `:ro` đảm bảo container không vô tình tạo hoặc sửa file trong `/app`.

---

## 🔍 Quyền Đọc/Ghi Của Các Thư Mục

| 📁 Thư Mục         | Loại Volume        | Quyền      | Mục Đích                                               |
|--------------------|-------------------|------------|--------------------------------------------------------|
| `/app`             | Bind Mount (`:ro`) | Chỉ đọc    | Chứa code (như `server.js`), container chỉ đọc từ host |
| `/app/feedback`    | Named Volume      | Đọc + ghi  | Lưu file feedback (ví dụ: `title.txt`), container ghi được |
| `/app/temp`        | Anonymous Volume  | Đọc + ghi  | Lưu file tạm (ví dụ: `temp-title.txt`), container ghi được |
| `/app/node_modules`| Anonymous Volume  | Đọc + ghi  | Bảo vệ thư viện từ image, container không ghi (theo code) |

Container mặc định: Có thể đọc và ghi vào mọi thư mục trong layer của nó, trừ khi bị giới hạn bởi `:ro` hoặc quyền hệ thống.

Ví dụ: Nếu bạn gửi feedback qua `feedback.html`, `server.js` sẽ ghi file vào `/app/feedback` (Named Volume) và `/app/temp` (Anonymous Volume), nhưng không thể ghi vào `/app` vì `/app` là read-only.

---

## 🔄 Đồng Bộ Giữa Host Và Container

### 🔸 Thay Đổi Từ Host

- Sửa file trên host: Nếu bạn sửa `server.js` trong `path-to-host`, thay đổi sẽ tự động cập nhật trong `/app` của container mà không cần build lại image.

- Ví dụ: Thêm `console.log("Hello")` vào `server.js` trên host, container sẽ chạy code mới ngay lập tức.

### 🔸 Thay Đổi Từ Container

- Ghi vào `/app`: Không được, vì `/app` là read-only (`:ro`). Container sẽ báo lỗi nếu thử.

- Ghi vào `/app/feedback` hoặc `/app/temp`: Được, dữ liệu lưu vào volume (Named hoặc Anonymous), không ảnh hưởng đến host.

- Ví dụ: Gửi feedback qua form, `server.js` tạo file `title.txt` trong `/app/feedback`. File này lưu trong volume feedback, không đồng bộ với host.

### 🔸 Đồng Bộ Là Gì?

- **Host → Container:** Bind Mount (`/app`) cho phép container đọc code từ host, nên sửa host sẽ tự động cập nhật trong container.

- **Container → Host:** Không, vì `/app` là read-only. Dữ liệu ghi vào volume (như `/app/feedback`) chỉ lưu trong volume, không ảnh hưởng host.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `:ro` tạo read-only volume, bảo vệ `/app` khỏi bị ghi.

✅ Quyền: `/app` chỉ đọc, `/app/feedback` và `/app/temp` đọc + ghi.

✅ Đồng bộ: Sửa host → container (qua Bind Mount), container → volume (không host).

✅ Lợi ích: Bảo vệ code, quản lý dữ liệu động an toàn.

---

### 🚀 Read-only volumes giúp kiểm soát dữ liệu trong Docker dễ dàng!
