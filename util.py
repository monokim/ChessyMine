import time

class Timer():
    def __init__(self):
        self.times = []
        self.cnt = 0

    def set_timer(self, name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                t[0] = time.time()
                break

        if flag == False:
            self.times.append([time.time(), name])

    def print_time(self, name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                print(name + " takes (%.5f)s" % (time.time() - t[0]))
                break

        if flag == False:
            raise Exception("There is no timer")

    def delete_timer(self, name = None):
        for i, t in enumerate(self.times):
            if t[1] == name:
                self.times.pop(i)
                break
