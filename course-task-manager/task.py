"""Simple task manager for the Git lesson."""

def add_task(tasks, task):
   tasks.append(task)


def show_tasks(tasks):
    """Print the current tasks as a numbered list."""
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main() :
    tasks = ["Read the lesson notes", "Practice Python"]
    show_tasks(tasks)


if __name__ == "__main__":
    main()

