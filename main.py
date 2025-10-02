#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
실시간 전력/자원 기록기 → CSV 저장
- psutil로 CPU/메모리 사용률 기록 (전력은 Power Gadget 있으면 연동 가능)
- 1초마다 한 줄씩 CSV에 추가
"""

import psutil
import time
import datetime
import csv
from pathlib import Path

LOGFILE = Path("resource_log.csv")

def main():
    # 파일이 없으면 새로 만들고, 있으면 이어쓰기
    new_file = not LOGFILE.exists()
    with LOGFILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # 헤더는 파일 처음 만들 때만
        if new_file:
            writer.writerow(["timestamp", "cpu_percent", "mem_percent"])
        try:
            while True:
                ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cpu = psutil.cpu_percent(interval=20)
                mem = psutil.virtual_memory().percent
                writer.writerow([ts, cpu, mem])
                f.flush()  # 즉시 저장
                print(ts, cpu, mem)
        except KeyboardInterrupt:
            print("\n종료됨.")

if __name__ == "__main__":
    main()
