def mathematics(number_list):
    return sum(number_list)


if __name__ == "__main__":
    number_list = []
    
    for _ in range(int(input())):
        number = int(input())
        
        number_list.append(number)
        
    print(mathematics(number_list=number_list))