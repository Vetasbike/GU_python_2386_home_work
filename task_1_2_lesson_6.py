"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
которых превышает объем ОЗУ компьютера.
"""
def parse_logs(txt_file):

    if txt_file:
        with open(txt_file,"r",encoding="utf-8") as f:
            for line in f:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)


def find_spamer(parsed_log):

    if not parsed_log:
        return None

    ip = {}

    for log in parsed_log:
        if not ip.get(log[0]):
            ip[log[0]] = {"count":1, "files":set([log[2]])}
        else:
            ip[log[0]]["count"] += 1
            ip[log[0]]["files"].add(log[2])

    return max(ip.items(), key=lambda x: x[1]["count"])

if __name__ == "__main__":
    result_pars = parse_logs("nginx_logs.txt")
    for lists in result_pars:
        print(lists)

    parsed_log = parse_logs("./nginx_logs.txt")
    spamer = find_spamer(parsed_log)
    if spamer:
       print(f"IP spamer: {spamer[0]}, {spamer[1]}")
