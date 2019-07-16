#!/usr/bin/python3
# 2019-7-16

from AssasiansBot.server import server

def main():
    server.run(
        host='0.0.0.0', 
        port=5598
    )

if __name__ == "__main__":
    main()