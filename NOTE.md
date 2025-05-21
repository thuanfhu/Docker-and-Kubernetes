# 📝 Container-to-Container Communication: A Basic Approach

## 📌 Tổng Quan

🔗 `Container-to-container communication` cho phép các container giao tiếp với nhau, như giữa ứng dụng và dịch vụ (database, cache, API server). Cách tiếp cận cơ bản là dùng `IP của container` để kết nối trực tiếp.

---

## 🚀 Cách Thực Hiện

**1️⃣ Chạy Container Dịch Vụ**
  
Tạo container cho một dịch vụ (ví dụ: MongoDB):

```
docker run -d --name service-container mongo
```

Ví dụ: Container mongo chạy MongoDB.

---

**2️⃣ Lấy IP Của Container Dịch Vụ**  

Kiểm tra IP bằng lệnh:

```
docker container inspect service-container
```

Trong phần NetworkSettings, tìm IPAddress, ví dụ: `"IPAddress": "172.17.0.2"`. IP này dùng để container khác kết nối tới.

---

**3️⃣ Kết Nối Từ Container Ứng Dụng** 

Trong mã ứng dụng, kết nối tới container dịch vụ bằng IP:

```js
// Ví dụ: Kết nối tới MongoDB từ ứng dụng Node.js
mongoose.connect(
  'mongodb://172.17.0.2:27017/swfavorites',
  { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
  },
  (err) => {
    if (err) {
      console.log(err);
    } else {
      app.listen(3000);
    }
  }
);
```

Container ứng dụng gọi container dịch vụ (MongoDB) qua IP `172.17.0.2` trên cổng `27017`.

---

## ⚠️ Vấn Đề Với Cách Tiếp Cận

- ❗ **IP không cố định:** IP của container (như `172.17.0.2`) thay đổi mỗi khi container khởi động lại hoặc trong môi trường network phức tạp, gây lỗi kết nối.

- ❗ **Khó quản lý:** Phải kiểm tra IP thủ công mỗi lần, không phù hợp khi mở rộng hoặc tự động hóa.

- ❗ **Không hỗ trợ DNS:** Default bridge network không cho phép gọi container bằng tên, phải dùng IP.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Container dịch vụ: Chạy với `docker run --name service-container`.

✅ Lấy IP: Dùng `docker container inspect` để tìm IPAddress.

✅ Kết nối: Ứng dụng dùng IP để gọi dịch vụ (ví dụ: MongoDB).

✅ Vấn đề: IP động, khó quản lý, không hỗ trợ DNS.

---

### 🚀 Cách cơ bản để container giao tiếp, nhưng không tối ưu!