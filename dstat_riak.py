### Author: James Martin <jmartin@basho.com>


class dstat_plugin(dstat):
    """
    Riak Stats counter

    Displays Riak Stats
    """
    def __init__(self):
        self.name = 'riak'
        self.nick = ('gets', 'glat', 'puts', 'plat')
        self.vars = ('node_gets_total', 'node_get_fsm_time_mean',
                     'node_puts_total', 'node_put_fsm_time_mean')
        self.type = 'd'
        self.width = 6
        self.scale = 50

    def check(self):
        try:
            import json
            import urllib2
            global json, urllib2
        except:
            raise Exception('Plugin needs json and urllib2 module')

    def extract(self):
        try:
            stats_raw = urllib2.urlopen(
                'http://127.0.0.1:8098/stats', None, 5).read()
        except:
            raise Exception(
                'Make sure you can access your riak stats interface')

        stats = json.loads(stats_raw)

        for name in self.vars:
            if name.find('_total') != -1:
                self.set2[name] = float(stats[name])
                self.val[name] = (
                    self.set2[name] - self.set1[name]) * 1.0 / elapsed
            else:
                self.val[name] = long(stats[name])

        if step == op.delay:
            self.set1.update(self.set2)
