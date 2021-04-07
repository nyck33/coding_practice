def is_ordered(arr):
    '''
    Use Python sorted method that is not in place.
    Could also make a copy and do copy.sort() and compare to arr
    I also just learned about Python's all method
    '''
    new_list = sorted(arr)
    if new_list == arr:
        return True
    return False

def is_ordered_two(arr):
    '''
    use dp if arr(i) > arr(i-1): T(i) = T(i-1) + 1
    else: T(i) = 1
    T(1) = 1 base case
    '''
    T = [0 for x in range(len(arr))]
    T[0] = 1 # base case
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            T[i] = T[i-1] + 1
        else:
            return False #not looking for longest increasing subsequence

    return True


def is_ordered_three(arr):
    '''
    check for min in decreasing size subarrays from 1 to n-1
    I was going to do a merge sort but Python Tim Sort is faster and this is
    kind of a fun way to do it
    '''
    n = len(arr)
    count = 0
    while True:
        if count >= n:
            break
        curr_min = arr[count]
        curr_sub = arr[count:]
        if curr_min != min(curr_sub):
            return False
        count += 1

    return True

import copy
def make_q_vars(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    n = len(lines)
    # list of q_nums
    q_nums = []
    # list of questions
    questions = []
    # list of lists of answers, each sublist for each questions
    answers = []
    curr_answers = []
    # list of lists for above answers
    ans_nums = []
    curr_ans_nums=[]
    i = 0
    done = False
    while True:
        if done:
            answers.append(copy.deepcopy(curr_answers))
            ans_nums.append(copy.deepcopy(curr_ans_nums))
            break
        # split line at white space
        curr_line = lines[i].split()
        if '?' in curr_line[-1]:
            q_num = curr_line[0].split('.')[0]
            q_nums.append(q_num)
            q = ' '.join(curr_line[1:])
            questions.append(q)

            j = i + 1
            #for j in range(i+1, len(lines)):
            while True:
                if j >= len(lines):
                    done = True
                    i=j
                    break
                ans_line = lines[j].split()
                if len(ans_line) == 0: # blank line
                    j += 1
                    continue
                if '?' in ans_line[-1]:
                    i = j
                    answers.append(copy.deepcopy(curr_answers))
                    ans_nums.append(copy.deepcopy(curr_ans_nums))
                    curr_answers[:] = []
                    curr_ans_nums[:] = []
                    break # it's a question
                else:
                    ans_num = ans_line[0].split('.')[0]
                    curr_ans_nums.append(ans_num)
                    curr_ans = ' '.join(ans_line[1:])
                    curr_answers.append(curr_ans)
                j += 1

    return questions, q_nums, answers, ans_nums




def main(file_path):
    '''
    Calls make_q_vars and holds required lists in variables
    :param file_path:
    :return:
    '''
    questions, q_nums, answers, ans_nums = make_q_vars(file_path)
    print(questions, q_nums, answers, ans_nums)


import sys
import random
if __name__ =="__main__":

    for i in range(100):
        random_arr = random.sample(range(-100,100),50)
        ans = is_ordered(random_arr)
        ans_two = is_ordered_two(random_arr)
        ans_three = is_ordered_three(random_arr)

        assert ans == ans_two == ans_three, f'1:{ans}, 2:{ans_two}, 3:{ans_three}'
        print(f'{ans}, {ans_two},{ans_three}')

    file_path = sys.argv[1]

    main(file_path)
