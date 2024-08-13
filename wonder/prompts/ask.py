import sys


def ask_options(question: str, answers: list, chunk_size: int = 5, allow_quit: bool = False) -> int:
    chunked = True if len(answers) > chunk_size else False

    chunk_list = list()

    if chunked:
        for i in range(0, len(answers), chunk_size):
            chunk_list.append(answers[i:i+chunk_size])

        if "debug" in sys.argv:
            print(chunk_list)
    else:
        chunk_list = answers

    current_chunk = 0

    while True:
        print(question)
        for index, chunk in enumerate(chunk_list):
            num = 1
            num = num + (index * chunk_size)
            for answer in chunk:
                if current_chunk != index:
                    continue
                print("{}. {}".format(num, answer))
                num += 1
        if chunked:
            quit_msg = "or `quit`" if allow_quit else ""
            print("Answer with number or `more` {}".format(quit_msg))
        prompt_answer = input(">> ")

        if prompt_answer == "more":
            if current_chunk == len(chunk_list) - 1:
                current_chunk = 0
            else:
                current_chunk += 1
        elif prompt_answer == "quit" and allow_quit:
            return 0
        else:
            try:
                prompt_answer = int(prompt_answer)
                if 1 <= prompt_answer <= len(answers):
                    return prompt_answer
                else:
                    print("ERROR: Please pick number between 1 - {}".format(len(answers)))
                    wait_prompt()
            except ValueError:
                print("ERROR: Please pick a proper number between 1 - {}".format(len(answers)))
                wait_prompt()


def wait_prompt():
    input("- Click Enter to continue -")
