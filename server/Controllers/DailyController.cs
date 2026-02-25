using Microsoft.AspNetCore.Mvc;
using MaturApp.Models;
using System.Text;
using System.Text.Json;

namespace MaturApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class DailyController : ControllerBase
    {
        private readonly IConfiguration _config;
        private readonly HttpClient _http;

        private static readonly List<string> _topics = new()
        {
            "Logarytmy", "Potegi i pierwiastki", "Procenty",
            "Wzory skroconego mnozenia", "Rownania kwadratowe", "Uklady rownan",
            "Funkcja kwadratowa", "Funkcja liniowa", "Wlasnosci funkcji",
            "Ciag arytmetyczny", "Ciag geometryczny",
            "Planimetria", "Geometria analityczna", "Stereometria",
            "Statystyka opisowa", "Prawdopodobienstwo", "Trygonometria"
        };

        public DailyController(IConfiguration config)
        {
            _config = config;
            _http = new HttpClient();
        }

        [HttpGet("task-of-the-day")]
        public async Task<IActionResult> GetDailyTask()
        {
            int seed = DateTime.UtcNow.DayOfYear + DateTime.UtcNow.Year * 1000;
            var rng = new Random(seed);
            var topic = _topics[rng.Next(_topics.Count)];

            try
            {
                var task = await GenerateTaskWithAI(topic);
                return Ok(task);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Blad AI: {ex.Message} - uzywam fallbacku");
                Console.WriteLine($"Szczegoly: {ex}");
                return Ok(GetFallbackTask(topic));
            }
        }

        [HttpGet("task-by-topic/{topic}")]
        public async Task<IActionResult> GetTaskByTopic(string topic)
        {
            try
            {
                var task = await GenerateTaskWithAI(topic);
                return Ok(task);
            }
            catch (Exception ex)
            {
                return StatusCode(500, new { error = ex.Message });
            }
        }

        private async Task<DailyTask> GenerateTaskWithAI(string topic)
        {
            var apiKey = _config["OpenRouter:ApiKey"];
            if (string.IsNullOrEmpty(apiKey))
                throw new Exception("Brak klucza API OpenRouter w appsettings.json");

            var prompt = "Wygeneruj jedno zadanie maturalne z matematyki na temat: " + topic + ".\n" +
                         "Poziom: matura podstawowa (Polska, liceum).\n\n" +
                         "Odpowiedz TYLKO czystym JSON (bez markdown, bez ```), w dokladnie tym formacie:\n" +
                         "{\n" +
                         "  \"subject\": \"Matematyka\",\n" +
                         "  \"topic\": \"" + topic + "\",\n" +
                         "  \"question\": \"tresc zadania\",\n" +
                         "  \"expectedAnswer\": \"odpowiedz (tylko liczba lub wyrazenie, np. 4 albo 1/3)\",\n" +
                         "  \"rewardPoints\": 50\n" +
                         "}\n\n" +
                         "Zasady:\n" +
                         "- Pytanie musi byc po polsku\n" +
                         "- Odpowiedz to jedna liczba lub prosty ulamek\n" +
                         "- rewardPoints od 30 do 70 w zaleznosci od trudnosci\n" +
                         "- Nie dodawaj zadnego tekstu poza JSON";

            var requestBody = new
            {
                model = "google/gemma-3-4b-it:free",
                max_tokens = 500,
                messages = new[]
                {
                    new { role = "user", content = prompt }
                }
            };

            var json = JsonSerializer.Serialize(requestBody);
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            _http.DefaultRequestHeaders.Clear();
            _http.DefaultRequestHeaders.Add("Authorization", "Bearer " + apiKey);
            _http.DefaultRequestHeaders.Add("HTTP-Referer", "https://maturapp.local");
            _http.DefaultRequestHeaders.Add("X-Title", "MaturApp");

            var response = await _http.PostAsync("https://openrouter.ai/api/v1/chat/completions", content);
            var responseString = await response.Content.ReadAsStringAsync();

            Console.WriteLine($"OpenRouter response: {responseString}");

            if (!response.IsSuccessStatusCode)
                throw new Exception($"API error {response.StatusCode}: {responseString}");

            using var doc = JsonDocument.Parse(responseString);
            var text = doc.RootElement
                .GetProperty("choices")[0]
                .GetProperty("message")
                .GetProperty("content")
                .GetString() ?? "";

            text = text.Trim();
            if (text.StartsWith("```"))
                text = text.Replace("```json", "").Replace("```", "").Trim();

            var task = JsonSerializer.Deserialize<DailyTask>(text, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            return task ?? throw new Exception("Nie udalo sie sparsowac odpowiedzi AI");
        }

        private static DailyTask GetFallbackTask(string topic)
        {
            return new DailyTask
            {
                Subject = "Matematyka",
                Topic = topic,
                Question = "Zadanie z dzialu " + topic + " jest chwilowo niedostepne. Sprobuj ponownie za chwile.",
                ExpectedAnswer = "?",
                RewardPoints = 0
            };
        }
    }
}