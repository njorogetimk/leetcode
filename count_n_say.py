
class Solution:
    def countAndSay(self, n: int) -> str:
        for i in range(n):
            
            # First round
            if i == 0:
                say = '1'
            else:
                new = []
                prev = ''
                for char in say:
                    if prev == '':
                        new.append(char)
                        prev = char
                    else:
                        if prev == char:
                            t = new.pop()
                            new.append(t+char)
                        else:
                            new.append(char)
                            prev = char
                
                say = ''.join([str(len(nums)) + nums[0] for nums in new])

        return say