### Flask settings
PORT = 8000
DEBUG = False

### MongoDB settings
MONGO_PORT = 27017

MONGO_PW = "pwd1"
MONGO_USER = "user1"
MONGO_URL = "mongodb://{}:{}@clustermoonshot-shard-00-00-zpcbx.mongodb.net:27017,clustermoonshot-shard-00-01-zpcbx.mongodb.net:27017,clustermoonshot-shard-00-02-zpcbx.mongodb.net:27017/test?ssl=true&replicaSet=ClusterMoonshot-shard-0&authSource=admin&retryWrites=true&w=majority".format(MONGO_USER, MONGO_PW)
