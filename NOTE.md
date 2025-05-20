# 📝 Understanding Named Volumes in Docker

## 📌 Tổng Quan

Docker hỗ trợ hai loại lưu trữ dữ liệu bên ngoài: **Volumes** (quản lý bởi Docker) và **Bind Mounts** (quản lý bởi bạn). Volumes chia thành **Anonymous Volumes** và **Named Volumes**, giúp lưu trữ dữ liệu vĩnh viễn. Named Volumes được quản lý qua lệnh `docker volume`, còn Anonymous Volumes tự động tạo bởi Docker.

---

## 🚀 Anonymous Volumes Với VOLUME Trong Dockerfile

**Tình Huống**: Dockerfile có lệnh `VOLUME ["/app/feedback"]`

- Quy trình: Image → Container → Khi chạy container, Docker tự động tạo Anonymous Volume cho `/app/feedback`.

**Kiểm tra:**: `docker volume ls`

**Kết quả ví dụ:**
```
DRIVER    VOLUME NAME
local     1a2b3c4d5e6f...
```

- Chúng ta thấy rằng các volume ẩn danh (anonymous volumes) sẽ tự động bị xóa khi container bị xóa, và điều này xảy ra khi bạn khởi động/chạy container với tùy chọn `--rm`.

- Nếu bạn khởi động container mà không dùng tùy chọn đó, volume ẩn danh sẽ không bị xóa ngay cả khi bạn xóa container (bằng `docker rm`...); tuy nhiên, nếu bạn tạo lại và chạy lại container (tức là chạy `docker run` ... lần nữa), một volume ẩn danh mới sẽ được tạo

- Do đó, dù volume cũ không bị xóa tự động, nó cũng không hữu ích vì volume ẩn danh khác sẽ được gắn khi container khởi động lại (tức là bạn đã xóa container cũ và chạy container mới); lúc này, bạn sẽ tích lũy nhiều volume ẩn danh không dùng đến, và có thể dọn chúng bằng `docker volume rm VOL_NAME` hoặc `docker volume prune`.

---

### Anonymous Volume Lưu Ở Đâu?

Theo tài liệu Docker, Anonymous Volumes lưu trên ổ cứng máy chủ tại thư mục do Docker quản lý:

- **Linux:** `/var/lib/docker/volumes/<volume-id>/_data`

- **Windows/Mac:** Tùy vào cấu hình Docker Desktop.

**Có nên tìm và truy cập không?**

- Không khuyến khích: Đường dẫn phức tạp, không có tên cụ thể, và không dễ quản lý.

- Quyền truy cập: Có, nếu bạn có quyền root trên host, nhưng không nên chỉnh sửa trực tiếp vì dễ gây lỗi.

---

## 🔍 Named Volumes Với -v

**Tạo Named Volume**: Dùng `-v` để tạo Named Volume khi chạy container: `docker run -v my-volume:/app/feedback my-app`

- Kết quả: Tạo volume tên `my-volume`, ánh xạ vào `/app/feedback` trong container.

**Kiểm tra:** `docker volume ls`

**Kết quả ví dụ:**
```
DRIVER    VOLUME NAME
local     my-volume
```

- Ưu điểm: Dễ quản lý, có tên cụ thể, tồn tại độc lập với container.

---

### So Sánh Anonymous và Named Volumes

| Đặc Điểm    | Anonymous Volumes                        | Named Volumes                        |
|-------------|------------------------------------------|--------------------------------------|
| Cách tạo    | Tự động qua VOLUME trong Dockerfile.     | Chỉ định bằng -v <name>:/path.       |
| Tên         | ID ngẫu nhiên (ví dụ: 1a2b3c4d5e6f).     | Tên do bạn đặt (ví dụ: my-volume).   |
| Quản lý     | Khó tìm, khó truy cập.                   | Dễ quản lý qua docker volume.        |
| Tính bền vững| Tồn tại cho đến khi container bị xóa.   | Tồn tại độc lập, xóa bằng docker volume rm. |
| Dùng khi    | Dữ liệu tạm thời, không cần quản lý chi tiết. | Dữ liệu quan trọng, cần quản lý lâu dài. |

---

## 🗂️ Giới Thiệu Ngắn Về Bind Mounts

**Bind Mounts:** Ánh xạ trực tiếp một thư mục cụ thể trên host (ví dụ: `/some-path`) vào container (ví dụ: `/app/data`).  

**Đặc điểm:** Bạn quản lý đường dẫn, phù hợp khi cần chỉnh sửa dữ liệu trực tiếp trên host.  

**Khác với Volumes:** Không do Docker quản lý, bạn chịu trách nhiệm về đường dẫn và quyền truy cập.

---

## ⚠️ Lưu Ý Quan Trọng

❌ Anonymous Volumes khó quản lý: Không có tên cụ thể, không nên dùng cho dữ liệu quan trọng.

✅ Named Volumes phù hợp hơn: Dễ theo dõi, quản lý bằng lệnh docker volume.

✅ Dữ liệu an toàn: Cả hai loại volume đều tồn tại sau khi container dừng, trừ khi xóa thủ công.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Anonymous Volumes: Tự động tạo qua VOLUME, lưu tại /var/lib/docker/volumes, khó quản lý.

✅ Named Volumes: Tạo bằng -v, có tên cụ thể, dễ quản lý.

✅ Bind Mounts: Ánh xạ thư mục host, bạn tự quản lý.

✅ Dùng Named Volumes cho dữ liệu quan trọng, tránh chỉnh sửa trực tiếp Anonymous Volumes.

---

### 🚀 Hiểu rõ volumes để lưu trữ dữ liệu hiệu quả trong Docker!