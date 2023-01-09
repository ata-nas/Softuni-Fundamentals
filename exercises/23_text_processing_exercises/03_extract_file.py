file_to_parse = input().split(sep='.')

file_name = file_to_parse[0].split(sep='\\')[-1]
file_extension = file_to_parse[1]

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
