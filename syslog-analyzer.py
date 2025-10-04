line = "Oct  3 14:10:01 server01 CRON[12345]: (root) CMD (run-parts /etc/cron.hourly)"
items = line.split()

date = " ".join(items[0:3])  # Oct 3 14:10:01
host = items[3]  # server01
proc_name = line[4].split("[")[0]  # CRON
proc_num = line[4].split("[")[1].split("]")[0]  # 12345

msg_items = line.split()[5:]
msg = ""

for msg_item in msg_items:
    msg += msg_item + " "

msg.strip()
