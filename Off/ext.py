from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import pysolr
solr = pysolr.Solr("http://host.docker.internal:8983/solr/my_core")
# solr = pysolr.Solr("http://127.0.0.1:8983/solr/my_core")

import redis
redis_cache = redis.Redis(host='redis-17093.c1.ap-southeast-1-1.ec2.cloud.redislabs.com', port=17093, db=0, username='sonar', password='S0narTest@')