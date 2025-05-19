# 📝 Copying Files Into & From A Container

## 📌 Lệnh `docker cp` Là Gì?

Lệnh `docker cp` dùng để sao chép file hoặc thư mục giữa máy chủ (host) và container hoặc ngược lại, ngay cả khi container đang chạy hoặc đã dừng.

**Cú pháp**

```bash
docker cp [SOURCE_PATH] [DESTINATION_PATH]
```

* `SOURCE_PATH`: Đường dẫn file/thư mục nguồn (trên host hoặc container).

* `DESTINATION_PATH`: Đường dẫn đích (trên container hoặc host).

* Định dạng: `<container-ID>:<path-in-container>` hoặc `<path-on-host>`.

## 🚀 Tại Sao Cần `docker cp`?

✅ Sao chép file vào container: Thêm config, script, hoặc dữ liệu

✅ Trích xuất file từ container: Lấy log, file cấu hình, hoặc kết quả xử lý

✅ Debug hoặc backup: Kiểm tra nội dung hoặc lưu trữ dữ liệu từ container

## 🔍 Cách Sử Dụng `docker cp`

### 1. Sao Chép Từ Host Vào Container

Sao chép file `config.json` từ host vào thư mục `/app` trong container:

```bash
docker cp config.json <container-ID>:/app/config.json
```

* `<container-ID>`: ID của container (xem bằng `docker ps` hoặc `docker ps -a`).
* File sẽ xuất hiện tại `/app/config.json` trong container.

### 2. Sao Chép Từ Container Ra Host

Sao chép file `logs.txt` từ thư mục `/app` trong container ra host:

```bash
docker cp <container-ID>:/app/logs.txt ./logs.txt
```

* File `logs.txt` sẽ được lưu vào thư mục hiện tại trên host.

### 3. Sao Chép Thư Mục

Sao chép toàn bộ thư mục `data` từ host vào container:

```bash
docker cp ./data <container-ID>:/app/data
```

Hoặc từ container ra host:

```bash
docker cp <container-ID>:/app/data ./data
```

## 🎯 Ví Dụ Thực Tế

Giả sử bạn có container `my-node-app` (ID: `abc123`) chạy ứng dụng Node.js.

**Thêm file cấu hình:**

```bash
docker cp server-config.js abc123:/app/server-config.js
```

**Lấy file log:**

```bash
docker cp abc123:/app/app.log ./app.log
```

**Kiểm tra container:**

```bash
docker ps
```

**Kết quả ví dụ:**

```
CONTAINER ID   IMAGE         COMMAND                  CREATED
abc123         my-node-app   "node server.js"         1 hour ago
```

## ⚠️ Lưu Ý Quan Trọng

❌ Container phải tồn tại: Container không cần chạy (`docker ps -a`), nhưng phải được tạo

❌ Đường dẫn chính xác: Đảm bảo đường dẫn trong container tồn tại, nếu không sẽ gặp lỗi

✅ Quyền truy cập: Kiểm tra quyền của user trong container để tránh lỗi permission

✅ Khác với `COPY` trong Dockerfile: `docker cp` hoạt động trên container, còn `COPY` dùng khi build image

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `docker cp` sao chép file/thư mục giữa host và container

✅ Cú pháp: `docker cp [SOURCE] [DESTINATION]`

✅ Hỗ trợ cả container đang chạy và đã dừng

✅ Dùng để thêm file, lấy log, hoặc debug

✅ Đảm bảo container tồn tại và đường dẫn hợp lệ

🚀 Sao chép file dễ dàng để quản lý container hiệu quả!