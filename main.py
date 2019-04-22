if __name__ == '__main__':
    file = open('report.txt')
    lines = file.readlines()
    str = ''
    str = str.join(lines)

    import jieba
    x1 = jieba.cut(str)
    x2 = [item for item in x1 if len(item) > 1]

    import collections
    x3 = collections.Counter(x2)
    y = x3.most_common(20)
    print(y)