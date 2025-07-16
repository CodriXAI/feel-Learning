from AIclasificator import clasificator

#Testing the model with the following sentences

phrases = [
	"I feel good",
	"I feel great!",
	"I feel bad",
	"So-so",
	"Very happy!",
	"Good, happy",
	"Neither good nor bad",
	"We're doing great",
	"We're doing really badly"
]

print("-----------feelLearning 0.0.1 version----------")
print("Prompts obtained:")

print("------------------------------------------------------")
for phrase in phrases:
	print(phrase)
print("------------------------------------------------------")

for phrase in phrases:
	result = clasificator(phrase)
	print(f"'{phrase}' -> {result}")
