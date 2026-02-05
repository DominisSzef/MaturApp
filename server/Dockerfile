FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Kopiujemy konkretny plik projektu
COPY MaturAppApi.csproj .

# Przywracamy zależności
RUN dotnet restore "MaturAppApi.csproj"

# Kopiujemy resztę
COPY . .

# Budujemy
RUN dotnet publish "MaturAppApi.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .

# Uruchamiamy plik DLL o nowej nazwie
ENTRYPOINT ["dotnet", "MaturAppApi.dll"]