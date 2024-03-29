# class ClassName:
# Parent Class:
class Parent:
    def __init__(self):
        pass

# child class:
# single inheritance
class Child(Parent):
    def __init__(self):
        pass

# multi-level inheritance
class Child2(Child):
    def __init__(self):
        pass
# ---------------------------------------------------
# multiple inheritance
class A:
    def __init__(self):
        pass
class B:
    def __init__(self):
        pass

class C(A,B):
    def __init__(self):
        pass   

# ----------------------------------
# hierarchical inheritance
class R:
    def __init__(self):
        pass

class S(R):
    def __init__(self):
        pass

class T(R):
    def __init__(self):
        pass

# -----------------------
# Hybrid Inheritance
# child2 - multi level inheritance 
# c - multiple inheritance
class N(Child2, C):
    def __init__(self):
        pass
