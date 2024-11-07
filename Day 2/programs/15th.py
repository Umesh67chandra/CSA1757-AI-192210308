import math

def entropy(data):
    total = len(data)
    label_counts = {}
    for item in data:
        label = item[-1]
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1

    entropy_value = 0
    for label in label_counts:
        prob = label_counts[label] / total
        entropy_value -= prob * math.log2(prob)
    return entropy_value

def split_data(data, feature_index, value):
    left_split = [item for item in data if item[feature_index] == value]
    right_split = [item for item in data if item[feature_index] != value]
    return left_split, right_split

def information_gain(data, feature_index):
    total_entropy = entropy(data)
    feature_values = set(item[feature_index] for item in data)
    weighted_entropy = 0
    for value in feature_values:
        left, right = split_data(data, feature_index, value)
        left_weight = len(left) / len(data)
        right_weight = len(right) / len(data)
        weighted_entropy += left_weight * entropy(left) + right_weight * entropy(right)
    return total_entropy - weighted_entropy

def best_split(data):
    best_gain = -1
    best_feature = -1
    for feature_index in range(len(data[0]) - 1):
        gain = information_gain(data, feature_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    return best_feature

def build_tree(data):
    if len(set(item[-1] for item in data)) == 1:
        return data[0][-1]
    
    if len(data[0]) == 1:
        return data[0][-1]

    best_feature = best_split(data)
    tree = {best_feature: {}}

    feature_values = set(item[best_feature] for item in data)
    for value in feature_values:
        left, right = split_data(data, best_feature, value)
        if not left or not right:
            majority_class = max(set([item[-1] for item in data]), key=[item[-1] for item in data].count)
            tree[best_feature][value] = majority_class
        else:
            tree[best_feature][value] = build_tree(left) if left else build_tree(right)
    return tree

data = [
    [1, 'Sunny', 'Hot', 'High', 'Weak', 'No'],
    [2, 'Sunny', 'Hot', 'High', 'Strong', 'No'],
    [3, 'Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    [4, 'Rain', 'Mild', 'High', 'Weak', 'Yes'],
    [5, 'Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    [6, 'Rain', 'Cool', 'Normal', 'Strong', 'No'],
    [7, 'Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    [8, 'Sunny', 'Mild', 'High', 'Weak', 'No'],
    [9, 'Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    [10, 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
]

tree = build_tree(data)
print("Decision Tree:", tree)
