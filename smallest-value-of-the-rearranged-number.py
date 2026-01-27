class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        is_negative = num < 0
        s_num = str(abs(num))
        digits = list(s_num)

        if is_negative:
            # For negative numbers, to get the smallest value (most negative),
            # we need the largest absolute value. This means arranging digits
            # in descending order.
            digits.sort(reverse=True)
            result_str = "".join(digits)
            result = int(result_str)
            return -result
        else:
            # For positive numbers, to get the smallest value,
            # we arrange digits in ascending order.
            # A special handling is required for leading zeros.
            digits.sort()
            
            # If the smallest digit is '0' and it's at the beginning,
            # we need to find the first non-zero digit and swap it
            # with the leading '0' to avoid a leading zero.
            if digits[0] == '0':
                first_non_zero_idx = -1
                for i in range(len(digits)):
                    if digits[i] != '0':
                        first_non_zero_idx = i
                        break
                
                # Swap the leading '0' with the first non-zero digit
                digits[0], digits[first_non_zero_idx] = digits[first_non_zero_idx], digits[0]
            
            result_str = "".join(digits)
            result = int(result_str)
            return result