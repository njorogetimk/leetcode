class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {}
        slider = []

        counter = 0
        for char in s:
            if counter == 0:
                slider.append(char)
                counter += 1
                continue
            
            # print(char, slider)
            if char in slider:
                substrings[''.join(slider)] = len(slider)

                if char == slider[0]:
                    slider.pop(0)
                    slider.append(char)
                else:
                    slider = slider[slider.index(char)+1:]
                    slider.append(char)
                # slider.append(char)
                # slider = []
                # slider.append(char)
            else:
                slider.append(char)
            
        
        substrings[''.join(slider)] = len(slider)

        return max(list(substrings.values()))