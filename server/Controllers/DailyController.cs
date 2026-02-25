using Microsoft.AspNetCore.Mvc;
using MaturApp.Models;
using System;
using System.Collections.Generic;

namespace MaturApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class DailyController : ControllerBase
    {

        private static readonly List<DailyTask> _mathTasks = new List<DailyTask>
        {
            // Liczby rzeczywiste i logarytmy
            new DailyTask { Subject = "Matematyka", Topic = "Logarytmy", Question = "Oblicz wartość wyrażenia: log_2(16) + log_3(27).", ExpectedAnswer = "7", RewardPoints = 50 },
            new DailyTask { Subject = "Matematyka", Topic = "Potęgi i pierwiastki", Question = "Oblicz: (2^3)^2 / 2^4.", ExpectedAnswer = "4", RewardPoints = 40 },
            new DailyTask { Subject = "Matematyka", Topic = "Procenty", Question = "Cena butów po obniżce o 20% wynosi 160 zł. Jaka była cena początkowa?", ExpectedAnswer = "200", RewardPoints = 45 },

            // Wyrażenia algebraiczne i równania
            new DailyTask { Subject = "Matematyka", Topic = "Wzory skróconego mnożenia", Question = "Oblicz wartość wyrażenia (x-2)^2 dla x = 5.", ExpectedAnswer = "9", RewardPoints = 30 },
            new DailyTask { Subject = "Matematyka", Topic = "Równania kwadratowe", Question = "Podaj mniejszy z pierwiastków równania: x^2 - 5x + 6 = 0.", ExpectedAnswer = "2", RewardPoints = 60 },
            new DailyTask { Subject = "Matematyka", Topic = "Układy równań", Question = "Rozwiąż układ równań: x+y=5 i x-y=1. Podaj wartość x.", ExpectedAnswer = "3", RewardPoints = 50 },

            // Funkcje
            new DailyTask { Subject = "Matematyka", Topic = "Funkcja kwadratowa", Question = "Podaj współrzędną x wierzchołka paraboli o równaniu y = x^2 - 4x + 3.", ExpectedAnswer = "2", RewardPoints = 55 },
            new DailyTask { Subject = "Matematyka", Topic = "Funkcja liniowa", Question = "Dla jakiego m funkcja y = (m-3)x + 2 jest stała?", ExpectedAnswer = "3", RewardPoints = 40 },
            new DailyTask { Subject = "Matematyka", Topic = "Własności funkcji", Question = "Podaj miejsce zerowe funkcji y = 2x - 8.", ExpectedAnswer = "4", RewardPoints = 35 },

            // Ciągi
            new DailyTask { Subject = "Matematyka", Topic = "Ciąg arytmetyczny", Question = "W ciągu arytmetycznym a1 = 3, r = 4. Oblicz piąty wyraz tego ciągu (a5).", ExpectedAnswer = "19", RewardPoints = 50 },
            new DailyTask { Subject = "Matematyka", Topic = "Ciąg geometryczny", Question = "W ciągu geometrycznym a1 = 2, q = 3. Oblicz trzeci wyraz tego ciągu (a3).", ExpectedAnswer = "18", RewardPoints = 55 },

            // Geometria (Planimetria i Analityczna)
            new DailyTask { Subject = "Matematyka", Topic = "Planimetria", Question = "Oblicz pole trójkąta prostokątnego o przyprostokątnych 6 i 8.", ExpectedAnswer = "24", RewardPoints = 40 },
            new DailyTask { Subject = "Matematyka", Topic = "Planimetria", Question = "Długość przekątnej kwadratu wynosi 4√2. Jaki jest obwód tego kwadratu?", ExpectedAnswer = "16", RewardPoints = 50 },
            new DailyTask { Subject = "Matematyka", Topic = "Geometria analityczna", Question = "Podaj współczynnik kierunkowy prostej prostopadłej do prostej y = 2x + 1.", ExpectedAnswer = "-0.5", RewardPoints = 60 },
            new DailyTask { Subject = "Matematyka", Topic = "Geometria analityczna", Question = "Oblicz odległość między punktami A=(0,0) i B=(3,4).", ExpectedAnswer = "5", RewardPoints = 45 },

            // Stereometria
            new DailyTask { Subject = "Matematyka", Topic = "Stereometria", Question = "Krawędź sześcianu ma długość 3. Oblicz jego objętość.", ExpectedAnswer = "27", RewardPoints = 30 },
            new DailyTask { Subject = "Matematyka", Topic = "Stereometria", Question = "Oblicz pole powierzchni całkowitej sześcianu o krawędzi 2.", ExpectedAnswer = "24", RewardPoints = 40 },

            // Prawdopodobieństwo i statystyka
            new DailyTask { Subject = "Matematyka", Topic = "Statystyka", Question = "Oblicz średnią arytmetyczną zestawu liczb: 2, 4, 6, 8, 10.", ExpectedAnswer = "6", RewardPoints = 30 },
            new DailyTask { Subject = "Matematyka", Topic = "Statystyka", Question = "Podaj medianę zestawu danych: 1, 3, 5, 7, 9, 11.", ExpectedAnswer = "6", RewardPoints = 40 },
            new DailyTask { Subject = "Matematyka", Topic = "Prawdopodobieństwo", Question = "Rzucamy raz sześcienną kostką do gry. Jakie jest prawdopodobieństwo wyrzucenia liczby oczek większej niż 4? (Zapisz jako ułamek np. 1/3)", ExpectedAnswer = "1/3", RewardPoints = 60 }
        };

        [HttpGet("task-of-the-day")]
        public IActionResult GetDailyTask()
        {

            int dayOfYear = DateTime.UtcNow.DayOfYear;


            Random rand = new Random(dayOfYear);


            int randomIndex = rand.Next(_mathTasks.Count);
            var todaysTask = _mathTasks[randomIndex];

            return Ok(todaysTask);
        }
    }
}