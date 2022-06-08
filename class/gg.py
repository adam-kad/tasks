price_list = [1, 2, 4]

def global_price_sum(paka):
        sum = 0
        for gpl in paka:
            sum = sum + gpl
        return sum

print(global_price_sum(price_list))