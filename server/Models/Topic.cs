using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace MaturAppApi.Models;

public class Topic
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string? Id { get; set; }

        public string Title { get; set; } = null!;      // np. "1. Liczby rzeczywiste"
        public string Chapter { get; set; } = null!;    // np. "Rozdział I"
        public string TheoryHtml { get; set; } = "";    // Treść teorii
        public string TasksHtml { get; set; } = "";     // Treść zadań
    }

public class GuidedTask
{
    public string Question { get; set; } = null!;
    public List<string> Steps { get; set; } = new();
    public string FinalAnswer { get; set; } = null!;
}

public class PracticeTask
{
    public string Question { get; set; } = null!;
    public List<string> Options { get; set; } = new();
    public int CorrectIndex { get; set; }
    public string Difficulty { get; set; } = "Easy"; // Easy, Medium, Hard
    public string Explanation { get; set; } = null!;
}