using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace MaturApp.Controllers;

[ApiController]
[Route("api/chat")]
public class ChatController : ControllerBase
{
    private readonly HttpClient _http;
    private readonly IConfiguration _config;

    public ChatController(IHttpClientFactory httpClientFactory, IConfiguration config)
    {
        _http = httpClientFactory.CreateClient();
        _config = config;
    }


    [HttpPost("ask")]
        public async Task<IActionResult> Chat([FromBody] ChatRequest request)
        {
            var apiKey = _config["OpenRouter:ApiKey"];
            if (string.IsNullOrEmpty(apiKey))
                return StatusCode(500, new { error = "Brak klucza API na serwerze" });

            if (request.Messages == null || request.Messages.Count == 0)
                return BadRequest(new { error = "Brak wiadomości z frontu" });

            var messages = new List<object>();


            bool isFirstMessage = true;
            foreach (var msg in request.Messages)
            {
                if (msg.Role == "user" && isFirstMessage)
                {
                    messages.Add(new {
                        role = "user",
                        content = "ZACHOWUJ SIĘ JAK MATURBOT (pomocny asystent matematyczny dla polskich uczniów. Odpowiadaj po polsku, krótko i konkretnie).\n\nPYTANIE UCZNIA:\n" + msg.Content
                    });
                    isFirstMessage = false;
                }
                else
                {

                    messages.Add(new { role = msg.Role, content = msg.Content });
                }
            }

            var payload = new
            {

                model = "google/gemma-3-4b-it:free",
                messages = messages,
                max_tokens = 500
            };

            var json = JsonSerializer.Serialize(payload);
            var httpRequest = new HttpRequestMessage(HttpMethod.Post, "https://openrouter.ai/api/v1/chat/completions");
            httpRequest.Headers.Add("Authorization", "Bearer " + apiKey);
            httpRequest.Headers.Add("HTTP-Referer", "https://maturapp.local");
            httpRequest.Headers.Add("X-Title", "MaturApp");
            httpRequest.Content = new StringContent(json, Encoding.UTF8, "application/json");

            try
            {
                var response = await _http.SendAsync(httpRequest);
                var responseBody = await response.Content.ReadAsStringAsync();

                if (!response.IsSuccessStatusCode)
                {
                    Console.WriteLine("BŁĄD OPENROUTER CZAT: " + responseBody);
                    return StatusCode(502, new { error = "Błąd API AI: " + responseBody });
                }

                var parsed = JsonSerializer.Deserialize<JsonElement>(responseBody);
                var content = parsed
                    .GetProperty("choices")[0]
                    .GetProperty("message")
                    .GetProperty("content")
                    .GetString();

                return Ok(new { reply = content });
            }
            catch (Exception ex)
            {
                Console.WriteLine("BŁĄD WEWNĘTRZNY C#: " + ex.Message);
                return StatusCode(500, new { error = ex.Message });
            }
        }
    }

public class ChatRequest
{
    [JsonPropertyName("messages")]
    public List<ChatMessage> Messages { get; set; } = new();
}

public class ChatMessage
{
    [JsonPropertyName("role")]
    public string Role { get; set; } = "";

    [JsonPropertyName("content")]
    public string Content { get; set; } = "";
}