from django.core.cache import cache


def redis_set(key, value, time: 120):
    cache.set(key, value, time)
