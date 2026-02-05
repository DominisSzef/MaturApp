using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using MaturAppApi.Models;

namespace MaturAppApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class PillsController : ControllerBase
{
    private readonly IMongoCollection<KnowledgePill> _pillsCollection;

    public PillsController(IMongoCollection<KnowledgePill> pillsCollection)
    {
        _pillsCollection = pillsCollection;
    }

    [HttpGet]
    public async Task<List<KnowledgePill>> Get() =>
        await _pillsCollection.Find(_ => true).ToListAsync();
}