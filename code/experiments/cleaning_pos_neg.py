import re
import json
with open('positive.txt') as f:
    p_txt = f.read()
    p_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', p_txt)
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if cool is in the list
    print 'cool is in the postive list: ', 'cool' in p_list
with open('negative.txt') as f:
    n_txt = f.read()
    n_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', n_txt)
    n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if abrade is in the list
    print 'abrade is in the negative list: ', 'abrade' in n_list 
    # test if cool is in the list
    print 'cool is in the negative list: ', 'cool' in p_list