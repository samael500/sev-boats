# # -*- coding: utf-8 -*-

# from src.decorators import run_every

# @run_every(seconds=1)
# def print_f():
#     print "function is I"

# print_f()


# # from src import messages
# # from src.twitter import Twitter

# # m = messages.Messenger()

# # mm = m.get_messages()

# # t = Twitter()

# # _m = m.get_message()

# # # t.post(_m)
# # # r = t.post_tweet(_m)

# # # print r['id_str']

# # # sleep(40)

# # # print (t.delete_tweet(r['id_str']))

# # # r = t.post_tweet('#севастополь sevboats')

# import time

# # s = t.search(count=10)


# # lll = t.follow_list(t.search(count=10))

# time.sleep(30)

# # t.unfollow_list(lll)

# # # ss = s['statuses']

# # # for i in ss:
# # #     print i['text'], '\033[92m', i['user']['name'], '\033[91m', i['user']['id_str'], '\033[0m'

# # # t.delete_tweet(r['id_str'])


# # # print t.follow('2635565586')
# # # print t.unfollow('2635565586')



import settings
import os
from src.scrapper import Scrapper

scrap = Scrapper()
scrap.timeout = 0
scrap.ships_list_url = 'file:///%s' % os.path.join(settings.BASE_DIR, 'sevboats/tests/test_data/list-page:{page}.html')
scrap.ship_info_url = 'file:///%s' % os.path.join(settings.BASE_DIR, 'sevboats/tests/test_data/list.html')

# print scrap.ships_list_url

x = scrap.scrape_ships_list(['272083500', '272083700', '272083800', '272092200', '272105500', '272124300', ])

for key, value in x.iteritems():
    print key, value
print '--------------------------------------------------'
scrap.ships_list_url = 'file:///%s' % os.path.join(settings.BASE_DIR, 'sevboats/tests/test_data/list.html')
x = scrap.scrape_ships_list(['272083500', '272083700', '272083800', '272092200', '272105500', '272124300', ])

for key, value in x.iteritems():
    print key, value


x = scrap.scrape_ship('OST', '272093900')
print x

