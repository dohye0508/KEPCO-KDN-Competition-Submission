#!/usr/bin/env python3
"""
psutil 기반 시스템 리소스 모니터
- CPU 사용률
- 메모리 사용률
- 디스크 사용률
- 네트워크 전송/수신 속도
"""

import psutil
import time
import datetime as dt

def main():
    prev_net = psutil.net_io_counters()
    prev_sent, prev_recv = prev_net.bytes_sent, prev_net.bytes_recv

    print("timestamp, CPU%, MEM%, DISK%, NET_sent(KB/s), NET_recv(KB/s)")

    while True:
        ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        net = psutil.net_io_counters()
        sent_per_s = (net.bytes_sent - prev_sent) / 1024.0
        recv_per_s = (net.bytes_recv - prev_recv) / 1024.0
        prev_sent, prev_recv = net.bytes_sent, net.bytes_recv

        print(f"{ts}, {cpu:.1f}, {mem:.1f}, {disk:.1f}, {sent_per_s:.1f}, {recv_per_s:.1f}")

if __name__ == "__main__":
    main()
