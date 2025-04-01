import random
import os

# پیشوندهای IPv6
ipv6_prefixes = ["2606:4700:d1", "2606:4700:d0"]

# پیشوندهای IPv4
ipv4_prefixes = ["162.159.192.", "162.159.193.", "162.159.195.", "162.159.204.", "188.114.96.", "188.114.97.", "188.114.98.", "188.114.99."]
ports = "500 854 859 864 878 880 890 891 894 903 908 928 934 939 942 943 945 946 955 968 987 988 1002 1010 1014 1018 1070 1074 1180 1387 1701 1843 2371 2408 2506 3138 3476 3581 3854 4177 4198 4233 4500 5279 5956 7103 7152 7156 7281 7559 8319 8742 8854 8886"

# تولید آدرس‌های IPv6 و IPv4
ipv6_ips = []
ipv4_ips = []
for _ in range(10):
    ipv6_prefix = random.choice(ipv6_prefixes)
    ipv4_prefix = random.choice(ipv4_prefixes)
    port = random.choice(ports.split())
    
    # تولید آدرس IPv6
    random_part = ":".join(f"{random.randint(0, 65535):04x}" for _ in range(4))
    ipv6_ip = f"{ipv6_prefix}::{random_part}:{port}"
    ipv6_ips.append(ipv6_ip)
    
    # تولید آدرس IPv4
    ipv4_ip = f"{ipv4_prefix}{random.randint(0, 255)}:{port}"
    ipv4_ips.append(ipv4_ip)

# ذخیره در فایل ips.txt
with open("ips.txt", "w") as f:
    f.write("IPv4:\n")
    for ipv4 in ipv4_ips:
        f.write(f"{ipv4}\n")
    f.write("\nIPv6:\n")
    for ipv6 in ipv6_ips:
        f.write(f"{ipv6}\n")

# ذخیره در README.md
with open("README.md", "w") as f:
    f.write("## IPv4\n")
    for ipv4 in ipv4_ips:
        f.write(f"``````\n")
    f.write("\n## IPv6\n")
    for ipv6 in ipv6_ips:
        f.write(f"``````\n")

# پاک کردن و ذخیره در README
with open("README.md", "w") as f:
    f.write("## IPv4\n")
    for ipv4 in ipv4_ips:
        f.write(f"```\n {ipv4}\n```\n")
    f.write("\n## IPv6\n")
    for ipv6 in ipv6_ips:
        f.write(f"```\n {ipv6}\n```\n")
