import redis
import settings

class RedisWrapper(object):
    shared_state = {}

    def __init__(self, *args, **kwargs):
        self.__dict__ = self.shared_state
        asyncore.dispatcher.__init__(self)
        global _redis
        _redis = self.redis_connect(server_key='main_server')
        print(_redis.ping())
        super(RedisWrapper, self).__init__(*args, **kwargs)

    def redis_connect(self, server_key):
        redis_server_conf = settings.REDIS_SERVER_CONF['servers'][server_key]
        connection_pool = redis.ConnectionPool(host=redis_server_conf['HOST'], port=redis_server_conf['PORT'],
                                               db=redis_server_conf['DATABASE'])
        return redis.StrictRedis(connection_pool=connection_pool)
