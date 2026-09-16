FROM php:8.2-apache

# 1. 安装必要的系统依赖（Composer 下载依赖包需要 git、unzip 等）
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libzip-dev \
    && docker-php-ext-install zip

# 2. 直接在 PHP 8.2 环境中安装 Composer（彻底解决版本不兼容问题）
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# 3. 设置工作目录
WORKDIR /var/www/html

# 4. 复制项目所有文件
COPY . .

# 5. 【关键调试步骤】打印当前目录文件列表，检查 composer.json 是否存在
RUN ls -la

# 6. 执行安装（加上 --no-interaction 防止 CI 环境卡住）
RUN composer install --no-dev --optimize-autoloader --no-interaction

# 7. 暴露端口
EXPOSE 80