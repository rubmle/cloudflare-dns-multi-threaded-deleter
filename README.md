**Cloudflare DNS 记录删除器**

一个开源的 Python 脚本,用于通过 Cloudflare API 批量删除指定区域(Zone)中的 DNS 记录。它使用多线程来加快删除速度,同时避免触发 Cloudflare 的速率限制。

主要功能:

- 获取指定 Cloudflare 区域中的所有 DNS 记录列表
- 创建工作队列,将所有记录添加到队列中
- 使用线程池和固定数量的工作线程并行删除队列中的记录
- 输出正在删除的记录名称和指向的 IP 地址
- 等待所有工作线程完成,确保全部记录被删除

使用方式:

1. 克隆该仓库到本地
2. 安装必要的 Python 库: `requests`
3. 修改脚本中的 `API_TOKEN` 和 `ZONE_ID` 为您自己的 Cloudflare 凭据
4. 运行脚本: `python cloudflare-dns-record-deleter.py`
5. 查看输出,等待所有记录被删除

该脚本适用于需要批量清除 Cloudflare DNS 记录的场景,例如域名过期、更换 DNS 服务商等。通过使用多线程,可以显著提高删除效率。同时,也包含了适当的限制,避免发送过多请求导致 IP 被 Cloudflare 暂时封禁。


**Cloudflare DNS Record Deleter**

An open-source Python script to bulk delete DNS records from a Cloudflare zone via the Cloudflare API. It utilizes multi-threading to speed up the deletion process while avoiding rate limits.

Key Features:

- Fetch a list of all DNS records in the specified Cloudflare zone
- Create a work queue and add all records to the queue
- Use a thread pool with a fixed number of worker threads to delete records from the queue in parallel
- Output the name and content of the record being deleted
- Wait for all worker threads to complete, ensuring all records are deleted

Usage:

1. Clone the repository locally
2. Install required Python libraries: `requests`
3. Modify the `API_TOKEN` and `ZONE_ID` in the script with your Cloudflare credentials
4. Run the script: `python cloudflare-dns-record-deleter.py`
5. View the output and wait for all records to be deleted

This script is useful for scenarios where you need to bulk clear DNS records from Cloudflare, such as domain expiration or changing DNS providers. By utilizing multi-threading, the deletion process is significantly faster. At the same time, it includes appropriate rate limiting to avoid sending too many requests and getting your IP temporarily banned by Cloudflare.
