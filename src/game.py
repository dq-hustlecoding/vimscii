from blessed import Terminal
from typing import List
import os
import time
from stage import Stage
from records import StageRecord


class Vimscii:
    def __init__(self):
        self.term = Terminal()
        self.current_stage = None
        self.user_buffer = []
        self.start_time = None
        self.is_insert_mode = False
        self.stages = self.load_stages()
        self.cursor_x = 0
        self.cursor_y = 0

    def load_stages(self) -> List[Stage]:
        """Load all stages from the stages directory"""
        stages = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stages_dir = os.path.join(os.path.dirname(current_dir), "stages")

        if not os.path.exists(stages_dir):
            raise FileNotFoundError(f"Stages directory not found at {stages_dir}")

        for category in os.listdir(stages_dir):
            category_path = os.path.join(stages_dir, category)
            if os.path.isdir(category_path):
                for stage_file in os.listdir(category_path):
                    if stage_file.endswith(".txt"):
                        file_path = os.path.join(category_path, stage_file)
                        try:
                            with open(file_path, "r") as f:
                                content = f.read().rstrip()
                                name = stage_file[:-4]
                                stages.append(Stage(name, content, category))
                        except Exception as e:
                            print(f"Error loading {file_path}: {e}")

        if not stages:
            raise ValueError("No stages found in stages directory")

        return stages

    def show_stage_selection(self):
        """Show stage selection menu"""
        print(self.term.clear)
        print(self.term.home + self.term.white_on_black("Welcome to VIMSCII!\n"))
        print("Available stages:\n")

        # 카테고리별로 스테이지 표시
        categories = {}
        for stage in self.stages:
            if stage.category not in categories:
                categories[stage.category] = []
            categories[stage.category].append(stage)

        stage_list = []  # 전체 스테이지 리스트 (선택용)

        for category, stages in categories.items():
            print(self.term.bold(f"\n{category}:"))
            for stage in stages:
                stage_list.append(stage)
                print(f"{len(stage_list)}. {stage.name}")

        print("\nEnter stage number (or 'q' to quit): ")

        while True:
            with self.term.cbreak():
                choice = self.term.inkey()
                if choice.lower() == "q":
                    return False
                try:
                    stage_num = int(choice) - 1
                    if 0 <= stage_num < len(stage_list):
                        self.current_stage = stage_list[stage_num]
                        self.user_buffer = [""]
                        self.start_time = time.time()
                        return True
                    else:
                        print("Invalid stage number. Try again: ")
                except ValueError:
                    print("Please enter a number or 'q' to quit: ")

    def draw_screen(self):
        """Draw the main game screen"""
        print(self.term.clear)
        width = self.term.width // 2
        height = self.term.height

        # 구분선
        for y in range(height - 1):  # 맨 아래 줄은 상태바용으로 남김
            print(self.term.move(y, width) + "│")

        # 목표 ASCII art
        if self.current_stage:
            for i, line in enumerate(self.current_stage.content.splitlines()):
                print(self.term.move(i + 2, width + 2) + line)

        # 사용자 입력
        for i, line in enumerate(self.user_buffer):
            print(self.term.move(i + 2, 2) + line)

        # 커서 표시 (모드에 따라 다른 형태로)
        cursor_y = self.cursor_y + 2
        cursor_x = self.cursor_x + 2

        if self.is_insert_mode:
            print(
                self.term.move(cursor_y, cursor_x) + self.term.reverse(" "),
                end="",
                flush=True,
            )
        else:
            print(
                self.term.move(cursor_y, cursor_x) + self.term.underline(" "),
                end="",
                flush=True,
            )

        # vim 스타일 상태/커맨드 라인 (맨 아래 줄)
        status_line = ""
        if hasattr(self, "command_buffer") and self.command_buffer:
            # 커맨드 모드일 때
            status_line = self.command_buffer
        elif self.is_insert_mode:
            # INSERT 모드일 때
            status_line = "-- INSERT --"

        # 상태바 배경색 설정 (검은 배경에 흰 글씨)
        status_bg = self.term.black_on_white(status_line.ljust(self.term.width))
        print(self.term.move(height - 1, 0) + status_bg, end="", flush=True)

        # 타이머는 오른쪽 상단에 표시
        elapsed = time.time() - self.start_time if self.start_time else 0
        timer = f"Time: {elapsed:.1f}s"
        print(self.term.move(0, self.term.width - len(timer)) + timer)

    def compare_with_target(self):
        """현재 입력과 목표 ASCII art를 비교"""
        target_lines = self.current_stage.content.splitlines()

        # 줄 수가 다르면 False
        if len(self.user_buffer) != len(target_lines):
            return False
        # 각 줄을 비교
        for user_line, target_line in zip(self.user_buffer, target_lines):
            # 끝의 공백을 제거하고 비교
            if user_line.rstrip() != target_line.rstrip():
                return False

        return True

    def show_result_screen(self, success: bool):
        """결과 화면 표시"""
        print(self.term.clear)
        height = self.term.height
        width = self.term.width

        if success:
            elapsed = time.time() - self.start_time
            record = StageRecord()
            best_time = record.get_best_time(self.current_stage.name)
            record.save_record(self.current_stage.name, elapsed)

            is_new_record = elapsed < best_time

            messages = [
                "🎉 Stage Cleared! 🎉",
                f"Time: {elapsed:.2f} seconds",
                (
                    f"Best: {best_time:.2f} seconds"
                    if best_time != float("inf")
                    else "New stage record!"
                ),
                "NEW RECORD! 🏆" if is_new_record else "",
                "",
                "Press any key to continue...",
            ]
        else:
            messages = [
                "❌ Not quite right!",
                "Use :q! to quit without saving",
                "Or keep trying and use :wq when ready",
                "",
                "Press any key to continue...",
            ]

        # 메시지를 화면 중앙에 표시
        start_y = height // 2 - len(messages) // 2
        for i, msg in enumerate(messages):
            x = width // 2 - len(msg) // 2
            if msg:  # 빈 문자열이 아닐 때만 출력
                print(self.term.move(start_y + i, x) + msg)

        with self.term.cbreak():
            self.term.inkey()  # 아무 키나 누를 때까지 대기

    def handle_input(self):
        """Handle vim-style keyboard input"""
        key = self.term.inkey()

        if not hasattr(self, "command_buffer"):
            self.command_buffer = ""

        if key.code == self.term.KEY_ESCAPE:
            self.is_insert_mode = False
            self.command_buffer = ""
        elif not self.is_insert_mode:
            if key == "i":
                self.is_insert_mode = True
            elif key == ":":  # 커맨드 모드 시작
                self.command_buffer = ":"
            elif self.command_buffer.startswith(":"):  # 커맨드 모드 중
                if key.code == self.term.KEY_ENTER:
                    if self.command_buffer == ":wq":  # 저장 및 종료 커맨드
                        success = self.compare_with_target()
                        self.show_result_screen(success)
                        return False if success else True  # 성공시에만 종료
                    elif self.command_buffer == ":q!":  # 강제 종료
                        return False
                    self.command_buffer = ""
                elif key.code == self.term.KEY_BACKSPACE:
                    self.command_buffer = self.command_buffer[:-1]
                else:
                    self.command_buffer += key
            elif key == "h" and self.cursor_x > 0:
                self.cursor_x -= 1
            elif key == "l":
                self.cursor_x += 1
            elif key == "k" and self.cursor_y > 0:
                self.cursor_y -= 1
            elif key == "j":
                self.cursor_y += 1
        else:  # Insert 모드
            while len(self.user_buffer) <= self.cursor_y:
                self.user_buffer.append("")

            current_line = self.user_buffer[self.cursor_y]

            if key.is_sequence:
                if key.code == self.term.KEY_ENTER:
                    self.cursor_y += 1
                    self.cursor_x = 0
                elif key.code == self.term.KEY_BACKSPACE:
                    if self.cursor_x > 0:
                        self.user_buffer[self.cursor_y] = (
                            current_line[: self.cursor_x - 1]
                            + current_line[self.cursor_x :]
                        )
                        self.cursor_x -= 1
            else:
                self.user_buffer[self.cursor_y] = (
                    current_line[: self.cursor_x] + key + current_line[self.cursor_x :]
                )
                self.cursor_x += 1

        return True

    def run(self):
        """Main game loop"""
        if not self.show_stage_selection():
            return

        try:
            with self.term.fullscreen(), self.term.cbreak():  # hidden_cursor 제거
                while True:
                    self.draw_screen()
                    if not self.handle_input():
                        break
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    game = Vimscii()
    game.run()
