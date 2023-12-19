from pynput import keyboard
import time

key_press_times = {}
time_threshold = 0.0  # 2秒的时间阈值

def on_key_press(key):
    current_time = time.time()
    key_press_times[key] = current_time

def on_key_release(key):
    current_time = time.time()
    key_down_time = key_press_times.get(key, None)

    if key_down_time is not None:
        key_usage_time = current_time - key_down_time
        if key_usage_time >= time_threshold:
            # 执行操作，例如打印消息
            print(f"Key {key} was pressed for {key_usage_time} seconds. Performing action.")

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()