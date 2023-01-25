from collections import deque

class Task(object):
  def __init__(self,taskDesc,hasPriority = False):
     self.taskDesc = taskDesc
     self.hasPriority = hasPriority

  def __str__(self):
     return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

task_queue = deque()

def add_task(task):
  if(task.hasPriority):
    task_queue.appendleft(task)
  else:
    task_queue.append(task)

def do_task():
  return task_queue.popleft()

def print_task():
  for t in task_queue:
     print(t.taskDesc)

def main():
    #add code here
    print(task_queue)
    add_task(Task("Make List"))
    add_task(Task("Make Breakfast",True))
    add_task(Task("Wake up",True))
    print(task_queue)
    print_task()
    print(do_task())
    return

if __name__ == "__main__":
    main()