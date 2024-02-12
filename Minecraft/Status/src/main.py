from mcstatus import JavaServer
import os

server_ip = os.getenv("MC_SERVER")

server = JavaServer.lookup(server_ip)

status = server.status()
print(f"The server has {status.players.online}")

latency = server.ping()
print(f"The server replied in {latency} ms")

query = server.query()
print(f"The server has the following players online: {', '.join(query.players.names)}")