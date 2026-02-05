using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using MaturAppApi.Models; // <--- WAŻNE: Odwołujemy się do nowego namespace

namespace MaturAppApi.Controllers; // Zmienione z 'server.Controllers'

[ApiController]
[Route("api/topics")]
public class TopicController : ControllerBase
{
    private readonly IMongoCollection<Topic> _topics;

    public TopicController(IConfiguration config)
    {
        var client = new MongoClient(config.GetConnectionString("MongoDb"));
        var database = client.GetDatabase("MaturAppDb");
        _topics = database.GetCollection<Topic>("Topics");
    }

    [HttpGet]
    public async Task<List<Topic>> GetTopics()
    {
        return await _topics.Find(_ => true).ToListAsync();
    }

    [HttpPost]
    public async Task<IActionResult> CreateTopic([FromBody] Topic newTopic)
    {
        if (newTopic == null) return BadRequest("Brak danych");

        var existing = await _topics.Find(t => t.Title == newTopic.Title).FirstOrDefaultAsync();
        if (existing != null)
        {
            newTopic.Id = existing.Id;
            await _topics.ReplaceOneAsync(t => t.Id == existing.Id, newTopic);
            return Ok(new { message = "Zaktualizowano temat", id = existing.Id });
        }

        await _topics.InsertOneAsync(newTopic);
        return CreatedAtAction(nameof(GetTopics), new { id = newTopic.Id }, newTopic);
    }
}