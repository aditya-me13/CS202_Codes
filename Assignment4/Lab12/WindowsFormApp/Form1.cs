using System;
using System.Drawing;
using System.Windows.Forms;

namespace WindowsFormApp
{
    public partial class Form1 : Form
    {
        private System.Windows.Forms.Timer timer;
        private DateTime targetTime;
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
            timer = new System.Windows.Forms.Timer();
            timer.Interval = 1000; // 1 second
            timer.Tick += Timer_Tick;
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            if (DateTime.TryParse(textBoxTime.Text, out targetTime))
            {
                targetTime = DateTime.Today.Add(targetTime.TimeOfDay);
                timer.Start();
            }
            else
            {
                MessageBox.Show("Invalid time format. Use HH:MM:SS format.", 
                    "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            this.BackColor = Color.FromArgb(random.Next(256), random.Next(256), random.Next(256));

            if (DateTime.Now >= targetTime)
            {
                timer.Stop();
                MessageBox.Show("Target time reached!", "Time Up", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {
            // No action needed
        }
    }
}
