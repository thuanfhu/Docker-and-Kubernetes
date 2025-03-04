# 🖥️ Docker Interactive Mode: Tương Tác Hiệu Quả Với Container

## 🔹 1. Interactive Mode trong Docker là gì?

Interactive Mode cho phép người dùng tương tác trực tiếp với container thông qua terminal. Điều này rất hữu ích khi cần chạy ứng dụng có nhập liệu từ bàn phím hoặc kiểm tra bên trong container.

Khi container được chạy ở chế độ này, bạn có thể nhập lệnh, kiểm tra trạng thái, hoặc thực thi chương trình ngay trong môi trường container.

---

## 🔹 2. Cách chạy container ở chế độ Interactive

### 📌 Lệnh cơ bản:

```sh
docker run -it ubuntu bash
```

**Giải thích:**

- `-i` (interactive): Giữ kết nối đầu vào từ bàn phím.
- `-t` (tty): Cấp phát một terminal ảo.
- `ubuntu`: Tên image được sử dụng.
- `bash`: Lệnh shell chạy bên trong container.

Sau khi chạy, bạn sẽ thấy terminal chuyển sang môi trường bên trong container:

```sh
root@container-id:/#
```

Lúc này, bạn có thể gõ lệnh như trên một máy Linux thông thường.

---

## 🔹 3. Lỗi gặp phải khi chạy Interactive Mode và cách khắc phục

### ❌ Lỗi: `EOFError: EOF when reading a line`

**Lỗi:**

```sh
docker run sha256:c9df4e84149cf7ca6a4924129bed8af57c53adb54351b35cb89f8c39b4b0c5a2
```

**Nguyên nhân:**

- Lỗi này xảy ra khi `input()` trong Python cố gắng đọc dữ liệu nhưng không có đầu vào nào được cung cấp.
- Thường gặp khi container chạy mà không có terminal kết nối.

**Cách khắc phục:**

Chạy container với chế độ interactive:

```sh
docker run -it sha256:c9df4e84149cf7ca6a4924129bed8af57c53adb54351b35cb89f8c39b4b0c5a2
```

- `-i`: Cho phép nhập dữ liệu từ bàn phím.
- `-t`: Cấp phát terminal ảo.

---

### ❌ Lỗi khi chạy `docker start <CONTAINER_ID>`

**Nguyên nhân:**

- Nếu container đã bị **stop trước đó**, khi chạy `docker start <CONTAINER_ID>` thì container sẽ khởi động nhưng **không hiển thị output** vì mặc định nó chạy ở chế độ detached.
- Nếu container yêu cầu input (`input()` trong Python chẳng hạn), nó có thể bị lỗi hoặc dừng ngay lập tức vì không có terminal tương tác.

**Cách khắc phục:**

1. Nếu muốn thấy output của container khi chạy lại, sử dụng `-a`:

   ```sh
   docker start -a <CONTAINER_ID>
   ```

   *Nhưng nếu container yêu cầu nhập dữ liệu, lệnh này có thể vẫn bị lỗi.*

2. Nếu container yêu cầu nhập dữ liệu, bạn cần chạy với interactive mode:

   ```sh
   docker start -a -i <CONTAINER_ID>
   ```

   - `-a`: Hiển thị output của container.
   - `-i`: Cho phép nhập dữ liệu từ bàn phím.

---

## 🔹 4. Tóm lược

✔️ **Interactive Mode** giúp bạn kiểm tra và làm việc trong container như trên một hệ thống thực tế.

✔️ **Dùng ************************`-it`************************ để giữ terminal hoạt động và nhận input từ bàn phím.**

✔️ **Nếu container yêu cầu input, sử dụng ************************`docker start -a -i`************************ thay vì ************************`docker start -a`************************.**&#x20;

✔️ **Kiểm tra logs và image nếu gặp lỗi khi chạy.**