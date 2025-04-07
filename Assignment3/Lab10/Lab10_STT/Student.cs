using System;

class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
    public double Marks { get; set; }

    public Student(string name, int id, double marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    public string GetGrade()
    {
        if (Marks >= 90) return "A";
        if (Marks >= 75) return "B";
        if (Marks >= 60) return "C";
        return "F";
    }

    public void Display()
    {
        Console.WriteLine($"Student: {Name}, ID: {ID}, Marks: {Marks}, Grade: {GetGrade()}");
    }
}
