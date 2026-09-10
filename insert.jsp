<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>HPE University Docker&Kubernetes Learning</title>
</head>
<body  align="center">
        <%
java.sql.Connection conn=null;
java.lang.String strConn;
java.sql.PreparedStatement stmt=null;
java.sql.ResultSet rs=null;
// 修改1：驱动类名改为 com.mysql.cj.jdbc.Driver
Class.forName("com.mysql.cj.jdbc.Driver").newInstance();
try{
      request.setCharacterEncoding("UTF-8");
      Class.forName("com.mysql.cj.jdbc.Driver");
       String ip=System.getenv("MYSQL_SERVICE_HOST");
       String port=System.getenv("MYSQL_SERVICE_PORT");
       ip=(ip==null)?"localhost":ip;
       port=(port==null)?"3306":port;
       System.out.println("Connecting to database...");

      // 修改2：连接 URL 加上 /HPE_APP 数据库名，以及 useSSL=false 和 allowPublicKeyRetrieval=true 参数
      conn = java.sql.DriverManager.getConnection("jdbc:mysql://"+ip+":"+port+"/HPE_APP?useUnicode=true&characterEncoding=UTF-8&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=Asia/Shanghai", "root","123456");

      String sql = "insert into HPE_APP.T_USERS(USER_NAME,LEVEL) values(?,?)";
      stmt= conn.prepareStatement(sql);

      stmt.setString (1, request.getParameter("user_name"));
      stmt.setString (2, request.getParameter("level"));
      stmt.execute();
  %>
  <h3> Success add your info</h3>
  <%
   }catch(Exception se){
   se.printStackTrace();
   %>

  <h3> Error:<%= se %></h3>
   <%
   }finally{
      //finally block used to close resources
      try{
         if(stmt!=null)
            stmt.close();
      }catch(Exception se2){
      }// nothing we can do
      try{
         if(conn!=null)
            conn.close();
      }catch(Exception se){
         se.printStackTrace();
      }//end finally try
   }//end try

   System.out.println("Goodbye!");
   %>
   <input type="button" name="Submit" value="return"   onclick="location.href=index.jsp" />
</body>
</html>
