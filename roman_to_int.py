

class Solution:
    """ Do the convertion"""

    def romanToInt(self, roman: str):
        """Accept the roman numeral to convert"""
        
        if len(roman) > 15:
            return 'Invalid roman numeral length'
        
        find_quotation = True if roman.find('"') >= 0 else False

        roman = roman.split('"')[1] if find_quotation else roman


        roman = roman.upper()  # Convert the numeral to uppercase

        # The table to use for conversion
        c_table = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        indiv_rom_vals = [
        ]  # Used to store individual roman values i.e ['L', 'I', 'V'] from 'LIV'
        for rom in roman:
            # Check if a valid roman numeral otherwise store the split
            if rom not in 'IVXLCDM':
                return f'{rom} is not a roman numeral'
            indiv_rom_vals.append(rom)

        final_split = []  # Store the final split combination
        temp = ''
        counter = 0

        for value in indiv_rom_vals:
            if counter == 0:
                # Store the first value to temp
                temp = value
                counter += 1
            else:
                # Join the next two numerals to check if they appear in table
                # If not they are seperate values
                check_in = ''.join([temp, value])
                if check_in in c_table:
                    temp = check_in
                else:
                    final_split.append(temp)
                    temp = value
        temp = [temp]
        final_split.extend(temp)

        solv = []
        counter = 0
        for value in final_split:
            if counter > 0:
                # Check for wrong formatting of numerals
                if c_table[value] > solv[counter - 1]:
                    return 'Wrong Roman Numeral Format'
                # Add the value of the roman numeral to the solv list
                solv.append(c_table[value])
                counter += 1
            else:
                # Store the first value to solv list
                solv.append(c_table[value])
                counter += 1

        # Get the sum of the roman numeral input
        sol = sum(solv)
        return sol


def main():
    """The main function"""
    
    roman = input('Enter the roman numeral: ')
    converter = Solution()
    solved = converter.romanToInt(roman)
    print(solved)


if __name__ == "__main__":
    main()
