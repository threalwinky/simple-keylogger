import sys
import os

def parse_keylog_lines(lines, line_width=20):
    typed_text = []
    cursor_pos = 0

    for line in lines:
        key_part = line.split()[0]

        if len(key_part) == 1:
            typed_text.insert(cursor_pos, key_part)
            cursor_pos += 1
        elif key_part == "Key.space":
            typed_text.insert(cursor_pos, ' ')
            cursor_pos += 1
        elif key_part == "Key.enter":
            typed_text.insert(cursor_pos, '\n')
            cursor_pos += 1
        elif key_part == "Key.backspace":
            if cursor_pos > 0:
                del typed_text[cursor_pos - 1]
                cursor_pos -= 1
        elif key_part == "Key.delete":
            if cursor_pos < len(typed_text):
                del typed_text[cursor_pos]
        elif key_part == "Key.left":
            cursor_pos = max(0, cursor_pos - 1)
        elif key_part == "Key.right":
            cursor_pos = min(len(typed_text), cursor_pos + 1)
        elif key_part == "Key.up":
            cursor_pos = max(0, cursor_pos - line_width)
        elif key_part == "Key.down":
            cursor_pos = min(len(typed_text), cursor_pos + line_width)

    return ''.join(typed_text)

def quick_convert(log_file=None):
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
        cleaned = []
        for line in lines:
            line = line.strip()
            if line and line.startswith("'") and len(line) > 2 and line[2] == "'":
                line = line[1] + line[3:]
            if line:
                cleaned.append(line)
        return parse_keylog_lines(cleaned)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python convert_logs_to_data.py <log_file>")
        print("Example: python convert_logs_to_data.py logs/log_2025-07-16_15-43-44.txt")
        sys.exit(1)

    result = quick_convert(sys.argv[1])
    
    log_filename = os.path.basename(sys.argv[1])
    data_filename = f"data/{log_filename}"

    with open(data_filename, 'w') as f:
        f.write(result)