def merge_dicts(dict1, dict2):

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:

            merged_dict[key] += value
        else:

            merged_dict[key] = value

    return merged_dict

dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {2: 30, 3: 40, 4: 50}

merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)

# this task using dict, it can help us effectively manage and operate data.

# chat history with ai
#     You
#     are
#     given
#     two
#     dictionaries, dict1 and dict2, each
#     containing
#     integer
#     keys and values.Write
#     a
#     Python
#     function
#     merge_dicts(dict1, dict2)
#     that
#     merges
#     the
#     two
#     dictionaries, such
#     that if there
#     are
#     common
#     keys in both
#     dictionaries,
#     the
#     corresponding
#     values
#     are
#     summed
#     up.The
#     function
#     should
#     return the
#     merged
#     dictionary as the
#     output.
#     # Sample Input
#     dict1 = {1: 10, 2: 20, 3: 30}
#     dict2 = {2: 30, 3: 40, 4: 50}
#     # Output
#     # Merged dictionary: {1: 10, 2: 50, 3: 70, 4: 50}

# def merge_dicts(dict1, dict2):
#     # 创建一个新的字典来存储合并结果
#     merged_dict = dict1.copy()
#
#     # 遍历 dict2 中的每个键值对
#     for key, value in dict2.items():
#         if key in merged_dict:
#             # 如果键在 dict1 中存在，则将值相加
#             merged_dict[key] += value
#         else:
#             # 如果键在 dict1 中不存在，则直接添加键值对
#             merged_dict[key] = value
#
#     return merged_dict
#
#
# # 示例输入
# dict1 = {1: 10, 2: 20, 3: 30}
# dict2 = {2: 30, 3: 40, 4: 50}
#
# # 调用函数并打印结果
# merged_dict = merge_dicts(dict1, dict2)
# print("Merged dictionary:", merged_dict)
