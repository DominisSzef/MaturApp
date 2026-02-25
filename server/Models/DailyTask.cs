namespace MaturApp.Models
{
    public class DailyTask
    {
        public string Subject { get; set; } //
        public string Topic { get; set; }   //
        public string Question { get; set; } //
        public string ExpectedAnswer { get; set; }
        public int RewardPoints { get; set; }
    }
}