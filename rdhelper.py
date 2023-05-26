# Sample server_list.dat
#
# hostname,ip,domain,user,pwd
# hostname,ip,domain,user,pwd
# hostname,ip,domain,user,pwd
# hostname,ip,domain,user,pwd
# hostname,ip,domain,user,pwd





import subprocess
import curses

def read_server_list(filename):
    server_list = []
    with open(filename, 'r') as file:
        for line in file:
            hostname, ipv4, domain, user, password = line.strip().split(',')
            server_list.append((hostname, ipv4, domain, user, password))
    return server_list


def display_server_list(stdscr, server_list, selected_index):
    stdscr.clear()
    stdscr.addstr("Lista dei server disponibili:\n")
    for index, (hostname, ipv4, _, _, _) in enumerate(server_list, start=1):
        if index == selected_index:
            stdscr.addstr(f"> {index}. {hostname} ({ipv4})\n", curses.A_REVERSE)
        else:
            stdscr.addstr(f"  {index}. {hostname} ({ipv4})\n")
    stdscr.refresh()

def connect_to_server(server, stdscr):
    _, ipv4, domain, user, password = server
    command = f"rdesktop {ipv4} -d {domain} -u {user} -p {password}"
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()
    subprocess.call(command, shell=True)
    stdscr.clear()
    stdscr.refresh()

def edit_server(server):
    # Funzione per modificare un server
    # Implementa il form di modifica qui
    pass

def write_server_list(filename, server_list):
    with open(filename, 'w') as file:
        for server in server_list:
            hostname, ipv4, domain, user, password = server
            file.write(f"{hostname},{ipv4},{domain},{user},{password}\n")

# Esempio di utilizzo
filename = "server_list.dat"  # Inserisci il nome del file contenente la lista dei server

server_list = read_server_list(filename)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    selected_index = 1
    display_server_list(stdscr, server_list, selected_index)

    while True:
        try:
            key = stdscr.getch()

            if key == curses.KEY_UP and selected_index > 1:
                selected_index -= 1
                display_server_list(stdscr, server_list, selected_index)
            elif key == curses.KEY_DOWN and selected_index < len(server_list):
                selected_index += 1
                display_server_list(stdscr, server_list, selected_index)
            elif key in range(ord('1'), ord('1') + len(server_list)):
                index = key - ord('1')
                selected_index = index + 1
                display_server_list(stdscr, server_list, selected_index)
            elif key == ord('\n'):
                connect_to_server(server_list[selected_index - 1], stdscr)
                display_server_list(stdscr, server_list, selected_index)
            elif key == ord('m') or key == ord('M'):
                edited_server = edit_server(server_list[selected_index - 1])
                server_list[selected_index - 1] = edited_server
                write_server_list(filename, server_list)
                display_server_list(stdscr, server_list, selected_index)

        except curses.error:
            pass

curses.wrapper(main)
