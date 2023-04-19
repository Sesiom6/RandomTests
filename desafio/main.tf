#Escolhendo o provider e a região, passando as keys.
provider "aws" {
  region = var.aws_region
}

#Criando a VPC.
resource "aws_vpc" "vpc_test" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
}

#Criando subnet pública.
resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.vpc_test.id
  cidr_block = "10.0.1.0/24"
}

#Criando a instância no ec2.
resource "aws_instance" "webserver_test" {
  ami = var.instance_ami
  instance_type = var.instance_type
  subnet_id = aws_subnet.public_subnet.id   

  tags = {
    Name = "Instancia01"
  }
}

#Criando o security group.
resource "aws_security_group" "group01" {
  name_prefix = "group01"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

#Criando a regra do sg.
resource "aws_security_group_rule" "group01_rule" {
  security_group_id = aws_security_group.group01.id

  type        = "ingress"
  from_port   = 5432
  to_port     = 5432
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}

#Criando instancia e instalando.
resource "aws_instance" "Apache php" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.example_subnet.id
  user_data     = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker
              systemctl enable docker
              systemctl start docker
              docker run -d -p 80:80 php:7.4-apache
              docker run -d -p 5432