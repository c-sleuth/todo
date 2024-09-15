import argparse
import os


def add_task(args):
    task = ' '.join(args.task)
    try:
        with open("todo_tasks/tasks.txt", "a+") as f:
            f.write(f"{task}\n")
            print(f"{task} added to todo list")
    except Exception as e:
        print(e)


def finish_task(args):
    if not args.id:
        print("no id given")
        return
    try:
        with open("todo_tasks/tasks.txt", "r") as f:
            lines = f.readlines()
            for i in args.id:
                print(f"{lines[i - 1]}has been finished")
                del lines[i - 1]
        with open("todo_tasks/tasks.txt", "w") as f:
            f.writelines(lines)

    except Exception as e:
        print(e)


def list_tasks(args):
    print("tasks")
    print("-"*10)
    try:
        with open("todo_tasks/tasks.txt", "r") as f:
            for line_num, line in enumerate(f, start=1):
                print(f"[{line_num}] {line}")
    except Exception as e:
        print(e)


def todo_init(args):
    if os.path.exists(os.path.join(args.path, "todo_tasks")):
        print(f"todo app already initialised at {args.path}")
        return

    os.mkdir(os.path.join(args.path, "todo_tasks"))
    task_dir = os.path.join(args.path, "todo_tasks")
    with open(os.path.join(task_dir, "tasks.txt"), "w"):
        pass
    print("[+] todo enviroment successfully initialised")


def main():
    parser = argparse.ArgumentParser("cli todo")
    subparsers = parser.add_subparsers(title="Commands")
    # commands for adding tasks
    add_task_parser = subparsers.add_parser("add",
                                            help="Add a new task")
    add_task_parser.add_argument("task",
                                 help="Task details",
                                 nargs="*",
                                 type=str)
    add_task_parser.set_defaults(func=add_task)
    # commands for removing tasks
    finish_task_parser = subparsers.add_parser("finish",
                                               help="""Finish a task
                                               using the task ID""")
    finish_task_parser.add_argument("id",
                                    help="ID associated with a task",
                                    nargs="*",
                                    type=int)
    finish_task_parser.set_defaults(func=finish_task)

    # commands for listing tasks
    list_tasks_parser = subparsers.add_parser("list",
                                              help="List tasks in todo list")
    list_tasks_parser.set_defaults(func=list_tasks)
    # init todo app enviroment
    todo_init_parser = subparsers.add_parser("init",
                                             help="Initialise todo app env")
    todo_init_parser.add_argument("-p", "--path",
                                  default="",
                                  nargs="*",
                                  help="""Path for todo directories,
                                  default = current dir of script""")
    todo_init_parser.set_defaults(func=todo_init)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)


if __name__ == "__main__":
    main()
