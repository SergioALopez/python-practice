# Lambda is a shortcut for a tiny, throwaway function

# def get_age(s):             |    lambda s: int(s["age"])
# 	return int(s["age"])  |

words = ["hi", "hello", "hey", "greetings"]

longest = max(words, key=lambda w: len(w))	# Here lambda says "compare words by their length"
print(longest)					# max returns the actual longest word, not the length number

# labda can only hold a single expression - no loops, no multiple lines, no if/else blocks (one-line conditionals are possible but they get messy)
