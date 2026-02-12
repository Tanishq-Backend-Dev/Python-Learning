def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            return mid
        else:
            if list[mid]< n:
                l = mid
            else:
                u = mid    
        return "Not Found"

list = [4,7,8,12,45,99]
n = 999
print(search(list,n))
