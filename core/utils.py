from paramiko import SSHClient, AutoAddPolicy


# username = 'user1'
# password = '12345678'
# port = 22
# ip = '192.168.2.97'


def exec_command(username, password, ip, cmd):
    conn = SSHClient()
    conn.set_missing_host_key_policy(AutoAddPolicy())
    # rsa_key = paramiko.RSAKey.from_private_key_file()

    conn.connect(ip, username=username, password=password, port=22)

    stdin, stdout, stderr = conn.exec_command(cmd)
    response = stdout.read().decode("utf-8")
    conn.close()
    return response

