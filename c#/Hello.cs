using System;

namespace hello
{
	class Program
	{
		static void Main(string[] args)
		{
			try 
			{
				Message msg = new Message(args[0]);
				Console.Write(msg.response());
			}
			catch (IndexOutOfRangeException)
			{
				Console.Write("NO ARGUMENT!");
			}
		}

	}

	public class Message
	{
		private string num;
		
		public Message(string num)
		{
			this.num = num;
		}

		public string response()
		{
			if (num == "1")
				return "HELLO WORLD!";
			else if (num == "2")
				return "HELLO MARS!";
			else
				return "NO COMMENT!";
		}
		
	}
}