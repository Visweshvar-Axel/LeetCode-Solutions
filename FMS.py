import os

# print(os.getcwd())
# number = input("Enter a number: ")
# file_name = input("Enter the file name: ")
number = "58"
file_name = "Length of Last Word"

safe_file_name = file_name.replace(" ", "")

current_directory = os.getcwd()

directory_name = f"{number}_{safe_file_name}"
directory_path = os.path.join(current_directory, directory_name)

os.makedirs(directory_path, exist_ok=True)

question_content = r"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

java_content = r"""
class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split("\\s+");
        return arr[arr.length-1].length();
    }
}
"""

python_content = r"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        print(len(s[-1]))
        return len(s[-1])
        # count = 0
        # for i in range(0,len(s)):
        #     if not s[-i] == ' ':
        #         count += 1
        # return count
"""

cpp_content = """

"""

content_dict = {
    "cpp": cpp_content,
    "py": python_content,
    "java": java_content,
}

for ext, content in content_dict.items():
    file_path = os.path.join(directory_path, f"{safe_file_name}.{ext}")
    with open(file_path, "w") as file:
        file.write(content)

txt_file_path = os.path.join(directory_path, f"Question_{safe_file_name}.txt")
with open(txt_file_path, "w") as file:
    file.write(question_content)

print(
    f"Directory '{directory_name}' created with files: {', '.join([f'{safe_file_name}.{ext}' for ext in content_dict.keys()])}, Question_{safe_file_name}.txt"
)
