import sys
import os
import termios
import tty

# Стандартные файловые дескрипторы:
# stdin_fd = sys.stdin.fileno()   # 0 - клавиатура
# stdout_fd = sys.stdout.fileno() # 1 - экран  
# stderr_fd = sys.stderr.fileno() # 2 - ошибки

# print(f"STDIN: {stdin_fd}, STDOUT: {stdout_fd}, STDERR: {stderr_fd}")

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            ch += sys.stdin.read(2)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
