class MyCounter:
    def set_count(self, n):
        self.count = n

mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)