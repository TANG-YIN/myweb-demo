import os

class Config:
    MYSQL_HOST = os.getenv("MYSQL_SERVICE_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_SERVICE_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "123456")
    MYSQL_DB = os.getenv("MYSQL_DB", "HPE_APP")
