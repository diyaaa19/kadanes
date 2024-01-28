arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum=0
current_sum=0
start_index=-1
end_index=-1
n=len(arr)
for i in range (n):
    current_sum = max(arr[i], current_sum + arr[i])
    if current_sum<0:
        current_sum=0
        start_index=i
        
    if current_sum>max_sum:
        max_sum=i
        end_index=i

print("Subarray = ",arr[start_index+1:end_index+1])
print(max_sum)