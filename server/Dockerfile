# Wybieramy obraz z SDK .NET, aby zbudować aplikację
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Kopiujemy plik projektu i pobieramy zależności
COPY *.csproj ./
RUN dotnet restore

# Kopiujemy resztę kodu i budujemy aplikację
COPY . .
RUN dotnet publish -c Release -o /app

# Budujemy finalny, lekki obraz do uruchomienia
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "MaturAppApi.dll"]