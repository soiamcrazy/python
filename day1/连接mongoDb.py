import pymongo
client = pymongo.MongoClient('localhost') #mongoDb连接
db = client['newtestdb'] #创建数据库
db['table'].insert({'name':'BOB'}) #插入table中数据
db['table'].find_one({'name':'BOB'}) #查询table表中数据
print(db['table'].find_one({'name':'BOB'}))