# Сelestia-nodes-explorer

This is a tool that allows you to explore the network of nodes in the Celestia blockchain. This allows you to view the statistics of the node (Validators, bridge, full storage, light), as well as information about the node and other characteristics.

Сelestia Nodes Explorer: http://94.131.100.195/

## Project preparation and launch

```sh
git clone git@github.com:AlexBesedin/celestia-nodes-explorer.git
```

## Install docker on the server:

```sh
sudo apt install docker.io 
```
## Install docker-compose on the server:

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
## Expand containers and collect static

```sh
cd celestia-nodes-explorer/infra/
sudo docker-compose up -d --build
sudo docker-compose exec backend python3 manage.py collectstatic --no-input
```
## Author:


[Alex Beszedin](https://github.com/AlexBesedin/)
