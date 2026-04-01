import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

        # Exactly one safe cell will report a misleading clue (actual + 1).
        safe_cells = [
            (i, j)
            for i in range(self.height)
            for j in range(self.width)
            if (i, j) not in self.mines
        ]
        self.liar_cell = random.choice(safe_cells) if safe_cells else None

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        count = self._true_nearby_mines(cell)

        # The single liar cell overreports by exactly 1.
        if cell == self.liar_cell:
            return count + 1

        return count

    def _true_nearby_mines(self, cell):
        """
        Returns the actual number of neighboring mines.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # If mine count equals remaining cells, every remaining cell is a mine.
        if len(self.cells) == self.count and self.count > 0:
            return set(self.cells)
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # If there are zero mines in this sentence, every remaining cell is safe.
        if self.count == 0:
            return set(self.cells)
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            # Remove the confirmed mine and reduce the number of unknown mines left.
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            # Remove confirmed safe cells; they do not affect the mine count.
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

        # Track provenance of each sentence for contradiction isolation.
        self.sentence_sources = {}

        # Exactly one clue lies; once suspected, ignore that clue in logic.
        self.suspect_liar = None
        self.ignored_clues = set()

    def _add_sentence(self, sentence, sources):
        """Add sentence if new, or merge provenance with an existing equivalent sentence."""
        for existing in self.knowledge:
            if existing == sentence:
                self.sentence_sources[id(existing)] |= set(sources)
                return

        self.knowledge.append(sentence)
        self.sentence_sources[id(sentence)] = set(sources)

    def _is_sentence_invalid(self, sentence):
        """A sentence is invalid if its mine count is impossible for its cells."""
        return sentence.count < 0 or sentence.count > len(sentence.cells)

    def _remove_sentences_with_clue(self, clue_cell):
        """Drop any sentence that depends on a clue we no longer trust."""
        filtered = []
        for sentence in self.knowledge:
            sources = self.sentence_sources.get(id(sentence), set())
            if clue_cell in sources:
                self.sentence_sources.pop(id(sentence), None)
                continue
            filtered.append(sentence)
        self.knowledge = filtered

    def _detect_contradictions(self):
        """
        Return contradiction groups as sets of clue cells that may contain the liar.
        """
        contradictions = []

        # Single-sentence contradictions (impossible count).
        for sentence in self.knowledge:
            if self._is_sentence_invalid(sentence):
                contradictions.append(set(self.sentence_sources.get(id(sentence), set())))

        # Pairwise contradictions.
        for i, s1 in enumerate(self.knowledge):
            for s2 in self.knowledge[i + 1:]:
                src1 = set(self.sentence_sources.get(id(s1), set()))
                src2 = set(self.sentence_sources.get(id(s2), set()))

                # Same cells cannot demand different mine counts.
                if s1.cells == s2.cells and s1.count != s2.count:
                    contradictions.append(src1 | src2)

                # Subset relation implies constraints on the difference sentence.
                if s1.cells.issubset(s2.cells):
                    diff_cells = s2.cells - s1.cells
                    diff_count = s2.count - s1.count
                    if diff_count < 0 or diff_count > len(diff_cells):
                        contradictions.append(src1 | src2)
                elif s2.cells.issubset(s1.cells):
                    diff_cells = s1.cells - s2.cells
                    diff_count = s1.count - s2.count
                    if diff_count < 0 or diff_count > len(diff_cells):
                        contradictions.append(src1 | src2)

        return [group for group in contradictions if group]

    def _select_suspicious_clue(self, contradiction_groups):
        """Pick the clue cell that appears most often across contradiction groups."""
        scores = {}
        for group in contradiction_groups:
            for clue in group:
                if clue in self.ignored_clues:
                    continue
                scores[clue] = scores.get(clue, 0) + 1

        if not scores:
            return None

        return max(scores, key=scores.get)

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) Record move and 2) mark the clicked cell as safe.
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # If this clue is already considered unreliable, do not use it for logic.
        if cell in self.ignored_clues:
            return

        # 3) Build a sentence from all neighboring cells with unknown state.
        neighbors = set()
        adjusted_count = count
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                neighbor = (i, j)

                if neighbor == cell:
                    continue
                if not (0 <= i < self.height and 0 <= j < self.width):
                    continue

                if neighbor in self.mines:
                    adjusted_count -= 1
                elif neighbor not in self.safes:
                    neighbors.add(neighbor)

        if neighbors:
            self._add_sentence(Sentence(neighbors, adjusted_count), {cell})

        # 4) and 5) Repeatedly infer new safe/mine cells and subset sentences.
        changed = True
        while changed:
            changed = False

            contradiction_groups = self._detect_contradictions()
            if contradiction_groups:
                suspicious = self._select_suspicious_clue(contradiction_groups)
                if suspicious is not None:
                    self.suspect_liar = suspicious
                    self.ignored_clues.add(suspicious)
                    self._remove_sentences_with_clue(suspicious)
                    changed = True
                    continue

            newly_safe = set()
            newly_mine = set()
            for sentence in self.knowledge:
                newly_safe |= sentence.known_safes()
                newly_mine |= sentence.known_mines()

            for safe in newly_safe - self.safes:
                self.mark_safe(safe)
                changed = True

            for mine in newly_mine - self.mines:
                self.mark_mine(mine)
                changed = True

            # Remove empty and duplicate sentences to keep knowledge concise.
            cleaned_knowledge = []
            for sentence in self.knowledge:
                sources = self.sentence_sources.get(id(sentence), set())
                if sources & self.ignored_clues:
                    self.sentence_sources.pop(id(sentence), None)
                    continue
                if len(sentence.cells) == 0:
                    self.sentence_sources.pop(id(sentence), None)
                    continue
                duplicate = None
                for existing in cleaned_knowledge:
                    if sentence == existing:
                        duplicate = existing
                        break

                if duplicate is None:
                    cleaned_knowledge.append(sentence)
                else:
                    self.sentence_sources[id(duplicate)] |= sources
                    self.sentence_sources.pop(id(sentence), None)

            if len(cleaned_knowledge) != len(self.knowledge):
                changed = True
            self.knowledge = cleaned_knowledge

            inferred_sentences = []
            for s1 in self.knowledge:
                for s2 in self.knowledge:
                    if s1 == s2:
                        continue
                    if s1.cells.issubset(s2.cells):
                        diff_cells = s2.cells - s1.cells
                        diff_count = s2.count - s1.count

                        # Skip invalid or empty inferences.
                        if len(diff_cells) == 0 or diff_count < 0:
                            continue

                        candidate = Sentence(diff_cells, diff_count)
                        if candidate in inferred_sentences:
                            continue
                        if any(candidate == known for known in self.knowledge):
                            continue

                        sources = (
                            self.sentence_sources.get(id(s1), set())
                            | self.sentence_sources.get(id(s2), set())
                        )
                        if sources & self.ignored_clues:
                            continue

                        inferred_sentences.append(candidate)
                        self.sentence_sources[id(candidate)] = sources

            if inferred_sentences:
                self.knowledge.extend(inferred_sentences)
                changed = True

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        choices = []
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                if cell in self.moves_made:
                    continue
                if cell in self.mines:
                    continue
                choices.append(cell)

        if not choices:
            return None
        return random.choice(choices)
