import customtkinter as ctk

ctk.set_appearance_mode("light")

root = ctk.CTk()
root.geometry("300x300")

frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(pady=20, padx=20, fill="both", expand=True)

tk = ctk.CTkLabel(frame, text="Frame bo góc nè!")
tk.pack(pady=20)

root.mainloop()
