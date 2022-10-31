def hello_world():
    return "Hello World!"


def create_num_list(length):
    result = [x for x in range(length)]
    # print(result)
    return result


# create_num_list(10)

def custom_func_x(x, const, power):
    return const * (x) ** power


def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, const, power) for x in range(length)]
