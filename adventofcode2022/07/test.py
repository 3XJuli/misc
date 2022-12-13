import math


def higher_future_temp(temperatures):
    # Insert your code here
    output = [0] * len(temperatures)
    wait_temp_list = [max(temperatures)] * len(temperatures)
    for curr_ix, curr_temp in enumerate(temperatures):
        for wait_ix, wait_temp in enumerate(wait_temp_list[:curr_ix]):
            if wait_temp < curr_temp:
                output[wait_ix] = curr_ix - wait_ix
                wait_temp_list[wait_ix] = max(temperatures)
        wait_temp_list[curr_ix] = curr_temp
    return output


def main():
    input = [22, 23, 21, 25, 23]
    print(higher_future_temp(input))



if __name__ == '__main__':
    main()
