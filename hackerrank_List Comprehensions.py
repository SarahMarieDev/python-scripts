def list_cmp(x_list, y_list, z_list, n):
    results = [[i, j, k] for i in x_list for j in y_list for k in z_list if (i + j +k) != n]
    print(results)
    

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x_list = [x for x in range(x + 1)]
    y_list = [y for y in range(y + 1)]
    z_list = [z for z in range(z + 1)]
    
    list_cmp(x_list, y_list, z_list, n)