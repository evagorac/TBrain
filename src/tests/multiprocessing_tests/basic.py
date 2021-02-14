import multiprocessing as mp

def f(arg):
  name = mp.current_process().name
  print('arg passed :', arg)
  print('process ID: ', name)

def super_process():
  for i in range(5):
    p1 = mp.Process(target=f, name=('process '+str(i)), args=(i,)) #args must be an interable like a tuple
    p1.start() # starts async process
    p1.join() # waits for p1 to finish execution before conitnuing, makes asnyc tasks synchornous again

super_process()
