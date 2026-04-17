# 🔷 C# & .NET 10 Cheatsheet — Beginner to Master
> Comprehensive reference from first `Console.WriteLine` to production-grade patterns

---

## Table of Contents

**Beginner**

1. [Program Structure & Top-Level Statements](#1-program-structure--top-level-statements)
2. [Variables, Types & Literals](#2-variables-types--literals)
3. [String Handling](#3-string-handling)
4. [Operators & Expressions](#4-operators--expressions)
5. [Console I/O](#5-console-io)
6. [Conditional Logic](#6-conditional-logic)
7. [Loops](#7-loops)
8. [Arrays](#8-arrays)
9. [Methods](#9-methods)
10. [Exceptions](#10-exceptions)

**Intermediate**

11. [Collections — List, Dictionary, HashSet, Queue, Stack](#11-collections)
12. [Classes & OOP](#12-classes--oop)
13. [Interfaces & Abstract Classes](#13-interfaces--abstract-classes)
14. [Inheritance & Polymorphism](#14-inheritance--polymorphism)
15. [Properties, Indexers & Operator Overloading](#15-properties-indexers--operator-overloading)
16. [Structs & Records](#16-structs--records)
17. [Enums](#17-enums)
18. [Generics](#18-generics)
19. [Delegates, Events & Func/Action](#19-delegates-events--funcaction)
20. [LINQ](#20-linq)

**Advanced**

21. [Nullable Reference Types](#21-nullable-reference-types)
22. [Pattern Matching](#22-pattern-matching)
23. [Tuples & Deconstruction](#23-tuples--deconstruction)
24. [Extension Methods](#24-extension-methods)
25. [Iterators & yield](#25-iterators--yield)
26. [Anonymous Types & Dynamic](#26-anonymous-types--dynamic)
27. [Lambda & Closures](#27-lambda--closures)
28. [Attributes & Reflection](#28-attributes--reflection)
29. [File & Stream I/O](#29-file--stream-io)
30. [Async / Await & Task Parallel Library](#30-async--await--task-parallel-library)

**Master / .NET 10**

31. [Span\<T\>, Memory\<T\> & Unsafe Code](#31-spant-memoryt--unsafe-code)
32. [Concurrency — Channels, Parallel, PLINQ](#32-concurrency--channels-parallel-plinq)
33. [Dependency Injection](#33-dependency-injection)
34. [Configuration & Options Pattern](#34-configuration--options-pattern)
35. [Entity Framework Core](#35-entity-framework-core)
36. [ASP.NET Core & Minimal APIs](#36-aspnet-core--minimal-apis)
37. [Logging with ILogger](#37-logging-with-ilogger)
38. [Testing — xUnit & Moq](#38-testing--xunit--moq)
39. [C# 13 / .NET 10 New Features](#39-c-13--net-10-new-features)
40. [Idiomatic C# Patterns & Tips](#40-idiomatic-c-patterns--tips)

---

# BEGINNER

---

## 1. Program Structure & Top-Level Statements

```csharp
// .NET 6+ — top-level statements (no class/Main boilerplate needed)
Console.WriteLine("Hello, World!");

// Traditional entry point (still valid, required for some scenarios)
namespace MyApp;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        Console.WriteLine($"Args: {args.Length}");
    }
}

// async Main
static async Task Main(string[] args)
{
    await DoWorkAsync();
}

// Namespaces — file-scoped (C# 10+, preferred)
namespace MyApp.Services;

// Old block-scoped style
namespace MyApp.Services
{
    class MyService { }
}

// using directives — put at top of file
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

// Global usings (in any .cs file or a GlobalUsings.cs — applied project-wide)
global using System;
global using System.Collections.Generic;
// .NET 6+ SDK projects add common global usings automatically

// Regions (use sparingly)
#region Helpers
void Helper() { }
#endregion
```

---

## 2. Variables, Types & Literals

```csharp
// Implicit typing with var (type inferred at compile time — not dynamic)
var name    = "Alice";          // string
var age     = 25;               // int
var height  = 5.7;              // double
var pi      = 3.14f;            // float
var big     = 9_999_999_999L;   // long  (digit separators for readability)
var money   = 19.99m;           // decimal  (financial — no floating-point error)
var flag    = true;             // bool
var letter  = 'A';              // char
var nothing = (object?)null;    // null

// Explicit types
string  firstName = "Bob";
int     count     = 42;
double  ratio     = 0.618;
float   temp      = 36.6f;
decimal price     = 9.99m;
long    bigNum    = 10_000_000_000L;
bool    isActive  = false;
char    grade     = 'A';
byte    b         = 255;
short   s         = 32_000;
uint    u         = 4_000_000_000u;
object  obj       = "anything";

// Constants
const double Pi      = 3.14159265358979;
const int    MaxSize = 100;

// Readonly (set once — in constructor or inline)
readonly int _id;

// Default values
int    defaultInt    = default;   // 0
bool   defaultBool   = default;   // false
string defaultString = default!;  // null (! = null-forgiving operator)

// Type aliases (C# 12+)
using Point = (double X, double Y);
Point origin = (0.0, 0.0);

// Numeric literals
int hex  = 0xFF;                  // 255
int bin  = 0b1111_0000;           // 240
long sci = 1_000_000L;

// Checked arithmetic (throws OverflowException instead of wrapping)
checked
{
    int max = int.MaxValue;
    int overflow = max + 1;       // throws OverflowException
}

// Type system hierarchy
// object → string, ValueType → int/double/bool/struct/enum
```

### Value Types vs Reference Types

| | Value Types | Reference Types |
|---|---|---|
| Examples | int, double, bool, struct, enum | class, string, array, interface, delegate |
| Stored | Stack (usually) | Heap |
| Copies | Independent copy | Shared reference |
| Default | 0 / false / struct default | null |
| Nullable | `int?` | already nullable |

---

## 3. String Handling

```csharp
string s = "Hello, World!";

// Length & access
s.Length                        // 13
s[0]                            // 'H'
s[^1]                           // '!'  (index from end, C# 8+)

// Common methods
s.ToUpper()                     // "HELLO, WORLD!"
s.ToLower()                     // "hello, world!"
s.Trim()                        // remove whitespace both ends
s.TrimStart()
s.TrimEnd()
s.Replace("World", "C#")        // "Hello, C#!"
s.Contains("World")             // true
s.StartsWith("Hello")           // true
s.EndsWith("!")                 // true
s.IndexOf("World")              // 7
s.LastIndexOf('l')              // 10
s.Substring(7, 5)               // "World"
s[7..12]                        // "World" (range syntax, C# 8+)
s.Split(',')                    // ["Hello", " World!"]
s.Split(',', StringSplitOptions.TrimEntries) // trims each part
string.Join(", ", new[]{"a","b","c"})  // "a, b, c"
s.PadLeft(20)
s.PadRight(20, '-')
s.Remove(5)                     // "Hello"
s.Insert(5, " Beautiful")
s.ToCharArray()
string.IsNullOrEmpty(s)         // false
string.IsNullOrWhiteSpace("  ") // true
s.Equals("hello", StringComparison.OrdinalIgnoreCase)

// Slicing with ranges
string hello = s[..5];          // "Hello"
string world = s[7..12];        // "World"

// Interpolated strings
string msg = $"Hello, {name}! You are {age} years old.";
string fmt = $"Pi is {Math.PI:F4}";    // "Pi is 3.1416"
string pad = $"{age,10}";              // right-aligned in 10 chars
string padL = $"{name,-10}";           // left-aligned

// Verbatim strings (ignore escape sequences)
string path = @"C:\Users\Alice\Documents\file.txt";
string multiLine = @"Line 1
Line 2
Line 3";

// Raw string literals (C# 11+) — no escaping needed
string json = """
    {
        "name": "Alice",
        "age": 25
    }
    """;

// Interpolated raw strings
string greeting = $"""Hello, {name}! Welcome to "C#".""";

// StringBuilder — efficient for many concatenations
using System.Text;
var sb = new StringBuilder();
sb.Append("Hello");
sb.Append(", ");
sb.AppendLine("World!");
sb.Insert(0, ">> ");
sb.Replace("World", "C#");
string result = sb.ToString();

// String.Format (older style, still common in logging)
string old = string.Format("Name: {0}, Age: {1}", name, age);

// Span<char> for zero-allocation slicing
ReadOnlySpan<char> span = s.AsSpan(7, 5);   // no allocation
```

---

## 4. Operators & Expressions

```csharp
// Arithmetic
int a = 10 + 3;     // 13
int b = 10 - 3;     // 7
int c = 10 * 3;     // 30
double d = 10 / 3.0; // 3.333...
int e = 10 / 3;     // 3   (integer division)
int f = 10 % 3;     // 1   (modulo)
double g = Math.Pow(2, 10);  // 1024

// Compound assignment
x += 5;  x -= 3;  x *= 2;  x /= 4;  x %= 3;
x++;  x--;  ++x;  --x;

// Comparison
==  !=  >  <  >=  <=

// Logical
&&   ||   !
&    |    ^   (bitwise/non-short-circuit logical)

// Bitwise
&    |    ^    ~    <<    >>    >>>   (unsigned right shift, C# 11+)
x &= mask;  x |= flag;  x ^= toggle;
x <<= 2;    x >>= 1;

// Null-related
string? s = null;
s ??= "default";        // assign if null
string t = s ?? "default";     // null-coalescing
int len = s?.Length ?? 0;      // null-conditional + coalescing
s?.ToUpper()?.Trim();           // chain null-conditionals

// Conditional (ternary)
string label = age >= 18 ? "Adult" : "Minor";

// typeof, nameof, sizeof
Type t = typeof(int);
string name = nameof(Console.WriteLine);    // "WriteLine"
int size = sizeof(int);                     // 4

// is and as
if (obj is string str)          // pattern + declaration
    Console.WriteLine(str.Length);

string? asStr = obj as string;  // null if not string

// checked / unchecked
int result = checked(int.MaxValue + 1);    // throws
int wrapped = unchecked(int.MaxValue + 1); // -2147483648

// Operator precedence (high → low)
// ()  →  ++x --x  →  * / %  →  + -  →  << >>  →  < > <= >=
// →  == !=  →  &  →  ^  →  |  →  &&  →  ||  →  ??  →  ?:  →  =
```

---

## 5. Console I/O

```csharp
// Output
Console.WriteLine("Hello");           // with newline
Console.Write("Enter name: ");        // no newline
Console.WriteLine($"Pi = {Math.PI:F2}");
Console.Error.WriteLine("Error!");    // stderr

// Format specifiers in WriteLine
Console.WriteLine("{0:C}", 9.99);     // $9.99  (currency)
Console.WriteLine("{0:D5}", 42);      // 00042  (decimal padded)
Console.WriteLine("{0:F3}", 3.14159); // 3.142  (fixed point)
Console.WriteLine("{0:E2}", 1234567); // 1.23E+006
Console.WriteLine("{0:P}", 0.1234);   // 12.34%
Console.WriteLine("{0:X}", 255);      // FF     (hex)
Console.WriteLine("{0:N0}", 1000000); // 1,000,000

// Input
string? line = Console.ReadLine();    // returns null at EOF
int n = int.Parse(Console.ReadLine()!);
int.TryParse(Console.ReadLine(), out int parsed);  // safe parse

// Clear, beep, cursor
Console.Clear();
Console.SetCursorPosition(10, 5);
Console.ForegroundColor = ConsoleColor.Green;
Console.BackgroundColor = ConsoleColor.Black;
Console.ResetColor();

// Command-line args (top-level)
// dotnet run -- arg1 arg2
foreach (var arg in args)
    Console.WriteLine(arg);
```

---

## 6. Conditional Logic

```csharp
// if / else if / else
int score = 78;
if (score >= 90)
    Console.WriteLine("A");
else if (score >= 75)
    Console.WriteLine("B");
else if (score >= 60)
    Console.WriteLine("C");
else
    Console.WriteLine("F");

// switch statement
switch (score / 10)
{
    case 10:
    case 9:
        Console.WriteLine("A"); break;
    case 8:
        Console.WriteLine("B"); break;
    case 7:
        Console.WriteLine("C"); break;
    default:
        Console.WriteLine("F"); break;
}

// switch expression (C# 8+ — preferred)
string grade = score switch
{
    >= 90        => "A",
    >= 75        => "B",
    >= 60        => "C",
    _            => "F"      // _ is discard/default
};

// Pattern matching in switch
object shape = new Circle(5.0);
double area = shape switch
{
    Circle c              => Math.PI * c.Radius * c.Radius,
    Rectangle r           => r.Width * r.Height,
    Triangle { Base: var b, Height: var h } => 0.5 * b * h,
    null                  => throw new ArgumentNullException(nameof(shape)),
    _                     => throw new InvalidOperationException()
};

// Conditional expressions
bool isAdult = age >= 18;
string msg = isAdult ? "Welcome" : "Access denied";

// when guards in switch
string category = temperature switch
{
    < 0                  => "Freezing",
    >= 0 and < 10        => "Cold",
    >= 10 and < 20       => "Cool",
    >= 20 and < 30       => "Warm",
    _                    => "Hot"
};
```

---

## 7. Loops

```csharp
// for
for (int i = 0; i < 10; i++)
    Console.WriteLine(i);

for (int i = 10; i >= 0; i -= 2)
    Console.Write($"{i} ");

// foreach
string[] fruits = { "apple", "banana", "cherry" };
foreach (var fruit in fruits)
    Console.WriteLine(fruit);

// foreach with index (no built-in — use LINQ or local var)
foreach (var (fruit, i) in fruits.Select((f, i) => (f, i)))
    Console.WriteLine($"{i}: {fruit}");

// while
int count = 0;
while (count < 5)
{
    Console.WriteLine(count);
    count++;
}

// do-while (always executes at least once)
do
{
    Console.Write("Enter positive number: ");
    int.TryParse(Console.ReadLine(), out count);
} while (count <= 0);

// Loop control
for (int i = 0; i < 20; i++)
{
    if (i % 2 == 0) continue;  // skip even
    if (i > 15)     break;     // stop
    Console.WriteLine(i);
}

// Nested loop with labeled break — use goto (rare but valid)
for (int i = 0; i < 5; i++)
    for (int j = 0; j < 5; j++)
    {
        if (i + j > 6) goto done;
        Console.WriteLine($"{i},{j}");
    }
done:

// foreach over ranges (C# 8+)
foreach (int i in 1..11)   // not directly valid — use:
foreach (int i in Enumerable.Range(1, 10))
    Console.WriteLine(i);

// Infinite loop patterns
while (true)
{
    // break on condition
    break;
}
```

---

## 8. Arrays

```csharp
// Declaration & initialization
int[] nums = new int[5];                    // [0,0,0,0,0]
int[] primes = { 2, 3, 5, 7, 11 };         // collection initializer
int[] squares = new int[] { 1, 4, 9, 16 };
var mixed = new[] { 1, 2, 3 };             // type inferred

// Access
primes[0]       // 2
primes[^1]      // 11  (index from end)
primes[^2]      // 7

// Ranges (C# 8+)
int[] slice = primes[1..4];     // [3, 5, 7]  (from 1, up to not including 4)
int[] last2 = primes[^2..];     // [7, 11]
int[] copy  = primes[..];       // full copy

// Properties & methods
primes.Length           // 5
Array.Sort(nums);
Array.Reverse(nums);
Array.Find(nums, x => x > 3);
Array.FindAll(nums, x => x % 2 == 0);
Array.IndexOf(primes, 5);       // 2
Array.Fill(nums, 99);
Array.Copy(primes, nums, 3);
Array.Clear(nums, 0, nums.Length);

// Multidimensional
int[,] matrix = new int[3, 3];
int[,] grid = { {1,2,3}, {4,5,6}, {7,8,9} };
grid[1, 2]      // 6
grid.GetLength(0)   // 3 (rows)
grid.GetLength(1)   // 3 (cols)

// Jagged array (array of arrays — more flexible)
int[][] jagged = new int[3][];
jagged[0] = new[] { 1, 2 };
jagged[1] = new[] { 3, 4, 5 };
jagged[2] = new[] { 6 };

// Span<T> — stack-allocated slice (no heap allocation)
Span<int> span = primes.AsSpan(1, 3);  // slice without copy
```

---

## 9. Methods

```csharp
// Basic method
static int Add(int a, int b)
{
    return a + b;
}

// Expression-bodied method (C# 6+)
static int Multiply(int a, int b) => a * b;

// void method
static void Greet(string name) => Console.WriteLine($"Hello, {name}!");

// Default parameters
static double Power(double base, double exp = 2.0) => Math.Pow(base, exp);
Power(3);       // 9.0
Power(3, 3);    // 27.0

// Named arguments
Power(exp: 3, base: 2);  // order doesn't matter

// Out parameters (return multiple values)
static bool TryDivide(int a, int b, out double result)
{
    if (b == 0) { result = 0; return false; }
    result = (double)a / b;
    return true;
}

if (TryDivide(10, 3, out double r))
    Console.WriteLine(r);

// Discard out params you don't need
int.TryParse("abc", out _);

// Ref parameters (pass by reference)
static void Swap(ref int a, ref int b) => (a, b) = (b, a);
Swap(ref x, ref y);

// In parameters (read-only ref — no copy, no modify)
static double Length(in Point p) => Math.Sqrt(p.X * p.X + p.Y * p.Y);

// Params array (variable args)
static int Sum(params int[] nums) => nums.Sum();
Sum(1, 2, 3, 4, 5);    // 15

// Local functions
static int Factorial(int n)
{
    return n <= 1 ? 1 : n * Inner(n - 1);

    static int Inner(int x) => x <= 1 ? 1 : x * Inner(x - 1);
}

// Method overloading
static string Format(int n)    => $"int: {n}";
static string Format(double d) => $"double: {d}";
static string Format(string s) => $"string: {s}";

// Recursive method
static long Fibonacci(int n) => n <= 1 ? n : Fibonacci(n-1) + Fibonacci(n-2);
```

---

## 10. Exceptions

```csharp
// try / catch / finally
try
{
    int result = int.Parse(Console.ReadLine()!);
    int division = 10 / result;
}
catch (FormatException ex)
{
    Console.WriteLine($"Not a number: {ex.Message}");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Cannot divide by zero");
}
catch (Exception ex) when (ex.Message.Contains("special"))
{
    // Exception filter — only catches if condition is true
    Console.WriteLine("Special error");
}
catch (Exception ex)
{
    Console.WriteLine($"Unexpected: {ex}");
    throw;  // rethrow — preserves stack trace (NOT: throw ex;)
}
finally
{
    Console.WriteLine("Always runs — great for cleanup");
}

// Throwing
throw new ArgumentNullException(nameof(name), "Name cannot be null");
throw new ArgumentException($"Invalid age: {age}", nameof(age));
throw new InvalidOperationException("Must call Init() first");
throw new NotImplementedException();
throw new NotSupportedException("Feature not available");

// Custom exceptions
public class InsufficientFundsException : Exception
{
    public decimal Amount { get; }

    public InsufficientFundsException(decimal amount)
        : base($"Insufficient funds. Need {amount:C} more.")
    {
        Amount = amount;
    }

    public InsufficientFundsException(decimal amount, Exception inner)
        : base($"Insufficient funds.", inner)
    {
        Amount = amount;
    }
}

// Expression throw (C# 7+)
string Validate(string? s) => s ?? throw new ArgumentNullException(nameof(s));

// Common exception types
// ArgumentNullException     — null arg
// ArgumentException         — invalid arg
// ArgumentOutOfRangeException — index/range
// InvalidOperationException — wrong state
// NotImplementedException
// NotSupportedException
// IOException               — file/stream
// FileNotFoundException
// NullReferenceException    — usually a bug (avoid catch)
// IndexOutOfRangeException  — array bounds
// OverflowException         — arithmetic overflow
// FormatException           — string parse failure
// TimeoutException
// OperationCanceledException — async cancellation
```

---

# INTERMEDIATE

---

## 11. Collections

```csharp
using System.Collections.Generic;
using System.Collections.Concurrent;

// ── List<T> ────────────────────────────────────────────────
var list = new List<int> { 3, 1, 4, 1, 5, 9 };
list.Add(2);
list.AddRange(new[] { 6, 5, 3 });
list.Insert(0, 99);
list.Remove(1);             // first occurrence
list.RemoveAt(0);           // by index
list.RemoveAll(x => x < 3);
list.Contains(5);           // true
list.IndexOf(4);
list.Sort();
list.Sort((a, b) => b.CompareTo(a));    // descending
list.Reverse();
list.Find(x => x > 4);
list.FindAll(x => x % 2 == 0);
list.Count;
list.Capacity;              // internal array size
list.TrimExcess();
list.Clear();
list.ToArray();

// ── Dictionary<TKey, TValue> ───────────────────────────────
var dict = new Dictionary<string, int>
{
    ["alice"] = 90,
    ["bob"]   = 85,
};
dict.Add("charlie", 78);
dict["alice"] = 95;                         // update
dict.TryAdd("alice", 100);                  // no-op if exists
dict.TryGetValue("bob", out int bobScore);  // safe get
dict.ContainsKey("alice");
dict.ContainsValue(85);
dict.Remove("bob");

foreach (var (key, value) in dict)
    Console.WriteLine($"{key}: {value}");

dict.Keys;   dict.Values;   dict.Count;

// ── HashSet<T> ────────────────────────────────────────────
var set = new HashSet<int> { 1, 2, 3 };
set.Add(4);
set.Remove(2);
set.Contains(3);        // O(1)
set.UnionWith(new[] { 3, 4, 5 });
set.IntersectWith(new[] { 3, 4 });
set.ExceptWith(new[] { 4 });
set.IsSubsetOf(other);
set.IsSupersetOf(other);

// ── Queue<T> — FIFO ───────────────────────────────────────
var queue = new Queue<string>();
queue.Enqueue("first");
queue.Enqueue("second");
string next = queue.Peek();     // see without removing
string item = queue.Dequeue();  // remove and return
queue.TryDequeue(out string? val);
queue.Count;

// ── Stack<T> — LIFO ───────────────────────────────────────
var stack = new Stack<int>();
stack.Push(1);
stack.Push(2);
stack.Push(3);
int top = stack.Peek();         // 3
int popped = stack.Pop();       // 3
stack.TryPop(out int val2);
stack.Count;

// ── LinkedList<T> ─────────────────────────────────────────
var ll = new LinkedList<int>(new[] { 1, 2, 3 });
ll.AddFirst(0);
ll.AddLast(4);
ll.AddAfter(ll.Find(2)!, 99);
ll.Remove(99);
ll.First!.Value;
ll.Last!.Value;

// ── SortedDictionary / SortedList ─────────────────────────
var sd = new SortedDictionary<string, int>();   // sorted by key
var sl = new SortedList<string, int>();         // sorted, array-backed

// ── PriorityQueue<TElement, TPriority> (NET 6+) ───────────
var pq = new PriorityQueue<string, int>();
pq.Enqueue("low",    10);
pq.Enqueue("high",    1);
pq.Enqueue("medium",  5);
pq.Dequeue();           // "high" (lowest priority number = highest priority)
pq.TryDequeue(out string? el, out int pri);

// ── Concurrent collections (thread-safe) ──────────────────
var cb = new ConcurrentBag<int>();
var cd = new ConcurrentDictionary<string, int>();
cd.TryAdd("key", 1);
cd.AddOrUpdate("key", 1, (k, old) => old + 1);
cd.GetOrAdd("key", 0);

// Collection initializer with LINQ
var sorted  = list.OrderBy(x => x).ToList();
var set2    = new HashSet<int>(list);
var asArray = list.ToArray();
```

---

## 12. Classes & OOP

```csharp
public class BankAccount
{
    // ── Fields ────────────────────────────────────────────
    private decimal _balance;
    private static int _nextId = 1;
    private readonly int _id;

    // ── Auto-properties ───────────────────────────────────
    public string Owner { get; private set; }
    public DateTime CreatedAt { get; } = DateTime.UtcNow;

    // ── Constructor ───────────────────────────────────────
    public BankAccount(string owner, decimal initialBalance = 0)
    {
        Owner    = owner ?? throw new ArgumentNullException(nameof(owner));
        _balance = initialBalance;
        _id      = _nextId++;
    }

    // ── Constructor chaining ──────────────────────────────
    public BankAccount(string owner) : this(owner, 0) { }

    // ── Properties with logic ─────────────────────────────
    public decimal Balance
    {
        get => _balance;
        private set
        {
            if (value < 0) throw new InvalidOperationException("Negative balance");
            _balance = value;
        }
    }

    // ── Methods ───────────────────────────────────────────
    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("Must be positive");
        _balance += amount;
        Console.WriteLine($"Deposited {amount:C}. Balance: {Balance:C}");
    }

    public bool Withdraw(decimal amount)
    {
        if (amount > _balance) return false;
        _balance -= amount;
        return true;
    }

    // ── Static method ─────────────────────────────────────
    public static BankAccount Open(string owner, decimal deposit = 0)
        => new(owner, deposit);

    // ── Overrides ─────────────────────────────────────────
    public override string ToString() => $"Account#{_id} [{Owner}]: {Balance:C}";
    public override bool Equals(object? obj)
        => obj is BankAccount other && _id == other._id;
    public override int GetHashCode() => _id;

    // ── Operator overloading ──────────────────────────────
    public static BankAccount operator +(BankAccount a, BankAccount b)
        => new(a.Owner, a._balance + b._balance);

    // ── Finalizer (use sparingly — IDisposable preferred) ─
    ~BankAccount() => Console.WriteLine($"Account#{_id} finalized");
}

// Usage
var acc = new BankAccount("Alice", 100m);
acc.Deposit(50m);
acc.Withdraw(30m);
Console.WriteLine(acc);

// Object initializer (only works with settable properties)
var point = new Point { X = 1.0, Y = 2.0 };

// With-expressions (records — see §16)
```

---

## 13. Interfaces & Abstract Classes

```csharp
// Interface — defines contract, no state (until default methods)
public interface IShape
{
    double Area { get; }
    double Perimeter { get; }
    void Draw();

    // Default interface method (C# 8+)
    string Describe() => $"{GetType().Name}: area={Area:F2}";
}

// Interface inheritance
public interface IAnimatable : IShape
{
    void Animate(double seconds);
}

// Abstract class — partial implementation, can have state
public abstract class Shape : IShape
{
    public string Color { get; set; } = "Black";

    public abstract double Area { get; }        // must implement
    public abstract double Perimeter { get; }   // must implement

    public virtual void Draw()                  // can override
        => Console.WriteLine($"Drawing {GetType().Name} in {Color}");
}

// Concrete class
public class Circle : Shape
{
    public double Radius { get; }
    public Circle(double radius) => Radius = radius;

    public override double Area      => Math.PI * Radius * Radius;
    public override double Perimeter => 2 * Math.PI * Radius;
}

public class Rectangle : Shape
{
    public double Width  { get; }
    public double Height { get; }
    public Rectangle(double w, double h) { Width = w; Height = h; }

    public override double Area      => Width * Height;
    public override double Perimeter => 2 * (Width + Height);
}

// Multiple interface implementation
public class Square : Shape, IAnimatable
{
    public double Side { get; }
    public Square(double s) => Side = s;

    public override double Area      => Side * Side;
    public override double Perimeter => 4 * Side;
    public void Animate(double s)    => Console.WriteLine($"Animating for {s}s");
}

// Interface as type
IShape shape = new Circle(5);
shape.Area;     // polymorphism
shape.Describe();
List<IShape> shapes = new() { new Circle(3), new Rectangle(4,5) };
shapes.ForEach(s => s.Draw());
```

---

## 14. Inheritance & Polymorphism

```csharp
public class Animal
{
    public string Name { get; }
    public Animal(string name) => Name = name;

    public virtual string Speak() => "...";
    public sealed override string ToString() => $"{GetType().Name}({Name})";
}

public class Dog : Animal
{
    public string Breed { get; }
    public Dog(string name, string breed) : base(name) => Breed = breed;

    public override string Speak() => $"{Name} says Woof!";
}

public class Cat : Animal
{
    public Cat(string name) : base(name) { }
    public override string Speak() => $"{Name} says Meow!";
}

// sealed class — no further inheritance
public sealed class GoldenRetriever : Dog
{
    public GoldenRetriever(string name) : base(name, "Golden Retriever") { }
    public override string Speak() => base.Speak() + " *wags tail*";
}

// Polymorphism
Animal[] animals = { new Dog("Rex","Lab"), new Cat("Whiskers"), new Dog("Buddy","Poodle") };
foreach (var a in animals)
    Console.WriteLine(a.Speak());   // each calls its own override

// Type checking
foreach (var a in animals)
{
    if (a is Dog dog)
        Console.WriteLine($"Breed: {dog.Breed}");

    if (a is not Cat)
        Console.WriteLine("Not a cat");
}

// new keyword — hide (not override) base member
public class Logger
{
    public void Log(string msg) => Console.WriteLine(msg);
}
public class FileLogger : Logger
{
    public new void Log(string msg) => File.AppendAllText("log.txt", msg);
    // Logger l = new FileLogger(); l.Log() → calls Logger.Log  (hiding, not virtual!)
}
```

---

## 15. Properties, Indexers & Operator Overloading

```csharp
public class Temperature
{
    private double _celsius;

    // Full property
    public double Celsius
    {
        get => _celsius;
        set => _celsius = value < -273.15
            ? throw new ArgumentOutOfRangeException(nameof(value), "Below absolute zero")
            : value;
    }

    // Computed property
    public double Fahrenheit
    {
        get => _celsius * 9 / 5 + 32;
        set => _celsius = (value - 32) * 5 / 9;
    }

    // Init-only property (C# 9+)
    public string Unit { get; init; } = "°C";

    // Required property (C# 11+)
    public required string Label { get; set; }

    // Operator overloading
    public static Temperature operator +(Temperature a, Temperature b)
        => new() { Celsius = a._celsius + b._celsius, Label = "Sum" };

    public static bool operator >(Temperature a, Temperature b)  => a._celsius > b._celsius;
    public static bool operator <(Temperature a, Temperature b)  => a._celsius < b._celsius;
    public static bool operator >=(Temperature a, Temperature b) => a._celsius >= b._celsius;
    public static bool operator <=(Temperature a, Temperature b) => a._celsius <= b._celsius;

    // Implicit / explicit conversion
    public static implicit operator double(Temperature t)  => t._celsius;
    public static explicit operator Temperature(double c)  => new() { Celsius = c, Label = "Converted" };
}

// Indexer
public class WordDictionary
{
    private readonly Dictionary<string, string> _data = new();

    public string this[string key]
    {
        get => _data.TryGetValue(key, out var v) ? v : "not found";
        set => _data[key] = value;
    }

    // Multi-parameter indexer
    public string this[string key, string defaultValue]
        => _data.GetValueOrDefault(key, defaultValue);
}

var d = new WordDictionary();
d["hello"] = "a greeting";
Console.WriteLine(d["hello"]);          // "a greeting"
Console.WriteLine(d["missing"]);        // "not found"
Console.WriteLine(d["missing", "N/A"]); // "N/A"
```

---

## 16. Structs & Records

```csharp
// Struct — value type, stack-allocated, no inheritance
public struct Point
{
    public double X { get; }
    public double Y { get; }

    public Point(double x, double y) { X = x; Y = y; }

    public double DistanceTo(Point other)
        => Math.Sqrt(Math.Pow(X - other.X, 2) + Math.Pow(Y - other.Y, 2));

    public override string ToString() => $"({X}, {Y})";

    // Deconstruct
    public void Deconstruct(out double x, out double y) { x = X; y = Y; }
}

var p1 = new Point(0, 0);
var p2 = new Point(3, 4);
p1.DistanceTo(p2);  // 5.0
var (x, y) = p2;    // deconstruction

// readonly struct — all fields readonly, can be passed by in ref
public readonly struct Vector2D(double X, double Y)  // primary constructor (C# 12+)
{
    public double Magnitude => Math.Sqrt(X*X + Y*Y);
    public Vector2D Normalize() => new(X / Magnitude, Y / Magnitude);
    public static Vector2D operator +(Vector2D a, Vector2D b) => new(a.X+b.X, a.Y+b.Y);
}

// ref struct — can only live on stack (used for Span<T>)
ref struct StackBuffer
{
    private Span<byte> _data;
    public StackBuffer(Span<byte> data) => _data = data;
}

// ── Records (C# 9+) — immutable reference types with value semantics ──
public record Person(string FirstName, string LastName);

// Auto-generated: constructor, properties, ToString, Equals, GetHashCode
var alice = new Person("Alice", "Smith");
var alice2 = new Person("Alice", "Smith");
alice == alice2;        // true  (value equality)
Console.WriteLine(alice);   // Person { FirstName = Alice, LastName = Smith }

// Non-destructive mutation with 'with'
var bob = alice with { FirstName = "Bob" };

// Record with additional members
public record Employee(string Name, string Role) : Person(Name, "")
{
    public decimal Salary { get; init; }
    public string Department { get; init; } = "General";

    public string Display() => $"{Name} ({Role}) — {Salary:C}";
}

// record struct (C# 10+) — value type record
public record struct Coordinate(double Lat, double Lon);

// Positional deconstruction
var (first, last) = alice;

// readonly record struct
public readonly record struct Color(byte R, byte G, byte B)
{
    public static readonly Color Red   = new(255, 0, 0);
    public static readonly Color Green = new(0, 255, 0);
    public static readonly Color Blue  = new(0, 0, 255);
}
```

---

## 17. Enums

```csharp
// Basic enum
public enum Direction { North, South, East, West }
Direction dir = Direction.North;

// Explicit values
public enum StatusCode
{
    Unknown  = 0,
    Active   = 1,
    Inactive = 2,
    Deleted  = 99
}

// Flags enum — combine with bitwise OR
[Flags]
public enum Permissions
{
    None    = 0,
    Read    = 1 << 0,   // 1
    Write   = 1 << 1,   // 2
    Execute = 1 << 2,   // 4
    Admin   = Read | Write | Execute  // 7
}

Permissions p = Permissions.Read | Permissions.Write;
p.HasFlag(Permissions.Read);    // true
p |= Permissions.Execute;       // add permission
p &= ~Permissions.Write;        // remove permission

// Enum methods
Enum.GetNames<Direction>();
Enum.GetValues<Direction>();
Enum.TryParse<Direction>("North", out var parsed);
(int)Direction.East;            // 2
(Direction)3;                   // West

// switch on enum
string msg = dir switch
{
    Direction.North => "Going up",
    Direction.South => "Going down",
    Direction.East  => "Going right",
    Direction.West  => "Going left",
    _               => "Unknown"
};

// Enum in interfaces / pattern matching
if (dir is Direction.North or Direction.East)
    Console.WriteLine("Right half");
```

---

## 18. Generics

```csharp
// Generic method
static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) >= 0 ? a : b;

Max(3, 5);          // 5
Max("apple", "pear"); // "pear"

// Generic class
public class Stack<T>
{
    private readonly List<T> _items = new();

    public void Push(T item) => _items.Add(item);
    public T Pop()
    {
        if (_items.Count == 0) throw new InvalidOperationException("Empty stack");
        var last = _items[^1];
        _items.RemoveAt(_items.Count - 1);
        return last;
    }
    public T Peek() => _items[^1];
    public int Count => _items.Count;
    public bool IsEmpty => _items.Count == 0;
}

// Generic interface
public interface IRepository<T> where T : class
{
    T? GetById(int id);
    IEnumerable<T> GetAll();
    void Add(T entity);
    void Remove(T entity);
}

// Constraints
void Process<T>(T item) where T : class                // reference type
void Process<T>(T item) where T : struct               // value type
void Process<T>(T item) where T : new()               // has parameterless ctor
void Process<T>(T item) where T : IDisposable         // implements interface
void Process<T>(T item) where T : Animal              // inherits from Animal
void Process<T, U>(T a, U b) where T : U             // T inherits U
void Process<T>(T item) where T : notnull            // non-nullable

// Multiple constraints
void Create<T>(T item) where T : class, IDisposable, new() { }

// Generic with covariance / contravariance
IEnumerable<Dog> dogs = new List<Dog>();
IEnumerable<Animal> animals = dogs;          // covariance (out T)

Action<Animal> animalAction = a => a.Speak();
Action<Dog> dogAction = animalAction;        // contravariance (in T)

// Generic type inference — compiler deduces T
var result = Max(10, 20);       // T inferred as int
```

---

## 19. Delegates, Events & Func/Action

```csharp
// Delegate — type-safe function pointer
public delegate int MathOperation(int a, int b);

MathOperation add = (a, b) => a + b;
MathOperation mul = (a, b) => a * b;
int result = add(3, 4);     // 7

// Multicast delegate
Action<string> log = Console.WriteLine;
log += s => File.AppendAllText("log.txt", s + "\n");
log("Hello");   // invokes both

// Remove handler
log -= Console.WriteLine;

// Func<T, TResult> — has return value
Func<int, int, int> sum = (a, b) => a + b;
Func<string, int> len  = s => s.Length;
Func<int>         rand = () => Random.Shared.Next();

// Action<T> — returns void
Action<string>        print = Console.WriteLine;
Action<string, int>   repeat = (s, n) => { for (int i=0; i<n; i++) Console.WriteLine(s); };
Action                ring = () => Console.Beep();

// Predicate<T> — returns bool
Predicate<int> isEven = n => n % 2 == 0;
isEven(4);  // true

// Events
public class Button
{
    // Event declaration using EventHandler<TEventArgs>
    public event EventHandler<ButtonClickedEventArgs>? Clicked;

    public void Click()
    {
        Clicked?.Invoke(this, new ButtonClickedEventArgs { Timestamp = DateTime.Now });
    }
}

public class ButtonClickedEventArgs : EventArgs
{
    public DateTime Timestamp { get; init; }
}

// Subscribe / unsubscribe
var btn = new Button();
btn.Clicked += (sender, e) => Console.WriteLine($"Clicked at {e.Timestamp}");
btn.Click();

// Custom event accessor
private EventHandler? _onClick;
public event EventHandler OnClick
{
    add    => _onClick += value;
    remove => _onClick -= value;
}
```

---

## 20. LINQ

```csharp
using System.Linq;

var numbers = new[] { 5, 3, 8, 1, 4, 9, 2, 7, 6 };
var words   = new[] { "hello", "world", "linq", "csharp" };
var people  = new[]
{
    new { Name = "Alice", Age = 30, Dept = "Eng" },
    new { Name = "Bob",   Age = 25, Dept = "HR"  },
    new { Name = "Carol", Age = 35, Dept = "Eng" },
    new { Name = "Dave",  Age = 28, Dept = "HR"  },
};

// ── Filtering ─────────────────────────────────────────────
numbers.Where(n => n > 5)                       // [8,9,7,6]
people.Where(p => p.Age > 28)
people.Where(p => p.Dept == "Eng")

// ── Projection ────────────────────────────────────────────
numbers.Select(n => n * 2)
people.Select(p => p.Name)
people.Select(p => new { p.Name, Senior = p.Age > 30 })

// SelectMany — flatten
new[] { new[]{1,2}, new[]{3,4} }.SelectMany(x => x)  // [1,2,3,4]

// ── Ordering ──────────────────────────────────────────────
numbers.OrderBy(n => n)
numbers.OrderByDescending(n => n)
people.OrderBy(p => p.Age).ThenBy(p => p.Name)

// ── Aggregation ───────────────────────────────────────────
numbers.Count()                     // 9
numbers.Count(n => n > 5)          // 4
numbers.Sum()                       // 45
numbers.Min()                       // 1
numbers.Max()                       // 9
numbers.Average()                   // 5.0
numbers.Aggregate((a, b) => a * b)  // product

// ── Element access ────────────────────────────────────────
numbers.First()                     // 5 (throws if empty)
numbers.First(n => n > 5)           // 8
numbers.FirstOrDefault(n => n > 99) // 0 (default for int)
numbers.Single(n => n == 9)         // 9 (throws if 0 or 2+)
numbers.Last()                      // 6
numbers.ElementAt(3)                // 1

// ── Partitioning ──────────────────────────────────────────
numbers.Take(3)                     // [5,3,8]
numbers.Skip(6)                     // [2,7,6]
numbers.TakeLast(2)                 // [7,6]
numbers.SkipLast(2)                 // [5,3,8,1,4,9]
numbers.TakeWhile(n => n < 9)
numbers.SkipWhile(n => n > 2)
numbers.Take(2..5)                  // by range (NET 6+)

// ── Grouping ──────────────────────────────────────────────
var byDept = people.GroupBy(p => p.Dept);
foreach (var group in byDept)
{
    Console.WriteLine($"{group.Key}: {group.Count()} people");
    foreach (var p in group) Console.WriteLine($"  {p.Name}");
}

// ── Joining ───────────────────────────────────────────────
var ids    = new[] { (Id: 1, Name: "Alice"), (Id: 2, Name: "Bob") };
var scores = new[] { (Id: 1, Score: 90),     (Id: 2, Score: 85) };

var joined = ids.Join(scores,
    i => i.Id,
    s => s.Id,
    (i, s) => new { i.Name, s.Score });

// GroupJoin (left outer join)
var groupJoined = ids.GroupJoin(scores, i => i.Id, s => s.Id,
    (i, ss) => new { i.Name, Scores = ss.Select(s => s.Score) });

// ── Set operations ────────────────────────────────────────
new[]{1,2,3}.Union(new[]{2,3,4})            // [1,2,3,4]
new[]{1,2,3}.Intersect(new[]{2,3,4})        // [2,3]
new[]{1,2,3}.Except(new[]{2,3})             // [1]
numbers.Distinct()
numbers.DistinctBy(n => n % 3)              // (NET 6+)

// ── Conversion ────────────────────────────────────────────
numbers.ToList()
numbers.ToArray()
numbers.ToDictionary(n => n, n => n * n)
numbers.ToHashSet()
numbers.AsEnumerable()
numbers.AsQueryable()

// ── Checking ──────────────────────────────────────────────
numbers.Any(n => n > 8)         // true
numbers.All(n => n > 0)         // true
numbers.SequenceEqual(numbers)  // true
numbers.Contains(7)             // true

// ── Query syntax (equivalent to method syntax) ────────────
var query =
    from p in people
    where p.Age > 25
    orderby p.Age
    select new { p.Name, p.Dept };

var groupQuery =
    from p in people
    group p by p.Dept into g
    select new { Dept = g.Key, Count = g.Count(), Avg = g.Average(x => x.Age) };

// ── Zip ───────────────────────────────────────────────────
var keys   = new[] { "a", "b", "c" };
var vals   = new[] {  1,   2,   3  };
keys.Zip(vals, (k, v) => $"{k}={v}")    // ["a=1","b=2","c=3"]
keys.Zip(vals)                          // (a,1),(b,2),(c,3)  (NET 6+)

// ── Chunk ─────────────────────────────────────────────────
numbers.Chunk(3)    // [[5,3,8],[1,4,9],[2,7,6]]  (NET 6+)
```

---

# ADVANCED

---

## 21. Nullable Reference Types

```csharp
// Enable in .csproj (default in NET 6+)
// <Nullable>enable</Nullable>

string  name  = "Alice";   // non-nullable — compiler warns on null assign
string? alias = null;      // nullable — must check before use

// Null checks
if (alias != null)
    Console.WriteLine(alias.Length);   // safe

Console.WriteLine(alias?.Length ?? 0); // null-conditional + coalescing

// Null-forgiving operator (tells compiler "trust me")
string definitelyNotNull = alias!;  // use carefully

// Guard clauses (recommended pattern)
void Process(string? input)
{
    ArgumentNullException.ThrowIfNull(input);       // .NET 7+
    // input is now non-null below
    Console.WriteLine(input.ToUpper());
}

// Pattern matching for null
if (alias is { } nonNull)
    Console.WriteLine(nonNull.Length);  // alias is not null here

// Nullable value types
int? age = null;
age.HasValue        // false
age.Value           // throws if null
age.GetValueOrDefault()     // 0
age.GetValueOrDefault(18)   // 18
age ?? 0                    // 0

// Null checks in LINQ
people.Where(p => p.Address?.City is not null)

// MemberNotNull attribute
private string? _name;

[MemberNotNull(nameof(_name))]
void Initialize()
{
    _name = "default";
}

// NotNullWhen, NotNullIfNotNull
bool TryGet([NotNullWhen(true)] out string? value) { ... }

// Required properties (C# 11+) — null safety at construction
public class Config
{
    public required string ConnectionString { get; init; }
}
```

---

## 22. Pattern Matching

```csharp
// Type pattern
if (obj is int n)
    Console.WriteLine($"int: {n}");

// Declaration pattern
object[] items = { 42, "hello", 3.14, true, null };
foreach (var item in items)
{
    string desc = item switch
    {
        int i when i < 0  => $"negative int: {i}",
        int i             => $"positive int: {i}",
        string s          => $"string of length {s.Length}",
        double d          => $"double: {d:F2}",
        bool b            => $"bool: {b}",
        null              => "null",
        _                 => $"other: {item}"
    };
    Console.WriteLine(desc);
}

// Property pattern
string Classify(Person p) => p switch
{
    { Age: < 18 }                         => "Minor",
    { Age: >= 18, Name.Length: > 5 }      => "Adult with long name",
    { Name: "Admin" }                     => "Administrator",
    _                                     => "Regular adult"
};

// Positional pattern (with Deconstruct)
string DescribePoint(Point p) => p switch
{
    (0, 0)      => "Origin",
    (var x, 0) => $"On X-axis at {x}",
    (0, var y) => $"On Y-axis at {y}",
    (var x, var y) when x == y => $"On diagonal at {x}",
    _           => "Somewhere else"
};

// List pattern (C# 11+)
int[] arr = { 1, 2, 3, 4, 5 };
bool match = arr switch
{
    []               => true,  // empty
    [1, 2, ..]       => true,  // starts with 1, 2
    [.., 4, 5]       => true,  // ends with 4, 5
    [1, .. var mid, 5] => true, // capture middle
    [var first, _]   => false
};

// Relational & logical patterns
bool InRange(int n) => n is >= 0 and <= 100;
bool IsEdge(int n)  => n is 0 or 100;
bool NotNull(object? o) => o is not null;

// Extended property pattern (C# 10+)
bool IsEngManager(Employee e) => e is
{
    Department.Name: "Engineering",
    Role: "Manager",
    Salary: > 80_000m
};

// Var pattern (always matches, binds value)
if (GetValue() is var v && v > 0)
    Console.WriteLine(v);
```

---

## 23. Tuples & Deconstruction

```csharp
// Value tuples (C# 7+)
var tuple = (1, "hello", 3.14);
tuple.Item1     // 1
tuple.Item2     // "hello"

// Named tuples
var person = (Name: "Alice", Age: 25);
person.Name     // "Alice"
person.Age      // 25

// Returning multiple values
static (double Min, double Max, double Avg) Stats(IEnumerable<double> nums)
{
    var list = nums.ToList();
    return (list.Min(), list.Max(), list.Average());
}

var (min, max, avg) = Stats(new[] { 1.0, 2.0, 3.0, 4.0, 5.0 });
Console.WriteLine($"Min={min} Max={max} Avg={avg}");

// Deconstruction — ignore with discard _
var (_, name, _) = (1, "Alice", true);

// Deconstruction in foreach
var pairs = new[] { (1, "one"), (2, "two"), (3, "three") };
foreach (var (n, word) in pairs)
    Console.WriteLine($"{n} = {word}");

// Tuple equality
var t1 = (1, "hello");
var t2 = (1, "hello");
t1 == t2;   // true

// Deconstructing custom types
public class Rectangle
{
    public double Width  { get; }
    public double Height { get; }
    public Rectangle(double w, double h) { Width = w; Height = h; }

    public void Deconstruct(out double w, out double h) { w = Width; h = Height; }
}

var rect = new Rectangle(10, 5);
var (w, h) = rect;
Console.WriteLine($"Width={w} Height={h}");

// Tuple as dictionary key
var dict = new Dictionary<(int, int), string>
{
    [(0, 0)] = "origin",
    [(1, 0)] = "right",
    [(0, 1)] = "up",
};
dict[(0, 0)];   // "origin"
```

---

## 24. Extension Methods

```csharp
// Extension method — must be in static class, first param is 'this'
public static class StringExtensions
{
    public static bool IsNullOrEmpty(this string? s)
        => string.IsNullOrEmpty(s);

    public static string Truncate(this string s, int maxLength, string suffix = "...")
    {
        if (s.Length <= maxLength) return s;
        return s[..(maxLength - suffix.Length)] + suffix;
    }

    public static string ToTitleCase(this string s)
    {
        if (string.IsNullOrEmpty(s)) return s;
        return string.Join(' ', s.Split(' ').Select(w =>
            w.Length > 0 ? char.ToUpper(w[0]) + w[1..].ToLower() : w));
    }

    public static IEnumerable<string> Lines(this string s)
        => s.Split('\n').Select(l => l.TrimEnd('\r'));
}

public static class EnumerableExtensions
{
    public static IEnumerable<T> Shuffle<T>(this IEnumerable<T> source)
    {
        var arr = source.ToArray();
        Random.Shared.Shuffle(arr);   // .NET 8+
        return arr;
    }

    public static IEnumerable<IEnumerable<T>> Batch<T>(this IEnumerable<T> source, int size)
        => source.Chunk(size);

    public static void ForEach<T>(this IEnumerable<T> source, Action<T> action)
    {
        foreach (var item in source) action(item);
    }
}

// Usage — looks like instance methods
"hello world".ToTitleCase();           // "Hello World"
"A very long string".Truncate(10);    // "A very lon..."

var nums = Enumerable.Range(1, 100);
nums.Shuffle().Take(5).ForEach(Console.WriteLine);
```

---

## 25. Iterators & yield

```csharp
// yield return — lazily produces sequence
static IEnumerable<int> Range(int start, int count)
{
    for (int i = 0; i < count; i++)
        yield return start + i;
}

foreach (var n in Range(5, 10))
    Console.Write($"{n} ");    // 5 6 7 8 9 10 11 12 13 14

// yield break — stop iteration
static IEnumerable<int> TakeUntil(IEnumerable<int> source, int limit)
{
    foreach (var item in source)
    {
        if (item > limit) yield break;
        yield return item;
    }
}

// Infinite generator
static IEnumerable<int> Naturals()
{
    int n = 1;
    while (true) yield return n++;
}

Naturals().TakeWhile(n => n < 100).Sum();  // 4950

// Fibonacci
static IEnumerable<long> Fibonacci()
{
    long a = 0, b = 1;
    while (true)
    {
        yield return a;
        (a, b) = (b, a + b);
    }
}

Fibonacci().Take(10).ToList();  // [0,1,1,2,3,5,8,13,21,34]

// IAsyncEnumerable (C# 8+) — async streaming
static async IAsyncEnumerable<int> StreamDataAsync(
    [EnumeratorCancellation] CancellationToken ct = default)
{
    for (int i = 0; i < 100; i++)
    {
        await Task.Delay(10, ct);
        yield return i;
    }
}

await foreach (var item in StreamDataAsync())
    Console.WriteLine(item);
```

---

## 26. Anonymous Types & Dynamic

```csharp
// Anonymous types — read-only, compiler-generated
var anon = new { Name = "Alice", Age = 25, Score = 98.5 };
anon.Name       // "Alice"
// anon.Name = "Bob";  // COMPILE ERROR — immutable

// Mostly used in LINQ projections
var results = people
    .Where(p => p.Age > 25)
    .Select(p => new { p.Name, Initials = $"{p.Name[0]}." });

// ExpandoObject — dynamic property bag
using System.Dynamic;

dynamic expando = new ExpandoObject();
expando.Name  = "Alice";
expando.Age   = 25;
expando.Greet = (Action)(() => Console.WriteLine($"Hi, I'm {expando.Name}"));
expando.Greet();

// Convert to dictionary
var dict = (IDictionary<string, object?>)expando;
dict["Name"];   // "Alice"

// dynamic keyword — runtime dispatch (avoids compile-time type checking)
dynamic obj = GetSomeObject();
obj.DoSomething();      // resolved at runtime, no compile error
obj.Property = 42;

// COM interop / Office automation often uses dynamic
// dynamic excel = Activator.CreateInstance(Type.GetTypeFromProgID("Excel.Application")!);

// Note: dynamic has performance cost — use only when necessary
// Prefer pattern matching or generics over dynamic where possible
```

---

## 27. Lambda & Closures

```csharp
// Lambda syntax
Func<int, int>       square  = x => x * x;
Func<int, int, int>  add     = (x, y) => x + y;
Func<int, bool>      isEven  = x => x % 2 == 0;
Action<string>       print   = msg => Console.WriteLine(msg);
Action<string>       print2  = Console.WriteLine;   // method group

// Block lambda
Func<int, string> describe = n =>
{
    if (n < 0) return "negative";
    if (n == 0) return "zero";
    return "positive";
};

// Expression trees (when lambda assigned to Expression<>)
Expression<Func<int, bool>> expr = x => x > 5;
// Used by EF Core, LINQ to SQL — compiled to SQL, not IL

// Closures — capture outer variables
int multiplier = 3;
Func<int, int> triple = x => x * multiplier;   // closes over multiplier
triple(5);      // 15
multiplier = 10;
triple(5);      // 50  (captures reference, not value!)

// Capture in loop — classic gotcha
var actions = new List<Action>();
for (int i = 0; i < 5; i++)
{
    int captured = i;   // create new variable each iteration
    actions.Add(() => Console.WriteLine(captured));
}
actions.ForEach(a => a());  // 0 1 2 3 4 (NOT 5 5 5 5 5)

// Static lambdas (C# 9+) — cannot capture, avoids accidental closure allocation
Func<int, int> pure = static x => x * 2;

// Lambda with attributes (C# 10+)
Func<int, int> traced = [DebuggerStepThrough] x => x + 1;

// Natural type inference (C# 10+)
var lambda = (int x) => x * x;     // compiler infers Func<int, int>
```

---

## 28. Attributes & Reflection

```csharp
// Built-in attributes
[Obsolete("Use NewMethod instead", error: false)]
void OldMethod() { }

[Serializable]
public class Config { }

[NonSerialized]
private int _cache;

[DebuggerDisplay("{Name} ({Age})")]
public class Person { public string Name; public int Age; }

[Description("User account model")]
[JsonPropertyName("user_id")]
public int UserId { get; set; }

// Custom attribute
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method,
    AllowMultiple = false, Inherited = true)]
public class AuthorAttribute : Attribute
{
    public string Name    { get; }
    public string Version { get; init; } = "1.0";

    public AuthorAttribute(string name) => Name = name;
}

[Author("Alice", Version = "2.1")]
public class MyService { }

// Reading attributes via reflection
var attr = typeof(MyService).GetCustomAttribute<AuthorAttribute>();
Console.WriteLine(attr?.Name);      // "Alice"
Console.WriteLine(attr?.Version);   // "2.1"

// Reflection — inspect types at runtime
Type type = typeof(BankAccount);
type.Name;              // "BankAccount"
type.FullName;
type.IsClass;
type.IsValueType;
type.GetProperties();
type.GetMethods();
type.GetFields(BindingFlags.NonPublic | BindingFlags.Instance);

// Create instance
var instance = Activator.CreateInstance(type, "Alice", 100m);

// Invoke method
MethodInfo method = type.GetMethod("Deposit")!;
method.Invoke(instance, new object[] { 50m });

// Get/set property
PropertyInfo prop = type.GetProperty("Owner")!;
prop.GetValue(instance);
prop.SetValue(instance, "Bob");

// Source generators (preferred over reflection in hot paths)
// [GeneratedRegex(@"\d+")]
// private static partial Regex NumbersRegex();
```

---

## 29. File & Stream I/O

```csharp
using System.IO;

// ── File helpers (small files) ────────────────────────────
File.WriteAllText("file.txt", "Hello, World!\n");
File.AppendAllText("file.txt", "More content\n");
string content = File.ReadAllText("file.txt");
string[] lines = File.ReadAllLines("file.txt");
File.WriteAllLines("output.txt", lines);
byte[] bytes = File.ReadAllBytes("image.png");
File.WriteAllBytes("copy.png", bytes);
File.Copy("src.txt", "dst.txt", overwrite: true);
File.Move("old.txt", "new.txt");
File.Delete("file.txt");
File.Exists("file.txt");

// ── Directory ─────────────────────────────────────────────
Directory.CreateDirectory("path/to/dir");
Directory.Exists("path");
Directory.Delete("path", recursive: true);
Directory.GetFiles(".", "*.txt");
Directory.GetDirectories(".");
Directory.GetFiles(".", "*.cs", SearchOption.AllDirectories);

// ── Path ──────────────────────────────────────────────────
Path.Combine("folder", "sub", "file.txt")   // cross-platform
Path.GetFileName("path/to/file.txt")        // "file.txt"
Path.GetFileNameWithoutExtension("file.txt")// "file"
Path.GetExtension("file.txt")               // ".txt"
Path.GetDirectoryName("path/to/file.txt")   // "path/to"
Path.GetFullPath("relative.txt")
Path.GetTempPath()
Path.GetTempFileName()

// ── StreamReader / StreamWriter ───────────────────────────
using var writer = new StreamWriter("file.txt", append: false, Encoding.UTF8);
writer.WriteLine("Line 1");
writer.WriteLine("Line 2");

using var reader = new StreamReader("file.txt");
while (!reader.EndOfStream)
{
    string? line = reader.ReadLine();
    Console.WriteLine(line);
}

// ── FileStream (low-level, binary) ───────────────────────
using var fs = new FileStream("data.bin", FileMode.Create, FileAccess.Write);
byte[] data = Encoding.UTF8.GetBytes("hello");
await fs.WriteAsync(data);

// ── MemoryStream ──────────────────────────────────────────
using var ms = new MemoryStream();
using var sw = new StreamWriter(ms, leaveOpen: true);
sw.WriteLine("In memory");
sw.Flush();
ms.Position = 0;
using var sr = new StreamReader(ms);
Console.WriteLine(sr.ReadToEnd());

// ── Async file I/O (preferred in modern code) ─────────────
string text = await File.ReadAllTextAsync("file.txt");
await File.WriteAllTextAsync("out.txt", "async content");
string[] asyncLines = await File.ReadAllLinesAsync("file.txt");

// ── PathInfo (pathlib equivalent) ─────────────────────────
var dir  = new DirectoryInfo(".");
var file = new FileInfo("file.txt");
file.Exists;
file.Length;            // bytes
file.CreationTimeUtc;
file.LastWriteTimeUtc;
file.Extension;
file.Directory;
```

---

## 30. Async / Await & Task Parallel Library

```csharp
using System.Threading;
using System.Threading.Tasks;

// ── Async basics ──────────────────────────────────────────
async Task<string> FetchDataAsync(string url, CancellationToken ct = default)
{
    using var http = new HttpClient();
    return await http.GetStringAsync(url, ct);
}

// Always await (never fire-and-forget without care)
string data = await FetchDataAsync("https://api.example.com");

// ── Task.Run — offload CPU-bound work ─────────────────────
int result = await Task.Run(() => ExpensiveComputation(1_000_000));

// ── Task.WhenAll — run concurrently ───────────────────────
var urls = new[] { "https://a.com", "https://b.com", "https://c.com" };
var tasks = urls.Select(u => FetchDataAsync(u));
string[] results = await Task.WhenAll(tasks);

// ── Task.WhenAny — first to complete ──────────────────────
var first = await Task.WhenAny(tasks);
Console.WriteLine(await first);

// ── CancellationToken ─────────────────────────────────────
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));
try
{
    string r = await FetchDataAsync("https://slow.com", cts.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("Request cancelled or timed out");
}

// Cancel manually
cts.Cancel();
// Linked tokens
using var linked = CancellationTokenSource.CreateLinkedTokenSource(ct1, ct2);

// ── Progress reporting ─────────────────────────────────────
async Task ProcessAsync(IProgress<int> progress, CancellationToken ct)
{
    for (int i = 0; i <= 100; i++)
    {
        await Task.Delay(10, ct);
        progress.Report(i);
    }
}

var progress = new Progress<int>(p => Console.Write($"\r{p}%"));
await ProcessAsync(progress, CancellationToken.None);

// ── ValueTask — for hot paths (avoids heap alloc when sync) ─
async ValueTask<int> GetCachedAsync(int id)
{
    if (_cache.TryGetValue(id, out int val)) return val;    // synchronous, no alloc
    return await LoadFromDbAsync(id);
}

// ── ConfigureAwait(false) — library code ──────────────────
// Avoid capturing SynchronizationContext in libraries
await SomeOperationAsync().ConfigureAwait(false);

// ── Parallel class ────────────────────────────────────────
Parallel.For(0, 100, i => ProcessItem(i));
Parallel.ForEach(items, item => Process(item));
Parallel.ForEachAsync(items, async (item, ct) => await ProcessAsync(item, ct));  // .NET 6+

var options = new ParallelOptions
{
    MaxDegreeOfParallelism = Environment.ProcessorCount,
    CancellationToken = cts.Token
};
Parallel.ForEach(items, options, Process);

// ── Semaphore — limit concurrency ────────────────────────
var semaphore = new SemaphoreSlim(3);   // max 3 concurrent
var tasks2 = items.Select(async item =>
{
    await semaphore.WaitAsync();
    try { await ProcessAsync(item); }
    finally { semaphore.Release(); }
});
await Task.WhenAll(tasks2);

// ── Thread safety ─────────────────────────────────────────
// Interlocked — atomic operations
int sharedCounter = 0;
Interlocked.Increment(ref sharedCounter);
Interlocked.Add(ref sharedCounter, 10);
Interlocked.CompareExchange(ref sharedCounter, newVal, expectedVal);

// lock — mutual exclusion
private readonly object _lock = new();
lock (_lock)
{
    _sharedList.Add(item);  // thread-safe
}

// Mutex, ReaderWriterLockSlim for more complex scenarios
var rwLock = new ReaderWriterLockSlim();
rwLock.EnterReadLock();
try    { /* read */ }
finally { rwLock.ExitReadLock(); }
```

---

# MASTER / .NET 10

---

## 31. Span\<T\>, Memory\<T\> & Unsafe Code

```csharp
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// ── Span<T> — contiguous memory slice, stack-only ─────────
int[] array = { 1, 2, 3, 4, 5 };
Span<int> span   = array;
Span<int> slice  = span[1..4];      // no allocation
slice[0] = 99;                      // modifies original array

// Stack-allocated span
Span<byte> stackBuf = stackalloc byte[256];
stackBuf.Fill(0);
stackBuf[0] = 42;

// String as span — zero allocation parsing
ReadOnlySpan<char> text = "Hello, World!".AsSpan();
ReadOnlySpan<char> hello = text[..5];
int comma = text.IndexOf(',');

// MemoryExtensions
text.Equals("Hello, World!", StringComparison.Ordinal);
text.Contains(",", StringComparison.Ordinal);
text.StartsWith("Hello");
MemoryExtensions.Split(text, ',');     // split without alloc

// ── Memory<T> — heap-friendly, safe for async ─────────────
Memory<byte> mem = new byte[1024];
ReadOnlyMemory<byte> roMem = "hello"u8.ToArray();   // UTF-8 literal

async Task ProcessAsync(Memory<byte> buffer)
{
    var span2 = buffer.Span;   // only inside sync method
    await socket.ReceiveAsync(buffer);
}

// ── ArrayPool<T> — rent/return buffers ────────────────────
var pool = ArrayPool<byte>.Shared;
byte[] rented = pool.Rent(1024);    // may return larger array
try
{
    var usable = rented.AsSpan(0, 1024);
    // use usable...
}
finally
{
    pool.Return(rented, clearArray: false);
}

// ── Unsafe code ───────────────────────────────────────────
// Must enable: <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
unsafe
{
    int value = 42;
    int* ptr = &value;
    *ptr = 100;
    Console.WriteLine(value);  // 100

    // Fixed buffer (pin managed object)
    fixed (int* p = array)
    {
        *(p + 2) = 999;
    }
}

// ── MemoryMarshal ─────────────────────────────────────────
ReadOnlySpan<byte> bytes = MemoryMarshal.AsBytes(span);
Span<int>  ints = MemoryMarshal.Cast<byte, int>(stackBuf);

// ── Inline arrays (C# 12) ─────────────────────────────────
[InlineArray(8)]
public struct Buffer8<T>
{
    private T _element;
}

// Fast alternative to fixed buffers
Buffer8<float> buf = default;
buf[0] = 1.5f;

// ── Intrinsics (SIMD) ─────────────────────────────────────
using System.Runtime.Intrinsics;
using System.Runtime.Intrinsics.X86;

if (Avx2.IsSupported)
{
    var v1 = Vector256.Create(1.0f);
    var v2 = Vector256.Create(2.0f);
    var sum = Avx.Add(v1, v2);
}

// Vector<T> — portable SIMD
var vA = new Vector<float>(new float[] { 1,2,3,4,5,6,7,8 });
var vB = new Vector<float>(new float[] { 1,1,1,1,1,1,1,1 });
var vC = vA + vB;
```

---

## 32. Concurrency — Channels, Parallel, PLINQ

```csharp
using System.Threading.Channels;

// ── Channel<T> — producer/consumer pipeline ───────────────
var channel = Channel.CreateBounded<int>(capacity: 100);
// or: Channel.CreateUnbounded<int>()

// Producer
async Task ProduceAsync(ChannelWriter<int> writer)
{
    for (int i = 0; i < 1000; i++)
    {
        await writer.WriteAsync(i);
        await Task.Delay(1);
    }
    writer.Complete();
}

// Consumer
async Task ConsumeAsync(ChannelReader<int> reader)
{
    await foreach (var item in reader.ReadAllAsync())
        Console.WriteLine(item);
}

await Task.WhenAll(
    ProduceAsync(channel.Writer),
    ConsumeAsync(channel.Reader));

// Multiple consumers (fan-out)
var consumers = Enumerable.Range(0, 4)
    .Select(_ => ConsumeAsync(channel.Reader));
await Task.WhenAll(consumers);

// ── PLINQ — parallel LINQ ─────────────────────────────────
var results = Enumerable.Range(0, 1_000_000)
    .AsParallel()
    .WithDegreeOfParallelism(4)
    .WithCancellation(cts.Token)
    .Where(n => n % 2 == 0)
    .Select(n => n * n)
    .ToList();

// Order preservation
.AsParallel().AsOrdered()           // preserve input order (slower)
.AsParallel().AsUnordered()         // fastest (default unordered)

// ── Dataflow (TPL Dataflow) ───────────────────────────────
// dotnet add package System.Threading.Tasks.Dataflow
using System.Threading.Tasks.Dataflow;

var transform = new TransformBlock<int, string>(
    n => $"Item-{n}",
    new ExecutionDataflowBlockOptions { MaxDegreeOfParallelism = 4 });

var action = new ActionBlock<string>(
    s => Console.WriteLine(s));

transform.LinkTo(action, new DataflowLinkOptions { PropagateCompletion = true });

for (int i = 0; i < 10; i++)
    await transform.SendAsync(i);

transform.Complete();
await action.Completion;

// ── Reactive Extensions (Rx.NET) ──────────────────────────
// dotnet add package System.Reactive
using System.Reactive.Linq;

var observable = Observable
    .Interval(TimeSpan.FromMilliseconds(100))
    .Take(10)
    .Where(n => n % 2 == 0)
    .Select(n => n * n);

observable.Subscribe(
    onNext:      n => Console.WriteLine(n),
    onError:     e => Console.WriteLine(e),
    onCompleted: () => Console.WriteLine("Done"));
```

---

## 33. Dependency Injection

```csharp
using Microsoft.Extensions.DependencyInjection;

// ── Service interfaces & implementations ──────────────────
public interface IEmailService
{
    Task SendAsync(string to, string subject, string body);
}

public interface IUserRepository
{
    Task<User?> GetByIdAsync(int id);
    Task SaveAsync(User user);
}

public class SmtpEmailService(ILogger<SmtpEmailService> logger) : IEmailService
{
    public async Task SendAsync(string to, string subject, string body)
    {
        logger.LogInformation("Sending email to {To}", to);
        // actual SMTP implementation
        await Task.CompletedTask;
    }
}

public class UserService(IUserRepository repo, IEmailService email)
{
    public async Task RegisterAsync(string name, string emailAddr)
    {
        var user = new User { Name = name, Email = emailAddr };
        await repo.SaveAsync(user);
        await email.SendAsync(emailAddr, "Welcome!", $"Hi {name}, welcome!");
    }
}

// ── Registration ──────────────────────────────────────────
var services = new ServiceCollection();

// Lifetimes
services.AddTransient<IEmailService, SmtpEmailService>();       // new instance every request
services.AddScoped<IUserRepository, UserRepository>();          // same within scope
services.AddSingleton<IConfiguration>(configuration);          // one instance ever

// Factory registration
services.AddTransient<IEmailService>(sp =>
{
    var config = sp.GetRequiredService<IConfiguration>();
    return new SmtpEmailService(config["Smtp:Host"]!,
                                sp.GetRequiredService<ILogger<SmtpEmailService>>());
});

// Options pattern (see §34)
services.AddOptions<SmtpOptions>()
    .BindConfiguration("Smtp")
    .ValidateDataAnnotations();

var provider = services.BuildServiceProvider();

// ── Resolution ────────────────────────────────────────────
var userService = provider.GetRequiredService<UserService>();
var email       = provider.GetService<IEmailService>();         // null if not registered

// Scope (for scoped services)
using var scope = provider.CreateScope();
var scopedRepo  = scope.ServiceProvider.GetRequiredService<IUserRepository>();

// Keyed services (NET 8+)
services.AddKeyedSingleton<IEmailService, SmtpEmailService>("smtp");
services.AddKeyedSingleton<IEmailService, SendGridService>("sendgrid");

// Resolve by key
var smtp = provider.GetRequiredKeyedService<IEmailService>("smtp");

// Constructor injection with primary constructors (C# 12+)
public class OrderProcessor(
    IUserRepository users,
    IEmailService email,
    ILogger<OrderProcessor> logger)
{
    public async Task ProcessAsync(int orderId)
    {
        logger.LogInformation("Processing order {Id}", orderId);
        // ...
    }
}
```

---

## 34. Configuration & Options Pattern

```csharp
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Options;

// ── Configuration sources ─────────────────────────────────
var config = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("appsettings.json", optional: true)
    .AddJsonFile($"appsettings.{env}.json", optional: true)
    .AddEnvironmentVariables()
    .AddCommandLine(args)
    .AddUserSecrets<Program>()   // local dev secrets
    .Build();

// Read values
string? connStr = config.GetConnectionString("Default");
string? apiKey  = config["ExternalApi:Key"];
int     timeout = config.GetValue<int>("Timeout", defaultValue: 30);

// ── Options pattern ───────────────────────────────────────
public class DatabaseOptions
{
    public const string SectionName = "Database";

    [Required]
    public string ConnectionString { get; set; } = "";
    public int CommandTimeout { get; set; } = 30;
    public int MaxRetries      { get; set; } = 3;
    public bool EnableSensitiveLogging { get; set; }
}

// appsettings.json:
// {
//   "Database": {
//     "ConnectionString": "Server=...;Database=...;",
//     "CommandTimeout": 60
//   }
// }

// Registration
services.AddOptions<DatabaseOptions>()
    .BindConfiguration(DatabaseOptions.SectionName)
    .ValidateDataAnnotations()
    .ValidateOnStart();

// Consumption
public class DataService(IOptions<DatabaseOptions> opts)
{
    private readonly DatabaseOptions _opts = opts.Value;
    // opts.Value is cached — same instance for lifetime of app
}

// IOptionsSnapshot — reloaded per scope (for hot-reload support)
public class DataService2(IOptionsSnapshot<DatabaseOptions> opts)
{
    public void Process() => Console.WriteLine(opts.Value.ConnectionString);
}

// IOptionsMonitor — hot-reload + change notifications
public class HotConfig(IOptionsMonitor<DatabaseOptions> monitor)
{
    public HotConfig() => monitor.OnChange(opts =>
        Console.WriteLine($"Config changed: {opts.ConnectionString}"));
}
```

---

## 35. Entity Framework Core

```csharp
// dotnet add package Microsoft.EntityFrameworkCore.SqlServer
// or: Npgsql.EntityFrameworkCore.PostgreSQL / SQLite / etc.
using Microsoft.EntityFrameworkCore;

// ── Models ────────────────────────────────────────────────
public class Blog
{
    public int    Id      { get; set; }
    public string Title   { get; set; } = "";
    public string Url     { get; set; } = "";
    public DateTime CreatedAt { get; set; }

    public ICollection<Post> Posts { get; set; } = new List<Post>();
}

public class Post
{
    public int    Id      { get; set; }
    public string Title   { get; set; } = "";
    public string Content { get; set; } = "";
    public int    BlogId  { get; set; }
    public Blog   Blog    { get; set; } = null!;
}

// ── DbContext ─────────────────────────────────────────────
public class AppDbContext(DbContextOptions<AppDbContext> options)
    : DbContext(options)
{
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }

    protected override void OnModelCreating(ModelBuilder mb)
    {
        mb.Entity<Blog>(entity =>
        {
            entity.HasKey(b => b.Id);
            entity.Property(b => b.Title).IsRequired().HasMaxLength(200);
            entity.Property(b => b.Url).HasMaxLength(500);
            entity.HasIndex(b => b.Url).IsUnique();
            entity.HasMany(b => b.Posts)
                  .WithOne(p => p.Blog)
                  .HasForeignKey(p => p.BlogId)
                  .OnDelete(DeleteBehavior.Cascade);
        });
    }
}

// Registration
services.AddDbContext<AppDbContext>(opt =>
    opt.UseSqlite("Data Source=app.db")
       .EnableSensitiveDataLogging()
       .EnableDetailedErrors());

// ── Migrations ────────────────────────────────────────────
// dotnet ef migrations add InitialCreate
// dotnet ef database update

// ── CRUD operations ───────────────────────────────────────
public class BlogService(AppDbContext db)
{
    // Create
    public async Task<Blog> CreateAsync(string title, string url)
    {
        var blog = new Blog { Title = title, Url = url, CreatedAt = DateTime.UtcNow };
        db.Blogs.Add(blog);
        await db.SaveChangesAsync();
        return blog;
    }

    // Read
    public Task<Blog?> GetByIdAsync(int id)
        => db.Blogs.Include(b => b.Posts).FirstOrDefaultAsync(b => b.Id == id);

    public Task<List<Blog>> SearchAsync(string title)
        => db.Blogs
             .Where(b => b.Title.Contains(title))
             .OrderByDescending(b => b.CreatedAt)
             .AsNoTracking()   // read-only, faster
             .ToListAsync();

    // Update
    public async Task<bool> UpdateAsync(int id, string newTitle)
    {
        int rows = await db.Blogs
            .Where(b => b.Id == id)
            .ExecuteUpdateAsync(s => s.SetProperty(b => b.Title, newTitle));  // EF 7+
        return rows > 0;
    }

    // Delete
    public async Task<bool> DeleteAsync(int id)
    {
        int rows = await db.Blogs
            .Where(b => b.Id == id)
            .ExecuteDeleteAsync();   // EF 7+ — no load required
        return rows > 0;
    }

    // Raw SQL (when LINQ won't do)
    public Task<List<Blog>> RawAsync()
        => db.Blogs.FromSqlRaw("SELECT * FROM Blogs WHERE CreatedAt > {0}", DateTime.UtcNow.AddDays(-7))
              .ToListAsync();

    // Transactions
    public async Task TransferAsync(int fromId, int toId)
    {
        await using var tx = await db.Database.BeginTransactionAsync();
        try
        {
            // operations...
            await db.SaveChangesAsync();
            await tx.CommitAsync();
        }
        catch
        {
            await tx.RollbackAsync();
            throw;
        }
    }
}
```

---

## 36. ASP.NET Core & Minimal APIs

```csharp
// dotnet new webapi -n MyApi
var builder = WebApplication.CreateBuilder(args);

// Register services
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDbContext<AppDbContext>(opt =>
    opt.UseSqlite(builder.Configuration.GetConnectionString("Default")));
builder.Services.AddScoped<BlogService>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

// ── Minimal API endpoints ─────────────────────────────────
var blogs = app.MapGroup("/api/blogs").WithTags("Blogs");

blogs.MapGet("/", async (BlogService svc) =>
    Results.Ok(await svc.GetAllAsync()));

blogs.MapGet("/{id:int}", async (int id, BlogService svc) =>
    await svc.GetByIdAsync(id) is { } blog
        ? Results.Ok(blog)
        : Results.NotFound());

blogs.MapPost("/", async (CreateBlogDto dto, BlogService svc) =>
{
    var blog = await svc.CreateAsync(dto.Title, dto.Url);
    return Results.CreatedAtRoute("GetBlog", new { id = blog.Id }, blog);
}).WithName("GetBlog");

blogs.MapPut("/{id:int}", async (int id, UpdateBlogDto dto, BlogService svc) =>
    await svc.UpdateAsync(id, dto.Title)
        ? Results.NoContent()
        : Results.NotFound());

blogs.MapDelete("/{id:int}", async (int id, BlogService svc) =>
    await svc.DeleteAsync(id)
        ? Results.NoContent()
        : Results.NotFound());

// ── DTOs ──────────────────────────────────────────────────
public record CreateBlogDto(string Title, string Url);
public record UpdateBlogDto(string Title);

// ── Middleware ────────────────────────────────────────────
app.UseMiddleware<RequestLoggingMiddleware>();

public class RequestLoggingMiddleware(RequestDelegate next, ILogger<RequestLoggingMiddleware> logger)
{
    public async Task InvokeAsync(HttpContext ctx)
    {
        logger.LogInformation("{Method} {Path}", ctx.Request.Method, ctx.Request.Path);
        await next(ctx);
        logger.LogInformation("Response: {StatusCode}", ctx.Response.StatusCode);
    }
}

// ── Controller-based (traditional) ───────────────────────
[ApiController]
[Route("api/[controller]")]
public class BlogsController(BlogService service) : ControllerBase
{
    [HttpGet]
    public async Task<IActionResult> GetAll() => Ok(await service.GetAllAsync());

    [HttpGet("{id:int}", Name = nameof(GetById))]
    public async Task<IActionResult> GetById(int id)
        => await service.GetByIdAsync(id) is { } blog ? Ok(blog) : NotFound();

    [HttpPost]
    [ProducesResponseType(StatusCodes.Status201Created)]
    public async Task<IActionResult> Create(CreateBlogDto dto)
    {
        var blog = await service.CreateAsync(dto.Title, dto.Url);
        return CreatedAtAction(nameof(GetById), new { id = blog.Id }, blog);
    }
}

app.Run();
```

---

## 37. Logging with ILogger

```csharp
using Microsoft.Extensions.Logging;

// ── Setup ─────────────────────────────────────────────────
// In Program.cs — builder.Logging is configured automatically
// but you can customise:
builder.Logging
    .ClearProviders()
    .AddConsole()
    .AddDebug()
    .SetMinimumLevel(LogLevel.Information);

// Add Serilog (popular structured logging)
// dotnet add package Serilog.AspNetCore
// builder.Host.UseSerilog((ctx, cfg) => cfg.ReadFrom.Configuration(ctx.Configuration));

// ── Usage in services ─────────────────────────────────────
public class OrderService(ILogger<OrderService> logger)
{
    public async Task ProcessOrderAsync(int orderId)
    {
        // Log levels: Trace Debug Information Warning Error Critical
        logger.LogTrace("Entering {Method}", nameof(ProcessOrderAsync));
        logger.LogDebug("Processing order {OrderId}", orderId);
        logger.LogInformation("Order {OrderId} started", orderId);

        try
        {
            // process...
            logger.LogInformation("Order {OrderId} completed successfully", orderId);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "Order {OrderId} failed with error", orderId);
            throw;
        }
    }
}

// ── Source-generated log methods (C# performance tip) ─────
public static partial class Log
{
    [LoggerMessage(Level = LogLevel.Information, Message = "Processing order {OrderId}")]
    public static partial void ProcessingOrder(ILogger logger, int orderId);

    [LoggerMessage(Level = LogLevel.Error, Message = "Order {OrderId} failed")]
    public static partial void OrderFailed(ILogger logger, int orderId, Exception ex);
}

// Usage
Log.ProcessingOrder(logger, 42);

// ── Scopes — add context to log entries ──────────────────
using (logger.BeginScope("RequestId:{RequestId}", Guid.NewGuid()))
{
    logger.LogInformation("Inside scope");  // log entry includes RequestId
}

// ── appsettings.json logging config ──────────────────────
// {
//   "Logging": {
//     "LogLevel": {
//       "Default": "Information",
//       "Microsoft": "Warning",
//       "MyApp.Services": "Debug"
//     }
//   }
// }
```

---

## 38. Testing — xUnit & Moq

```csharp
// dotnet add package xunit xunit.runner.visualstudio Moq FluentAssertions coverlet.collector

using Xunit;
using Moq;
using FluentAssertions;

// ── Basic tests ───────────────────────────────────────────
public class CalculatorTests
{
    private readonly Calculator _sut = new();  // sut = system under test

    [Fact]
    public void Add_TwoPositiveNumbers_ReturnsSum()
    {
        // Arrange
        int a = 3, b = 4;

        // Act
        int result = _sut.Add(a, b);

        // Assert
        result.Should().Be(7);
        Assert.Equal(7, result);            // xUnit built-in
    }

    [Theory]
    [InlineData(0, 0, 0)]
    [InlineData(1, 2, 3)]
    [InlineData(-1, 1, 0)]
    [InlineData(int.MaxValue, 1, int.MinValue)]  // overflow test
    public void Add_VariousInputs_ReturnsExpected(int a, int b, int expected)
        => _sut.Add(a, b).Should().Be(expected);

    [Fact]
    public void Divide_ByZero_ThrowsDivideByZeroException()
    {
        Action act = () => _sut.Divide(10, 0);
        act.Should().Throw<DivideByZeroException>()
           .WithMessage("*zero*");
    }
}

// ── Mocking with Moq ──────────────────────────────────────
public class UserServiceTests
{
    private readonly Mock<IUserRepository> _repoMock = new();
    private readonly Mock<IEmailService>   _emailMock = new();
    private readonly UserService           _sut;

    public UserServiceTests()
    {
        _sut = new UserService(_repoMock.Object, _emailMock.Object);
    }

    [Fact]
    public async Task Register_ValidUser_SavesAndSendsEmail()
    {
        // Arrange
        _repoMock.Setup(r => r.SaveAsync(It.IsAny<User>()))
                 .Returns(Task.CompletedTask);
        _emailMock.Setup(e => e.SendAsync(It.IsAny<string>(), It.IsAny<string>(), It.IsAny<string>()))
                  .Returns(Task.CompletedTask);

        // Act
        await _sut.RegisterAsync("Alice", "alice@example.com");

        // Assert
        _repoMock.Verify(r => r.SaveAsync(It.Is<User>(u => u.Name == "Alice")), Times.Once);
        _emailMock.Verify(e => e.SendAsync("alice@example.com", It.IsAny<string>(), It.IsAny<string>()), Times.Once);
    }

    [Fact]
    public async Task GetUser_NotFound_ReturnsNull()
    {
        _repoMock.Setup(r => r.GetByIdAsync(99)).ReturnsAsync((User?)null);

        var result = await _sut.GetUserAsync(99);

        result.Should().BeNull();
    }
}

// ── Fixtures — shared context ──────────────────────────────
public class DatabaseFixture : IAsyncLifetime
{
    public AppDbContext Db { get; private set; } = null!;

    public async Task InitializeAsync()
    {
        var opts = new DbContextOptionsBuilder<AppDbContext>()
            .UseSqlite("Data Source=:memory:")
            .Options;
        Db = new AppDbContext(opts);
        await Db.Database.EnsureCreatedAsync();
    }

    public async Task DisposeAsync() => await Db.DisposeAsync();
}

public class IntegrationTests(DatabaseFixture fixture) : IClassFixture<DatabaseFixture>
{
    [Fact]
    public async Task CreateBlog_PersistsToDatabase()
    {
        var blog = new Blog { Title = "Test", Url = "https://test.com" };
        fixture.Db.Blogs.Add(blog);
        await fixture.Db.SaveChangesAsync();

        var loaded = await fixture.Db.Blogs.FindAsync(blog.Id);
        loaded.Should().NotBeNull();
        loaded!.Title.Should().Be("Test");
    }
}
```

---

## 39. C# 13 / .NET 10 New Features

```csharp
// ── C# 13 (ships with .NET 9/10) ─────────────────────────

// params collections — not just arrays
void PrintAll(params IEnumerable<string> items)
{
    foreach (var item in items) Console.WriteLine(item);
}
PrintAll("a", "b", "c");                    // works
PrintAll(new List<string> { "x", "y" });    // works

// ref struct interfaces — ref structs can now implement interfaces
// (enables Span<T> to implement IEnumerable in limited contexts)
ref struct SpanWrapper<T> : ISomeInterface
{
    private Span<T> _data;
    public SpanWrapper(Span<T> data) => _data = data;
}

// Partial properties (C# 13)
public partial class MyViewModel
{
    public partial string Name { get; set; }
}

public partial class MyViewModel
{
    private string _name = "";
    public partial string Name
    {
        get => _name;
        set => SetProperty(ref _name, value);
    }
}

// Lock object — new System.Threading.Lock type (C# 13)
private readonly Lock _lock = new();
lock (_lock) { /* critical section */ }
// Better than lock(object) — avoids Monitor overhead

// Overload resolution priority (C# 13)
[OverloadResolutionPriority(1)]
public static void Process(ReadOnlySpan<byte> data) { }  // preferred
public static void Process(byte[] data) { }              // fallback

// Escape character \e for ESC (0x1B) (C# 13)
Console.Write("\e[31mRed text\e[0m");

// ── .NET 10 highlights ────────────────────────────────────

// LINQ enhancements
var nums = Enumerable.Range(1, 10);
nums.CountBy(x => x % 3);             // groups + counts in one call
nums.AggregateBy(x => x % 3, seed: 0, (acc, x) => acc + x);  // group + aggregate
nums.Index();                          // (0,1),(1,2),(2,3),...  (equivalent to Select with index)

// OrderedDictionary<TKey,TValue> — ordered by insertion
var od = new OrderedDictionary<string, int>
{
    ["first"]  = 1,
    ["second"] = 2,
    ["third"]  = 3
};
od.GetAt(0);                // ("first", 1) — index access
od.IndexOf("second");       // 1

// Tensor<T> — ML / math  (preview in .NET 9, stable .NET 10)
using System.Numerics.Tensors;
var t1 = Tensor.Create<float>([1, 2, 3, 4], [2, 2]);  // 2×2 tensor
var t2 = Tensor.Create<float>([5, 6, 7, 8], [2, 2]);
var sum = Tensor.Add(t1, t2);

// TensorPrimitives — SIMD-accelerated spans
TensorPrimitives.Add(spanA, spanB, destination);
TensorPrimitives.Dot(spanA, spanB);
TensorPrimitives.CosineSimilarity(spanA, spanB);

// HybridCache (NET 9/10) — L1 in-process + L2 distributed
// dotnet add package Microsoft.Extensions.Caching.Hybrid
builder.Services.AddHybridCache();

public class ProductService(HybridCache cache)
{
    public async Task<Product?> GetAsync(int id, CancellationToken ct)
        => await cache.GetOrCreateAsync(
            $"product:{id}",
            async ct => await LoadFromDbAsync(id, ct),
            cancellationToken: ct);
}

// TimeProvider (testable time — NET 8+, widely adopted .NET 10)
public class Scheduler(TimeProvider time)
{
    public bool IsBusinessHours()
    {
        var now = time.GetLocalNow();
        return now.Hour is >= 9 and < 17;
    }
}
// In tests:
var fakeTime = new FakeTimeProvider();
fakeTime.SetUtcNow(new DateTimeOffset(2025, 1, 1, 10, 0, 0, TimeSpan.Zero));

// UUID v7 (monotonic, time-sortable) — NET 9+
Guid guid = Guid.CreateVersion7();         // sortable by creation time!

// Improved SearchValues<T>
var vowels = SearchValues.Create("aeiouAEIOU");
"Hello World".AsSpan().IndexOfAny(vowels);  // 1

// Random.Shared improvements
Random.Shared.GetItems(['a','b','c'], 5);   // pick 5 with replacement
Random.Shared.Shuffle(myArray);             // NET 8+

// Base64Url (NET 9+)
string encoded = Base64Url.EncodeToString(bytes);
byte[] decoded = Base64Url.DecodeFromChars(encoded);

// Task.WhenEach (NET 9+) — process tasks as they complete
await foreach (var completed in Task.WhenEach(tasks))
    Console.WriteLine(await completed);
```

---

## 40. Idiomatic C# Patterns & Tips

```csharp
// ── Object Expressions (anonymous implementations) ─────────
// Not available in C# (unlike Java/Kotlin) — use local class or lambda adapter

// ── Builder pattern ────────────────────────────────────────
public class QueryBuilder
{
    private readonly StringBuilder _sb = new("SELECT * FROM Users");
    private readonly List<string>  _conditions = new();

    public QueryBuilder Where(string condition) { _conditions.Add(condition); return this; }
    public QueryBuilder OrderBy(string col)     { _sb.Append($" ORDER BY {col}"); return this; }

    public string Build()
    {
        if (_conditions.Any())
            _sb.Insert(_sb.ToString().IndexOf("FROM"), "")
               .Append(" WHERE " + string.Join(" AND ", _conditions));
        return _sb.ToString();
    }
}

new QueryBuilder().Where("Age > 18").Where("Active = 1").OrderBy("Name").Build();

// ── Repository + Unit of Work ──────────────────────────────
public interface IUnitOfWork : IAsyncDisposable
{
    IBlogRepository Blogs { get; }
    IPostRepository Posts { get; }
    Task<int> SaveChangesAsync(CancellationToken ct = default);
}

// ── Result<T> — railway-oriented / functional errors ──────
public readonly record struct Result<T>
{
    public T?     Value   { get; init; }
    public string? Error  { get; init; }
    public bool   IsOk    => Error is null;

    public static Result<T> Ok(T value)      => new() { Value = value };
    public static Result<T> Fail(string err) => new() { Error = err };

    public Result<U> Map<U>(Func<T, U> f)
        => IsOk ? Result<U>.Ok(f(Value!)) : Result<U>.Fail(Error!);

    public void Match(Action<T> onOk, Action<string> onFail)
    {
        if (IsOk) onOk(Value!);
        else onFail(Error!);
    }
}

Result<int> Divide(int a, int b)
    => b == 0 ? Result<int>.Fail("Division by zero") : Result<int>.Ok(a / b);

Divide(10, 2).Match(Console.WriteLine, Console.Error.WriteLine);

// ── Guard clauses (fail fast) ─────────────────────────────
public class UserValidator
{
    public static void Validate(User user)
    {
        ArgumentNullException.ThrowIfNull(user);
        ArgumentException.ThrowIfNullOrWhiteSpace(user.Name, nameof(user.Name));
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(user.Age, nameof(user.Age));
    }
}

// ── Immutability patterns ─────────────────────────────────
// Prefer records for immutable data
public record Order(int Id, string Customer, IReadOnlyList<OrderLine> Lines)
{
    public decimal Total => Lines.Sum(l => l.Total);
    public Order WithLine(OrderLine line) => this with { Lines = [..Lines, line] };
}

// ── Primary constructors (C# 12+) ────────────────────────
public class HttpClientService(HttpClient client, ILogger<HttpClientService> logger)
{
    public async Task<string> GetAsync(string url)
    {
        logger.LogInformation("GET {Url}", url);
        return await client.GetStringAsync(url);
    }
}

// ── Collection expressions (C# 12+) ─────────────────────
int[] arr    = [1, 2, 3];
List<int> ls = [1, 2, 3];
Span<int> sp = [1, 2, 3];
int[] combined = [..arr, 4, 5, ..new[]{6, 7}];  // spread

// ── Useful BCL classes ────────────────────────────────────
// Math & MathF
Math.Clamp(value, min, max);
Math.Min(a, b);  Math.Max(a, b);
Math.Round(3.145, 2, MidpointRounding.AwayFromZero);
Math.Log(x);  Math.Log2(x);  Math.Log10(x);
Math.Abs(-5);

// BitConverter
byte[] bytes = BitConverter.GetBytes(42);
int back = BitConverter.ToInt32(bytes, 0);

// Guid
Guid.NewGuid();
Guid.Parse("d3b07384-d9a0-4f14-b4b3-5e2b5e0e7d97");
Guid.TryParse(str, out var id);
Guid.Empty;

// Environment
Environment.MachineName;
Environment.UserName;
Environment.ProcessorCount;
Environment.GetEnvironmentVariable("PATH");
Environment.CurrentDirectory;
Environment.Version;           // .NET version
Environment.Exit(0);

// Stopwatch — precise timing
var sw = Stopwatch.StartNew();
DoWork();
sw.Stop();
Console.WriteLine(sw.Elapsed);         // TimeSpan
Console.WriteLine(sw.ElapsedMilliseconds);

// ── Performance tips ──────────────────────────────────────
// Use Span<T> for slicing instead of Substring (no alloc)
// Use ArrayPool for temporary large arrays
// Use StringBuilder for string concatenation in loops
// Use ValueTask instead of Task for hot paths that often complete synchronously
// Use ReadOnlySpan<char> in parsing methods
// Use sealed classes — JIT can devirtualize calls
// Prefer struct for small, immutable, frequently created data
// Use AsNoTracking() in EF for read-only queries
// Use ConfigureAwait(false) in library code
// Use cancellation tokens everywhere
// Profile before optimizing — use BenchmarkDotNet
// dotnet add package BenchmarkDotNet

[MemoryDiagnoser]
[SimpleJob(RuntimeMoniker.Net90)]
public class MyBenchmarks
{
    [Benchmark]
    public void Method1() => DoWork1();

    [Benchmark]
    public void Method2() => DoWork2();
}
// Run: dotnet run -c Release
```

---

## Quick Reference Card

| Concept | C# Syntax |
|---|---|
| Null-coalescing | `x ?? "default"` |
| Null-conditional | `obj?.Method()?.Property` |
| Null-coalescing assign | `x ??= GetDefault()` |
| Pattern matching | `obj is string s` |
| Switch expression | `x switch { > 5 => "big", _ => "small" }` |
| Ternary | `cond ? a : b` |
| String interpolation | `$"Hello, {name}!"` |
| Raw string | `"""multi "line" string"""` |
| Range | `arr[1..^1]` |
| Index from end | `arr[^1]` |
| Tuple | `(int X, int Y) p = (1, 2)` |
| Deconstruct | `var (x, y) = point;` |
| Discard | `_ = Unused()` |
| with expression | `rec with { Prop = val }` |
| Collection expression | `int[] a = [1, 2, 3]` |
| Spread in collection | `[..a, 4, 5]` |
| Primary constructor | `class Foo(int X)` |
| Expression body | `int Add(int a, int b) => a + b;` |
| Local function | `int Inner(int x) { ... }` |
| Async/Await | `await SomethingAsync()` |
| Throw expression | `x ?? throw new Exception()` |
| nameof | `nameof(MyMethod)` |
| typeof | `typeof(MyClass)` |
| is not null | `if (x is not null)` |
| and / or patterns | `x is > 0 and < 100` |
| Required property | `public required string Name { get; init; }` |
| Unsafe | `unsafe { int* p = &x; }` |
| stackalloc | `Span<byte> buf = stackalloc byte[64]` |
| checked | `checked { int x = int.MaxValue + 1; }` |
| Lock (C# 13) | `private readonly Lock _lock = new()` |

---

### .NET CLI Cheat Sheet

```bash
# Create projects
dotnet new console -n MyApp
dotnet new webapi  -n MyApi
dotnet new xunit   -n MyApp.Tests
dotnet new classlib -n MyLib

# Build & run
dotnet run
dotnet run --project ./MyApp/MyApp.csproj
dotnet build
dotnet build -c Release

# Test
dotnet test
dotnet test --filter "Category=Unit"
dotnet test --collect:"XPlat Code Coverage"

# Packages
dotnet add package Newtonsoft.Json
dotnet add package Microsoft.EntityFrameworkCore --version 9.0.0
dotnet remove package OldPackage
dotnet list package

# Publish
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release -r win-x64 -p:PublishSingleFile=true

# Tools
dotnet tool install -g dotnet-ef
dotnet ef migrations add Init
dotnet ef database update
dotnet ef migrations remove

# Info
dotnet --version
dotnet --list-sdks
dotnet --list-runtimes
```

---

*Built with ❤️ for C# & .NET developers — from first `Console.WriteLine` to cloud-native production code.*
