# 📝 Getting Started With Bind Mounts (Code Sharing)

## 📌 Tổng Quan

Bind Mounts cho phép ánh xạ trực tiếp một thư mục hoặc file từ máy chủ (host) vào container, giúp chia sẻ code giữa host và container trong quá trình phát triển. Theo tài liệu chính thức của Docker, Bind Mounts được quản lý bởi người dùng, khác với Volumes (quản lý bởi Docker).

---

## 🚀 Sử Dụng Bind Mounts Để Chia Sẻ Code

Bind Mounts thường dùng để đồng bộ code giữa host và container, giúp chỉnh sửa code trên host mà không cần build lại image.

**Cú pháp:**

```
docker run -v /path/on/host:/path/in/container image_name
```

- `/path/on/host`: Đường dẫn tuyệt đối trên host.

- `/path/in/container`: Đường dẫn trong container.

**Ví Dụ:** Chia sẻ thư mục `/home/user/project` trên host vào `/app` trong container:

```
docker run -v /home/user/project:/app my-app
```

Mọi thay đổi trong `/home/user/project` trên host sẽ được phản ánh ngay lập tức trong `/app` của container, và ngược lại. Container có thể chạy ứng dụng trực tiếp từ code được ánh xạ.

---

## 📝 Ghi Chú Về Shortcut

Ghi chú nhanh: Nếu bạn không muốn luôn phải nhập đường dẫn đầy đủ, có thể dùng các shortcut sau:  

- macOS/Linux: `-v $(pwd):/app`  

- Windows: `-v "%cd%":/app`

---

## 🔍 So Sánh Bind Mounts Với Volumes

| Đặc Điểm      | Bind Mounts                              | Volumes                                 |
|---------------|------------------------------------------|-----------------------------------------|
| Quản lý       | Người dùng quản lý đường dẫn trên host.   | Docker quản lý (Named/Anonymous).       |
| Đường dẫn     | Ánh xạ đường dẫn cụ thể từ host.         | Lưu trữ trong /var/lib/docker/volumes.  |
| Dùng khi      | Phát triển, cần chỉnh sửa code trực tiếp. | Lưu trữ dữ liệu vĩnh viễn (như DB).     |
| Tính linh hoạt| Dễ truy cập trên host, nhưng phụ thuộc host. | Độc lập với host, dễ di chuyển.      |

---

## 🎯 Ví Dụ Thực Tế

Bạn có thư mục code `/home/user/my-node-app` trên host.

Chạy container với Bind Mount:

```
docker run -v /home/user/my-node-app:/app -p 3000:3000 node:18
```

Chỉnh sửa file trong `/home/user/my-node-app` trên host, container sẽ tự động nhận thay đổi mà không cần restart.

---

## 🛠️ Vấn Đề Ghi Đè Với Bind Mounts

**Tình Huống** 

Khi chạy container với Bind Mount và Named Volume:

```
docker run -d -p 3000:80 --rm --name my-container-volumes-1 -v feedback:/app/feedback -v "D:\Workspace\...\NodeJS Data Volumes:/app" nodejs-app:volumes
```

- Vấn đề: Nếu Dockerfile đã cài đặt node_modules trong `/app` (qua COPY và RUN npm install), Bind Mount `-v "D:\Workspace\...\NodeJS Data Volumes:/app"` sẽ ghi đè toàn bộ `/app` trong container bằng nội dung thư mục trên host. Nếu thư mục host không có node_modules, container sẽ thiếu thư viện, dẫn đến lỗi và dừng.

- Hậu quả với `--rm`: Vì container dùng `--rm`, khi dừng, container sẽ tự động bị xóa, bao gồm cả dữ liệu tạm thời (nhưng Named Volume feedback vẫn tồn tại).

- Giải pháp: Tránh ánh xạ toàn bộ `/app`. Thay vào đó, ánh xạ thư mục con cụ thể hoặc đảm bảo thư mục trên host có node_modules.

---

## ⚠️ Lưu Ý Quan Trọng

❌ Phụ thuộc vào host: Nếu thư mục trên host không tồn tại, Docker sẽ tạo thư mục rỗng, có thể gây lỗi.

❌ Ghi đè Bind Mounts: Ánh xạ thư mục chính (như /app) có thể xóa dữ liệu quan trọng như node_modules (như ví dụ trên).

✅ Phù hợp cho phát triển: Bind Mounts lý tưởng để đồng bộ code, nhưng không nên dùng cho dữ liệu production (dùng Volumes thay thế).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Bind Mounts ánh xạ thư mục host vào container, giúp chia sẻ code dễ dàng.

✅ Cú pháp: -v /path/on/host:/path/in/container.

✅ Shortcut: $(pwd) (macOS/Linux) hoặc "%cd%" (Windows).

✅ Khác Volumes: Người dùng quản lý, phù hợp cho phát triển.

✅ Kiểm tra quyền truy cập để tránh lỗi đọc/ghi.

✅ Tránh ghi đè /app khi dùng Bind Mounts để không mất dữ liệu như node_modules.

---

### 🚀 Dùng Bind Mounts để phát triển nhanh hơn với Docker!