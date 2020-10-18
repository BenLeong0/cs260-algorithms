# U = {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
#      'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'
# }

S = [{'a1', 'a2', 'a3', 'a4', 'a5'},
     {'b1', 'b2', 'b3', 'b4', 'b5'},
     {'a1', 'b1'},
     {'a2', 'a3', 'b2', 'b3'},
     {'a4', 'a5', 'a6', 'a7', 'b4', 'b5', 'b6', 'b7'},
]


def greedy_set_cover(S):
    U = {ele for subset in S for ele in subset}
    I = []
    V = U.copy()
    while V:
        def sort_sets(subset):
            v_int = V.intersection(subset)
            return len(v_int)
        S.sort(key=sort_sets, reverse=True)
        I.append(S[0])
        V -= S[0]
    return I


print(greedy_set_cover(S))
