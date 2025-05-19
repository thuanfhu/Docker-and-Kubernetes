# 📝 Naming & Tagging Containers and Images

## 📌 Naming & Tagging Là Gì?

Trong Docker, **naming** và **tagging** giúc định danh và quản lý image và container một cách rõ ràng:

* **Image**: Được đặt tên (name) và gắn thẻ (tag) để xác định phiên bản hoặc mục đích (ví dụ: `my-app:latest`).

* **Container**: Có thể được đặt tên (name) để dễ nhận diện thay vì dùng ID ngẫu nhiên.

Theo tài liệu chính thức của Docker, tên và tag giúc tổ chức và triển khai image/container hiệu quả.

## 🚀 Naming & Tagging Image

### 1. Đặt Tên và Tag Khi Build Image

Dùng `-t` trong lệnh `docker build` để đặt tên và tag:

```bash
docker build -t my-app:latest .
```

**Cấu trúc**: `<name>:<tag>`

* `name`: Tên image (ví dụ: `my-app`, thường là chữ thường).

* `tag`: Phiên bản hoặc nhãn (ví dụ: `latest`, `v1.0`, `dev`).

*Nếu không chỉ định tag, mặc định là `latest`.*

**Ví dụ:**

```bash
docker build -t my-app:v1.0 .
```

Tạo image với tên `my-app` và tag `v1.0`.

### 2. Gắn Lại Tag (Retag)

Để thêm hoặc thay đổi tag cho image đã có:

```bash
docker tag my-app:v1.0 my-app:stable
```

* Tạo một tag mới (`stable`) cho cùng image.

* *Không sao chép dữ liệu, chỉ tạo tham chiếu mới.*

### 3. Quy Tắc Đặt Tên Image

* Tên image thường gồm: `[repository]/[image]:[tag]` (ví dụ: `docker.io/my-app:v1.0`).

* Nếu không chỉ định repository, mặc định là `docker.io` (Docker Hub).

**Tên hợp lệ:** Chữ thường, số, dấu gạch dưới (\_), dấu gạch ngang (-), dấu chấm (.).

**Tag hợp lệ:** Tối đa 128 ký tự, thường là phiên bản hoặc nhãn mô tả.

## 🔍 Naming Container

### 1. Đặt Tên Khi Chạy Container

Dùng `--name` trong lệnh `docker run` để đặt tên container:

```bash
docker run --name my-container -p 3000:3000 my-app:latest
```

* `my-container`: Tên do bạn chọn, thay vì ID ngẫu nhiên (ví dụ: `abc123`).

* Tên phải **duy nhất**. Nếu trùng, Docker báo lỗi.

### 2. Tự Động Gán Tên

Nếu không dùng `--name`, Docker tự gán tên ngẫu nhiên (kết hợp tính từ và danh từ, ví dụ: `happy_feynman`).

Xem tên container:

```bash
docker ps
```

### 3. Quy Tắc Đặt Tên Container

* **Tên hợp lệ:** Chữ, số, `_`, `-`, `.`

* **Không được trùng** với container đang tồn tại.

* Tên giúc dễ quản lý khi dùng lệnh như `docker stop`, `docker rm`.

## 🎯 Ví Dụ Thực Tế

**Build Image:**

```bash
docker build -t my-node-app:v1.0 .
```

Kết quả: Image `my-node-app:v1.0`.

**Retag Image:**

```bash
docker tag my-node-app:v1.0 my-node-app:prod
```

Kết quả: Image có thêm tag `my-node-app:prod`.

**Chạy Container:**

```bash
docker run --name app-prod -p 3000:3000 my-node-app:prod
```

Kết quả: Container tên `app-prod` chạy từ image `my-node-app:prod`.

**Kiểm Tra:**

```bash
docker images
```

**Kết quả ví dụ:**

```
REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
my-node-app     v1.0      a1b2c3d4e5f6   1 hour ago     900MB
my-node-app     prod      a1b2c3d4e5f6   1 hour ago     900MB
```

```bash
docker ps
```

**Kết quả ví dụ:**

```
CONTAINER ID   NAME        IMAGE              COMMAND
xyz789         app-prod    my-node-app:prod   "node server.js"
```

## ⚠️ Lưu Ý Quan Trọng

❌ Không trùng tên container: Container đang tồn tại phải được xóa (`docker rm`) trước khi tái sử dụng tên

❌ Tag không phải phiên bản duy nhất: Nhiều tag có thể trỏ cùng một image ID

✅ Tag rõ ràng: Dùng tag như `v1.0`, `prod`, `dev` thay vì chỉ `latest` để tránh nhầm lẫn

✅ Kiểm tra trước khi dùng: Dùng `docker images` hoặc `docker ps` để xác minh tên/tag

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Image được đặt tên và tag bằng `-t` trong `docker build` hoặc `docker tag`

✅ Container được đặt tên bằng `--name` trong `docker run`

✅ Tên image/container: Chữ thường, số, `_`, `-`, `.`

✅ Tag giúc phân biệt phiên bản: `v1.0`, `prod`, `dev`

✅ Không trùng tên container, dùng tag rõ ràng để quản lý

🚀 Đặt tên và tag thông minh để quản lý Docker dễ dàng!