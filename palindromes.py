# I think it's O(n)
# Maybe O(n*2), but that's still linear
def is_pal(string: str):
	alphatized = "".join(ch for ch in string.lower() if ch.isalpha())
	print(alphatized)
	return alphatized == "".join(reversed(alphatized))