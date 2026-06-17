import tkinter as tk
from tkinter import ttk

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý công việc")
        self.tasks = []

        # Entry + nút thêm task
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.add_btn = tk.Button(root, text="Thêm công việc", command=self.add_task)
        self.add_btn.pack(pady=5)

        # Frame chứa checkbox
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.progress.pack(pady=10)

    def add_task(self):
        task_name = self.entry.get()
        if task_name:
            var = tk.IntVar()
            cb = tk.Checkbutton(self.task_frame, text=task_name, variable=var,
                                command=self.update_progress)
            cb.pack(anchor='w')
            self.tasks.append(var)
            self.entry.delete(0, tk.END)
            self.update_progress()

    def update_progress(self):
        if not self.tasks:
            self.progress['value'] = 0
            return
        completed = sum(task.get() for task in self.tasks)
        total = len(self.tasks)
        self.progress['value'] = (completed / total) * 100

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
