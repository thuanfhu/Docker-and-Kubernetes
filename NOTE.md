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

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Bind Mounts ánh xạ thư mục host vào container, giúp chia sẻ code dễ dàng.

✅ Cú pháp: -v /path/on/host:/path/in/container.

✅ Shortcut: $(pwd) (macOS/Linux) hoặc "%cd%" (Windows).

✅ Khác Volumes: Người dùng quản lý, phù hợp cho phát triển.

✅ Kiểm tra quyền truy cập để tránh lỗi đọc/ghi.

---

### 🚀 Dùng Bind Mounts để phát triển nhanh hơn với Docker!