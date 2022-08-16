"""
If functions is directly called from the .py file it inhabits, the variable __name__ 
for the function is set to "__main__"

However, if module is imported and the function within the module is then called, 
the __name__ variable for the function is set to the name of module

The following code makes that whenever the module customtools is imported, terminal
will call print the __name__ variable of customtools
"""
if __name__:
    print(f"calc function called from {__name__}")
