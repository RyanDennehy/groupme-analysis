import json, re, collections, sys
from collections import Counter, defaultdict

"""
File: groupme-analysis.py
Author: Ryan Dennehy <rmd5947 @ rit.edu>
"""

    #counts = collections.Counter([message['name'] for message in data])

    #for mem in counts.most_common():
    #    print("{0}: {1}/{2} = {3}".format(mem[0], str(l_c[mem[0]]), str(mem[1]), str(l_c[mem[0]]/mem[1])))

    #for message in data:
    #    if message['name'] == "Ryan Dennehy":
    #        print("{0}: {1} likes".format(message['text'], len(message['favorited_by'])))

    #likes = collections.Counter(itertools.chain.from_iterable([message['favorited_by'] for message in data]))
    #likes = collections.Counter([len(message['favorited_by']) for message in data])
    #print(likes)
    #for message in data:
    #    if len(message['favorited_by']) > 5:
    #        print(len(message['favorited_by']))
    #        print(message)
    #d={}
    #for message in data:
    #    if message['name'] in d:
    #        if message['picture_url'] is not None:
    #            d[message['name']] += 1
    #    else:
    #        if message['picture_url'] is not None:
    #            d[message['name']] = 1
    #d_s = sorted(zip(d.values(), d.keys()), reverse=True)
    #priint(d_s)

by_2nd = lambda x: x[-1]

def num_images(data):
    num_images = sum(msg['picture_url'] is not None for msg in data)
    print("{} images".format(num_images))

def num_images_by_user(data, sorting="name", reverse=False):
    d = defaultdict(int)
    for msg in data:
        if msg['picture_url'] is not None:
            d[msg['name']] += 1
    if sorting == "likes":
        print("{}".format(str(sorted(d.items(), key=by_2nd, reverse=reverse))))
    else:
        print("{}".format(str(sorted(d.items(), reverse=reverse))))

def likes_received(data, sorting="name", reverse=False, ignore_self=False):
    d = defaultdict(int)
    for msg in data:
        d[msg['name']] += len(msg['favorited_by'])
    if sorting == "likes":
        print("{}".format(str(sorted(d.items(), key=by_2nd, reverse=reverse))))
    else:
        print("{}".format(str(sorted(d.items(), reverse=reverse))))

def likes_per_message(data, sorting="name", reverse=False, ignore_self=False):
    likes = defaultdict(int)
    msgs  = defaultdict(int)
    for msg in data:
        likes[msg['name']] += len(msg['favorited_by'])
        if ignore_self:
            if msg['name'] in msg['favorited_by']:
                likes[msg['name']] -= 1
        msgs[msg['name']] += 1

    print("Username\tLikes\tMessages\tRatio")
    for x in zip(sorted(likes.items()), sorted(msgs.items())):
        print("{}\t{}\t{}\t{}".format(x[0][0], x[0][1], x[1][1], x[0][1]/x[1][1]))


def set_of_ids(data):
    s = set()
    for message in data:
        if message['user_id'] not in s:
            s.add(message['user_id'])

def num_messages(data):
    return len(data)

def main():
    filename = input("Filename: ")
    with open(filename) as f:
        data = json.load(f)
        likes_per_message(data)

if __name__ == "__main__":
    main()
    sys.exit(0)
