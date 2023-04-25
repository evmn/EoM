import re

'''
$$
( x , y )  \leq   F ( x) G ( y)
$$
other contents, shouldn't be matched
$$
r t - s  ^ {2}  =  \phi ( p , q )
$$
'''
def match_math_equations(input_file):
    with open(input_file, 'r') as file:
        content = file.read()
        pattern = r'\$\$(?:[^$]|(?<=\\)\$)+\$\$'
        matches = re.findall(pattern, content)

        return matches

def main():
    input_file = 'entries.txt'
    matches = match_math_equations(input_file)
    
    match_length = {}

    for i, match in enumerate(matches):
        match_length[i] = len(match)
    sorted_match = dict(sorted(match_length.items(), key=lambda item: item[1]))
    for k, v in sorted_match.items():
        print(matches[int(k)])
    total_match = len(matches)
    print(f"There are {total_match} matches!")

if __name__ == '__main__':
    main()
