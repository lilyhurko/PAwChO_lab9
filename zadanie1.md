# ============================

# Zadanie 3:

# ============================

a. Zbudowanie obrazu kontenera
docker build -t app .
To polecenie tworzy obraz kontenera na podstawie pliku Dockerfile znajdującego się w katalogu, w którym aktualnie pracujesz. Obraz zostaje nazwany app, co umożliwia późniejsze jego uruchomienie lub modyfikowanie.

b. Uruchomienie kontenera
docker run -p 5000:5000 app
Uruchamia kontener zbudowany z obrazu app. Mapuje port 5000 kontenera na port 5000 hosta, co oznacza, że aplikacja działająca w kontenerze będzie dostępna pod tym samym portem.

c. Uzyskanie informacji wygenerowanych przez serwer przy starcie (logi)
Jeśli kontener działa w trybie pierwszoplanowym, logi są od razu widoczne w terminalu, np.:
2025-05-06 06:41:33,980 - Autor aplikacji: Lilia Hurko
2025-05-06 06:41:33,980 - Aplikacja nasłuchuje na porcie TCP: 5000
2025-05-06 06:41:33,981 - 127.0.0.1 - - [06/May/2025 06:41:33] "GET / HTTP/1.1" 200 -
2025-05-06 06:42:04,049 - Aplikacja uruchomiona: 2025-05-06 06:42:04.049446
Lub tak, jezeli aplikacja dziala w tle:
docker logs <ID_lub_nazwa_kontenera>
docker ps # aby sprawdzić nazwę/ID kontenera

d. Sprawdzenie liczby warstw obrazu
docker history app
To polecenie pokazuje historię obrazu app, w tym informacje o każdej z warstw, które zostały utworzone w trakcie budowania obrazu.

IMAGE CREATED CREATED BY SIZE COMMENT
f5fd39319885 9 minutes ago CMD ["python" "app.py"] 0B buildkit.dockerfile.v0
<missing> 9 minutes ago EXPOSE map[5000/tcp:{}] 0B buildkit.dockerfile.v0
<missing> 9 minutes ago HEALTHCHECK &{["CMD-SHELL" "curl -f http://l… 0B buildkit.dockerfile.v0
