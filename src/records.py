from datetime import datetime


class StageRecord:
    def __init__(self, record_file="vimscii_records.txt"):
        self.record_file = record_file

    def save_record(self, stage_name: str, time_taken: float):
        with open(self.record_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} | {stage_name} | {time_taken:.2f}s\n")

    def get_best_time(self, stage_name: str) -> float:
        try:
            with open(self.record_file, "r") as f:
                times = []
                for line in f:
                    if stage_name in line:
                        time_str = line.split("|")[2].strip()
                        times.append(float(time_str[:-1]))
                return min(times) if times else float("inf")
        except FileNotFoundError:
            return float("inf")
