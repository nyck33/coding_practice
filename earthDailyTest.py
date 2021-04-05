'''
Inputs

- Original list of strings

- List of strings to be added

- List of strings to be removed

Return

- List shall only contain unique values

- List shall be ordered as follows

--- Most character count to least character count

--- In the event of a tie, reverse alphabetical

Other Notes

- You can use any programming language you like

- The function you submit shall be runnable

For example:

Original List = ['one', 'two', 'three',]

Add List = ['one', 'two', 'five', 'six]

Delete List = ['two', 'five']

Result List = ['three', 'six', 'one']*

source: https://www.geeksforgeeks.org/python-program-for-merge-sort/
'''
def main(arr, addarr, delarr):
    '''
    Assumes no duplicates in arr and addarr before concatenation
    :param arr:
    :param addarr:
    :param delarr:
    :return:
    '''
    # get intersection of arr and addarr
    add_items = set(addarr)
    total_arr = [x for x in arr if x in add_items]
    # unique values to arr
    only_arr = list(set(arr) - set(addarr))
    #unique values to add_arr
    only_addarr = list(set(addarr) - set(arr))
    #concatenate
    new_arr = total_arr + only_arr + only_addarr
    # remove in delarr
    clean_arr = [x for x in new_arr if x not in delarr]

    n= len(clean_arr)
    # call merge sort nlogn
    merge_sort(clean_arr,0,n-1)

    return clean_arr

def merge_rev_alpha(arr, l, m, r):
    new_arr = [0] * r
    # len of left subarray
    len_left = m - l + 1
    len_right = r - m

    #make two temp arrs
    left_arr = [0] * len_left
    right_arr = [0] * len_right

    #copy strings to temp arrays so don't mutate original arr
    for i in range(0, len_left):
        left_arr[i] = arr[l+i]

    for j in range(0, len_right):
        right_arr[j] = arr[m+1+j]

    #merge temp arrs back into arr[l...r]
    i = 0 #start idx left subarr
    j = 0 # start idx right subarr
    k = l # start idx merged subarray in arr

    while i < len_left and j < len_right:
        if len(left_arr[i]) > len(right_arr[j]):
            arr[k] = left_arr[i]
            i+=1
        elif len(left_arr[i]) == len(right_arr[j]):
            #compare alpha
            left_str = left_arr[i]
            right_str = right_arr[j]
            higher_alpha = sorted([left_str, right_str], reverse=True)[0]
            arr[k] = higher_alpha
            if higher_alpha == left_str:
                i +=1
            else:
                j +=1
        elif len(left_arr[i]) < len(right_arr[j]):
            arr[k] = right_arr[j]
            j+=1
        k += 1

    # copy remaining elements of left
    while i < len_left:
        arr[k] = left_arr[i]
        i+=1
        k+=1
    # same for right
    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l+(r-1)) // 2

        # sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge_rev_alpha(arr, l, m, r)


if __name__=="__main__":
    original= ['one', 'two', 'three']

    add_arr = ['one', 'two', 'five', 'six']

    delete_arr = ['two', 'five']

    #Result = ['three', 'six', 'one']

    print(main(original, add_arr, delete_arr))