# 替换为你当前 myweb 使用的基础镜像，例如 tomcat:9.0-jdk8
FROM kubeguide/tomcat-app:v1

# 删除基础镜像中可能存在的旧版驱动（如果有的话）
RUN rm -f /usr/local/tomcat/webapps/demo/WEB-INF/lib/mysql-connector-java-*.jar || true

# 复制新版 JDBC 驱动到指定目录
COPY mysql-connector-j-8.0.33.jar /usr/local/tomcat/webapps/demo/WEB-INF/lib/

# 复制修改后的 insert.jsp 覆盖原文件
COPY insert.jsp /usr/local/tomcat/webapps/demo/insert.jsp

# 确保权限正确（通常不需要，但以防万一）
# RUN chmod 644 /usr/local/tomcat/webapps/demo/insert.jsp
