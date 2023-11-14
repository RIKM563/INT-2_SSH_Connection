from django.shortcuts import render, redirect
from .models import Information, Input
import psycopg2
from .forms import InfoForm
import paramiko


def results(request):
    info = Information.objects.all()
    return render(request, 'main/results.html', {'title': 'Главная страница', 'info': info})


def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            host = form.cleaned_data.get("hostname")
            user = form.cleaned_data.get("username")
            secret = form.cleaned_data.get("password")
            port = form.cleaned_data.get("port")

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=secret, port=port)

            stdin, stdout, stderr = client.exec_command('echo $(date) :arch hi;arch')
            data3 = stdout.read() + stderr.read()
            log3 = data3.decode('utf-8').split("hi")[0]
            data3 = data3.decode('utf-8').split("hi")[-1]
            stdin, stdout, stderr = client.exec_command('echo $(date) :uname -r hi;uname -r')
            data2 = stdout.read() + stderr.read()
            log2 = data2.decode('utf-8').split("hi")[0]
            data2 = data2.decode('utf-8').split("hi")[-1]
            stdin, stdout, stderr = client.exec_command('echo $(date) :cat /etc/issue hi;cat /etc/issue')
            data1 = stdout.read() + stderr.read()
            log1 = data1.decode('utf-8')[:-8].split("hi")[0]
            data1 = data1.decode('utf-8')[:-8].split("hi")[-1]
            data = ('Architecture: ' + data3 + '\n' + 'Version: ' + data2 + '\n' + 'Logs:\n' + log1 + '\n' + log2 + '\n'
                    + log3)
            print(data)
            client.close()

            connection = psycopg2.connect(user="user",
                                          password="12345678",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="postgres")
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO main_information (os, info)
                                       VALUES (%s,%s)"""
            record_to_insert = (data1, data)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            return redirect(results)

    form = InfoForm()
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)
