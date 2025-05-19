# 📝 Working with Docker Hub: Pushing, Pulling, and Sharing Images

## 📌 Tổng Quan

Docker Hub là kho lưu trữ image mặc định cho Docker, cho phép *push* (đẩy), *pull* (tải), và chia sẻ image. Các lệnh như `docker login`, `docker logout`, `docker push`, `docker pull` giúc quản lý image trên Docker Hub.

## 🚀 Các Lệnh Chính

### 1. `docker login`

🔓 Đăng nhập vào Docker Hub để xác thực trước khi push/pull image từ repository cá nhân.

```bash
docker login
```

* Nhập username và password khi được yêu cầu.
* Lưu thông tin đăng nhập tại `~/.docker/config.json` (mặc định).

### 2. `docker logout`

🔑 Đăng xuất khỏi Docker Hub.

```bash
docker logout
```

* Xóa thông tin xác thực khỏi `~/.docker/config.json`.

### 3. `docker pull`

📥 Tải image từ Docker Hub về máy cục bộ.

```bash
docker pull [REPOSITORY]:[TAG]
```

**Ví dụ:**

```bash
docker pull myusername/my-app:latest
```

* Image phải có dạng `username/repository:tag`.

* Nếu không chỉ định tag, mặc định tải `latest`.

* Xem image cục bộ: `docker images`.

### 4. `docker push`

📤 Đẩy image từ máy cục bộ lên Docker Hub.

```bash
docker push [REPOSITORY]:[TAG]
```

**Ví dụ:**

```bash
docker push myusername/my-app:latest
```

* Image phải có dạng `username/repository:tag`.

* Nếu sai định dạng, đặt lại tên:

```bash
docker tag my-app:latest myusername/my-app:latest
```

* Phải đăng nhập trước (docker login).

## 🔍 Sử Dụng Image Từ Docker Hub

### Tạo Container Từ Image

```bash
docker run -p 3000:3000 myusername/my-app:latest
```

### 📤 Chia Sẻ Image

* **Public**: Ai cũng có thể pull image (VD: `docker pull myusername/my-app`).

* **Private**: Cần đăng nhập và phân quyền truy cập trên Docker Hub.

## ⚠️ Lưu Ý Quan Trọng

❌ Phiên bản không tự cập nhật:
Push image mới lên Docker Hub nhưng không pull về, lệnh `docker run` sẽ dùng image cũ (cache).

**Giải pháp:**

```bash
docker pull myusername/my-app:latest
docker run myusername/my-app:latest
```

❌ Định dạng tên image: Phải đúng dạng `username/repository:tag`. Nếu sai, dùng `docker tag` để sửa.

## 🎯 Ví Dụ Thực Tế

```bash
docker login

docker build -t my-app:latest .
docker tag my-app:latest myusername/my-app:latest

docker push myusername/my-app:latest

docker pull myusername/my-app:latest
docker run -p 3000:3000 myusername/my-app:latest

docker images
```

**Kết quả ví dụ:**

```
REPOSITORY            TAG       IMAGE ID       CREATED        SIZE
myusername/my-app     latest    a1b2c3d4e5f6   1 hour ago     900MB
```

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ `docker login` để xác thực, `docker logout` để đăng xuất

✅ `docker pull` tải, `docker push` đẩy image theo định dạng `username/repository:tag`

✅ Dùng `docker tag` đặt tên image trước khi push

✅ Luôn `docker pull` trước khi run container để đảm bảo dùng phiên bản mới nhất

✅ Docker Hub hỗ trợ chia sẻ image public hoặc private

🚀 Quản lý image trên Docker Hub để chia sẻ và triển khai dễ dàng!