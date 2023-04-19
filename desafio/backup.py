import subprocess
import boto3
import os

#Configurações do banco de dados PostgreSQL
pg_user = 'usuario'
pg_password = 'senha'
pg_database = 'nomedobanco'
pg_host = 'localhost'
pg_port = '5432'

#Nome do arquivo de backup
backup_name = 'backup.sql'

#Diretório onde o arquivo de backup será gerado
backup_dir = '/tmp'

#Conexão com o banco de dados PostgreSQL e geração do backup
pg_dump_command = f"PGPASSWORD={pg_password} pg_dump -U {pg_user} -h {pg_host} -p {pg_port} {pg_database} > {backup_dir}/{backup_name}"
subprocess.call(pg_dump_command, shell=True)

#Configurações do cliente S3
s3_client = boto3.client('s3')
bucket_name = 'nomedobucket'
s3_key = f'backups/{backup_name}'

#Upload do arquivo de backup para o S3
with open(f'{backup_dir}/{backup_name}', 'rb') as backup_file:
    s3_client.upload_fileobj(backup_file, bucket_name, s3_key)

#Remoção do arquivo de backup local
os.remove(f'{backup_dir}/{backup_name}')

print("Backup concluído com sucesso e armazenado no S3")
