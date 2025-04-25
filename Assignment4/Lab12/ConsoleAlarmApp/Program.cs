using System;
using System.Threading;

namespace ConsoleAlarmApp
{
    public class AlarmPublisher
    {
        public event Action raiseAlarm;

        public void StartChecking(DateTime targetTime)
        {
            while (true)
            {
                if (DateTime.Now.Hour == targetTime.Hour &&
                    DateTime.Now.Minute == targetTime.Minute &&
                    DateTime.Now.Second == targetTime.Second)
                {
                    raiseAlarm?.Invoke();
                    break;
                }
                Thread.Sleep(1000);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter target time in HH:MM:SS format:");
            string input = Console.ReadLine();
            DateTime targetTime = DateTime.ParseExact(input, "HH:mm:ss", null);

            AlarmPublisher alarm = new AlarmPublisher();
            alarm.raiseAlarm += Ring_alarm;

            alarm.StartChecking(targetTime);
        }

        static void Ring_alarm()
        {
            Console.WriteLine("ALARM! Time has been reached!");
        }
    }
}
