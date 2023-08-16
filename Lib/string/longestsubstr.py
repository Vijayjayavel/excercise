"""Write a Python program to find the longest common sub-string from two given strings"""

def lcsubstr(str1, str2):
   ans=0
   for i in range(len(str1)):
      for j in range(len(str2)):
         k=0
         while ((i + k) < len(str1) and (j + k) < len(str2)
				and str1[i + k] == str2[j + k]):
            k = k + 1;
            ans = max(ans, k);
   return ans;
print(lcsubstr('abcdwaxyz','xyzabcd'))

def longestSubString(str1, str2):
    longestString = ""
    maxLength = 0
    for i in range(0, len(str1)):
        if str1[i] in str2:
            for j in range(i + 1, len(str1)):
                if str1[i:j] in str2:
                    if(len(str1[i:j]) > maxLength):
                        maxLength = len(str1[i:j])
                        longestString =  str1[i:j]
    return longestString
print(longestSubString('abcdwaxyzagrgs','xyzabcdrgwedstyb56b5'))