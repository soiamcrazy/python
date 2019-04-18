import redis
r = redis.Redis('localhost',6379)
r.set('name','213')
r.set('user','张三')
r.set('phone','150930')
print(r.get('phone'))
