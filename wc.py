import sys

def count_lines(words):
    return len(words.splitlines())

def count_words(words):
    return len(words.split())

def count_chars(words):
    return len(words)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: wc [-lwc] [file ...]")
        sys.exit(1)
    
    flags = []
    files = []
    for arg in args:
        if arg.startswith('-'):
            flags.extend(arg[1:])
        else:
            files.append(arg)
    
    if not files:
        text = sys.stdin.read()
        files = [None]

    for filename in files:
        if filename:
            with open(filename, 'r') as f:
                text = f.read()
        
        lines = count_lines(text)
        words = count_words(text)
        chars = count_chars(text)
        
        if 'l' in flags:
            print(lines, end=' ')
        if 'w' in flags:
            print(words, end=' ')
        if 'c' in flags:
            print(chars, end=' ')
        if not flags:
            print(lines, words, chars, end=' ')
        if filename:
            print(filename)

if __name__ == "__main__":
    main()
