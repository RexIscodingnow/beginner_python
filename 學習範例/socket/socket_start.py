'''
    socket 模組

    socket( family = AF_INET, type = SOCK_STREAM, proto = 0, fileno = None )
        parameter 如下
        : family = AF_INET  或是  AF_INET6
                        AF_INET  => IPv4
                        AF_INET6 => IPv6
        : type: 通訊協定
                    SOCK_STREAM => TCP 協定 (可靠傳輸: 貨到不簽，不會走人)
                                        應用場景: ex: 上傳資料
                    SOCK_DGRAM  => UDP 協定 (不可靠的: 貨送出去，少一件，多一件，不管你)
                                        應用場景: ex: 直播 (RTP (即時傳輸協定): 比較適合)

    bind(address)
        : param address: 使用 Tuple => (host, port)
                    host => 網路 IP
                    port => 連接埠

    listen(backlog)
        : param backlog: int 型別  指的是 queue 大小
                    queue => 存放客戶端的連線，一旦有許多客戶端同時一起請求連線
                                    會暫時存放在 queue 裡面
                            (ex: 一間高人氣餐廳外面，多放幾張椅子讓客人坐著等待)

    accept()

'''

from socket import socket, AF_INET,SOCK_STREAM


sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(('localhost', 8000))
sockfd.listen(5)

conn, addr = sockfd.accept()
conn.close()





