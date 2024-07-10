import os

# print(os.getcwd())
# number = input("Enter a number: ")
# file_name = input("Enter the file name: ")
number = ""
file_name = ""

safe_file_name = file_name.replace(" ", "")

current_directory = os.getcwd()

directory_name = f"{number}_{safe_file_name}"
directory_path = os.path.join(current_directory, directory_name)

os.makedirs(directory_path, exist_ok=True)

question_content = r"""

"""

java_content = r"""

"""

python_content = r"""

"""

cpp_content = r"""

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


# ##### backup
# import os

# # print(os.getcwd())
# # number = input("Enter a number: ")
# # file_name = input("Enter the file name: ")
# number = "58"
# file_name = "Length of Last Word"

# safe_file_name = file_name.replace(" ", "")

# current_directory = os.getcwd()

# directory_name = f"{number}_{safe_file_name}"
# directory_path = os.path.join(current_directory, directory_name)

# os.makedirs(directory_path, exist_ok=True)

# question_content = r"""

# """

# java_content = r"""

# """

# python_content = r"""

# """

# cpp_content = """

# """

# content_dict = {
#     "cpp": cpp_content,
#     "py": python_content,
#     "java": java_content,
# }

# for ext, content in content_dict.items():
#     file_path = os.path.join(directory_path, f"{safe_file_name}.{ext}")
#     with open(file_path, "w") as file:
#         file.write(content)

# txt_file_path = os.path.join(directory_path, f"Question_{safe_file_name}.txt")
# with open(txt_file_path, "w") as file:
#     file.write(question_content)

# print(
#     f"Directory '{directory_name}' created with files: {', '.join([f'{safe_file_name}.{ext}' for ext in content_dict.keys()])}, Question_{safe_file_name}.txt"
# )
