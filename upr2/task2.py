class Counter:
    def __init__(self, inital = 0, step = 1):
        self.inital = inital
        self.step = step
        self.total = inital
    
    def increment(self):
        self.total += self.step

    def get_total(self):
        return int(self.total)
    
    @property
    def get_step(self):
        return int(self.step)


class TwowayCounter(Counter):
    def __init__(self):
        super().__init__()

    def decrement(self):
        self.total-=1


class LimitedCounter(Counter):
    def __init__(self, max):
        super().__init__()
        self.max = max

    def increment(self):
        if self.max < self.total:
            self.total+=self.step

    def get_max(self):
        return int(self.max)

    def get_total(self):
        return self.get_total

    def get_total(self):    
        return self.get_step
    

class LimitedTwowayCounter(LimitedCounter,TwowayCounter):

    def __init__(self, max, min):
        super().__init__(max)
        self.max = max
        self.min = min
    
    def increment(self):
        return super().increment()
    
    def decrement(self):
        if self.min < self.total-1:
            self.total-=1

    def get_min(self):
        return self.min
    
    def get_max(self):
        return LimitedCounter.max
    
    def get_total(self):
        return self.total
    
    def get_step(self):
        return self.step
    
class Semaphore(LimitedTwowayCounter):
    def __init__(self,is_available=False):
        super().__init__(max = 0, min = 1)
        if is_available:
            self.inital = 0
        else:
            self.total = 1

    def is_available(self):
        return bool(self.total > 0)
    
    def wait(self):
        self.decrement()

    def signal(self):
        self.increment()