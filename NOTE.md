# 📝 Optimized Container Communication: MongoDB, Node.js Backend, React Frontend with Networks and Volumes

## 📌 Tổng Quan

🚀 Hướng dẫn này tối ưu hóa giao tiếp giữa container MongoDB, backend Node.js, và frontend React.js bằng cách sử dụng network, named volume, anonymous volume, bind mount, và .dockerignore. Điều này đảm bảo hiệu suất, bảo mật, và dễ quản lý theo tài liệu Docker 2025.

---

## 🚀 Các Bước Thực Hiện

### 1️⃣ Tạo Docker Network

```
docker network create my-network
```

**Lý do:** User-defined network (my-network) hỗ trợ DNS resolution, cho phép container gọi nhau qua tên (ví dụ: mongodb) thay vì IP, khắc phục hạn chế của default bridge network.

---

### 2️⃣ Chạy Container MongoDB (mongodb)

```
docker run --name mongodb -d --rm --network my-network -v data:/data/db mongo
```

**Giải thích:**

- `--name mongodb`: Đặt tên container để các container khác gọi qua DNS.

- `-d`: Chạy nền.

- `--rm`: Tự xóa khi dừng (phù hợp với thử nghiệm).

- `--network my-network`: Gắn vào network đã tạo để giao tiếp qua tên.

- `-v data:/data/db`: Sử dụng named volume data để lưu dữ liệu MongoDB tại `/data/db` trong container. Named volume do Docker quản lý (thường ở /var/lib/docker/volumes/), đảm bảo dữ liệu bền vững và dễ backup.

**Tại sao làm vậy?** Named volume tránh mất dữ liệu khi container dừng, và network giúp giao tiếp ổn định giữa container.

---

### 3️⃣ Chạy Container Backend Node.js (nodejs-container)

**Cập Nhật Mã Nguồn**

**File app.js:**

```js
mongoose
  .connect(`mongodb://mongodb:27017/course-goals?authSource=admin`)
  .then(() => {
    console.log('CONNECTED TO MONGODB');
    app.listen(80);
  })
  .catch((err) => {
    console.error('FAILED TO CONNECT TO MONGODB');
    console.error(err);
  });
```

**File package.json:**

```json
{
  "name": "backend",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "nodemon app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "thuanflu",
  "license": "ISC",
  "dependencies": {
    "body-parser": "^2.2.0",
    "express": "^5.1.0",
    "mongoose": "^8.15.0",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "nodemon": "^3.1.10"
  }
}
```

**File Dockerfile:**

```
FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 80
CMD ["npm", "start"]
```

**File .dockerignore:**

```
node_modules
Dockerfile
.git
```

**Build và Chạy Container**

```
docker build -t nodejs-backend:image .
docker run --name nodejs-container -d --rm -p 80:80 -v nodejs-logs:/app/logs -v /app/node_modules -v "D:\Workspace for Learning\My Projects\Learn Technology\Docker-and-Kubernetes\Multi-Container Application\backend:/app" --network my-network nodejs-backend:image
```

**Giải thích:**

- `-p 80:80`: Ánh xạ cổng 80 để host truy cập backend qua localhost:80.

- `-v nodejs-logs:/app/logs`: Named volume nodejs-logs lưu log, quản lý dễ dàng.

- `-v /app/node_modules`: Anonymous volume ngăn host ghi đè thư mục node_modules trong container.

- `-v "D:\...\backend:/app"`: Bind mount ánh xạ thư mục host vào /app trong container, cho phép chỉnh sửa code trực tiếp từ host.

- `--network my-network`: Gắn vào network để gọi mongodb qua tên.

**Tại sao làm vậy?** Volume lưu dữ liệu/log, bind mount hỗ trợ phát triển, network tối ưu giao tiếp.

---

### 4️⃣ Chạy Container Frontend React.js (reactjs-container)

**Cập Nhật Mã Nguồn**

**File App.js (giữ nguyên localhost:80):**

```js
import React, { useState, useEffect } from 'react';

import GoalInput from './components/goals/GoalInput';
import CourseGoals from './components/goals/CourseGoals';
import ErrorAlert from './components/UI/ErrorAlert';

