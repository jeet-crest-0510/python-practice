class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
        l = s.split()
        while " " in l:
            l.remove(" ")
        l1 = l[::-1]
        s = " ".join(l1)
        return s


#{ 
 # Driver Code Starts
class Main:
    if __name__ == "__main__":
        t = int(input())  # Read the number of test cases

        for _ in range(t):
            s = input().strip()  # Read the input string

            # Remove surrounding quotes from the string
            str_ = s[1:-1]

            obj = Solution()  # Create an object of the Solution class
            ans = obj.reverseWords(str_)  # Reverse the words in the string

            # Print the result with surrounding quotes
            print(f'"{ans}"')