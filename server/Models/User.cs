using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace MaturAppApi.Models;

public class User
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? Id { get; set; }

    public string Username { get; set; } = null!;
    public string Password { get; set; } = null!; // W prawdziwym życiu hashujemy hasła!

    // Gamifikacja
    public int DailyStreak { get; set; } = 0;     // Dni pod rząd
    public DateTime LastLogin { get; set; }       // Żeby sprawdzać streak
    public int Xp { get; set; } = 0;              // Punkty doświadczenia
    public List<string> CompletedTopics { get; set; } = new(); // Zalicone działy
}