# tomcat/Dockerfile
FROM tomcat:11.0-jdk17-temurin

# 删除默认的 ROOT 应用（可选，但推荐）
RUN rm -rf /usr/local/tomcat/webapps/ROOT

# 复制你的自定义页面到 ROOT 应用目录
COPY index.html /usr/local/tomcat/webapps/ROOT/index.html

# 暴露 8080 端口
EXPOSE 8080
