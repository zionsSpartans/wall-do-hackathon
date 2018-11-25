```
root@ubun:~# python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pymongo import MongoClient
>>> import pprint
>>> import datetime
>>> import urllib.parse
>>> username = urllib.parse.quote_plus('root')
>>> password = urllib.parse.quote_plus('patata')
>>> client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
>>> db = client['pruebas']
>>> post = {"source": "auth.log",
...         "msg": "Failed login from user 'potato'",
...         "tags": ["sshd", "failed", "wtf"],
...         "date": datetime.datetime.utcnow()}
>>> posts = db.posts
>>> post_id = posts.insert_one(post).inserted_id
>>> post_id
ObjectId('5bf28e8da29d283f9ab121b6')
>>> pprint.pprint(posts.find_one())
{'_id': ObjectId('5bf28e8da29d283f9ab121b6'),
 'date': datetime.datetime(2018, 11, 19, 10, 21, 1, 830000),
 'msg': "Failed login from user 'potato'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
```

- Ejemplo multiple insert:
```
>>> new_posts = [{"source": "auth.log",
...               "msg": "Failed login from user 'trololo'",
...               "tags": ["sshd", "failed", "wtf"],
...               "date": (2018, 11, 19, 10, 22, 1, 830000)},
...              {"source": "auth.log",
...               "msg": "Failed login from user 'potato'",
...               "tags": ["sshd", "failed", "wtf"],
...               "date": (2018, 11, 19, 10, 23, 1, 830000)}]
>>> result = posts.insert_many(new_posts)
>>> result.inserted_ids
[ObjectId('5bf290e7a29d283f9ab121b7'), ObjectId('5bf290e7a29d283f9ab121b8')]
>>> for post in posts.find({"source": "auth.log"}):
...   pprint.pprint(post)
...
{'_id': ObjectId('5bf28e8da29d283f9ab121b6'),
 'date': datetime.datetime(2018, 11, 19, 10, 21, 1, 830000),
 'msg': "Failed login from user 'potato'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
{'_id': ObjectId('5bf290e7a29d283f9ab121b7'),
 'date': [2018, 11, 19, 10, 22, 1, 830000],
 'msg': "Failed login from user 'trololo'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
{'_id': ObjectId('5bf290e7a29d283f9ab121b8'),
 'date': [2018, 11, 19, 10, 23, 1, 830000],
 'msg': "Failed login from user 'potato'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
>>>
```

- Ejemplo búsqueda:
```
>>> res = posts.find({"msg":{'$regex': 'ailed' } } )
>>> res.count()
3
>>> pprint.pprint(posts.find({"msg":{'$regex': 'ailed' } } ))
<pymongo.cursor.Cursor object at 0x7fa8926c4eb8>
>>> for post in res:
...     pprint.pprint(post)
...
{'_id': ObjectId('5bf28e8da29d283f9ab121b6'),
 'date': datetime.datetime(2018, 11, 19, 10, 21, 1, 830000),
 'msg': "Failed login from user 'potato'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
{'_id': ObjectId('5bf290e7a29d283f9ab121b7'),
 'date': [2018, 11, 19, 10, 22, 1, 830000],
 'msg': "Failed login from user 'trololo'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
{'_id': ObjectId('5bf290e7a29d283f9ab121b8'),
 'date': [2018, 11, 19, 10, 23, 1, 830000],
 'msg': "Failed login from user 'potato'",
 'source': 'auth.log',
 'tags': ['sshd', 'failed', 'wtf']}
>>>
```
