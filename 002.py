class Test:
    count = 21
    def print_num(self):
        count = 20
        self.count += 20
        print(count)
test = Test()
test.print_num()
