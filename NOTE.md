# 📝 Container Communication: MongoDB, Node.js Backend, React Frontend, and Host Interaction

## 📌 Tổng Quan

🔗 Hướng dẫn này giải thích cách ba container (MongoDB, backend Node.js, frontend React.js) tương tác với nhau và với host machine, giải đáp các thắc mắc về networking và cách fetch hoạt động trong Docker.

---

## 🚀 Các Bước Thực Hiện

### 1️⃣ Chạy Container MongoDB (mongodb)

```
docker run --name mongodb --rm -p 27017:27017 -d mongo
```

- `-p 27017:27017`: Ánh xạ cổng 27017 của container mongodb ra cổng 27017 trên host.

- Container mongodb có thể truy cập từ host tại `localhost:27017`.

---

### 2️⃣ Chạy Container Backend Node.js (node-container) và Kết Nối Với MongoDB

Trong mã backend (`app.js`) của container node-container, kết nối với MongoDB:

```js
mongoose
  .connect('mongodb://host.docker.internal:27017/course-goals', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log('CONNECTED TO MONGODB');
    app.listen(80);
  })
  .catch((err) => {
    console.error('FAILED TO CONNECT TO MONGODB');
    console.error(err);
  });
```

- **Giải thích:** `host.docker.internal` là tên DNS đặc biệt ánh xạ đến IP của host. Container node-container dùng `host.docker.internal:27017` để gọi container mongodb thông qua cổng 27017 trên host (ánh xạ bởi `-p`).

- **Sai nếu dùng localhost:** Trong container node-container, `localhost` là chính nó, không phải host, nên không thể gọi mongodb.

- **Build và chạy container node-container:**

  ```
  docker build -t node-backend:image .
  docker run --name node-container -d --rm -p 80:80 node-backend:image
  ```

- `-p 80:80`: Ánh xạ cổng 80 của container node-container ra `localhost:80` trên host.

- Host truy cập `localhost:80` sẽ gọi API từ container node-container.

---

### 3️⃣ Chạy Container Frontend React.js (react-container) và Kết Nối Với Backend

Mã frontend (`App.js`) trong container react-container gọi API backend:

```js
const response = await fetch('http://localhost:80/goals');
```

- **Build và chạy container react-container:**

  ```
  docker build -t react-frontend .
  docker run --name react-container --rm -p 3000:3000 -d react-frontend
  ```

- `-p 3000:3000`: Ánh xạ cổng 3000 của container react-container ra `localhost:3000` trên host.

---

## 💡 Giải Thích Chi Tiết Thắc Mắc

### Thắc mắc 1: Container react-container gọi được localhost:80 của container node-container? Tại sao không cần host.docker.internal?

- Đúng, container react-container không gọi trực tiếp `localhost:80`. Thay vào đó, container react-container chỉ phục vụ các file tĩnh (HTML, CSS, JavaScript) cho trình duyệt trên host khi truy cập `localhost:3000`. Lệnh `fetch('http://localhost:80/goals')` trong App.js được thực thi bởi trình duyệt trên host, không phải trong container react-container.

- **Tại sao không cần host.docker.internal?** Vì fetch chạy trên trình duyệt (host), `localhost:80` là địa chỉ trên host, ánh xạ đến container node-container (qua `-p 80:80`). `host.docker.internal` chỉ cần khi container gọi host, không áp dụng ở đây.

---

### Thắc mắc 2: Lệnh fetch thuộc host machine, còn localhost:80 là container node-container?

- Đúng. Khi host truy cập `localhost:3000`, trình duyệt tải file JavaScript từ container react-container. JavaScript thực thi lệnh fetch trên trình duyệt (host), gọi `localhost:80` – địa chỉ trên host ánh xạ đến cổng 80 của container node-container. Do đó, giao tiếp là giữa trình duyệt (host) và container node-container, không phải giữa container react-container và node-container.

---

> 📝 **Lưu ý:** Các container chạy trên default bridge network, không hỗ trợ DNS resolution, nên container node-container phải dùng `host.docker.internal` để gọi mongodb trên host.

---

## 🔍 Cách Container Tương Tác và Với Host Machine

- **Container mongodb ↔ Container node-container:** Container node-container gọi container mongodb qua `host.docker.internal:27017` (cổng host ánh xạ từ mongodb).

- **Container node-container ↔ Host:** Host gọi API của container node-container qua `localhost:80` (ánh xạ cổng).

- **Container react-container ↔ Host ↔ Container node-container:** Container react-container phục vụ file JavaScript cho trình duyệt (host) qua `localhost:3000`. Trình duyệt thực thi fetch để gọi API từ container node-container qua `localhost:80`.

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Container mongodb: Chạy trên host (localhost:27017) qua -p.

✅ Container node-container: Dùng host.docker.internal:27017 gọi mongodb, phục vụ API tại localhost:80.

✅ Container react-container: Phục vụ file cho trình duyệt tại localhost:3000, fetch chạy trên host gọi node-container.

✅ Networking: fetch chạy trên trình duyệt (host), gọi localhost:80 (container node-container).

---

### 🚀 Hiểu rõ container và host tương tác để triển khai hiệu quả!