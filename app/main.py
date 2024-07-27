class Deck:
    def __init__(
            self,
            row: int,
            column: int,
            is_alive: bool = True
    ) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
            self,
            start: tuple,
            end: tuple,
            is_drowned: bool = False
    ) -> None:
        self.is_drowned = is_drowned
        self.decks = []
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                self.decks.append(Deck(row, col))

    def get_deck(
            self,
            row: int,
            column: int
    ) -> Deck | None:
        for deck in self.decks:
            if deck.row == row:
                if deck.column == column:
                    return deck
        return None

    def fire(
            self,
            row: int,
            column: int
    ) -> int:
        got_deck = self.get_deck(row, column)
        if got_deck is None or not got_deck.is_alive:
            return 1
        got_deck.is_alive = False
        if all(not deck.is_alive for deck in self.decks):
            self.is_drowned = True
            return 3
        return 2


class Battleship:
    def __init__(self, ships: list) -> None:
        self.field = {
            ship: Ship(ship[0], ship[1]) for ship in ships
        }

    def fire(self, location: tuple) -> str:
        for ship in self.field:
            attempt = self.field[ship].fire(location[0], location[1])
            if attempt >= 2:
                if attempt == 3:
                    return "Sunk!"
                return "Hit!"
        return "Miss!"
