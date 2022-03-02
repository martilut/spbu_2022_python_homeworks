def head(file, strings=10):
    for i in range(strings):
        print(file.readline(), end="")


def tail(file, strings=10):
    lines = [line for line in file]
    lines.reverse()
    for i in range(strings):
        print(lines[i], end="")


def wc(file):
    wordCount = 0
    symbolCount = 0
    lines = [line for line in file]
    lineCount = len(lines)
    for line in lines:
        words = line.split(" ")
        if "\n" in words:
            words.remove("\n")
        wordCount += len(words)
        symbolCount += len(line) - 1
    print(str(lineCount) + " " + str(wordCount) + " " + str(symbolCount))


def nl(file, are_empty_lines_numbered=False, increment=1, separator=" ", start_number=1):
    current_number = start_number
    for line in file:
        if line == "\n" and not are_empty_lines_numbered:
            current_number += increment
            print("\n", end="")
            continue
        print(str(current_number) + separator + line, end="")
        current_number += increment
