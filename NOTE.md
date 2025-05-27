# 📝 **Adding a Nginx (Web Server) Container**

---

## 🚀 **Tổng Quan**

Trong dự án **PHP Laravel Dockerized**, chúng ta thêm một container **Nginx** để xử lý các yêu cầu web, hoạt động như một web server cho ứng dụng Laravel. `Nginx` sẽ chuyển các yêu cầu PHP đến container PHP thông qua **FastCGI**.

---

## 🔍 **Giải Thích File Cấu Hình**

### 1. File `nginx.conf`

File `nginx.conf` định nghĩa cách Nginx xử lý các yêu cầu HTTP:

```nginx
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    root /var/www/html/public;
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass php:3000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

**Giải thích chi tiết:**

- **listen 80:** Nginx lắng nghe trên cổng 80 (HTTP mặc định).

- **index index.php index.html:** Ưu tiên file index.php (Laravel entry point) hoặc index.html.

- **server_name localhost:** Tên server (dùng localhost trong môi trường dev).

- **root /var/www/html/public:** Thư mục gốc cho ứng dụng, trỏ đến thư mục public của Laravel.

- **location /**: Xử lý mọi yêu cầu, chuyển hướng đến index.php nếu không tìm thấy file.

- **location ~ \.php$**: Xử lý file PHP, chuyển yêu cầu PHP đến container php qua fastcgi_pass.

---

### 2. File `docker-compose.yaml`

File `docker-compose.yaml` định nghĩa dịch vụ nginx:

```yaml
name: PHP Laravel Dockerized

services:
  nginx:
    image: nginx:stable-alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
```

**Giải thích chi tiết:**

- **name:** Tên dự án Docker Compose.

- **services.nginx:** Dịch vụ Nginx, chạy container web server.

- **image:** Dùng image nginx phiên bản stable-alpine (nhẹ, tối ưu).

- **ports:** Ánh xạ cổng 8080 trên host đến cổng 80 trong container (truy cập ứng dụng qua http://localhost:8080).

- **volumes:** Ánh xạ file nginx.conf từ thư mục ./nginx trên host vào /etc/nginx/nginx.conf trong container. `:ro` (read-only): Đảm bảo file chỉ đọc, không sửa đổi trong container, tăng bảo mật.

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **Nginx Container:** Dùng nginx:stable-alpine, xử lý yêu cầu web cho Laravel.

✅ **nginx.conf:** Định nghĩa cổng, root `/var/www/html/public`, chuyển yêu cầu PHP đến `php:3000`.

✅ **docker-compose.yaml:** Ánh xạ cổng 8080:80, mount file config với `:ro` để bảo mật.

✅ **FastCGI:** Kết nối Nginx và PHP qua `fastcgi_pass`.

---

### 🚀 **Thêm Nginx Container để chạy ứng dụng Laravel hiệu quả!**