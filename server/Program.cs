using MaturAppApi.Models;
using MongoDB.Driver;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddHttpClient();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});


var mongoConnectionString = builder.Configuration.GetConnectionString("MongoDb") ?? "mongodb://localhost:27017";
var mongoDatabaseName = builder.Configuration["MongoDb:DatabaseName"] ?? "MaturAppDb";

var mongoClient = new MongoClient(mongoConnectionString);
var mongoDatabase = mongoClient.GetDatabase(mongoDatabaseName);

// Rejestrujemy kolekcje tak żeby PillsController mógł je dostać przez DI
builder.Services.AddSingleton<IMongoClient>(mongoClient);
builder.Services.AddSingleton(mongoDatabase);
builder.Services.AddSingleton(mongoDatabase.GetCollection<KnowledgePill>("Pills"));
builder.Services.AddSingleton(mongoDatabase.GetCollection<Topic>("Topics"));

var app = builder.Build();

// KOLEJNOŚĆ JEST WAŻNA!
app.UseCors("AllowAll");

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();
app.MapControllers();
app.Run();