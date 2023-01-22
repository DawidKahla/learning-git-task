shopping_dict = {
    "piekarnia" : ['chleb', 'pączek', 'rukola'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}
X = 0
print('Lista zakupów')
for place in shopping_dict:
    print(f"Idę do {place.title()}, kupuję tu następujące rzeczy: {', '.join([product.title() for product in shopping_dict[place]])}.")
    X += len(shopping_dict[place])
print(f"W sumię kupuję {X} produktów.")
