def find_substring_indexes(s, sub):
    indexes = []
    for i in range(len(s) - len(sub) + 1):
        if s[i : i + len(sub)] == sub:
            indexes.append(i)
    return indexes


def filter_indexes(s, sub, indexes):
    result = []
    for i in indexes:
        if i + len(sub) <= len(s):
            if s[i : i + len(sub)] == sub:
                result.append(i)
    return result


file = open("D:/repos/MoraXtreme8_CodeXplorers/Competition/help.txt", "r")
t = int(file.readline())

for i in range(t):
    l, p, q = map(int, file.readline().split())
    code = file.readline()

    if code[0] == code[1] and q < p:
        val = p + q

    val = 2 * p
    current = code[:2]
    remaining = code[2:]

    while len(current) < l:
        sub_len = 2
        if len(remaining) >= sub_len:
            indexes = find_substring_indexes(current, remaining[:sub_len])
            # print(indexes)
            if len(indexes):
                sub_len += 1
                if len(remaining) >= sub_len:
                    while len(remaining) >= sub_len:
                        sub = remaining[:sub_len]
                        # print(sub)
                        indexes = filter_indexes(current, sub, indexes)
                        # print(indexes)
                        # indexes = find_substring_indexes(current, sub)
                        if len(indexes):
                            sub_len += 1
                        else:
                            current += sub[:-1]
                            remaining = remaining[sub_len - 1 :]
                            val += min(q, (sub_len - 1) * p)
                            break
                    else:
                        current += sub
                        remaining = remaining[sub_len - 1 :]
                        val += min(q, (sub_len - 1) * p)
                else:
                    current += remaining[: sub_len - 1]
                    remaining = remaining[sub_len - 1 :]
                    val += min(q, (sub_len - 1) * p)
            else:
                current += remaining[:1]
                remaining = remaining[1:]
                val += p
        else:
            current += remaining
            remaining = ""
            val += p

        # print(current, remaining, val)

    print(val)
