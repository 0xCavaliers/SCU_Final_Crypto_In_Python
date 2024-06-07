def check_consistency(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = f1.read()
        data2 = f2.read()
    
    if data1 == data2:
        return "success"
    else:
        return "failure"
