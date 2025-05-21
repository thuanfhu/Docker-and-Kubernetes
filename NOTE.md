# 📝 Don't COPY Everything: Using "dockerignore" Files

## 📌 Tổng Quan

`COPY . .` trong Dockerfile sao chép toàn bộ thư mục hiện tại vào image, nhưng không phải lúc nào cũng cần sao chép mọi thứ.

Theo tài liệu chính thức của Docker, file `.dockerignore` giúp loại bỏ các file/thư mục không cần thiết, tối ưu hóa build image.

---

## 🚀 Tại Sao Cần .dockerignore?

**Vấn đề với `COPY . .` :**  

- Sao chép tất cả file/thư mục (bao gồm cả file không cần thiết như `node_modules`, `.git`) vào image.

- Hậu quả: Image phình to, build chậm, có thể chứa dữ liệu nhạy cảm (như `.env`).

**Giải pháp:** Tạo file `.dockerignore` để chỉ định file/thư mục bỏ qua.

**Ví dụ:** Bỏ qua `node_modules` vì Dockerfile thường có `RUN npm install` để cài lại trong image.

**File .dockerignore:**

```
node_modules
.git
.env
```

---

## 🔍 Ví Dụ Cụ thể: Loại Bỏ node_modules

**Không dùng .dockerignore:** `COPY . .` sao chép `node_modules` từ host vào image, nhưng `RUN npm install` cài lại `node_modules`, dẫn đến trùng lặp và tăng kích thước image.

**Dùng .dockerignore:**

- Thêm `node_modules` vào `.dockerignore`, `COPY . .` sẽ bỏ qua thư mục này.

- Kết quả: Image nhỏ hơn, build nhanh hơn, tránh xung đột.

---

## 🔍 So Sánh Với Cách Cũ

| Phương Thức           | Ưu Điểm                        | Nhược Điểm                                 |
|-----------------------|--------------------------------|--------------------------------------------|
| Không dùng .dockerignore | Đơn giản, không cần cấu hình  | Image to, build chậm, có thể chứa file nhạy cảm |
| Dùng .dockerignore    | Image nhẹ, build nhanh, bảo mật tốt | Cần cấu hình file .dockerignore           |

---

## ⚠️ Lưu Ý Quan Trọng

❌ Không bỏ qua file cần thiết: Đảm bảo không loại bỏ file code chính (như `server.js`).

✅ Kiểm tra `.dockerignore`: Dùng trước khi build để tránh lỗi.

✅ Tối ưu hóa: Loại bỏ file lớn hoặc nhạy cảm (như `node_modules`, `.env`).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `COPY . .` sao chép tất cả, dễ gây phình image.

✅ `.dockerignore` loại bỏ file không cần, như `node_modules`.

✅ Lợi ích: Build nhanh, image nhẹ, bảo mật tốt.

✅ Cách dùng: Thêm file/thư mục vào `.dockerignore` trước khi build.

---

### 🚀 Dùng .dockerignore để tối ưu hóa image Docker!
