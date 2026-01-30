#30-01-2026
#Q68)Recursion:-
def show(n):
  if n<=0:
    return
  print(n)
  show(n-1)
show(10)
