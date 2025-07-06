import copy
from collections import Counter
from itertools import combinations

def mahan_dist(s):
    curr = [0]
    mahan = 0
    for i in range(len(s)):
        if s[i] == 'r':
            curr[0] += 1
        elif s[i] == 'l':
            curr[0] -= 1
        mahan = max(mahan, abs(curr[0]))
    return mahan

def dir_cmb(s, k):
    r_indice = []
    l_indice = []
    for i in range(len(s)):
        if s[i] == 'r':
            r_indice += [i]
        elif s[i] == 'l':
            l_indice += [i]
    r_cmb = list(combinations(r_indice, k))
    l_cmb = list(combinations(l_indice, k))
    return l_cmb, r_cmb

def alt_mahan_dist(s, k):
    assert k >= 0
    if k == 0:
        return mahan_dist(s)
    else:
        l_cmb, r_cmb = dir_cmb(s, k)
        l_mahan = 0
        r_mahan = 0
        for rcmb in r_cmb:
            s_cp = copy.deepcopy(s)
            ls_cp = list(s_cp)
            for ind in rcmb:
                ls_cp[ind] = 'l'
            sls_cp = ''.join(ls_cp)
            l_mahan = max(l_mahan, mahan_dist(sls_cp))
        for lcmb in l_cmb:
            s_cp = copy.deepcopy(s)
            ls_cp = list(s_cp)
            for ind in lcmb:
                ls_cp[ind] = 'r'
            sls_cp = ''.join(ls_cp)
            r_mahan = max(r_mahan, mahan_dist(sls_cp))
        return max(l_mahan, r_mahan)

testcase1 = 'rlrlrrl'
print(alt_mahan_dist(testcase1, 1))
print(alt_mahan_dist(testcase1, 2))

testcase2 = 'lrlrlrrl'
testcase3 = 'lrrrrllll'
print(alt_mahan_dist(testcase2, 1))
print(alt_mahan_dist(testcase3, 1))

def convert_udrl(ud):
    str_ew = ""
    for i in range(len(ud)):
        if ud[i] == 'u':
            str_ew += 'r'
        elif ud[i] == 'd':
            str_ew += 'l'
    return str_ew

def extract_udrl(s):
    str_ud = ""
    str_rl = ""
    for i in range(len(s)):
        if s[i] == 'r' or s[i] == 'l':
            str_rl += s[i]
        elif s[i] == 'u' or s[i] == 'd':
            str_ud += s[i]
    return str_ud, str_rl

def td_mahat(s):
    mahat = 0
    curr = [0, 0]
    for i in range(len(s)):
        if s[i] == 'u':
            curr[1] += 1
        elif s[i] == 'd':
            curr[1] -= 1
        elif s[i] == 'r':
            curr[0] += 1
        elif s[i] == 'l':
            curr[0] -= 1
        mahat = max(mahat, abs(curr[0]) + abs(curr[1]))
    return mahat

def dir_cmb_dir(s, k, d):
    r_indice = []
    l_indice = []
    for i in range(len(s)):
        if s[i] == d:
            r_indice += [i]
        else:
            l_indice += [i]
    r_cmb = list(combinations(r_indice, k))
    l_cmb = list(combinations(l_indice, k))
    return l_cmb, r_cmb

def alt_mahan_dist_dir(s, k, d):
    assert k >= 0
    if k == 0:
        return td_mahat(s)
    else:
        r_mahan = 0
        for j in range(k+1):
            l_cmb, r_cmb = dir_cmb_dir(s, j, d)
            for lcmb in l_cmb:
                s_cp = copy.deepcopy(s)
                ls_cp = list(s_cp)
                for ind in lcmb:
                    ls_cp[ind] = d
                sls_cp = ''.join(ls_cp)
                r_mahan = max(r_mahan, td_mahat(sls_cp))
        return r_mahan

print('2d-testing')
print(alt_mahan_dist_dir('urld', 2, 'r'))
print(alt_mahan_dist_dir('urld', 2, 'l'))
print(alt_mahan_dist_dir('urld', 2, 'u'))
print(alt_mahan_dist_dir('urld', 2, 'd'))

testcase_4 = 'urlddddurrrld'
print(td_mahat(testcase_4))
print(alt_mahan_dist_dir(testcase_4, 2, 'r'))
print(alt_mahan_dist_dir(testcase_4, 2, 'l'))
print(alt_mahan_dist_dir(testcase_4, 2, 'u'))
print(alt_mahan_dist_dir(testcase_4, 2, 'd'))
