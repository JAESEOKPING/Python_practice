# word_length.py

ani_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

longest = max(ani_list, key=len)
shortest = min(ani_list,key=len)


print(f'단어 목록: {ani_list}')
print(f'가장 긴 단어: {longest} ({len(longest)}글자)')
print(f'가장 짧은 단어: {shortest} ({len(shortest)}글자)')