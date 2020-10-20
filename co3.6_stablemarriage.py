W = [
    {'pref': [0,2,1,3], 'engaged': False},
    {'pref': [2,3,0,1], 'engaged': False},
    {'pref': [3,1,2,0], 'engaged': False},
    {'pref': [2,1,0,3], 'engaged': False},
]

M = [
    {'pref': [1,0,2,3], 'engaged': False},
    {'pref': [3,0,1,2], 'engaged': False},
    {'pref': [0,2,1,3], 'engaged': False},
    {'pref': [1,2,0,3], 'engaged': False},
]

while list((x for x in M if not x['engaged'])):
    m = list((x for x in M if not x['engaged']))[0]
    m_index = M.index(m)
    w_index = m['pref'].pop(0)
    w = W[w_index]
    if not w['engaged']:
        m['match'], m['engaged'] = w_index, True
        w['match'], w['engaged'] = m_index, True
    elif w['pref'].index(m_index) < w['pref'].index(w['match']):
        M[w['match']]['engaged'] = False
        del M[w['match']]['match']      # Removes old match, not necessary
        m['match'], m['engaged'] = w_index, True
        w['match'] = m_index

print(M)

for i in range(len(M)):
    print(i, M[i]['match'])
