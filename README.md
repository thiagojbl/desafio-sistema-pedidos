## Desafio - Desenvolvedor Python e Django. 


### Você será o programador back-end de um sistema de pedidos, este sistema será feito por um front-end e um back-end, onde o front-end vai desenvolver as telas em um framework front-end como (react ou vue) e vai consumir os dados de sua API, que será desenvolvida em Python e Django Rest Framework. 


### Modelo de negócio a ser implementado
### Você vai desenvolver uma API que contemple:
#### 1) Cadastro de clientes (dados simples);
#### 2) Cadastro de produtos (dados simples);
#### 3) Cadastro de pedidos (dados do pedido, produtos, quantidades, dados do cliente)
### Para os 3, você vai implementar os métodos POST, GET, DELETE e UPDATE. Além destes, você vai implementar 3 endpoint personalizadas:
#### 1) Todos os pedidos por cliente (filtro pelo cliente);
#### 2) Faturamento total;
#### 3) Lucro total.


### Plus: Você sabe ou já trabalhou com AWS? (opcional)
#### Se sim, vamos avaliar seus conhecimentos de AWS EC2 (serviços de instâncias da AWS) utilizado para colocar sistemas web em um ambiente de uso real? Se você tem conhecimentos na área, pedimos que suba este projeto para uma instância gratuita da AWS também. Se você decidir fazer este desafio plus, no mesmo formulário de inscrição você vai mandar a URL da API já em modo de produção.


<div align="center"/> <img src="https://user-images.githubusercontent.com/64503493/179872720-d25f6bd1-b8a0-43bd-b21a-12624e1a531d.png"/> </div>


<hr>


## 🚀 Tecnologias
<p align="center">
    <a href="https://www.python.org/">Python</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.djangoproject.com/">Django</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.django-rest-framework.org/api-guide/viewsets/">Django Rest Framework</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.docker.com/">Docker</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.sqlite.org/cli.html/">SQLITE3</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://git-scm.com/">GIT</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://aws.amazon.com/">AWS</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.postman.com/">Postman</a>
</p>
<hr>

## ⚙️ Utilização

Para utilizar a aplicação basta acessar o link público: <a href="http://ec2-18-211-64-16.compute-1.amazonaws.com/"> Desafio-Thiago </a>.

<hr>

## Clone o repositório

    $ git clone https://github.com/thiagojbl/desafio-sistema-pedidos.git


### Execute no docker

   $  ```docker run -p 8000:8000 thiagojb12/desafio-thiago:3```

## Endpoints 

#### 1) Todos os pedidos por cliente (filtro pelo cliente):

  $ ```GET /api/pedido/?cliente=Jose```

#### 2) Faturamento total:

  $ ```GET /api/pedido/faturamento_total/```

#### 3) Lucro total:

  $ ```GET /api/pedido/lucro/```




#### Collections utilizadas neste projeto


[desafio.postman_collection.zip](https://github.com/thiagojbl/desafio-sistema-pedidos/files/9145635/desafio.postman_collection.zip)




  
