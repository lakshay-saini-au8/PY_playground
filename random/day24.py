# permutation

def permute(string, cur_index):
    if cur_index == len(string):
        print("".join(string))
    for i in range(cur_index, len(string)):
        string = [str for str in string]
        string[cur_index], string[i] = string[i], string[cur_index]
        permute(string, cur_index+1)


permute("abc", 0)
