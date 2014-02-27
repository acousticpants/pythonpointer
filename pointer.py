class ptr:
    def __init__(self. obj):
        self.obj = obj

    def get(self):
        return self.obj

    def set(self, obj):
        self.obj = obj
        
a = ref([1, 2])
b = a

print a.get()   # expect => [1, 2]
print b.get()   # expect => [1, 2]

b.set(2)

print a.get()   # expect => 2
print b.get()   # expect => 2
