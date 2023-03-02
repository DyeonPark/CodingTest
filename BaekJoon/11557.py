ques_num = int(input())

for _ in range(ques_num):
  school_num = int(input())
  dict = {}

  school_names = []
  drinks = []
  for _ in range(school_num):
    name, d_nums = input().split()
    school_names.append(name)
    drinks.append(int(d_nums))

  print(school_names[drinks.index(max(sorted(drinks)))])
    
