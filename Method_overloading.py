#Area of any shape
class Compute:
    def area_of_any_shape(self, x=None, y=None):
          if x!=None and y !=None:
              return "area of Rectangle =", x*y
          elif x!=None:
              return "area of Square =", x*x
          else:
              return 0
obj = Compute()
obj.area_of_any_shape()
print(obj.area_of_any_shape(6))
print(obj.area_of_any_shape(2,8))
