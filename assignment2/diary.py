import traceback

# Task 1: Diary

with open('./diary.txt', 'a') as file:
    try:
        #get the input from the user
        first_input = input('What happened today? ')
        #while loop to keep asking the user for input until they type 'done for now'
        while first_input != 'done for now':
            file.write(first_input + '\n')
            first_input = input('What else? ')
        #write done for now
        file.write(first_input + '\n')

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")