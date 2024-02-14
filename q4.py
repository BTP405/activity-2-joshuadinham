import statistics
def printStats(t):
    """Read file line by line and execute decorator function"""
    def readFile(file_name):
        num_list = []
        with open(file_name) as file_contents:
            for line in file_contents:
                num_list = for_each_number(line.strip(), num_list)


    def line_decorator(func):
        """execute function and return the result"""
        def wrapper(line, num_list):
            result = func(line, num_list)
            return result
        return wrapper
    
    @line_decorator
    def for_each_number(number, num_list):
            """Append the number to the list, print the list, count, average, max and return the list """
            num_list.append(int(number))
            print(f"The current list of numbers: \n{num_list}")
            print(f"Count: {len(num_list)}")
            print(f"Average: {statistics.mean(num_list)}")
            print(f"Max: {max(num_list)}")
            return num_list

    readFile(t)
printStats("numbers.txt")