import socket
from _thread import *
from game import Game
import pickle


HOST = "192.168.0.101"
PORT = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, server started...")

connected = set()
games = {}
id_count = 0


def threaded_client(connection, player, g_id):
    global id_count
    connection.send(str.encode(str(player)))

    reply = ""
    while True:
        try:
            data = connection.recv(4096).decode()

            if g_id in games:
                game = games[g_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_went()
                    elif data != "get":
                        game.play(player, data)

                    reply = game
                    connection.sendall(pickle.dumps(reply))
            else:
                break
        except socket.error:
            break

    print("Lost connection")

    try:
        del games[g_id]
        print("Closing Game", g_id)
    except:
        pass
    id_count -= 1
    connection.close()


while True:
    conn, addr = s.accept()
    print('Connection to:', addr)

    id_count += 1
    p = 0
    game_id = (id_count - 1) // 2
    if id_count % 2 == 1:
        games[game_id] = Game(game_id)
        print("Creating a new game...")
    else:
        games[game_id].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, game_id))


