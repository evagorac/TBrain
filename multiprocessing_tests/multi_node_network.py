import multiprocessing as mp
from time import sleep
from random import random

# use multiple objects handling multiple pipes

def node(*args):
  # args is a tuple containing the current node index, a start flag telling the node to start first or not, and a list of pipes to all other nodes
  node_idx, start_flag, node_pipes = [arg for arg in args]
  print('node', node_idx, 'initialized.')

  if start_flag:
    sleep(1)
    print()
    print('node', node_idx, 'has received the start flag.  Sending value 1 to adjacent node')
    print()
    idx = node_idx if node_idx != len(node_pipes)-2 else node_idx-1
    node_pipes[idx].send((node_idx, 1))
    start_flag = False

  # cannot simply use pipe.recv() because that will block until something is received
  # must first check if data is available with pipe.poll()
  while True:
    for pipe in node_pipes:
      if pipe.poll():
        sleep(3)
        sender_idx, data = pipe.recv()
        print('node', node_idx, 'received', data, 'from sender', sender_idx)

        rand_idx = int(random()*len(node_pipes))
        rand_node_idx  = rand_idx+1 if rand_idx >= node_idx else rand_idx

        print('node', node_idx, 'sending value:', data+1, 'to random node', rand_node_idx)
        print()
        node_pipes[rand_idx].send((node_idx, data+1))


def setup():
  num_nodes = 5

  # create table of pipe ends, each row corresponds to a node's pipes to other nodes excluding itself
  pipe_table = [ [ None for i in range(num_nodes-1) ] for j in range(num_nodes) ]
  for i in range(num_nodes-1):
    for j in range(num_nodes-i-1):
      end1, end2 = mp.Pipe()
      pipe_table[i][i+j] = end1
      pipe_table[i+j+1][i] = end2

  node_process_list = []

  for i in range(num_nodes):
    start_flag = i == 0
    proc = mp.Process(target=node, args=(i, start_flag, pipe_table[i]))
    node_process_list.append(proc)
    proc.start()

  for p in node_process_list:
    p.join()

setup()





