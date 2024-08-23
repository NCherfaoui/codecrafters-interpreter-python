import sys
error_code = 0



def main():
    global error_code
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    # if file_contents:
    #     raise NotImplementedError("Scanner not implemented")
    # else:
    #     print("EOF  null") # Placeholder, remove this line when implementing the scanner

    for c in file_contents:
        match c:
            case "(":
                print("LEFT_PAREN ( null")
            case ")":
                print("RIGHT_PAREN ) null")
            case "{":
                print("LEFT_BRACE { null")
            case "}":
                print("RIGHT_BRACE } null")
            case ",":
                print("COMMA , null")
            case ".":
                print("DOT . null")
            case "-":
                print("MINUS - null")
            case "+":
                print("PLUS + null")
            case ";":
                print("SEMICOLON ; null")
            case "*":
                print("STAR * null")
            case _:
                error_code = 65
                line_number = (file_contents.count("\n", 0, file_contents.find(c)))+1
                print(
                    f"[line {line_number}] Error: Unexpected character: {c}",
                    file=sys.stderr,
                )
                exit(error_code)
    print("EOF  null")
if __name__ == "__main__":
    main()
