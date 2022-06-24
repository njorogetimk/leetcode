
class Solution:
    def get_power(self, lo: int, hi: int, k: int) -> int:
        # Loop through lo to hi
        # for each iterarion get the power of i
        # Store the power in a dictionary
        # Loop throught the dictionary while sorting them in ascending order
        # return the kth+1 int value of the dictionary
        
        def power_of(n):
            if n == 1:
                return 0
            
            ans = n // 2 if n%2 == 0 else ((n * 3)+1)

            power = 1 + power_of(ans)

            return power
        
        def partition(arr, start=0, end=None):
    
            if end == None:
                end = len(arr) -1
            
            l, r = start, end-1

            while l <= r:
                if arr[l][1] <= arr[end][1]:
                    l += 1
                
                # elif arr[l][1] == arr[end][1]:
                #     if arr[l][0] > arr[r][0]:
                #         arr[l], arr[r] = arr[r], arr[l]

                #     l += 1
                
                elif arr[r][1] > arr[end][1]:
                    r -= 1
                
                else:
                    arr[l], arr[r] = arr[r], arr[l]

            if arr[l][1] > arr[end][1]:
                arr[l], arr[end] = arr[end], arr[l]
                return l
            
            # print(arr[l][0], arr[l][1], arr[end][0], arr[end][1])

            return end
        
        def final_sort(arr):
            for i in range(1, len(arr)):
                if arr[i][1] == arr[i-1][1]:
                    if arr[i][0] < arr[i-1][0]:
                        arr[i], arr[i-1] = arr[i-1], arr[i]
            
            

    

        
        def quick_sort(arr, start = 0, end = None):
            """Returns a list of sorted integers"""

            if end is None:
                # arr = arr[:]
                end = len(arr) -1
            
            if start < end:
                pivot = partition(arr, start, end)
                quick_sort(arr, start, pivot-1)
                quick_sort(arr, pivot+1, end)
            
            final_sort(arr)
            
            return arr
        
        powers = {}
        
        for i in range (lo, hi+1):
            power = power_of(i)
            powers[i] = (i, power)
        # print(list(powers.values()))
        # powers_l = list(powers.values())
        powers_l = quick_sort(list(powers.values()))
        # print(powers_l)
        # return quick_sort(list(powers.values()))[k-1][0]
        return powers_l[k-1][0]


        

