import itertools

def pict_table(*args):
    combinations = list(itertools.product(*args))
    headers = [f"Input{i+1}" for i in range(len(args))]
    rows = []
    for combination in combinations:
        rows.append(combination)
    return rows, headers
def get_combinations(rows):
    combinations = []
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            combinations.append((rows[i], rows[j]))
    return combinations
def check_combinations(testcase, combinations):
    """
    检查测试用例是否可删除
    """
    for comb in combinations:
        if comb in existing_combinations:
            return True
    for other_case in table:
        if other_case == testcase:
            continue
        for comb in combinations:
            if comb not in get_combinations(other_case):
                break
        else:
            return True
    return False

input1 = ['1', '2']
input2 = ['Q', 'R']
input3 = ['5', '6']

existing_combinations = []
deleted_indices = []

rows, headers = pict_table(input1, input2, input3)
print("\t".join(headers))
for row in rows:
    print("\t".join(str(val) for val in row))
table = []
for i in range(len(rows)):
    table.append(rows[i])

# 从最后一行开始向前遍历
for i in range(len(table) - 1, -1, -1):
    testcase = table[i]
    combinations = get_combinations(testcase)
    # 如果测试用例可删除，则记录删除的下标
    if check_combinations(testcase, combinations):
        deleted_indices.append(i)
    # 否则，将测试用例的两两组合值加入已有的组合值列表
    else:
        existing_combinations.extend(combinations)
table1 = []
# 根据删除的下标，从测试用例列表中删除测试用例
for i in deleted_indices:
    table1.append(table.pop(i))

# 反向输出
n = len(table1)
for j in range(len(table1)//2):
    table1[j],table1[n-j-1]=table1[n-j-1],table1[j]

# 输出结果
for testcase in table1:
    print(' '.join(testcase))