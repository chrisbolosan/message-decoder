
def decode(file_path):
    with open(file_path, 'r') as file:
        txt_file = [line.strip() for line in file if line.strip()]
    sorted_file = sorted((t for t in map(str.split, txt_file) if t), key=lambda t: int(t[0]))

    output = []

    count = i = 1

    while i <= len(sorted_file):
        output.append(sorted_file[i - 1][1])
        count += 1
        i += count

    return ' '.join(output)

decoded_message = decode("./coding_qual_input.txt")
print(decoded_message)



