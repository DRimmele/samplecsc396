from fastapi import FastAPI, HTTPException

app = FastAPI()

class flashcards:
        def __init__(id, question, answer):
        self.id = id
        self.question = question
        self.answer = answer


users = {}
next_id = 1

@app.post("/flashcards", status_code=201)
def create_flashcards(cards: List[Flashcard]):
    global next_id
    created_cards = []
    for card in cards:
        card.id = next_id
        next_id += 1
        user[card.id] = card
        created_cards.append(card)
    return created_cards

@app.get("/flashcards/{card_id}")
def get_flashcard(card_id: int):
    if card_id in user:
        return user[card_id]
    raise HTTPException(status_code=404, detail="Flashcard not found")

@app.patch("/flashcards/{card_id}")
def update_flashcard(card_id: int, updated_card: Flashcard):
    if card_id not in user:
        raise HTTPException(status_code=404, detail="Flashcard not found")

    stored_card = user[card_id]
    if updated_card.question is not None:
        stored_card.question = updated_card.question
    if updated_card.answer is not None:
        stored_card.answer = updated_card.answer

    return stored_card

@app.delete("/flashcards/{card_id}")
def delete_flashcard(card_id: int):
    if card_id not in user:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    del user[card_id]

@app.get("/flashcards")
def get_all_flashcards():
    return list(user.values())
