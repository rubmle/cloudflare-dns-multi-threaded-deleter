import requests
from threading import Thread
from queue import Queue

# 设置最大线程数量
# Set the maximum number of threads
MAX_THREADS = 10

# Cloudflare API token和Zone ID
# Cloudflare API token and Zone ID
API_TOKEN = ""
ZONE_ID = ""

# 构建Cloudflare API URL
# Build the Cloudflare API URL
base_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
headers = {
    'Authorization': f"Bearer {API_TOKEN}",
    'Content-Type': "application/json"
}

# 获取DNS记录列表
# Get the list of DNS records
list_url = f"{base_url}?per_page=500"
print(list_url)
response = requests.get(list_url, headers=headers)
records = response.json()['result']

# 定义删除DNS记录的函数
# Define the function to delete a DNS record
def delete_record(record):
    delete_url = f"{base_url}/{record['id']}"
    print(f"Deleting {record['name']} that points to {record['content']}")
    requests.delete(delete_url, headers=headers)
    print(delete_url)

# 创建工作队列,并将DNS记录添加到队列中
# Create a work queue and add DNS records to the queue
queue = Queue()
for record in records:
    queue.put(record)

# 定义工作线程函数
# Define the worker thread function
def worker():
    while not queue.empty():
        record = queue.get()
        delete_record(record)
        queue.task_done()

# 创建并启动工作线程
# Create and start worker threads
threads = []
for _ in range(MAX_THREADS):
    thread = Thread(target=worker)
    threads.append(thread)
    thread.start()

# 等待队列为空,所有工作完成
# Wait for the queue to be empty, and all work to be completed
queue.join()
