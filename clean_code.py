

# -*- coding: utf-8 -*-
from unicodedata import normalize
import optparse
import codecs
import sys
import re
from math import sqrt
import string
from kras_test import find_key_length



def generate_array(key):

    """Create Polybius square with transposition.
    :param key: transposition word
    :return: array
    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    array = []
    _tmp = []
    key = re.sub(r'[^a-zA-Z]+', '', key)  # remove non-alpha character
    key = key.upper()

    if key:
        for k in key:
            alphabet = alphabet.replace(k, '')

        alphabet = key + alphabet

    for y in range(5):
        for x in range(5):
            _tmp.append(alphabet[0 + 5 * y + x])
        array.append(_tmp)
        _tmp = []
    return array


def decode(numbers, array):

    """
    Polybius square decryption.
    :param numbers: numbers to decrypt
    :return: decrypted string
    """

    numbers = re.sub(r'[\D]+', '', numbers)  # remove non-digit character

    xy = ''
    yx = ''
    for number in range(0, len(numbers), 2):
        try:
            oy = int(numbers[number]) - 1
            ox = int(numbers[number + 1]) - 1
            yx += array[oy][ox]
            xy += array[ox][oy]
        except IndexError:
            pass
        continue

    return [xy,yx]



def generateKey(string, key):
    #If key is lune and there are 20 letters in the cipher it will return lunelunelunelunelune
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    orig_text = []
    #if first leter in cipher is a, we wil have 0 + 12(L for Lune) + 26 = 38 % 26 = 12. So it would return L.
    for i in range(len(cipher_text)):
        current_letter =cipher_text[i].lower()
        x=(alpha.index(current_letter) - alpha.index(key[i]) + 26) % 26
        orig_text.append(alpha[x])
    return("" . join(orig_text))




possible_keys = ['abbey', 'able', 'access', 'across', 'added', 'afront', 'after', 'again', 'ages', 'agree', 'alley', 
 'also', 'amando', 'arcane', 'around', 'arrive', 'arts', 'asked', 'astral', 'author', 'aware', 'away', 'awoke', 'bach', 'back', 'based',
  'basics', 'baths', 'became', 'been', 'before', 'began', 'begins', 'begun', 'being', 'beings', 'belief', 'below', 'beyond', 'bias', 'billed',
   'binds', 'birth', 'blood', 'bodel', 'bodels', 'body', 'born', 'built', 'call', 'called', 'cambio', 'came', 'cannot', 'care', 'carmen', 'cast', 
   'cause', 'caused', 'cell', 'centre', 'change', 'chief', 'chri', 'city', 'citys', 'civil', 'claim', 'clash', 'clawk', 'clear', 'close', 'closer',
    'code', 'codes', 'common', 'corner', 'cosmos', 'could', 'court', 'cover', 'cracks', 'crawl', 'create', 'curse', 'dare', 'date', 'dawn', 'days',
    'dead', 'debate', 'deep', 'degree', 'delay', 'demi', 'deneir', 'dents', 'descri', 'device', 'differ', 'divine', 'docu', 'done', 'down', 'dream', 
    'dreams', 'droop', 'during', 'each', 'earn', 'ease', 'edwin', 'effort', 'eight', 'either', 'else', 'emerge', 'ended', 'ending', 'enough', 'entire',
    'entity', 'events', 'every', 'evil', 'exact', 'except', 'exist', 'exists', 'eyes', 'fabric', 'fact', 'facts', 'faerie', 'failed', 'favor', 'felt',
       'feys', 'find', 'finds', 'firm', 'first', 'five', 'fluid', 'flux', 'follow', 'form', 'formed', 'former', 'foun', 'found', 'four', 'free', 'friday', 
       'from', 'full', 'fully', 'funded', 'given', 'glasmi', 'goal', 'gods', 'gone', 'goss', 'great', 'grom', 'group', 'groups', 'growth', 'guild', 'guilds', 
       'gumash', 'hall', 'handy', 'harm', 'harpy', 'have', 'having', 'heart', 'help', 'here', 'higgs', 'high', 'higher', 'hilda', 'hold', 'hole', 'home',
        'hopp', 'hours', 'house', 'illday', 'import', 'inda', 'influx', 'ingold', 'inner', 'into', 'itself', 'juster', 'kater', 'knocks', 'know', 'known', 
        'large', 'last', 'late', 'latter', 'leave', 'left', 'legal', 'length', 'lest', 'lether', 'letter', 'levi', 'life', 'like', 'likely', 'lili', 'list', 
        'lists', 'little', 'livery', 'local', 'logic', 'long', 'longer', 'look', 'loose', 'lose', 'lost', 'ltdiii', 'lune', 'luut', 'made', 'mages', 'magic',
         'major', 'make', 'makers', 'makes', 'manner', 'manual', 'many', 'march', 'marked', 'masons', 'master', 'matter', 'means', 'meet', 'ments', 'mesav',
          'metal', 'mettle', 'milk', 'mind', 'minor', 'minute', 'mist', 'mobius', 'model', 'modern', 'modron', 'money', 'month', 'months', 'more', 'mortal',
           'most', 'move', 'much', 'murky', 'music', 'must', 'myazu', 'myself', 'name', 'named', 'names', 'native', 'nature', 'naught', 'neday', 'need', 'neer', 
           'never', 'newest', 'newly', 'nexus', 'noble', 'nola', 'note', 'noted', 'notes', 'notice', 'nugget', 'number', 'nurses', 'object', 'occur', 'offer', 
           'office', 'often', 'oghma', 'ones', 'only', 'open', 'opened', 'orbit', 'order', 'orders', 'orient', 'other', 'outer', 'outset', 'over', 'paamzn', 
           'paid', 'palli', 'pang', 'paper', 'part', 'pass', 'passes', 'past', 'period', 'person', 'place', 'placed', 'plan', 'planar', 'plane', 'planes',
            'played', 'point', 'post', 'power', 'press', 'prime', 'primer', 'primes', 'print', 'prior', 'proven', 'public', 'purely', 'pyre', 'quasi', 
            'quirk', 'race', 'races', 'rapid', 'rather', 'ratio', 'reach', 'reader', 'real', 'realm', 'realms', 'reason', 'recent', 'reddy', 'region', 
            'remove', 'resi', 'rest', 'result', 'review', 'reward', 'rigid', 'rising', 'role', 'routes', 'rules', 'ruth', 'safe', 'same', 'sand', 'sanneh', 
            'scope', 'scream', 'scribe', 'seat', 'second', 'seek', 'seen', 'sentra', 'series', 'shadow', 'shame', 'sheday', 'shift', 'shoe', 'short', 'should',
             'show', 'shown', 'shut', 'sicas', 'side', 'siege', 'sieges', 'sights', 'signs', 'simon', 'since', 'slaadi', 'slang', 'slow', 'slower', 'sneed', 
             'snsn', 'solid', 'some', 'soul', 'source', 'space', 'spaces', 'sparse', 'spends', 'spirit', 'spoken', 'spread', 'spring', 'square', 'start',
              'state', 'states', 'status', 'still', 'stop', 'strong', 'study', 'such', 'sudden', 'sumday', 'surely', 'swup', 'system', 'tables', 'take', 
              'takes', 'terms', 'terra', 'tether', 'than', 'thanks', 'that', 'their', 'them', 'then', 'there', 'these', 'they', 'think', 'this', 'those', 
              'throne', 'tilers', 'time', 'times', 'titan', 'today', 'token', 'took', 'topic', 'tower', 'traced', 'trade', 'travel', 'true', 'truly', 'trust',
               'truth', 'truths', 'tune', 'twelve', 'unfit', 'unique', 'unlike', 'until', 'upon', 'usage', 'valid', 'values', 'vera', 'very', 'visit', 'walked',
                'walls', 'weeks', 'well', 'were', 'what', 'when','which', 'while', 'whole', 'will', 'with', 'within', 'words', 
                'work', 'works', 'world', 'worlds', 'would', 'woven', 'year', 'years', 'young', 'your', 'zero', 'zibua']
#the code rian original gave us
initial_coder = ("""45 51 25 41 44 44 24 45 31 22 44 11 31 35 54 13 12 52 34 54 12 52 51 52 14 43 43 52 43 12 
                23 23 52 51 54 55 55 25 14 53 14 55 11 21 54 43 53 33 53 13 31 14 25 14 13 23 21 51 53 43 
                23 24 45 54 13 31 11 31 44 15 33 54 33 14 53 14 32 33 35 51 45 51 45 43 24 51 23 13 35 51
                35 25 52 34 53 45 11 52 33 35 22 54 13 24 45 22 43 11 43 53 14 35 53 53 54 12 54 11 53 43 23 14 25 24 15 12 32 25 23 35 44 12 31 31 22 31 43
                35 54 22 45 35 25 52 13 35 22 43 31 12 11 24 13 35 51 13 11 51 53 22 45 51 25 34 14 44 24 25 51 34 35 54 12 31 42 23 52 51 34 
                53 35 21 33 53 13 35 11 52 33 35 55 12 45 31 13 31 43 31 34 11 44 24 31 51 54 12 24 35 
                22 54 12 54 11 33 54 41 43 31 43 11 23 23 23 14 55 23 21 42 21 44 44 24 15 51 54 51 45 
                15 53 43 23 55 42 23 44 51 23 14 31 41 35 14 25 53 43 23 33 23 14 13 13 51 35""")


for keyword in possible_keys:
    #keyword = 'gods'
    square = generate_array(keyword)
    coded_string = decode(initial_coder,square)
    for s in coded_string:
        keystream = generateKey(s, keyword)
        answer = originalText(s, keystream)
        if 'the' in answer:
            if "is" in answer:
                if "in" in answer:
                    print("")
                    print("")
                    if coded_string.index(s) == 0:
                        print('YX')
                    else:
                        print('YX')
                    print(keyword)
                    print("Decoded String :", answer)
                    print("")
                    print("")
