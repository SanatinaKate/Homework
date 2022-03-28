from http import HTTPStatus
import re
import socket


def get_free_port():
    with socket.socket() as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


def get_status(value: int):
    try:
        status = HTTPStatus(value)
    except ValueError:
        result = "200 OK"
    else:
        result = f"{status.value} {' '.join(status.name.split('_'))}"
    return result


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
    server = ("", get_free_port())
    print(f"Starting echo-server on {server}\n")
    sock.bind(server)
    sock.listen(1)
    while True:
        print("Waiting for connection...")
        connect, client = sock.accept()
        closed = False
        print(f"Handling connection from {client}")
        while not closed:
            data = connect.recv(1024).decode("utf-8")
            if len(data) > 0:
                print(f"Received data:\n{data}")
                data_list = data.split("\r\n")
                method = re.search(r"^\w+", data_list[0]).group()
                body = f"Request Method: {method}<br/>\r\n"
                body += f"Request Source: {client}<br/>\r\n"
                search = re.search(r"/\?status=(\d{3}) ", data_list[0])
                recv_status = int(search.group(1)) if (search is not None) else -1
                resp_status = get_status(recv_status)
                body += f"Response Status: {resp_status}<br/>\r\n"
                for elem in data_list[1:]:
                    if ":" in elem:
                        body += f"{elem}<br/>\r\n"
                recv_http = re.search(r"HTTP/\d+.\d+", data_list[0]).group()
                status_line = f"{recv_http} {resp_status}"
                headers = "\r\n".join([
                    status_line,
                    "Content-Type: text/html; charset=UTF-8",
                    f"Content-Length: {len(body)}",
                ])
                response = "\r\n\r\n".join([
                    headers,
                    body
                ])
                print(f"Prepared response:\n{response}")
                print("Sending data back to the client\n")
                connect.send(response.encode("utf-8"))
            else:
                print(f"There is no received data - closing connection with {client}\n")
                closed = True
        connect.close()
