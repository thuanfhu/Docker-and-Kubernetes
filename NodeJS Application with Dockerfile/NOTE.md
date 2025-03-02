# 📝 Docker: Image, Container và Ảnh Hưởng Khi Cập Nhật Image

## 🔹 Container có bị ảnh hưởng khi cập nhật Image?

- Container **không sao chép** toàn bộ Image mà dùng chung các layers của Image.
- Khi bạn build lại Image với tag mới (ví dụ: `my-app:v2`), Docker tạo một Image mới thay vì cập nhật Image cũ (`my-app:v1`).
- **Các container đã được tạo từ Image cũ (`my-app:v1`) vẫn tiếp tục sử dụng Image cũ**, ngay cả khi bạn đã build lại Image (`my-app:v2`).
- Nếu muốn container sử dụng Image mới, bạn **phải xóa container cũ và tạo lại từ Image mới**.

📌 **Ví dụ:**

```sh
docker build -t my-app:v2 .  # Tạo Image mới
docker run -d --name container1 my-app:v2  # Container từ Image mới
```

## 🔹 Điều gì xảy ra khi xóa Image gốc?

- Nếu container `container1` đang sử dụng Image `my-app:v1`, bạn **không thể xóa Image `my-app:v1`** vì nó đang được sử dụng.
- Nếu container `container1` đang **stopped**, Docker **vẫn không cho phép xóa Image**, vì container vẫn tham chiếu đến Image.
- Nếu bạn xóa container `container1`, Docker **cho phép xóa Image `my-app:v1`**.