import time
import sys
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

# Constants for the display
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Adjustable parameters
ref_eye_height = 40
ref_eye_width = 40
ref_space_between_eye = 10
ref_corner_radius = 10

# Current state of the eyes
left_eye_height = ref_eye_height
left_eye_width = ref_eye_width
left_eye_x = 32
left_eye_y = 32
right_eye_x = 32 + ref_eye_width + ref_space_between_eye
right_eye_y = 32
right_eye_height = ref_eye_height
right_eye_width = ref_eye_width

# Setup the OLED display
serial = i2c(port=1, address=0x3C)  # Adjust the port if necessary
device = sh1106(serial)
try:
	font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",15)
except IOError:
	print("Not found")
	font = Image.load.default()

def draw_eyes(update=True):
    valid_left_eye_height = max(left_eye_height, 0)
    valid_right_eye_height = max(right_eye_height, 0)
    with canvas(device) as draw:
        # Draw left eye
        draw.rectangle((left_eye_x - left_eye_width // 2, left_eye_y -  valid_left_eye_height  // 2,
                        left_eye_x + left_eye_width // 2, left_eye_y +  valid_left_eye_height  // 2), outline="white", fill="white")
        # Draw right eye
        draw.rectangle((right_eye_x - right_eye_width // 2, right_eye_y - valid_right_eye_height  // 2,
                        right_eye_x + right_eye_width // 2, right_eye_y + valid_right_eye_height // 2), outline="white", fill="white")

def center_eyes(update=True):
    global left_eye_x, right_eye_x, left_eye_y, right_eye_y, left_eye_height, right_eye_height
    left_eye_height = ref_eye_height
    left_eye_width = ref_eye_width
    right_eye_height = ref_eye_height
    right_eye_width = ref_eye_width
    left_eye_x = SCREEN_WIDTH // 2 - ref_eye_width // 2 - ref_space_between_eye // 2
    left_eye_y = SCREEN_HEIGHT // 2
    right_eye_x = SCREEN_WIDTH // 2 + ref_eye_width // 2 + ref_space_between_eye // 2
    right_eye_y = SCREEN_HEIGHT // 2
    draw_eyes(update)

def blink(speed=12):
    global left_eye_height, right_eye_height
    for _ in range(3):
        left_eye_height -= max(left_eye_height - speed, 0)
        right_eye_height -= max(right_eye_height - speed, 0)
        draw_eyes()
        time.sleep(0.01)
    for _ in range(3):
        left_eye_height +=min(left_eye_height + speed, ref_eye_height)
        right_eye_height += min(right_eye_height + speed, ref_eye_height)
        draw_eyes()
        time.sleep(0.01)

def sleep():
    global left_eye_height, right_eye_height
    left_eye_height = 2
    right_eye_height = 2
    draw_eyes()

def wakeup():
    sleep()
    for h in range(0, ref_eye_height + 1, 2):
        global left_eye_height, right_eye_height
        left_eye_height = h
        right_eye_height = h
        draw_eyes()

def happy_eye():
    center_eyes(False)
    # Draw happy eyes (inverted triangles)
    offset = ref_eye_height // 2
    with canvas(device) as draw:
        for i in range(10):
            draw.polygon([(left_eye_x - left_eye_width // 2 - 1, left_eye_y + offset),
                           (left_eye_x + left_eye_width // 2 + 1, left_eye_y + 5 + offset),
                           (left_eye_x - left_eye_width // 2 - 1, left_eye_y + left_eye_height + offset)], fill="black")
            draw.polygon([(right_eye_x + right_eye_width // 2 + 1, right_eye_y + offset),
                           (right_eye_x - right_eye_width // 2 - 1, right_eye_y + 5 + offset),
                           (right_eye_x + right_eye_width // 2 + 1, right_eye_y + right_eye_height + offset)], fill="black")
            offset -= 2
            draw_eyes()

def saccade(direction_x, direction_y):
    global left_eye_x, right_eye_x, left_eye_y, right_eye_y, left_eye_height, right_eye_height
    direction_x_movement_amplitude = 8
    direction_y_movement_amplitude = 6
    blink_amplitude = 8

    for _ in range(1):
        left_eye_x += direction_x_movement_amplitude * direction_x
        right_eye_x += direction_x_movement_amplitude * direction_x
        left_eye_y += direction_y_movement_amplitude * direction_y
        right_eye_y += direction_y_movement_amplitude * direction_y
        left_eye_height -= blink_amplitude
        right_eye_height -= blink_amplitude
        draw_eyes()
        time.sleep(0.01)

    for _ in range(1):
        left_eye_x += direction_x_movement_amplitude * direction_x
        right_eye_x += direction_x_movement_amplitude * direction_x
        left_eye_y += direction_y_movement_amplitude * direction_y
        right_eye_y += direction_y_movement_amplitude * direction_y
        left_eye_height += blink_amplitude
        right_eye_height += blink_amplitude
        draw_eyes()
        time.sleep(0.01)

def move_big_eye(direction):
    global left_eye_x, right_eye_x, left_eye_height, right_eye_height, left_eye_width, right_eye_width
    direction_movement_amplitude = 2
    blink_amplitude = 5

    for _ in range(3):
        left_eye_x += direction_movement_amplitude * direction
        right_eye_x += direction_movement_amplitude * direction
        left_eye_height = max(left_eye_height - blink_amplitude, 0)  # Ngăn không cho giá trị âm
        right_eye_height = max(right_eye_height - blink_amplitude, 0)  # Ngăn không cho giá trị âm
        if direction > 0:
            right_eye_height = min(right_eye_height + 1, ref_eye_height)
            right_eye_width = min(right_eye_width + 1, ref_eye_width)
        else:
            left_eye_height = min(left_eye_height + 1, ref_eye_height)
            left_eye_width = min(left_eye_width + 1, ref_eye_width)
        draw_eyes()
        time.sleep(0.01)

    # Reset position
    for _ in range(3):
        left_eye_x -= direction_movement_amplitude * direction
        right_eye_x -= direction_movement_amplitude * direction
        left_eye_height = min(left_eye_height + blink_amplitude, ref_eye_height)  # Đảm bảo không vượt quá chiều cao tối đa
        right_eye_height = min(right_eye_height + blink_amplitude, ref_eye_height)  # Đảm bảo không vượt quá chiều cao tối đa
        if direction > 0:
            right_eye_height = max(right_eye_height - 1, 0)  # Ngăn không cho giá trị âm
            right_eye_width = max(right_eye_width - 1, 0)  # Ngăn không cho giá trị âm
        else:
            left_eye_height = max(left_eye_height - 1, 0)  # Ngăn không cho giá trị âm
            left_eye_width = max(left_eye_width - 1, 0)  # Ngăn không cho giá trị âm
        draw_eyes()
        time.sleep(0.01)

def display_text(text, duration_seconds=0):
    # --- PHẦN LOGIC XUỐNG DÒNG ---
    words = text.split(' ')
    lines = []
    current_line = ''
    
    # Chiều cao của mỗi dòng chữ, bạn có thể chỉnh số này để tăng/giảm khoảng cách dòng
    line_height = 20 # Dựa trên kích thước font là 20

    # Dùng canvas tạm để đo chiều rộng text mà không cần vẽ ra màn hình
    with canvas(device) as draw:
        for word in words:
            # Kiểm tra xem nếu thêm từ mới vào, dòng hiện tại có bị quá dài không
            test_line = f'{current_line} {word}'.strip()
            if draw.textlength(test_line, font=font) <= SCREEN_WIDTH:
                current_line = test_line
            else:
                # Nếu dòng quá dài, lưu dòng hiện tại lại
                lines.append(current_line)
                # Và bắt đầu một dòng mới với từ vừa kiểm tra
                current_line = word
        
        # Đừng quên lưu lại dòng cuối cùng
        lines.append(current_line)

        # --- PHẦN VẼ CÁC DÒNG ĐÃ CHIA ---
        # Tính toán tổng chiều cao của khối văn bản để căn giữa theo chiều dọc
        total_text_height = len(lines) * line_height
        y_start = (SCREEN_HEIGHT - total_text_height) / 2

        # Vẽ từng dòng một
        for i, line in enumerate(lines):
            # Tính toán vị trí để mỗi dòng được căn giữa theo chiều ngang
            line_width = draw.textlength(line, font=font)
            x = (SCREEN_WIDTH - line_width) / 2
            
            # Tính vị trí y cho dòng hiện tại
            y = y_start + (i * line_height)
            
            draw.text((x, y), line, font=font, fill="white")

    # Nếu có thời gian hiển thị, chương trình sẽ đợi
    if duration_seconds > 0:
        time.sleep(duration_seconds)

# def main():
#     while True:
#         time.sleep(1)
#         wakeup()
#         print("Wake UP!")
#         time.sleep(1)
#         center_eyes(True)
#         print("Center Eyes!")
#         time.sleep(1)
#         move_big_eye(1)  # Move right
#         print("Moving Right!")
#         time.sleep(1)
#         move_big_eye(-1)  # Move left
#         print("Moving Left!")
#         time.sleep(1)
#         blink(10)
#         print("Short Blink!")
#         time.sleep(1)
#         happy_eye()
#         print("Happy Eye!")
#         time.sleep(1)
#         blink(20)
#         print("Long Blink!")
#         time.sleep(1)
#         print("All Motion!")

#         # Saccades in different directions
#         for dir_x, dir_y in [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]:
#             saccade(dir_x, dir_y)
#             time.sleep(0.3)

#         sleep()

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         sys.exit()
