import statsd

c = statsd.StatsClient('graphite', 8125)

foo_stats = statsd.StatsClient(prefix='foo')


for _ in range(3):
    foo_stats.incr('bar')