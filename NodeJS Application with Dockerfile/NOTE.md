# 📝 Docker: Container & Image - Cơ Chế Hoạt Động

## 📌 Container có copy lại source code và environment nhiều lần không?
Khi Docker tạo container từ image, nó **không copy lại source code hay environment nhiều lần**. Thay vào đó, container **sử dụng lại image gốc** và chỉ tạo thêm một **Writable Layer** để ghi dữ liệu thay đổi.

---

## 🛠 **Cơ chế hoạt động của Container từ Image**
Docker sử dụng kiến trúc **UnionFS (Union File System)** để quản lý file giữa Image và Container:

1. **Image (Read-Only Layers)**: 
   - Chứa tất cả source code, dependencies, hệ điều hành base,...
   - Không thể thay đổi sau khi đã build.
2. **Writable Layer (Container Layer)**:
   - Khi container chạy, Docker thêm một **Writable Layer** phía trên Image.
   - Mọi thay đổi (ghi file, cài thêm package, chỉnh sửa code trong container) chỉ xảy ra trên layer này.

📌 **Lưu ý:** Khi container bị xóa (`docker rm`), tất cả dữ liệu trong Writable Layer cũng bị mất.

---

## ❓ **Container có sử dụng lại image không?**
✅ **Có!** Container chỉ sử dụng lại Image gốc mà không copy lại nhiều lần.

- Khi chạy `docker run IMAGE_ID`, Docker lấy Image gốc và tạo một container mới dựa trên nó.
- Nếu bạn chạy nhiều container từ cùng một Image, chúng **sẽ chia sẻ Image gốc**, chỉ có phần dữ liệu thay đổi là riêng biệt.

---