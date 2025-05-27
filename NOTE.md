# 📝 **Adding a PHP Container**

---

## 🚀 **Tổng Quan**

Thêm container **PHP** để xử lý logic ứng dụng Laravel, kết nối với Nginx qua FastCGI. Container này được xây dựng từ file `php.dockerfile` và quản lý trong `docker-compose.yaml`, với cổng giao tiếp được cập nhật thành **9000**.

---

## 🔍 **Giải Thích File Cấu Hình**

### 1. File `php.dockerfile`

Tạo file `php.dockerfile` với nội dung:

```dockerfile
FROM php:8.4-rc-fpm-alpine
WORKDIR /var/www/html
RUN docker-php-ext-install pdo pdo_mysql
```

**Giải thích chi tiết:**

- **FROM php:8.4-rc-fpm-alpine:** Dùng image PHP 8.4 với FastCGI Process Manager (FPM) trên nền Alpine (nhẹ).

- **WORKDIR /var/www/html:** Đặt thư mục làm việc là thư mục ứng dụng Laravel.

- **RUN docker-php-ext-install pdo pdo_mysql:** Cài đặt extension PHP pdo và pdo_mysql để hỗ trợ kết nối cơ sở dữ liệu MySQL.

---

### 2. File `docker-compose.yaml`

Cập nhật file `docker-compose.yaml` với dịch vụ php:

```yaml
name: PHP Laravel Dockerized

services:
  nginx:
    image: nginx:stable-alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
  php:
    build:
      context: ./dockerfiles
      dockerfile: php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated
```

**Giải thích chi tiết:**

- **services.php:** Định nghĩa dịch vụ PHP, xây dựng từ `php.dockerfile` trong thư mục `./dockerfiles`.

- **build.context: ./dockerfiles:** Thư mục chứa file `php.dockerfile`.

- **build.dockerfile: php.dockerfile:** Chỉ định file build.

- **volumes: - ./src:/var/www/html:delegated:** Ánh xạ thư mục `./src` (mã nguồn Laravel) vào `/var/www/html`.

- **:delegated tối ưu hiệu suất:** Theo tài liệu Docker, `:delegated` là một tùy chọn volume trên macOS/Windows khi dùng Docker Desktop, ưu tiên hiệu suất bằng cách giảm tần suất đồng bộ hóa file từ container về host. Điều này cải thiện tốc độ khi làm việc với mã nguồn lớn (như Laravel), nhưng host không phản ánh thay đổi ngay lập tức từ container (dùng `:consistent` nếu cần đồng bộ tức thời).

---

### 3. Cập Nhật File `nginx.conf`

Cập nhật cổng trong `nginx.conf` để giao tiếp giữa container:

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
        fastcgi_pass php:9000; # update port 9000
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

**Cập nhật cổng:** Thay vì `php:3000`, giờ dùng `fastcgi_pass php:9000` để kết nối với container PHP trên cổng 9000, phù hợp với image `php:8.4-fpm-alpine` (mặc định dùng cổng 9000).

---

## 📌 **Tóm Tắt Kiến Thức Quan Trọng**

✅ **PHP Container:** Xây từ php:8.4-fpm-alpine, cài pdo và pdo_mysql.

✅ **docker-compose.yaml:** Build từ php.dockerfile, ánh xạ ./src vào /var/www/html với :delegated để tối ưu hiệu suất.

✅ **nginx.conf:** Cập nhật fastcgi_pass php:9000 để giao tiếp với PHP container.

✅ **Cổng 9000:** Tiêu chuẩn cho PHP-FPM, đảm bảo kết nối giữa Nginx và PHP.

---

### 🚀 **Thêm PHP Container để chạy ứng dụng Laravel hoàn chỉnh!**