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
        // Tutaj jest bezpieczne połączenie
        var client = new MongoClient(config.GetConnectionString("MongoDb"));
        var database = client.GetDatabase("MaturAppDb");
        _users = database.GetCollection<User>("Users");
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] User dto)
    {
        try
        {
            // Sprawdź czy User istnieje w bazie
            var user = await _users.Find(u => u.Username == dto.Username && u.Password == dto.Password).FirstOrDefaultAsync();

            if (user == null) return Unauthorized("Błędny login lub hasło");

            return Ok(new { username = user.Username, xp = user.Xp });
        }
        catch (Exception ex)
        {
            // Zamiast 500, wypisze błąd w konsoli
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
}