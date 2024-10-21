def outer(out_param1, out_param2):
    def inner(in_param1, in_param2):
        return in_param1 + in_param2
    return inner(out_param1, out_param2)

print(outer(5,6))