using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using MaturAppApi.Models;

namespace MaturAppApi.Controllers;

[ApiController]
[Route("api/auth")]
public class AuthController : ControllerBase
{
    private readonly IMongoCollection<User> _users;

    public AuthController(IConfiguration config)
    {

        var client = new MongoClient(config.GetConnectionString("MongoDb"));
        var database = client.GetDatabase("MaturAppDb");
        _users = database.GetCollection<User>("Users");
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] User dto)
    {
        try
        {

            var user = await _users.Find(u => u.Username == dto.Username && u.Password == dto.Password).FirstOrDefaultAsync();

            if (user == null) return Unauthorized("Błędny login lub hasło");

            return Ok(new { username = user.Username, xp = user.Xp });
        }
        catch (Exception ex)
        {

            Console.WriteLine("Błąd logowania: " + ex.Message);
            return StatusCode(500, "Serwer: " + ex.Message);
        }
    }

    [HttpPost("register")]
    public async Task<IActionResult> Register([FromBody] User dto)
    {
        try
        {
            var existing = await _users.Find(u => u.Username == dto.Username).FirstOrDefaultAsync();
            if (existing != null) return BadRequest("Taki login jest zajęty");

            var newUser = new User { Username = dto.Username, Password = dto.Password, Xp = 0 };
            await _users.InsertOneAsync(newUser);
            return Ok("Utworzono konto");
        }
        catch (Exception ex)
        {
            return StatusCode(500, "Serwer: " + ex.Message);
        }
    }


    [HttpPost("add-xp")]
        public async Task<IActionResult> AddXp([FromBody] AddXpRequest request)
        {
            var user = await _users.Find(u => u.Username == request.Username).FirstOrDefaultAsync();
            if (user == null) return NotFound(new { message = "Nie znaleziono użytkownika" });

            // Dodajemy XP oraz +1 rozwiązane zadanie
            user.Xp += request.Xp;
            user.TasksCompleted += 1;

            // Zapisujemy obie rzeczy do bazy
            var update = Builders<User>.Update
                .Set(u => u.Xp, user.Xp)
                .Set(u => u.TasksCompleted, user.TasksCompleted);

            await _users.UpdateOneAsync(u => u.Username == request.Username, update);

            return Ok(new { message = "Zapisano postęp", currentXp = user.Xp, tasksCompleted = user.TasksCompleted });
        }

        public class AddXpRequest
        {
            public string Username { get; set; }
            public int Xp { get; set; }
        }

        [HttpGet("get-user")]
        public async Task<IActionResult> GetUser([FromQuery] string username)
        {
            var user = await _users.Find(u => u.Username == username).FirstOrDefaultAsync();
            if (user == null) return NotFound("Nie znaleziono użytkownika");

            // Zwracamy na front XP oraz liczbę zadań
            return Ok(new { username = user.Username, xp = user.Xp, tasksCompleted = user.TasksCompleted });
        }
}