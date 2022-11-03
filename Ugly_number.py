def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        if(num==1):
            return 1
        else:
            return 0
a=int(input())
if(is_ugly(a)):
    print("Ugly Number")
else:
    print("Not Ugly Number")