# 使用官方的 PHP 8.2 Apache 镜像作为基础
FROM php:8.2-apache

# 安装 Composer（用于管理依赖）
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# 将工作目录设置为 Apache 的网站根目录
WORKDIR /var/www/html

# 复制项目文件（包括 composer.json 和 index.php）
COPY . .

# 使用 Composer 安装依赖（这会在 vendor/ 目录下安装 Predis 等库）
RUN composer install --no-dev --optimize-autoloader

# 暴露 Apache 默认的 80 端口
EXPOSE 80