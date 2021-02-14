import multiprocessing as mp
from time import sleep

# make paddles pipe a message to each other and print it

def paddle(*args):
  pipe, start_flag = [arg for arg in args]
  name = mp.current_process().name
  while True:
    if start_flag:
      print(name, 'starting throw with value 1')
      print()
      start_flag = False
      pipe.send(1)
    pong = pipe.recv() # recv will block until there is something that arrives
    print(name, 'caught', pong, 'from pipe', pipe)
    print('waiting...')
    sleep(2)
    print(name, 'sending a', pong+1)
    print()
    pipe.send(pong+1)

def main():
  pipe_end_1, pipe_end_2 = mp.Pipe()
  p1 = mp.Process(target=paddle, args=(pipe_end_1, True), name='paddle_1')
  p2 = mp.Process(target=paddle, args=(pipe_end_2, False), name='paddle_2')
  p1.start() # start async tasks
  p2.start()
  p1.join() # forgetting the join statements would cause the main prog to terminate early
  p2.join()

main()
