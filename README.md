# Spotify Playlist Generator

Este projeto usa a API do Spotify para criar uma playlist privada com músicas recomendadas com base nas suas faixas favoritas.

## Requisitos

- Instale as dependências com: `pip install spotipy`
- Configure um aplicativo no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) para obter as credenciais (`client_id`, `client_secret`, `redirect_uri`).

## Como Usar

1. Substitua as credenciais no código.
2. Execute o script: `python script.py`.
3. Autentique-se no Spotify e insira o nome da sua playlist.
4. O script criará uma playlist privada com músicas recomendadas.

## Funcionalidades

- Gera uma playlist com base nas suas faixas favoritas.
- Cria a playlist automaticamente no seu perfil do Spotify.
