 using MongoDB.Bson;
 using MongoDB.Bson.Serialization.Attributes;

 namespace MaturAppApi.Models;

 public class KnowledgePill
 {
     // Ten atrybut mówi MongoDB, że to pole jest unikalnym identyfikatorem (Kluczem głównym)
     [BsonId]
     [BsonRepresentation(BsonType.ObjectId)]
     public string? Id { get; set; }

     // Nazwa pigułki (np. "Wzór na deltę")
     public string Title { get; set; } = null!;

     // Treść (np. "Δ = b² - 4ac")
     public string Content { get; set; } = null!;

     // Kategoria dla łatwiejszego filtrowania (np. "Funkcja kwadratowa")
     public string Category { get; set; } = null!;
 }