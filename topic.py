# coding: utf-8
import json
from models.user import User
from models.mongua import Mongua
import logging
import time
ogger = logging.getLogger('bbs')


class Cache(object):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


class MemoryCache(Cache):
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class RedisCache(Cache):
    import redis
    redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

    def set(self, key, value):
        return RedisCache.redis_db.set(key, value)

    def get(self, key):
        return RedisCache.redis_db.get(key)


class Topic(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('content', str, ''),
        ('title', str, -1),
        ('user_id', int, -1),
        ('board_id', int, -1),
        ('views', int, 0),
    ]

    should_update_all = True
    cache = MemoryCache()
    redis_cache = RedisCache()

    def to_json(self):
        d = dict()
        for k in Topic.__fields__:
            key = k[0]
            if not key.startswith('_'):
                d[key] = getattr(self, key)
        return json.dumps(d)

    @classmethod
    def from_json(cls, j):
        d = json.loads(j)
        instance = cls()
        for k, v in d.items():
            setattr(instance, k, v)
        return instance

    @classmethod
    def all_delay(cls):
        time.sleep(3)
        return Topic.all()

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m

    def save(self):
        super(Topic, self).save()
        should_update_all = True

    @classmethod
    def cache_all(cls):
        if Topic.should_update_all:
            Topic.redis_cache.set('topic_all', json.dumps([i.to_json() for i in cls.all_delay()]))
            Topic.should_update_all = False
        j = json.loads(Topic.redis_cache.get('topic_all').decode('utf-8'))
        j = [Topic.from_json(i) for i in j]
        return j

    def replies(self):
        from .reply import Reply
        ms = Reply.find_all(topic_id=self.id)
        return ms

    def board(self):
        from .board import Board
        m = Board.find(self.board_id)
        return m

    def user(self):
        u = User.find(id=self.user_id)
        return u

    def ct(self):
        format = '%Y/%m/%d %H:%M:%S'
        value = time.localtime(int(self.created_time))
        dt = time.strftime(format, value)
        return dt