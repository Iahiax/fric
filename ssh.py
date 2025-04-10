from fabric import Connection

def deploy():
    conn = Connection('xyahyax@ssh.pythonanywhere.com', connect_kwargs={'Yahia-1411': 'Yahia-1411'})
    conn.run('uname -a')  # عرض معلومات النظام
    conn.run('df -h')     # عرض المساحة التخزينية
    conn.close()
