# 📝 A Look Behind the Scenes: Inspecting Images

## 📌 `docker image inspect` Là Gì?

Lệnh `docker image inspect` hiển thị thông tin chi tiết của Docker image dưới dạng **JSON**, bao gồm cấu hình, layer, và metadata.

### 🔧 Cú pháp

```sh
docker image inspect <image-ID>
```

* `<image-ID>`: ID image (ví dụ: `sha256:57b2f3a2d340...`) hoặc tên image.
* Xem danh sách image:

```sh
docker images
```

---

## 🚀 Tại Sao Cần Inspect?

✅ **Debug**: Kiểm tra `Cmd`, `Env`, `WorkingDir`.

✅ **Xác minh**: Xem layer, kích thước, cấu hình.

✅ **Deploy**: Đảm bảo image đúng yêu cầu.

---

## 🔍 Sử Dụng `docker image inspect`

### 📘 Ví dụ

Inspect image với ID `sha256:57b2f3a2d340...`:

```sh
docker image inspect sha256:57b2f3a2d3402eaf1bd2fd4323c0f7630f8ea9456ba0081fc13465955c9713cd
```

### 📄 Kết Quả (Rút Gọn)

```json
{
  "Id": "sha256:57b2f3a2d340...",
  "Created": "2025-05-19T02:13:40Z",
  "Size": 381801417,
  "Config": {
    "Env": ["PATH=/usr/local/bin:...", "PYTHON_VERSION=3.13.3"],
    "Cmd": ["python", "guess_number.py"],
    "WorkingDir": "/app"
  },
  "RootFS": {
    "Layers": ["sha256:247f...", ...]
  }
}
```

---

## 🧠 Giải Thích

| Trường              | Ý Nghĩa                                    |
| ------------------- | ------------------------------------------ |
| `Id`                | ID duy nhất của image.                     |
| `Created`           | Thời gian tạo image.                       |
| `Size`              | Kích thước image (byte).                   |
| `Config.Cmd`        | Lệnh mặc định: `python guess_number.py`.   |
| `Config.WorkingDir` | Thư mục làm việc: `/app`.                  |
| `Config.Env`        | Biến môi trường: Python 3.13.3, PATH, v.v. |
| `RootFS.Layers`     | Danh sách layer tạo nên image.             |

## ⚠️ Lưu Ý

❌ Không nhầm với `docker inspect` (kiểm tra container).

---

## 📌 Tóm Tắt

✅ `docker image inspect <image-ID>` trả về JSON chi tiết về image.

✅ Hữu ích để **debug**, **xác minh cấu hình**, **layer**.

✅ Trường chính: `Id`, `Config`, `Size`, `RootFS`.

🚀 **Inspect để khám phá bí mật bên trong image!**