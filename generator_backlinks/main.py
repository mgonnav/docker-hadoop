# import required module
import os
from random import seed
from random import randint
seed(1)

# assign directory
directory = 'input'
manual_rank_map = {}

for filename in os.listdir(directory):
  # rand is between max possible back links
  manual_rank_map.update({filename:randint(0, 999)})

# sorting map
manual_rank_map = sorted(manual_rank_map.items(), key=lambda x:x[1], reverse=True)
manual_rank_map = dict(manual_rank_map)

# saving sorted manual rank map
rank_file = open('rank.txt', 'a')

for current_filename in manual_rank_map:
  t = current_filename + ' \t\t\t '+ str(manual_rank_map[current_filename]) + '\n'
  rank_file.write(t)

rank_file.close()

# generating back link
for current_filename in manual_rank_map:
  # number of back links created
  i = 0
  for iter_filename in os.listdir(directory):
    if (iter_filename == current_filename):
      continue
    else:
      path = os.path.join(directory, iter_filename)
      file_object = open(path, 'a')
      file_object.write(iter_filename+'$'+current_filename+'\n')
      file_object.close()
      i += 1
    if (i == manual_rank_map[current_filename]):
      break
