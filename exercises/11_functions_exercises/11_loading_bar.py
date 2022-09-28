def loading_bar_progress(progress: int):
    loading_bar_start = "." * 10
    return loading_bar_start.replace(".", "%", progress // 10)


user_progress = int(input())

if user_progress == 100:
    print("100% Complete!\n"
          "[%%%%%%%%%%]")
else:
    print(f"{user_progress}% [{loading_bar_progress(user_progress)}]\n"
          f"Still loading...")
