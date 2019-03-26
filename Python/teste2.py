import redis
import hiredis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
# with r.pipeline(transaction=False) as pipe:
#     r['a'] = 0
#     while 1:
#         try:
#             pipe.watch('a')
#             current_value = pipe.get('a')
#             next_value = int(current_value) + 1
#             # now we can put the pipeline back into buffered mode with MULTI
#             pipe.multi()  
#             pipe.set('a', next_value)
#             pipe.execute()
#             break
#         except WatchError:
#             continue
#         finally:
#             pipe.reset()

def my_handler(message):
    print 'MY HANDLER: ', message['data']

def client_side_incr(pipe):
    current_value = pipe.get('a')
    next_value = int(current_value) + 1
    pipe.multi()
    pipe.set('a', next_value)
    pipe.execute()

r.transaction(client_side_incr, 'a')
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe(**{'my-channel': my_handler})
thread = p.run_in_thread(sleep_time=0.001)
# print r.publish('my-channel', 'opa')
message = p.get_message()