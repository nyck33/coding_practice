"""
strs
t
result
["ba","na","n","a"]
"banana"
3
["app","ap","p","l","e","ple","pp"]
"apple"
2
["ba","an","nan","ban","n"]
"banana"
-1
-1 if t cannot be constructed from fragments in strs
"""
import copy

def connect_word_fragments(strs, target):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frags_d = {}
    for frag in strs:
        first_alpha = frag[0]
        if first_alpha in frags_d:
            frags_d[first_alpha].append(frag)
        else:
            frags_d[first_alpha] = [frag]

    # sort all frags_list by len, descending so longest first
    for alpha, frags_arr in frags_d.items():
        frags_arr.sort(key=lambda s: len(s), reverse=True)

    all_targets = []
    # construct word as list for easy popping of frags
    curr_target = []
    curr_frag = ""
    curr_frags_arr = []
    alpha_count = 0
    curr_alpha = target[alpha_count]
    prev_alpha = ""
    num_frags = float('inf')
    count = 0
    # iterate frags_d and try to construct target with least num frags
    while True:
        curr_alpha = target[alpha_count]
        if curr_alpha in frags_d:
            curr_frags_arr = frags_d[curr_alpha]
            curr_frag = curr_frags_arr[count]
            curr_target.append(curr_frag)
            curr_len = len(curr_frag)
            alpha_count += curr_len
            target_len = len(target)
            if alpha_count == target_len:
                all_targets.append(copy.deepcopy(curr_target))
                # delete all frags in curr_target from frags_d
                frags_d = delete_found_word(curr_target, frags_d)
                curr_target[:] = []
                alpha_count = 0
            elif alpha_count > target_len:
                # go back one since going from longest to shortest
                # but delete this last frag
                bad_frag = curr_target.pop(-1)
                frags_d = delete_bad_frag(bad_frag, frags_d)
                alpha_count -= len(bad_frag)
        else:
            if alpha_count==0:
                # first frag not in frags_d, this is break condition
                # as it keeps coming back to first and deleting frags and key
                # eventually gets here
                break
            elif 0 < alpha_count < len(target):
                # go back one frag and try another
                bad_frag = curr_target.pop(-1)
                frags_d = delete_bad_frag(bad_frag, frags_d)
                # rewind alpha count
                alpha_count -= len(bad_frag)
                # try next longest fragment
                #count += 1 dont' need since it's deleted from frags_d
            elif alpha_count==len(target):
                if curr_target==target:
                    all_targets.append(copy.deepcopy(curr_target))
                    # since we try the longest first
                    frags_d = delete_found_word(curr_target, frags_d)
                    curr_target[:] = []
                    alpha_count = 0
                else:
                    # len is same but not target
                    bad_frag = curr_target.pop(-1)
                    frags_d = delete_bad_frag(bad_frag, frags_d)
                    alpha_count -= len(bad_frag)
                    #count += 1

    if len(all_targets) == 0:
        print("can't make target")
        return -1

    short = float('inf')
    short_target = ""
    for target_arr in all_targets:
        if len(target_arr) < short:
            short = len(target_arr)
            short_target = target_arr

    print(f'target_arr: {target_arr}')
    return short

def delete_bad_frag(bad_frag, frags_d):
    """
    delete bad_frag and return frags_d
    if it's the only word remaining del key from frags_d and return
    """
    first_alpha = bad_frag[0]
    if first_alpha not in frags_d:
        return frags_d
    frags_arr = frags_d[first_alpha]
    new_frags_arr = []
    for frag in frags_arr:
        if frag is not bad_frag:
            new_frags_arr.append(frag)

    if len(new_frags_arr) == 0:
        del frags_d[first_alpha]
    else:
        new_frags_arr.sort(key=lambda s: len(s), reverse=True)
        frags_d[first_alpha] = new_frags_arr

    return frags_d

def delete_found_word(curr_target, frags_d):
    """
    found word so delete each frag in curr_target from frags_d
    """
    for frag in curr_target:
        alpha_key = frag[0]
        new_frags_arr = []
        curr_frags_arr = frags_d[alpha_key]
        for f in curr_frags_arr:
            if f is not frag:
                new_frags_arr.append(f)
        if len(new_frags_arr) <= 0:
            del frags_d[alpha_key]
        else:
            frags_d[alpha_key] = new_frags_arr

    return frags_d

if __name__=="__main__":
    strs = ["ba", "na", "n", "a"]
    t = "banana"
    num_frags = connect_word_fragments(strs, t)
    print(num_frags)
    strs = ["app", "ap", "p", "l", "e", "ple", "pp"]
    t = "apple"
    num_frags = connect_word_fragments(strs, t)
    print(num_frags)
    #2
    strs = ["ba", "an", "nan", "ban", "n"]
    t = "banana"
    num_frags = connect_word_fragments(strs, t)

    #-1

    print(num_frags)