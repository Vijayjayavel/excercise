"""Write a Python program to count repeated characters in a string."""

def count_char(string):
    return {key:string.count(key) for key in string if string.count(key)>2}

print(count_char(';iuanfeuvdbtgaclyjdvbjfcaljgcljkhww'))
print(count_char('dfbvhjaifluabuelvyaeobiyrm;lxX>jnxccnhyueopoawa;klzZ<Mxnmhcxfhgdfytreyuw8ewopowpoaslkkds,z'))