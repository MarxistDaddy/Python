def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def count(n):
        if n > days:
           return
        print("Day", n)
        count(n + 1)

    count(1)
    print("Harvest time!")
