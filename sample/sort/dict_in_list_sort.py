"""
https://inma.tistory.com/138
"""
import pprint

sample = [
    { 'genre': 'classic', 'plays': 500, 'idx': 0 },
    { 'genre': 'pop', 'plays': 600, 'idx': 1 },
    { 'genre': 'classic', 'plays': 150, 'idx': 2 },
    { 'genre': 'classic', 'plays': 800, 'idx': 3 },
    { 'genre': 'pop', 'plays': 2500, 'idx': 4 }
]

# sortSample = sorted(sample, key = lambda s: s['plays'], reverse = True)
# print(sortSample)

sample = { 'G005919213591201'  : { 'cost'     : '4.5',
                                   'partnerId': 'jamy', },
           'G005919123608414'  : { 'cost'     : '7.5',
                                   'partnerId': '100bang', },
           'G005919637123825'  : { 'cost'     : '11.5',
                                   'partnerId': '100bang', },
           'G00591123968685'   : { 'cost'     : '11.5',
                                   'partnerId': 'jamy', },
           'G00591971230100'   : { 'cost'     : '5.5',
                                   'partnerId': 'jamy', },
           'G00591971230476'   : { 'cost'     : '7.5',
                                   'partnerId': '100bang', },
           'G00591923170917'   : { 'cost'     : '4.5',
                                   'partnerId': '100bang', },
           'G00591923171011'   : { 'cost': '12.5',
                                   },
           'G0059123972548'    : { 'cost': '12.5',
                                   },
           'G00591912373589'   : { 'cost': '5.5',
                                   },
           'YT2004393712387150': { 'cost': '4.5',
                                   },
           'YT2004401271239200': { 'cost'     : '4.5',
                                   'partnerId': 'tb85',
                                   },
           'YT2004401213621640': { 'cost'     : '5.5',
                                   'partnerId': 'htcn',
                                   },
           'YT2004401213635101': { 'cost'     : '6.5',
                                   'partnerId': 'htcn',
                                   },
           'YT2004401981237773': { 'cost'     : '7.5',
                                   'partnerId': 'tb67',
                                   },
           'YT2004414412389433': { 'cost'     : '4.5',
                                   'partnerId': 'al02',
                                   },
           'YT2004461123722780': { 'cost'     : '4.5',
                                   'partnerId': 'htcn',
                                   },
           'YT2004512512320704': { 'cost'     : '7.5',
                                   'partnerId': 'htcn',
                                   },
           'YT2004622112375265': { 'cost'     : '5.5',
                                   'partnerId': 'tb67',
                                   },
           'YT2004622312398296': { 'cost'     : '4.5',
                                   'partnerId': 'tb67',
                                   } }

sortSample = dict(sorted(sample.items(), key = lambda x: x[1]['partnerId'] if 'partnerId' in x[1].keys() else x[0]))
pp = pprint.PrettyPrinter(2)
pp.pprint(sortSample)
