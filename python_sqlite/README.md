Integration of SQLite database to Python
------

* It has the following features. 
  * Serverless 
  * Self-Contained 
  * Zero-Configuration
  * Single-Database
  

* Serverless 
  * Generally, an RDBMS such as MySQL, PostgreSQL, etc., needs a separate server process to operate. 
  * The applications that want to access the database server use TCP/IP protocol 
  * to send and receive requests, and it is called client/server architecture.
  
  * SQLite does not require a server to run. 
  * SQLite database is joined with the application that accesses the database. 
  * SQLite database read and write directly from the database files stored on disk 
  * and applications interact with that SQLite database.


* Self-Contained 
  * SQLite is self-contained means it does not need any external dependencies 
  like an operating system or external library. 


* Zero-Configuration 
  * SQLite is zero-configuration means no setup or administration needed. 
  * Because of the serverless architecture, you don’t need to “install” SQLite before using it. 
  * There is no server process that needs to be configured, started, and stopped.


* Single-Database 
  * SQLite is a single database that means it allows a single database connection 
  to access multiple database files simultaneously. 
  * These features bring many nice features like joining tables in different databases 
  or copying data between databases in a single command. 
  * SQLite also uses dynamic types for tables. 
  * It means you can store any value in any column, regardless of the data type.