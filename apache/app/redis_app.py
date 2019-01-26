import redis


redis_host="redis"
redis_port="6379"
redis_pass=""

redis_connection=redis.StrictRedis(host=redis_host,port=redis_port,db=0,password=redis_pass)


def set_hello():
	redis_connection.set("mesage","Hello mate, Hope you are doing well . Regards from Redis")


def get_messages():
	msg=redis_connection.get("mesage")
	return msg

def main():
	set_hello()
	msg=get_messages()
	print(msg)
	return msg

if __name__ == '__main__':
	# Testing
	pass
