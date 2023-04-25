import re

text = '''
$$
W  =  \left \|
$$
other chare
$$
\right \| .
$$
'''
with open('math.tex', 'r') as file:
    content = file.read()
    pattern = r'\$\$(?:[^$]|(?<=\\)\$)+\$\$'
    matches = re.findall(pattern, content)
    length = {}
    
    for i, match in enumerate(matches):
        length[i] = len(match)
    sorted_dict = dict(sorted(length.items(), key=lambda item: item[1]))
    for k, v in sorted_dict.items():
        print(matches[int(k)])
