import itertools

test_cases = int(input())


def get_substrings(s):
    substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    return substrings


for test in range(test_cases):
    second_line = input()
    l, p, q = [int(x) for x in second_line.split()]
    codeword = input()
    time = 0
    if codeword[0] == codeword[1] and q < p:
        time = p + q

    time = p * 2

    subsets = []
    # add the subsets of first two characters
    subsets.append(codeword[:2])
    subsets.append(codeword[0])
    subsets.append(codeword[1])
    subsets = set(subsets)
    intial = codeword[:2]
    final = codeword[2:]
    i = 2
    while len(final) > 0:
        print("subsets: ", subsets)
        substring_to_add = ""

        for j in range(1, len(final) + 1):
            substring = final[:j]
            print("substring: ", substring)
            if substring in subsets:
                substring_to_add = substring
                print("substring to add: ", substring_to_add)
            else:
                break

        sub_len = len(substring_to_add)
        if substring_to_add == "":
            time += p
            print("time added1: ", p)
            i += 1
            intial = intial + final[0]
            final = final[1:]

        elif len(substring_to_add) == 1:
            i += 1
            intial = intial + final[0]
            final = final[1:]
            time += min(q, (sub_len) * p)

        else:
            time += min(q, (sub_len) * p)
            i += len(substring_to_add)
            intial = intial + final[: len(substring_to_add)]
            final = final[len(substring_to_add) :]

            print("time added3: ", q)

        # add subsets of initial to subsets
        print("initial updates: ", intial)
        subsets = subsets.union(set(get_substrings(intial)))

    print(time)
