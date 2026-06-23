class Solution:
  def __init__(self,name):
    self.name = name
  def reverse(self):
    s = self.name[::-1]
    for i in range(0,200):
      print(self.name)
    return s

sol = Solution("Vaibhav")
print(sol.reverse())
