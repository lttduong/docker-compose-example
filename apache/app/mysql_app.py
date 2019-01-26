
import mysql.connector

class SqlOperator(object):
	"""docstring for SqlOperator"""

	def __init__(self, host, user, database, password, port):
		self.sql_host = host
		self.sql_user = user
		self.sql_database = database
		self.sql_password = password
		self.sql_port = port

	
	def SearchSql(self, connection, sql_search_query):
		try:
			cursor = connection.cursor()
			cursor.execute(sql_search_query)
			result = cursor.fetchall()
			return result
			cursor.close()
		except Exception as error:
			print("Failed to get data from SQL {}".format(error))

	def CloseConnection(self, connection):
		if(connection.is_connected()):
			connection.close()
			print("MySQL connection is closed")

	def StartConnection(self):
		try:
			connection = mysql.connector.connect(
				host=self.sql_host,
				user=self.sql_user,
				database=self.sql_database,
				password=self.sql_password,
				port=self.sql_port
				)
			return connection
		except Exception as error:
			print("Failed to establish connection with SQL {}".format(error))


	def FetchData(self, connection):
		sql_search_query = """ select * from  whoami """
		result = self.SearchSql(connection, sql_search_query)
		return result



	@staticmethod
	def main():
		sql_obj=SqlOperator(host='mysql',user="test",database="test",password="test",port='3306')
		connection=sql_obj.StartConnection()
		result=sql_obj.FetchData(connection)
		print(result)
		return result