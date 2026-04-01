def ask() -> str:
	return input("Make a title from... ")

def titlize(s: str) -> str:
	return s.title()

def main():
	# do not change code below
	s = ask()
	s = titlize(s)
	print(f"The title is: {s}")

if __name__ == "__main__":
	# do not change code below
	main()

