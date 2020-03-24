import time

a = input("Сколько раз запускать? ---->  ")

def time_this(num_runs):
  def decorator(func):
    def wrap():
      avg = 0
      for _ in range(num_runs):
        t0 = time.time()
        func()
        t1 = time.time()
        avg += (t1 - t0)
      avg /= num_runs
      print("Среднее время выполнения за %s запусков: %.5f секунд" % (num_runs, avg))
    return wrap
  return decorator

@time_this(num_runs=int(a))
def f():
  for j in range(1000000):
      pass

print(f())