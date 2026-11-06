# Microsserviços com Docker e Docker Swarm

Projeto prático desenvolvido como parte do bootcamp da DIO, demonstrando a utilização de containers Docker em um cenário de microsserviços.

## Arquitetura
- Aplicação PHP containerizada
- Banco de dados MySQL isolado
- Proxy reverso NGINX
- Orquestração com Docker Swarm
- Escalabilidade horizontal da aplicação

## Tecnologias utilizadas
- Docker
- Docker Swarm
- NGINX
- PHP 8
- MySQL 5.7

## Como executar o projeto

### Inicializar o Swarm
```bash
docker swarm init
````

### Subir a aplicação
```bash
docker stack deploy -c docker-compose.yml appstack
```

### Verificar serviços
```bash
docker service ls
```

### Escalar a aplicação
```bash
docker service scale appstack_app=5
```

### Objetivo

Demonstrar boas práticas de microsserviços, independência entre aplicações e infraestrutura, além de escalabilidade em ambientes cloud-native.
