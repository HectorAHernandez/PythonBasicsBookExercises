def scope_test():
    def do_local():
        spam = "local spam"  # Local scope to this function do_local()

    def do_nonlocal():
        nonlocal spam  # Indicates to use the spam variable defined in the
        # scope of the scope_test() method (line 18), which is nonlocal.
        spam = "nonlocal spam"

    def do_global():
        global spam  # indicates to use the span var referenced in the module,
        # and outside function scope_test(), this is line 29. so
        # the span in this scope_test() still have the value set
        # for the line 18 with do-nonlocal.
        spam = "global spam"

    # this is the non-local scope for above functions inside this scope_test().
    spam = "test spam"  # this spam variable is in the nonlocal scope
    do_local()
    print("After local assignment:", spam)  # print spam from nonlocal line 14
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # span changed in do-nonlocal
    do_global()
    print("After global assignment:", spam)  # still have the nonlocal setting


# Below is at the module scope, which is the real for 'global'
scope_test()
print("In global scope:", spam)

# The output of the example code is:
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam
