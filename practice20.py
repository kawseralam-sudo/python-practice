def analyze_numbers(numbers):
    total_num=0
    even_count=0
    odd_count=0
    total_sum=0
    average=0
    sec_max=numbers[0]
    max_num=numbers[0]
    min_num=numbers[0]
    
    for number in numbers:
        total_num+=1
        if number%2==0:
            even_count+=1
        else:
            odd_count+=1
        total_sum+=number

        if number > max_num:
            sec_max=max_num
            max_num=number

        if number < min_num:
            min_num=number
        if number < sec_max:
            sec_max=number
    
    average = total_sum / total_num
    
    return total_num,even_count,odd_count,total_sum,max_num,min_num,sec_max,average

  
numbers = [10, 25, 30, 15, 40, 7, 50]
total_num,even_count,odd_count,total_sum,max_num,min_num,sec_max,average=analyze_numbers(numbers)

print("total count:",total_num)
print("Total even count:",even_count)
print("total odd count:",odd_count)
print("total sum:",total_sum)
print("maxium number :",max_num)
print("minimum number:",min_num)
print(sec_max)
print(round(average,2))