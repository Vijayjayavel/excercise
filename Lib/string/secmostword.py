'''Write a Python program to find the second most repeated word in a given string'''

def sec_most(string):
    x=string.split()
    out={key:x.count(key) for key in x}
    return sorted(out.items(),key=lambda x:(x[1]))[-2]
print(sec_most('an eye for an eye makes the whole world blind'))
print(sec_most("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))