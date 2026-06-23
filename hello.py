class Solution:
  def __init__(self,name):
    self.name = name
  def reverse(self):
    s = self.name[::-1]
    return s

sol = Solution("Vaibhav")
print(sol.reverse())
