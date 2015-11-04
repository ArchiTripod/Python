import dis
def f(val):
    if val != None:
        return True
    return False
def g(val):
    if not (val is None):
        return True
    return False
def h(val):
    if val is not None:
        return True
    return False
print('f():')
dis.dis(f)
print('g():')
dis.dis(g)
print('h():')
dis.dis(h)
print('COMPARE_OP:')
print(cmp_op)
