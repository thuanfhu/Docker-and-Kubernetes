# 📝 Understanding Data Categories / Different Kinds of Data

## 📌 Tổng Quan

Trong Docker, dữ liệu được chia thành **3 loại chính** dựa trên cách lưu trữ và quản lý:

* 📦 **Application (Code + Environment)**

* 🔄 **Temporary App Data**

* 💾 **Permanent App Data**

> 📚 *Tài liệu chính thức của Docker nhấn mạnh cách dữ liệu này tương tác với image và container.*

## 🚀 Các Loại Dữ Liệu

### 1. 📦 Application (Code + Environment)

* **Nguồn:** Được cung cấp bởi developer (bạn) thông qua Dockerfile.
* **Thời điểm thêm:** Được nhúng vào image trong giai đoạn build.
* **Đặc tính:** "Fixed" – không thể thay đổi sau khi image được xây dựng.
* **Quyền truy cập:** Read-only, lưu trữ trong images.

🔧 **Ví dụ:** Code ứng dụng, thư viện, và cấu hình (như `node` và `npm` trong `FROM node:18`).

```Dockerfile
FROM node:18
COPY . /app
RUN npm install
```

---

### 2. 🔄 Temporary App Data

* **Nguồn:** Được tạo/tải trong container đang chạy (ví dụ: input người dùng).
* **Thời điểm lưu:** Lưu trong bộ nhớ hoặc file tạm thời.
* **Đặc tính:** Dynamic và thay đổi, nhưng bị xóa định kỳ hoặc khi container dừng.
* **Quyền truy cập:** Read + write, lưu trữ trong containers.

🔧 **Ví dụ:** Log tạm thời, cache session.

---

### 3. 💾 Permanent App Data

* **Nguồn:** Được tạo/tải trong container đang chạy (ví dụ: tài khoản người dùng).
* **Thời điểm lưu:** Lưu trong file hoặc cơ sở dữ liệu, phải tồn tại khi container dừng/khởi động lại.
* **Đặc tính:** Không được mất khi container dừng/restart.
* **Quyền truy cập:** Read + write, lưu trữ trong containers & volumes.

🔧 **Ví dụ:** Dữ liệu cơ sở dữ liệu, file cấu hình quan trọng.

```bash
docker run -v mydata:/app/data my-app
```

## 🔍 So Sánh Các Loại Dữ Liệu

| 💡 Loại Dữ Liệu    | 🔗 Nguồn               | 📂 Lưu Trữ              | 🔐 Quyền Truy Cập | ⚙️ Đặc Tính              |
| ------------------ | ---------------------- | ----------------------- | ----------------- | ------------------------ |
| Application        | Developer (Dockerfile) | 📦 Images               | 🔒 Read-only      | 🧱 Fixed, không thay đổi |
| Temporary App Data | Container đang chạy    | 🗂️ Containers (bộ nhớ) | ✍️ Read + Write   | ♻️ Dynamic, xóa định kỳ  |
| Permanent App Data | Container đang chạy    | 💾 Volumes + Containers | ✍️ Read + Write   | 🛡️ Dữ liệu không bị mất |

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ **Application:** Code và môi trường, fixed, lưu trong images.

✅ **Temporary App Data:** Dynamic, lưu trong containers, mất khi dừng.

✅ **Permanent App Data:** Quan trọng, lưu trong containers & volumes.

✅ **Dùng volume (`-v`) để lưu dữ liệu vĩnh viễn.**

✅ **Image không thay đổi sau build, cần quản lý dữ liệu riêng biệt.**

🚀 *Hiểu rõ dữ liệu để quản lý container hiệu quả!*