function App() {
  const [loadedGoals, setLoadedGoals] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(function () {
    async function fetchData() {
      setIsLoading(true);
      try {
        const response = await fetch('http://localhost:80/goals');
        const resData = await response.json();
        if (!response.ok) throw new Error(resData.message || 'Fetching failed.');
        setLoadedGoals(resData.goals);
      } catch (err) {
        setError(err.message || 'Fetching failed.');
      }
      setIsLoading(false);
    }
    fetchData();
  }, []);

  async function addGoalHandler(goalText) {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:80/goals', {
        method: 'POST',
        body: JSON.stringify({ text: goalText }),
        headers: { 'Content-Type': 'application/json' },
      });
      const resData = await response.json();
      if (!response.ok) throw new Error(resData.message || 'Adding failed.');
      setLoadedGoals((prevGoals) => [{ id: resData.goal.id, text: goalText }, ...prevGoals]);
    } catch (err) {
      setError(err.message || 'Adding failed.');
    }
    setIsLoading(false);
  }

  async function deleteGoalHandler(goalId) {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:80/goals/' + goalId, { method: 'DELETE' });
      const resData = await response.json();
      if (!response.ok) throw new Error(resData.message || 'Deleting failed.');
      setLoadedGoals((prevGoals) => prevGoals.filter((goal) => goal.id !== goalId));
    } catch (err) {
      setError(err.message || 'Deleting failed.');
    }
    setIsLoading(false);
  }

  return (
    <div>
      {error && <ErrorAlert errorText={error} />}
      <GoalInput onAddGoal={addGoalHandler} />
      {!isLoading && <CourseGoals goals={loadedGoals} onDeleteGoal={deleteGoalHandler} />}
    </div>
  );
}

export default App;
```

**File .dockerignore (giống backend):**

```
node_modules
Dockerfile
.git
```

**File Dockerfile:**

```
FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

**Build và Chạy Container**

```
docker build -t reactjs-frontend:image .
docker run --name reactjs-container --rm -p 3000:3000 -d -v /app/node_modules -v "D:\Workspace for Learning\My Projects\Learn Technology\Docker-and-Kubernetes\Multi-Container Application\frontend\src:/app/src" reactjs-frontend:image
```

**Giải thích:**

- `-p 3000:3000`: Ánh xạ cổng 3000 để host truy cập frontend qua localhost:3000.

- `-v /app/node_modules`: Anonymous volume bảo vệ thư mục node_modules.

- `-v "D:\...\frontend\src:/app/src"`: Bind mount ánh xạ thư mục nguồn từ host để cập nhật code trực tiếp.

**Tại sao không dùng network?** 

- Container reactjs-container chỉ phục vụ file tĩnh (HTML, JS) cho trình duyệt trên host. 

- `fetch('http://localhost:80/goals')` chạy trên trình duyệt (host), gọi container nodejs-container qua localhost:80 (ánh xạ cổng), nên không cần network để giao tiếp container với container.

> Lưu ý: React tự động restart khi thay đổi file (qua npm start), không cần dịch vụ như nodemon.

---

## 🔍 Cách Container Tương Tác và Với Host Machine

- **Container mongodb ↔ Container nodejs-container:** Container nodejs-container gọi mongodb:27017 qua network my-network.

- **Container nodejs-container ↔ Host:** Host truy cập API qua localhost:80 (ánh xạ cổng).

- **Container reactjs-container ↔ Host ↔ Container nodejs-container:** Container reactjs-container phục vụ file cho trình duyệt (host) qua localhost:3000. Trình duyệt thực thi fetch gọi localhost:80 (container nodejs-container).

---

## 📌 Tóm Tắt Kiến Thức Quan Trọng

✅ Network: my-network cho phép gọi qua tên (ví dụ: mongodb).

✅ Container mongodb: Dùng named volume data để lưu dữ liệu.

✅ Container nodejs-container: Sử dụng bind mount, network để tối ưu.

✅ Container reactjs-container: Dùng bind mount, không cần network, fetch chạy trên host.

✅ Đồng bộ file WSL 2: Nếu gặp vấn đề đồng bộ file trên Windows với WSL 2, tham khảo hướng dẫn khắc phục.

---

### 🚀 Tối ưu container với network và volume để triển khai hiệu quả!