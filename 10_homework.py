"""1"""
# import time

# class TrafficLight:
#     __color = ''

#     def running(self):
#         while True:
#             TrafficLight.__color = "\033[31mкрасный"
#             print(TrafficLight.__color)
#             time.sleep(7)
#             TrafficLight.__color = '\033[31mкрасный \033[37m+ \033[33mжёлтый'
#             print(TrafficLight.__color)
#             time.sleep(2)
#             TrafficLight.__color = '\033[32mзелёный'
#             print(TrafficLight.__color)
#             time.sleep(5)
#             TrafficLight.__color = '\033[33mжёлтый'
#             print(TrafficLight.__color)
#             time.sleep(2)

# a = TrafficLight()
# a.running()


"""2"""
class Road:
    _length = 0
    _width = 0
    def calc(self, l, w, m, h):
        Road._length = l
        Road._width = w
        self.massa = m
        self.hide = h
        res = float(Road._length * Road._width * self.massa * self.hide)
        if res > 1000:
            return str(res / 1000) + ' т.'
        else:
            return str(res) + ' кг.'
a = Road()
print(a.calc(5000, 20, 25, 5))